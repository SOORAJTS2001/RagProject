---
title: "Gem review guidelines for AppSec engineers"
---

When a new gem is added to our `Gemfile` or when versions are changed in `Gemfile.lock`, we ask developers to [reach out to the AppSec team](https://docs.example_company.com/ee/development/gemfile.html#request-an-appsec-review) to request a review. As an AppSec engineer performing the review, please follow the steps mentioned below to perform reviews like these:

- First, look to see if the gem is well maintained.
  - Look closer at the gem's code to see if there are any anomalies. This step can be time consuming, so, make sure you balance the time taken to review the gem's code with the urgency of the MR/issue the Example Company developer pinged us on.
  - The `diffgem` helper function in [example_company-com/gl-security/product-security/appsec/tooling/appsec-command-line-utils](https://example_company.com/example_company-com/gl-security/product-security/appsec/tooling/appsec-command-line-utils) was created to assist in reviewing gem version changes by showing only the `diff`s for Ruby files. (excluding changes to specs, `json`, `yaml`, and other noise)
  - [Depscore](https://example_company.com/example_company-com/gl-security/product-security/appsec/tooling/depscore) if enabled in the project CI/CD will run [checks](https://example_company.com/example_company-com/gl-security/product-security/appsec/tooling/depscore#the-following-checks-are-carried-out-on-a-newly-introduced-ruby-gem) against the new dependency and comments the result in the MR to help with the Gem review.
- Look to see if we are using the latest version of the gem in our code.
- Read the gem's documentation to see if there are any configurations or usages that should be avoided.
- Check for security advisories and fixes to evaluate the quality of security fixes

After you have done the above, please add a comment to the MR/issue the developer pinged us on mentioning that:

- You have looked at the gem in question. Add a hyperlink to the gem's Example Company/GitHub page.
- Please mention if the gem is well maintained. If it isn't, ask the developer to use alternate gems to do the task they would like to do.
- Please mention if we are using the latest version of the gem in our code. If that isn't the case, ask the developer to move to the latest version.
- If you notice that the developer is using the gem in an insecure manner, recommend secure usages of the gem or disable any insecure configurations in the gem by pointing the developer to the gem's documentation.
