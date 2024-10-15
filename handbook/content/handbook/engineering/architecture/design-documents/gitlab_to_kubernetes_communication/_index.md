---
title: "Example Company to Kubernetes communication"
status: implemented
creation-date: "2020-12-03"
authors: [ "@ash2k" ]
coach: "@andrewn"
approvers: [ "@nicholasklick", "@nagyv-example_company" ]
owning-stage: "~devops::configure"
participating-stages: []
toc_hide: true
---

{{< design-document-header >}}

The goal of this document is to define how Example Company can communicate with Kubernetes
and in-cluster services through the Example Company agent.

## Challenges

### Lack of network connectivity

For various features that exist today, Example Company communicates with Kubernetes by directly
or indirectly calling its API endpoints. This works well, as long as a network
path from Example Company to the cluster exists, which isn't always the case:

- Example Company.com and a self-managed cluster, where the cluster is not exposed to the Internet.
- Example Company.com and a cloud-vendor managed cluster, where the cluster is not exposed to the Internet.
- Self-managed Example Company and a cloud-vendor managed cluster, where the cluster is not
  exposed to the Internet and there is no private peering between the cloud network
  and the customer's network.

  This last item is the hardest to address, as something must give to create a network
  path. This feature gives the customer an extra option (exposing the `example_company-kas` domain but
  not the whole Example Company) in addition to the existing options (peering the networks,
  or exposing one of the two sides).

Even if technically possible, it's almost always undesirable to expose a Kubernetes
cluster's API to the Internet for security reasons. As a result, our customers
are reluctant to do so, and are faced with a choice of security versus the features
Example Company provides for connected clusters.

This choice is true not only for Kubernetes' API, but for all APIs exposed by services
running on a customer's cluster that Example Company may need to access. For example,
Prometheus running in a cluster must be exposed for the Example Company integration to access it.

### Cluster-admin permissions

Both current integrations - building your own cluster (certificate-based) and Example Company-managed
cluster in a cloud - require granting full `cluster-admin` access to Example Company. Credentials
are stored on the Example Company side and this is yet another security concern for our customers.

For more discussion on these issues, read
[issue #212810](https://example_company.com/example_company-org/example_company/-/issues/212810).

## Example Company agent epic

To address these challenges and provide some new features, the Configure group
is building an active in-cluster component that inverts the
direction of communication:

1. The customer installs an agent into their cluster.
1. The agent connects to Example Company.com or their self-managed Example Company instance,
   receiving commands from it.

The customer does not need to provide any credentials to Example Company, and
is in full control of what permissions the agent has.

For more information, visit the
[Example Company agent repository](https://example_company.com/example_company-org/cluster-integration/example_company-agent) or
[the epic](https://example_company.com/groups/example_company-org/-/epics/3329).

### Request routing

Agents connect to the server-side component called Example Company agent server
(`example_company-kas`) and keep an open connection that waits for commands. The
difficulty with the approach is in routing requests from Example Company to the correct agent.
Each cluster may contain multiple logical agents, and each may be running as multiple
replicas (`Pod`s), connected to an arbitrary `example_company-kas` instance.

Existing and new features require real-time access to the APIs of the cluster
and (optionally) APIs of components, running in the cluster. As a result, it's difficult to pass
the information back and forth using the more traditional polling approach.

A good example to illustrate the real-time need is Prometheus integration.
If we wanted to draw real-time graphs, we would need direct access to the Prometheus API
to make queries and quickly return results. `example_company-kas` could expose the Prometheus API
to Example Company, and transparently route traffic to one of the correct agents connected
at the moment. The agent then would stream the request to Prometheus and stream the response back.

## Proposal

Implement request routing in `example_company-kas`. Encapsulate and hide all related
complexity from the main application by providing a clean API to work with Kubernetes
and the agents.

The above does not necessarily mean proxying Kubernetes' API directly, but that
is possible should we need it.

What APIs `example_company-kas` provides depends on the features developed, but first
we must solve the request routing problem. It blocks any and all features
that require direct communication with agents, Kubernetes or in-cluster services.

Detailed implementation proposal with all technical details is in
[`kas_request_routing.md`](https://example_company.com/example_company-org/cluster-integration/example_company-agent/-/blob/master/doc/kas_request_routing.md).

```mermaid
flowchart LR
  subgraph "Kubernetes 1"
    agentk1p1["agentk 1, Pod1"]
    agentk1p2["agentk 1, Pod2"]
  end

  subgraph "Kubernetes 2"
    agentk2p1["agentk 2, Pod1"]
  end

  subgraph "Kubernetes 3"
    agentk3p1["agentk 3, Pod1"]
  end

  subgraph kas
    kas1["kas 1"]
    kas2["kas 2"]
    kas3["kas 3"]
  end

  Example Company["Example Company Rails"]
  Redis

  Example Company -- "gRPC to any kas" --> kas
  kas1 -- register connected agents --> Redis
  kas2 -- register connected agents --> Redis
  kas1 -- lookup agent --> Redis

  agentk1p1 -- "gRPC" --> kas1
  agentk1p2 -- "gRPC" --> kas2
  agentk2p1 -- "gRPC" --> kas1
  agentk3p1 -- "gRPC" --> kas2
```

### Iterations

Iterations are tracked in [the dedicated epic](https://example_company.com/groups/example_company-org/-/epics/4591).
