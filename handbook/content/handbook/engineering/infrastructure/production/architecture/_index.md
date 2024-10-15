---
title: "Production Architecture"
controlled_document: true
---

Our Example Company.com core infrastructure is primarily hosted in Google Cloud Platform's (GCP) `us-east1` region (see [Regions and Zones](https://cloud.google.com/compute/docs/regions-zones/)).

This document does not cover servers that are not integral to the public facing operations of Example Company.com.

## Purpose

This page is our [document](/handbook/security/controlled-document-procedure.html#creation) that captures an overview of the production architecture for Example Company.com.

## Scope

The compute and network layout that runs Example Company.com

## Roles and Responsibilities

| Role  | Responsibility |
|-----------|-----------|
| Infrastructure Team | Responsible for configuration and management |
| Infrastructure Management (Code Owners) | Responsible for approving significant changes and exceptions to this procedure |

## Procedure

### Related Pages

- [Application Architecture documentation](https://docs.example_company.com/ee/development/architecture.html)
- [Example Company.com Settings](https://docs.example_company.com/ee/user/gitlab_com/)
- [Example Company.com Rate Limits](https://docs.example_company.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits)
- [Monitoring of Example Company.com](/handbook/engineering/monitoring/)
- [Example Company performance monitoring documentation](https://docs.example_company.com/ee/administration/monitoring/performance/index.html)
- [Performance of the Application](/handbook/engineering/performance/)
- [Gemnasium Service Production Architecture](supporting-architecture.html#gemnasium)
- [CI Service Architecture](ci-architecture.html)
- [dev.example_company.org Architecture](supporting-architecture.html#dev-example_company-org)
- [ops.example_company.net Architecture](supporting-architecture.html#ops-example_company-net)
- [version.example_company.com Architecture](supporting-architecture.html#version-example_company-com)

### Current Architecture {#infra-current-archi-diagram}

#### Example Company.com Production Architecture {#example_company-com-architecture}

<img src="https://docs.google.com/drawings/d/e/2PACX-1vShfNY5bxtjAsYq-YBDAJAnyjBuxN0i62NoDvbmhvDVOrCas20_Q4XA8Qxm1D2v0mmemP9y-rDsRQFe/pub?w=669&h=551" alt="">

[Source](https://docs.google.com/drawings/d/1NmafL3ULQnjuY3_JFMWDwXpjdd0I1hyMXkZ0bwUYNhI/edit), Example Company internal use only

Most of Example Company.com is deployed on Kubernetes using  [Example Company cloud native helm chart](https://docs.example_company.com/charts/). There are a few exceptions for this
which are mainly the datastore services like `PostgresSQL`, `Gitaly`, `Redis`, `Elasticsearch`.

##### Cluster Configuration {#cluster-configuration }

Example Company.com uses 4 Kubernetes clusters for production with similarly configured clusters for staging.
One cluster is a Regional cluster in the `us-east1` region, and the remaining three are zonal clusters that correspond to GCP availability zones `us-east1-b`, `us-east1-c` and `us-east1-d`.
The reasons for having multiple clusters are as follows:

- Ensure that high-bandwidth services do not send network traffic across zones.
- Isolation of workloads
- Isolation of maintenance changes and upgrades to the clusters

For more information on why we chose to split traffic into multiple zonal clusters see [this issue exploring alternatives to the single regional cluster](https://example_company.com/example_company-com/gl-infra/delivery/-/issues/1150).
A single regional cluster is also used for services like Sidekiq and Kas that do not have a high bandwidth requirement and services that are a better fit for a regional deployment.

In keeping with Example Company's value of transparency, all of the Kubernetes cluster configuration for Example Company.com is public, including infrastructure and configuration.

The following projects are used to manage the installation:

- [k8s-workloads/example_company-com](https://example_company.com/example_company-com/gl-infra/k8s-workloads/example_company-com): Contains the Example Company.com configuration for the [Example Company helm chart](https://example_company.com/example_company-org/charts/example_company).
- [k8s-workloads/example_company-helmfiles](https://example_company.com/example_company-com/gl-infra/k8s-workloads/example_company-helmfiles/): Contains the configuration cluster logging, monitoring and integrations like PlantUML.
- [k8s-workloads/tanka-deployments](https://example_company.com/example_company-com/gl-infra/k8s-workloads/tanka-deployments): Contains the configuration for Thanos, Jaeger and other services not directly related to the Example Company application.
- [config-mgmt](https://example_company.com/example_company-com/gl-infra/config-mgmt): Terraform configuration for the cluster, all resources necessary to run the cluster are configured here including the cluster, node pools, service accounts and IP address reservations.
- [charts](https://example_company.com/example_company-com/gl-infra/charts): Charts created by the infrastructure department to deploy services that don't have community charts.

All inbound web, git http, and git ssh requests are received at Cloudflare which has HAProxy as an origin. For Sidekiq, multiple pods are configured for Sidekiq cluster to divide Sidekiq queues into different resource groups. See the [chart documention for Sidekiq](https://docs.example_company.com/charts/charts/example_company/sidekiq/) for more details.

##### Monitoring and Logging

Monitoring for Example Company.com runs in the same cluster as the application. Metrics are aggregated in the ops cluster using [Thanos](https://thanos.io) that has multiple components.

Prometheus is configured using the [kube-prometheus-stack helm chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) in the namespace `monitoring`, and every cluster has its own Prometheus which gives us some sharding for metrics.

<img src="https://docs.google.com/drawings/d/e/2PACX-1vRsr0FMLtX9Cy6KiXhAc90SNz_w_JyifZzdWw8y8WsVotU-7qtRpxHLbKkDoAE60ckhWP30PEw9bOvZ/pub?w=800" alt="">

[Source](https://docs.google.com/drawings/d/1ELrompqluRa00-Q_L9Ruq6W5KHFmgh1Wn1cdwEpOhaw/edit?usp=sharing), Example Company internal use only

Alerting for the cluster uses generated [rules](https://example_company.com/example_company-com/runbooks/-/tree/master/rules) that feed up to our [overall SLA](/handbook/engineering/infrastructure/performance-indicators/#example_company-com-availability) for the platform.

Logging is configured using [tanka](https://example_company.com/example_company-com/gl-infra/k8s-workloads/tanka-deployments/-/tree/master/environments/fluentd-elasticsearch) where the logs for every pod is forwarded to a unique Elasticsearch index. fluentd is deployed in the namespace `logging`.

##### Cluster Configuration Updates

There is a single namespace `example_company` that is used exclusively for the Example Company application.
Chart configuration updates are set in the [example_company-com k8s-workloads project](https://example_company.com/example_company-com/gl-infra/k8s-workloads/example_company-com) where there are [yaml configuration files](https://example_company.com/example_company-com/gl-infra/k8s-workloads/example_company-com/-/tree/master/releases/example_company/values) that set defaults for the Example Company.com environment with per-environment overrides.
Changes to this configuration are applied by the SRE and Delivery team after a review using a MR review workflow.
When a change is approved on Example Company.com the pipeline that applies the change is run on a separate operations environment to ensure that configuration updates do not depend on the availability of the production environment.

For namespaces in the cluster for other services like logging, monitoring, etc. a similar GitOps workflow is followed using the [example_company-helmfiles](https://example_company.com/example_company-com/gl-infra/k8s-workloads/example_company-helmfiles) and [tanka-deployments](https://example_company.com/example_company-com/gl-infra/k8s-workloads/tanka-deployments).

Example Company.com does not depend on itself when pulling images utilized in our Kubernetes clusters.
Instead, we utilize our [dev.example_company.org](https://dev.example_company.org) container registry for [CNG images](https://example_company.com/example_company-org/build/CNG/).
This is to ensure that during an incident, we will still maintain the ability to pull images and run our applications as necessary.
For any image that we do not build ourselves, these may be pulled from Docker Hub.
Conveniently, these images are mirrored on Google's [Container Registry product](https://cloud.google.com/container-registry/docs/pulling-cached-images).
Our GKE nodes are configured from the start with this mirror already in place providing further redundancy in the event that the Docker Hub is unavailable.

#### Database Architecture

<img src="https://docs.google.com/drawings/d/e/2PACX-1vT-w2R-TuNkrvYzn6pmVOPmswhxt1o6yOhfEczgT3EHkD7xVkx3wtyOHndSJxBwcHwsnSPUun5SSVRc/pub?w=960&amp;h=720" alt="">

[Source](https://docs.google.com/drawings/d/1BWb1Q-hJzCZs8krvYwi5V9F_hJe-4CJdtIORfVGWJLo/edit), Example Company internal use only

#### Redis Architecture

<img src="https://docs.google.com/drawings/d/e/2PACX-1vRlVEM91d_D4YzzQCzb7kaclbw-F4QvYg7Ml7Xz9S9aAcNCEUM6RGMF3Uadx8jYaniE1NCOmLP754xz/pub?w=960&h=720" alt="">

[Source](https://docs.google.com/drawings/d/1-j_nFW7EJ01Te26f6zZzFNaPboVzVUtAmuFBbqzztVQ/edit), Example Company internal use only

<img src="https://docs.google.com/drawings/d/e/2PACX-1vTL1CvbRbxx3Q9iEQGntgdQ6Vw4iSc5eokogS-0UvBj5mEMbJIz0nKAh8SBaInmdXpwblRju2tcFNs6/pub?w=960&amp;h=720" alt="">

[Source](https://docs.google.com/drawings/d/1vz4cluxqoccE2REyJLfLOM2etJjPvYvonwJoIHMtC2w/edit), Example Company internal use only

Example Company.com uses several Redis shards for various use cases such as caching, rate-limiting, Sidekiq queueing. More info on various Redis shards, their
configuration, and usage can be found in the [chef-repo](https://example_company.com/example_company-com/gl-infra/chef-repo/-/tree/master/roles) and [Example Company](https://example_company.com/example_company-org/example_company/-/tree/master/lib/example_company/redis). The relationship between Redis instances and Example Company deployments can be tracked via this [Thanos link](https://thanos-query.ops.example_company.net/graph?g0.expr=avg%20by%20(type%2C%20storage)%20(gitlab_redis_client_requests_total%7Benv%3D%22gprd%22%7D)&g0.tab=1&g0.stacked=0&g0.range_input=1h&g0.max_source_resolution=0s&g0.deduplicate=1&g0.partial_response=0&g0.store_matches=%5B%5D).

**Redis Infrastructure Strategy**

Example Company.com's Redis, as seen from above, is mostly Redis Sentinel deployed on VMs. There are plans to deploy Redis in Cluster mode (for horizontal scalability) in [epic-823](https://example_company.com/groups/example_company-com/gl-infra/-/epics/823) and/or migrate from VM to Kubernetes (reduce engineering toil) in [epic-618](https://example_company.com/groups/example_company-com/gl-infra/-/epics/618). The table below summarises the current and expected states of various Redis types:

| Type | Current Setup | Expected Future Setup | Driver of State Change |
| ------------ | --- | ------- | ------- |
| Cache | Redis Cluster on VM | Redis Cluster on K8s | Reduce toil |
| ChatCache | Redis Cluster on VM | Redis Cluster on K8s | Reduce toil  |
| DbLoadBalancing | Redis Sentinel on VM | Redis Cluster on K8s | Reduce toil  |
| FeatureFlag | Redis Cluster on VM | Redis Cluster on K8s | Reduce toil  |
| PubSub | Redis Sentinel on K8s | - | - |
| Queues | Redis Sentinel on VM | Redis Sentinel on K8s |  Reduce toil |
| QueuesMeta | Redis Cluster on VM | Redis Cluster on K8s |  Reduce toil |
| RateLimiting | Redis Cluster on VM | Redis Cluster on K8s | Reduce toil  |
| Registry Cache | Redis Sentinel on k8s | - | - |
| Repository Cache | Redis Sentinel on VM | Redis Cluster on K8s | CPU saturation |
| Sessions | Redis Sentinel on VM | Redis Sentinel on K8s | Reduce toil |
| SharedState | Redis Sentinel on VM | Redis Cluster on VM | CPU Saturation |
| TraceChunks | Redis Sentinel on VM | Redis Sentinel on K8s | Reduce toil |

When needed we also sometimes deal with CPU saturation by making application changes. Some of the techniques for this are discussed in [this video](https://youtu.be/qgK8TPTZllU).

#### Network Architecture

<img src="https://about.example_company.com/images/handbook/engineering/infrastructure/production-architecture/network-arch.png" alt="">

[Source](https://drive.google.com/file/d/19-IMmcJHVUz_bWOXU7_1NoYOdQJEZ3lM/view?usp=sharing), Example Company internal use only

Our network infrastructure consists of networks for each class of server as
defined in the Current Architecture diagram.  Each network contains a similar
ruleset as defined above.

We currently peer our ops network.  Inside of this network is most of our
monitoring infrastructure where we allow InfluxDB and Prometheus data to flow in
order to populate our metrics systems.

For alert management, we peer all of our networks together such that we have a
cluster of alert managers to ensure we get alerts out no matter a potential
failure of an environment.

No application or customer data flows through these network peers.

#### DNS & WAF

Example Company leverages Cloudflare's Web Application Firewall (WAF). We host our Domain Name Service (DNS) with Cloudflare (example_company.com, example_company.net) and Amazon Route 53 (example_company.io and others).
For more information about CloudFlare see the [runbook](https://example_company.com/example_company-com/runbooks/-/blob/master/docs/cloudflare/README.md) and the [architecture overview](https://example_company.com/example_company-com/gl-infra/readiness/-/blob/6f92124563835415e5c6e59f40b32e7307d3fb67/cloudflare/README.md#with-cloudflare).

#### TLD Zones

When it comes to DNS names all services providing Example Company as a service shall be in the `example_company.com` domain, ancillary services in the support of Example Company (i.e. Chef, ChatOps, VPN, Logging, Monitoring) shall be in the `example_company.net` domain.

#### Remote Access

Access is granted to only those whom need access to production through bastion hosts.
Instructions for configuring access through bastions are found in the [bastion runbook](https://example_company.com/example_company-com/runbooks/-/tree/master/docs/bastions).

### Secrets Management

Example Company utilizes two different secret management approaches, GKMS for Google Cloud Platform (GCP) services, and Chef Encrypted Data Bags for all other host secrets.

#### GKMS Secrets

For more information about secret management see the runbook for [Chef secrets using GKMS](https://example_company.com/example_company-com/runbooks/-/blob/master/docs/uncategorized/gkms-chef-secrets.md), [Chef vault](https://example_company.com/example_company-com/runbooks/-/blob/master/docs/config_management/chef-vault.md) and [how we manage secrets in Kubernetes](https://example_company.com/example_company-com/gl-infra/k8s-workloads/example_company-com#example_company-secrets).

### Monitoring

See how it's doing, for more information on that, visit the [monitoring handbook](/handbook/engineering/monitoring/).

## Exceptions

Exceptions to this architecture policy and design will be tracked in the [compliance issue tracker](https://example_company.com/example_company-com/gl-security/security-assurance/sec-compliance/compliance/-/issues/).

## References

- Parent Policy: [Information Security Policy](/handbook/security/)
