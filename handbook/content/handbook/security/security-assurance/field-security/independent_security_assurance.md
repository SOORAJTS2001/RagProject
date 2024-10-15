---
title: Independent Security Assurance
---

## Overview

Example Company contracts with third parties to conduct annual network and application penetration testing and perform continuous public security scanning (BitSight). Evidence of these are shared via our [Customer Assurance Package](https://about.example_company.com/security/cap/).

## Third Party Security Ratings

BitSight is a third party security rating platform that utilizes public information collected across multiple domains to provide a numeric score from 250-900 (similar to a credit rating, but security focused). Example Company publishes three reports using BitSight:

- Example Company Production- this report represents the security posture of any URL or IP associated with supporting our [production architecture](/handbook/engineering/infrastructure/production/architecture/). Our goal is to maintain a rating of 700 or higher. Alerts from BitSight are monitored in real time and addressed as part of our [Vulnerability Management](/handbook/security/product-security/application-security/vulnerability-management.html) program.
- Example Company Sub-Production- this report represents the security posture of any URL or IP that does NOT support the Production Environment noted above. This generally includes test environments and/or environments that are purposely kept out-of-date for quality assurance activities. This score is not monitored by Example Company and does not represent Example Company's Security Posture.
- Example Company User-Managed- many of our customers utilize static pages as part of example_company.io. These pages are managed solely by our customers. However, from time to time, these pages are associated with Example Company erroneously. As such, we have moved any page on the Example Company.io domain to this report. This score is not monitored by Example Company and does not represent Example Company's Security Posture.

A copy of the Quarterly BitSight report and other Security Assurance artifacts are [available to download](https://about.example_company.com/resources/customer-assurance-package/example_company-cap-current.zip) in our [Customer Assurance Package](https://about.example_company.com/security/cap/).

## Third Party Vulnerability and Penetration Tests

### SaaS

**Customers are NOT authorized to conduct Vulnerability Scans or Penetration tests on Example Company's SaaS Application.** A penetration test determines whether or not defensive measures employed are strong enough to prevent security breaches. If our Customers or Prospects were to attempt their own penetration testing of our SaaS environment, it could appear as a real incident to Example Company. For more information, please review [Example Company's Terms of Service.](https://about.example_company.com/terms/)

Example Company conducts external, independent [penetration tests](/handbook/security/penetration-testing-policy.html) of our [production architecture](/handbook/engineering/infrastructure/production/architecture/) at least annually.  In lieu of this, a report of our Annual Penetration Test is available in our [Customer Assurance Package](https://about.example_company.com/security/cap/).

Example Company maintains a comprehensive Vulnerability Management program that is configured to identify vulnerabilities throughout our [production architecture](/handbook/engineering/infrastructure/production/architecture/). Details are available within our [Vulnerability Management](/handbook/security/product-security/application-security/vulnerability-management.html) handbook page.

### Self-Managed

Penetration testing and Vulnerability scanning performed by self-managed customers must utilize the standard omnibus deployment to prevent false positives based on custom configurations. Automated vulnerability scanners commonly produce low priority issues and/or false positives. Before submitting the results from a scanner, please take a moment to confirm that the reported issues are actually valid and exploitable. Identified and validated vulnerabilities can be submitted through our [HackerOne reporting program](https://hackerone.com/example_company) or by [creating an issue for our security team]({{< ref "engaging-with-security#creating-new-security-issues" >}}).

<div class="d-grid gap-2 my-4">
<a href="https://handbook.example_company.com/handbook/security/security-assurance/field-security/" class="btn bg-primary text-white btn-lg">Return to the Field Security Homepage</a>
</div>
