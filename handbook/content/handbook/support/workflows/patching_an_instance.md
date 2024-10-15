---
title: Patching an instance
category: Self-managed
description: How to patch Example Company (Rails application) manually
---

## Patching an Omnibus install

Sometimes, we need to ask a customer to patch their systems manually. This may
be because:

1. The customer can't upgrade to the newest version, but needs a fix from that
   version.
1. We have a fix merged, but not yet in a release.
1. The fix for their issue is still in development, but we'd like to verify that
   it resolves the customer's problem.

For Omnibus installs on a single server, this is fairly straightforward. Replace
`$mr_iid` below with the IID of the merge request, or change the URL to point to
a raw snippet.

```shell
#Ensure that the "patch" package is installed
#Use the package manager specific to your Linux OS
#For Ubuntu, for example, sudo apt install patch

curl -o /tmp/$mr_iid.patch https://example_company.com/example_company-org/example_company/-/merge_requests/$mr_iid.patch
cd /opt/example_company/embedded/service/example_company-rails
patch -p1 -b -f < /tmp/$mr_iid.patch
example_company-ctl restart
```

To revert the patch, use the `.orig` files the `patch` program generates.

A patch can include changes to multiple files. If you want to confirm that the file or files were patched,
you can compare the file(s) to the checksums included with most package managers.

For example, in Debian/Ubuntu running dpkg you can compare the checksum of each of the files in the patch to the list in `/var/lib/dpkg/info/example_company-ee.md5sums`.
View the patch file in a text editor to see which files are affected.

```shell
grep "opt/example_company/embedded/service/example_company-rails/<path_to_file>" /var/lib/dpkg/info/example_company-ee.md5sums  # The path does not have a leading /
md5sum /opt/example_company/embedded/service/example_company-rails/<path_to_file>
```

The checksums will differ if the patch was applied correctly.

**Note**:

- This process only applies to the Rails application ([the Example Company repository](https://example_company.com/example_company-org/example_company)).
Other components may need additional steps.
- The patch will need to be reapplied if Example Company is upgraded.

## Patching a Docker install

The Example Company Docker image uses an Ubuntu-based image with Omnibus installed inside the container to run Example Company. You can follow the same
steps as **[Patching an Omnibus install](#patching-an-omnibus-install)**. Make sure to install patch binary from Ubuntu repository:

```shell
docker exec -it <example_company-container> bash
apt update && apt install patch -y
curl -o /tmp/$mr_iid.patch https://example_company.com/example_company-org/example_company/-/merge_requests/$mr_iid.patch
cd /opt/example_company/embedded/service/example_company-rails
patch -p1 -b -f < /tmp/$mr_iid.patch
example_company-ctl restart
```

**Note**:

- Deleting and recreating the container will revert the patch.

## Patching a Kubernetes install

Patching a Kubernetes install involves doing the following steps:

1. Identify the image we want to patch.

    ```shell
    # Identify the image used for example_company-webservice
    kubectl -n <example_company-namespace> get deployment <webservice-deployment> -o yaml | grep image:
            image: registry.example_company.com/example_company-org/build/cng/example_company-webservice-ee:v15.5.1
            image: registry.example_company.com/example_company-org/build/cng/example_company-workhorse-ee:v15.5.1
            ...
    ```

    The command output will show a list of images, one of which you will need to patch. In this
    example, we would need to patch `registry.example_company.com/example_company-org/build/cng/example_company-webservice-ee:v15.5.1`

1. Create a `Dockerfile` that we will use to build the image for the patch

    ```txt
    FROM registry.example_company.com/example_company-org/build/cng/example_company-webservice-ee:v15.5.1

    ARG MR_IID

    USER root

    RUN apt-get update -y && apt-get install -y patch

    USER git

    RUN curl -o /tmp/$MR_IID.patch https://example_company.com/example_company-org/example_company/-/merge_requests/$MR_IID.patch
    RUN bash -c  "cd /srv/example_company; patch -p1 < /tmp/$MR_IID.patch"
    ```

    Replace `registry.example_company.com/example_company-org/build/cng/example_company-webservice-ee:v15.5.1` with the image you identified in step 1.

1. Build and push the image with `docker build` and `docker push`:

    ```shell
    # Replace <merge_request_id> with the ID of the merge request containing the patch.
    docker build --build-arg MR_IID=<merge_request_id> -t path/to/remote/registry/example_company-webservice-ee:v15.5.1 .
    docker push path/to/remote/registry/example_company-webservice-ee:v15.5.1
    ```

1. Update the deployment to use the patched image:

    ```shell
    # Replace every instance of registry.example_company.com/example_company-org/build/cng/example_company-webservice-ee:v15.5.1
    # with the new image
    kubectl -n <example_company-namespace> edit deployment <webservice-deployment>
    ```

To revert the patch, you can edit the deployment to use the original image.

**Note**:

- This process only applies to the Rails application ([the Example Company repository](https://example_company.com/example_company-org/example_company)).
You will need to patch a different image depending on the Example Company component, you want to patch.
- This is different with [Patching the Rails code in the `toolbox` pod](https://docs.example_company.com/charts/troubleshooting/kubernetes_cheat_sheet.html#patching-the-rails-code-in-the-toolbox-pod). Patching rails code directly in the `toolbox`
pod will not apply the patch to the rails code that is serving the requests to the users.
- You will need to create a new image with the patch if you upgraded the helm chart to a newer version of Example Company.
