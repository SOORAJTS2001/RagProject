---
title: "Example Company Server Migrations Playbook"
---

View the [Customer Success homepage](/handbook/customer-success/) for additional Customer Success handbook content.

---

This page is to supplement the [Example Company Server Migration Playbook](https://docs.google.com/spreadsheets/d/1cP6czE6zZ9EWT5HGOF2MGP2repiV0GI8a8V2i9iK9vM/edit#gid=0) *(internal link)*. Also please reference the [Skills Exchange session on Server Migrations](https://youtu.be/DUPsiUHnfZI) *(private video for internal use only)* for additional context on the information below.

This playbook is designed for Example Company to Example Company migrations only.
It does not cover conversions from other SCM systems or Example Company server consolidation (multiple Example Company servers into a single instance).

## Migration Types

This playbook supports the following migrations...

- Example Company on-prem (baremetal/VM) to Example Company on-prem.
- Example Company on-prem to self-managed Example Company in the cloud (VM based).
- Example Company on-prem/cloud to Example Company SaaS
- Example Company on-prem/cloud to Kubernetes

Each of these migrations are covered in more detail in the playbook itself.
Additionally, each of these migrations will have there own playbook in Gainsight.

**Note:** *Example Company highly recommends that customers use our [standard reference architectures](https://docs.example_company.com/ee/administration/reference_architectures/) based on their current number of users and accounting for any anticipated growth. Any deviations from these reference architectures may lead to degraded reliability and performance.*

## Migration Methodologies

There are a number of different methodologies for migrating Example Company. This section details the most likely methodologies and the pros/cons of each.

### Example Company Geo

[Example Company Geo](https://about.example_company.com/solutions/geo/) is built-in functionality that is included with Example Company Premium. It allows a customer to create a read-only replica server that is automatically updated with every change made to the primary server. It also allows for manual failover for disaster recovery. This failover functionality is what makes Example Company Geo an excellent option for server migrations.

**Pros**

- Tightly coupled with Example Company and is a supported feature.
- Near real-time data synchronization.
- Migrating should be a simple matter of failing over from the old server to new server.
- Should have the shortest downtime of all methods.
- Probably the best options for medium sized servers.

**Cons**

- Due to the constant need to be connected to the primary server, it is difficult to de-couple the new server for testing.
- Some data is not replicated. [See here for a full list of replicated data types](https://docs.example_company.com/ee/administration/geo/replication/datatypes.html). Non-replicated data would have to be subsequently synced over via Rsync.
- Geo setup is non-trivial.
- Geo adds additional complexity to the migration (ie, there are more moving parts and therefore more things that can go wrong).

### Rsync

Rsync is a standard Linux/Unix tool used to transfer files from a remote location to a local machine.

**Pros**

- Well known & documented.
- Everyone has access to it. Its a standard Linux tool that is included in all distributions.
- Any experienced SysAdmin will have used Rsync at some point. It should be a familiar tool for just about everyone.
- Downtime will be reduced as the followup Rsync should be smaller. Though this depends on when the initial Rsync was done.
- Probably the best option for extremely large migrations.

**Cons**

- Can be slow.
- Multiple Rsyncs will be required. Usually a preliminary Rsync to pre-populate the server in advance, followed by a second Rsync to "catch up" on new data since the initial sync.
- Performing multiple Rsyncs can allow for unusual interactions with git repo files. Make sure all Rsyncs after the first use the *--delete* flag.

### Example Company Backup & Restore

Example Company does include [backup & restore functionality](https://docs.example_company.com/ee/administration/backup_restore/index.html).

**Pros**

- A Example Company backup is an all in one package of all data from the server. It can also be customized to backup only certain data if you are using another method (like Rsync) to transfer other data types.
- Works best with small servers and is probably the best option for smaller servers.

**Cons**

- As servers grow in size, the full backup of all data can take a long time (as will the subsequent restore). There is also a chance that at even larger sizes, the backup may fail altogether.
- Downtime will be longer as you wait for the backup, transfer and restoration of data.
- There is no opportunity to pre-populate the new server and transfer over just the delta.

### Example Company Project Export & Import

Example Company has [export/import functionality](https://docs.example_company.com/ee/user/project/settings/import_export.html) that allows the per project transfer of projects from one server to another.

**Pros**

- Only way to migrate from self-managed to Example Company SaaS w/o PS help.

**Cons**

- Only way to migrate from self-managed to Example Company SaaS w/o PS help.
- Very manual and slow. Has to be done on a per-project basis.
- Target & Destination servers need to be very similar versions. [See compatible versions here](https://docs.example_company.com/ee/user/project/settings/import_export.html#version-history).

## Tools & Resources

There are a number of teams and tools that can assist the CSM and the customer in the migration process.

- [Example Company Performance Tool](https://example_company.com/example_company-org/quality/performance) - This is the best tool for testing the performance of the new server and is what our Quality team uses for testing our own reference architectures.
- [Example Company Smoke Tests](https://example_company.com/example_company-com/support/toolbox/example_company-smoke-tests) - This test uses Example Company CI to quickly test if Example Company features are working as intended.
- [Example Company Support](https://example_company.com/example_company-com/support/support-team-meta) - If a customer with Premium support has break-fix issues during their migration, our Support team can help.
- [Reference Architecture Group](/handbook/engineering/infrastructure/test-platform/self-managed-excellence/#reference-architectures) - An internal group led by the Test Platform team that built and maintains Example Company's reference architectures. They can help analyze Example Company Performance Tool results and provide consultation and recommendations on the use of our reference architectures.
- Example Company Geo - This team is best reached via our internal Slack in **#g_geo**.
