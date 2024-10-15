---
title: "Performance"
---

## Performance Facets

We categorize performance into 3 facets

1. [Backend](#backend-performance)
1. [Frontend](#frontend-performance)
1. [Infrastructure](#infrastructure-performance)

### Backend performance

Backend performance is scoped to response time of API, Controllers and command line interfaces (e.g. git).

**DRI**: [Christopher Lefelhocz](https://example_company.com/clefelhocz1), VP of Development.

Performance Indicators:

- [Memory Utilization (backlog)](https://example_company.com/example_company-com/www-example_company-com/-/issues/8841)

### Frontend performance

Frontend performance is scoped to response time of the visible pages and UI components of Example Company.

**DRI**: [Christopher Lefelhocz](https://example_company.com/clefelhocz1), VP of Development.

Performance Indicators:

- [Largest Contentful Paint (LCP)](/handbook/engineering/development/performance-indicators/#largest-contentful-paint-lcp)

### Infrastructure performance

Infrastructure performance is scoped to the performance of Example Company SaaS Infrastructure.

**DRI**: [Steve Loyd](https://example_company.com/sloyd), VP of Infrastructure.

Performance Indicators:

- [Example Company.com known application scaling bottlenecks](/handbook/engineering/infrastructure/performance-indicators/#gitlabcom-known-application-scaling-bottlenecks)

## Other Related Pages

- [Example Company.com (infra) Architecture](/handbook/engineering/infrastructure/production/architecture/)
- [Monitoring Example Company.com](/handbook/engineering/monitoring/)
- [Application Architecture Documentation](https://docs.example_company.com/ee/development/architecture.html)
- [Example Company.com Settings](https://docs.example_company.com/ee/user/gitlab_com/)
- [Example Company Performance Monitoring Documentation](https://docs.example_company.com/ee/administration/monitoring/performance/index.html)

**Meta issue** to track various issues listed here is at on the [infrastructure tracker](https://example_company.com/example_company-com/infrastructure/issues/2373).

## Example Company's Application performance

## Measurement

### Target

Performance of Example Company and Example Company.com is ultimately about the user experience. As also described in the [product management handbook](/handbook/product/example_company-the-product/#performance), "faster applications are better applications".

Our current focus at the moment are two indicators:

- **[Largest Contentful Paint](https://web.dev/lcp/)** (LCP) to measure the complete loading performance. To provide a good user experience, LCP should occur within 2.5 seconds of when the page first starts loading.
- **[Time to first Byte](https://web.dev/time-to-first-byte/)** (TTFB) so we have an understanding how long the backend takes to send the base page. Our target for a good backend rendering is below 500ms

On a mid term we target to focus on all of the [Web Vitals](https://web.dev/vitals/) with introducing also a bigger focus on **[First Input delay](https://web.dev/fid/)** (FID) and **[Cumulative Layout Shift](https://web.dev/cls/)** (CLS). So if routes are already performing well with our main indicators please extend optimisations on those.

There are many other performance metrics that can be useful in analyzing and prioritizing work, some of those are discussed in the sections below. But the user experienced LCP is the target for the site as a whole, and should be what everything ties back to in the end.

Groups should monitor closely the user experience in regards of performance to also improve the [perceived performance](https://developer.mozilla.org/en-US/docs/Learn/Performance/perceived_performance) also outside those measured performance indicators. For example if any action after loading is very slow and takes a lot of time.

### What we measure

Every end-user performance metric we can, through [sitespeed.io](https://www.sitespeed.io/) by having automatic runs every 4 hours. Any data we collect can be helpful to provide us to analyze for improvements or bottle necks on specific routes. We are sending the data to an graphite instance for continous data storage which is used for all Grafana dashboards. On top of that we also save full reports (links are visible by activating the `Runs` toggle on a sitespeed dashboard) to have more insight data, slow motion data, HAR files and full [Lighthouse](https://developers.google.com/web/tools/lighthouse) reports.

### How we measure

We currently measure with an empty cache, the connection limited to `Cable` and a medium CPU based machine which is located in `us-central` every 4 hours.

### Past and Current Performance

The URLs from Example Company.com listed in the table below form the basis for measuring performance improvements - these are heavy use cases. The times indicate time passed from web request to "the average time at which visible parts of the page are displayed" (per the definition of Speed Index). Since the "user" of these URLs is a controlled entity in this case, it represents an _external_  measure of our previous performance metric "Speed Index".

| Type |  [2018-04](https://storage.googleapis.com/sitespeed-results-example_company/example_company.com/2018-04-24-17-10-35/pages.html) | [2019-09](https://storage.googleapis.com/sitespeed-results-example_company/example_company.com/2019-09-13-08-28-42/pages.html) | [2020-02](https://storage.googleapis.com/sitespeed-results-example_company/example_company.com/2020-02-27-00-22-14/pages.html) | Now* |
| Issue List: [Example Company FOSS Issue List](https://example_company.com/example_company-org/example_company-foss/issues) | 2872 | <span class="text-success">1197</span> | - | N/A |
| Issue List: [Example Company Issue List](https://example_company.com/example_company-org/example_company/issues) |  |  | <span class="text-danger">1581</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab_issues&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Issue: [Example Company FOSS #4058](https://example_company.com/example_company-org/example_company-foss/issues/4058) | 2414 | <span class="text-success">1332</span> | <span class="text-danger">1954</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab-foss_issues_4058&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Issue Boards: [Example Company FOSS repo boards](https://example_company.com/example_company-org/example_company-foss/boards) | 3295 | <span class="text-success">1773</span> | - | N/A |
| Issue Boards: [Example Company repo boards](https://example_company.com/example_company-org/example_company/-/boards/) | | | <span class="text-danger">2619</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab_boards&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Merge request: [Example Company FOSS !9546](https://example_company.com/example_company-org/example_company-foss/merge_requests/9546) | 27644 | <span class="text-success">2450</span> | <span class="text-success">1937</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab-foss_merge_requests_9546&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Pipelines: [Example Company FOSS pipelines](https://example_company.com/example_company-org/example_company-foss/pipelines) | 1965 | <span class="text-danger">4098</span> | - | N/A |
| Pipelines: [Example Company pipelines](https://example_company.com/example_company-org/example_company/pipelines) | | | <span class="text-danger">4289</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab_pipelines&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Pipeline: [Example Company FOSS pipeline 9360254](https://example_company.com/example_company-org/example_company-foss/pipelines/9360254) | 4131 | <span class="text-success">2672</span> |  <span class="text-success">2546</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab-foss_pipelines_9360254&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Project: [Example Company FOSS project](https://example_company.com/example_company-org/example_company-foss) | 3909 | <span class="text-success">1863</span> | - | N/A |
| Project: [Example Company project](https://example_company.com/example_company-org/example_company) | | | <span class="text-success">1533</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Repository: [Example Company FOSS Repository](https://example_company.com/example_company-org/example_company-foss/tree/master) | 3149 | <span class="text-success">1571</span> | - | N/A |
| Repository: [Example Company Repository](https://example_company.com/example_company-org/example_company/tree/master) | | | <span class="text-danger">1867</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab_tree_master&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Single File: [Example Company FOSS Single File Repository](https://example_company.com/example_company-org/example_company-foss/blob/master/app/assets/javascripts/main.js) | 2000 | <span class="text-success">1292</span> | - | N/A |
| Single File: [Example Company Single File Repository](https://example_company.com/example_company-org/example_company/blob/master/app/assets/javascripts/main.js) | | | <span class="text-danger">2012</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_gitlab-org_gitlab_blob_master_app_assets_javascripts_main_js&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Explore: [Example Company explore](https://example_company.com/explore) | 2346 | <span class="text-success">1354</span> | <span class="text-success">1336</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_explore&var-browser=chrome&var-connectivity=cable&var-function=median) |
| Snippet: [Example Company Snippet 1662597](https://example_company.com/snippets/1662597) | 1681 | <span class="text-success">1082</span> | <span class="text-danger">1378</span> | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary?orgId=1&var-base=sitespeed_io&var-path=desktop&var-group=gitlab_com&var-page=_snippets_1662597&var-browser=chrome&var-connectivity=cable&var-function=median) |

*To access the sitespeed grafana dashboards you need to be logged into your Google account

**Note:** Since this table spans time before and after single-codebase we kept Example Company FOSS pages close to Example Company ones to enable comparisons despite not being exactly the same project.

#### All Sitespeed Dashboards

[Sitespeed - Site summary](https://dashboards.example_company.net/d/000000045/sitespeed-site-summary?orgId=1)

[Sitespeed - Page summary](https://dashboards.example_company.net/d/000000043/sitespeed-page-summary)

[Sitespeed - Page timing summaries](https://dashboards.example_company.net/d/000000044/sitespeed-page-timing-metrics)

If you activate the `runs` toggle you will have annotations with links to all full reports. Currently we are running measurements every 2 hours.

---

## Steps

### Web Request {#flow-of-web-request}

All items that start with the tachometer (<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>) symbol represent a step in the flow that we _measure_. Wherever possible, the tachometer icon links to the relevant dashboard in our [monitoring](/handbook/engineering/monitoring/). Each step in the listing below links back to its corresponding entry in the [goals table](#web-goals-table).

Consider the scenario of a user opening their browser, and surfing to their dashboard by typing `example_company.com/dashboard`, here is what happens:

1. <a name="request-reaches-be"></a> [**User request**](#tb-request-reaches-be)
    1. <a name="start-request"></a> User enters example_company.com/dashboard in their browser and hits enter
    1. <a name="lookup-ip"></a> [Lookup IP in DNS](#tb-lookup-ip) (not measured)
       - Browser looks up IP address in DNS server
       - DNS request goes out and comes
    back (typically ~10-20 ms, [data?]; often times it is already cached so
      then it would be faster).
       - For more details on the steps from browser to application, enjoy reading <https://github.com/alex/what-happens-when>
    1. <a name="browser2azlb"></a> [Browser to Azure LB](#tb-browser2azlb) (not measured)
       - Now that the browser knows where to find the IP address, browser sends the web
    request (for example_company.com/dashboard) to Azure's load balancer (LB).
1. <a name="backend-processes"></a> [**Backend processes**](#tb-backend-processes)
    1. <a name="azlb2haproxy"></a> [Azure LB to HAProxy](#tb-azlb2haproxy) (not measured)
       - Azure's load balancer determines where to route the packet (request), and
       sends the request to our Frontend Load Balancer(s) (also referred to as
         HAProxy).
    1. <a name="haproxy-ssl"></a> [HAProxy SSL with browser](#tb-haproxy-ssl) (not measured)
       - HAProxy (load balancer) does SSL negotiation with the browser
    1. <a name="haproxy2nginx"></a> [HAProxy to NGINX](#tb-haproxy-ssl) (not measured)
       - HAProxy forwards the request to NGINX in one of our front end workers.
       In this case, since we are tracking a web request, it would be the NGINX box in the
         "Web" box in the [production-architecture diagram](/handbook/engineering/infrastructure/production/architecture/); but alternatively the request can come in via API or a git command
         from the command line, hence the API, and git "boxes" in that diagram.
       - Since all of our servers are in ONE Azure VNET, the overhead of SSL
          handshake and teardown between HAProxy and NGINX should be close to negligible.
    1. <a name="nginx-buffer"></a> [NGINX buffers request](#tb-nginx-buffer) (not measured)
       - NGINX gathers all network packets related to the request ("request
       buffering"). The request may be split into multiple packets by the intervening network,
       for more on that, read up on [MTUs](https://en.wikipedia.org/wiki/Maximum_transmission_unit).
       - In other flows, this won't be true. Specifically, request buffering is
       [switched off for LFS](https://example_company.com/example_company-org/example_company-workhorse/issues/130).
    1. <a name="nginx2workhorse"></a> [NGINX to Workhorse](#tb-nginx2workhorse) (not measured)
       - NGINX forwards the full request to Workhorse (in one combined request).
    1. <a name="workhorse2various"></a> [Workhorse distributes request](#tb-workhorse2various)
       - Workhorse splits the request into parts to forward to:
       - <a name="workhorse2unicorn"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=13&fullscreen&orgId=1)
       [Unicorn](#tb-workhorse2unicorn).  Time spent waiting for Unicorn to pick up a request is `HTTP queue time`.
       - <a name="workhorse2gitaly"></a> [Gitaly](#tb-workhorse2gitaly) [not in this scenario, but not measured in any case]
       - <a name="workhorse2nfs"></a> [NFS](#tb-workhorse2nfs) (git clone through HTTP) [not in this scenario, but not measured in any case]
       - <a name="workhorse2redis"></a> [Redis](#tb-workhorse2redis) (long polling) [not in this scenario, but not measured in any case]
    1. <a name="unicorn2various"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=2&fullscreen&orgId=1) [Unicorn calls services](#tb-unicorn2various)
       - Unicorn, (often just called "Rails", or "application server"),
       translates the request into a Rails controller request; in this case
       `RootController#index`. The round trip time it takes for a request to
       _start_  in Unicorn and _leave_ Unicorn is what we call `Transaction
       Timings`. RailsController requests are sent to (and data is received from):
       - <a name="unicorn2db"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=9&fullscreen&orgId=1) [PostgreSQL](#tb-unicorn2db) (`SQL timings`),
       - <a name="unicorn2nfs"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/daily-overview?panelId=14&fullscreen&orgId=1) [NFS](#tb-unicorn2nfs) (`git timings`),
       - <a name="unicorn2redis"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/daily-overview?panelId=13&fullscreen&orgId=1) [Redis](#tb-unicorn2redis) (`cache timings`).
       - In this `example_company.com/dashboard` example, the controller addresses all three [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/d/web-rails-controller/web-rails-controller?orgId=1&var-PROMETHEUS_DS=Global&var-environment=gprd&var-stage=main&var-controller=RootController&var-action=index).
       - There are usually _multiple_ SQL calls (or file, or cache, etc.) calls for a given
      controller request. These add to the overall timing, especially since they are
      sequential. For example, in
      this scenario, there are [29 SQL calls (search for `Load`)](http://profiler.gitlap.com/20170524/901687e2-9fa1-4256-8414-c4835dc31dbc.txt.gz)
      when this _particular user_ hits `example_company.com/dashboard/issues`. The number of SQL calls
      will depend on how many projects the person has, how much may already be in cache, etc.
       - Rails tackles the steps within a controller request sequentially.
          In other words if it needs to make calls out to the database and to
          git, it is not set up to those in parallel but rather has to wait for
          the response to the first step before proceeding to the next step.
       - In the Rails stack, middleware typically adds to the number of round trips
       to Redis, NFS, and PostgreSQL, per controller call, in addition to the
       timings of Rails controllers.  Middleware is used for {session state, user
      identity, endpoint authorization, rate limiting, logging, etc} while the
      controllers typically have at least one round trip for each of {retrieve
      settings, cache check, build model views, cache store, etc.}. Each such
      roundtrip is _estimated_ to take < 10 ms.
    1. <a name="unicorn-views"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=8&fullscreen&orgId=1)  [Unicorn constructs Views](#tb-unicorn-views)
         - The construction of views can take a long time (`view timings`).
         In some controllers, data is gathered _first_ after which a view is
         constructed. In other controllers, data is gathered _from within_  a
         View, so that the `view timing` in those cases includes the time it
         took to call NFS, PostgreSQL, Redis, etc. And in many cases, both are done.
         - A particular view in Rails will often be constructed from multiple partial
        views. These will be used from a template file, specified by the controller
        action, that is, itself, generally included within a layout template.
        Partials can include other partials. This is done for good code
        organization and reuse. As an example, when the _particular user_  from the
        example above loads `example_company.com/dashboard/issues`, there are [56 nested / partial views rendered (search for `View::`)](http://profiler.gitlap.com/20170524/901687e2-9fa1-4256-8414-c4835dc31dbc.html.gz)
         - Partial views may be cached via various [Rails techniques](http://guides.rubyonrails.org/caching_with_rails.html), such as Fragment Caching. In addition,
         Example Company has a Markdown cache stored in the database that is used to
         speed up the conversion of Markdown to HTML.
         - Perceived performance in the way of First Paint can be affected by
         how much of the content of a view is rendered by the backend vs.
         sending a "minimal" html blob to the user and relying on Javascript /
         AJAX / etc. to fetch additional elements that take the page from First
         Paint to "Fully Loaded". See the section about the frontend for more on this.
    1. <a name="unicorn2html"></a> [Unicorn makes HTML](#tb-unicorn2html) (not measured)
        - Once the Views are built, Unicorn completes making the "HTML blob" that
        is then returned to the browser.
        - Some of these blobs are expensive to compute, and are sometimes hard-coded
      to be sent from Unicorn to Redis (i.e. to cache) once rendered.
    1. <a name="html2browser"></a> [HTML to Browser](#tb-html2browser) (not measured)
       - The HTML blob is sent back to the Browser via the following path:
       - <a name="unicorn2workhorse"></a> [Unicorn to Workhorse](#tb-unicorn2workhorse) (not measured)
       - <a name="workhorse2nginx"></a> [Workhorse to NGINX](#tb-workhorse2nginx) (not measured)
       - <a name="nginx2haproxy"></a> [NGINX to HAProxy](#tb-nginx2haproxy) (not measured)
       - <a name="haproxy2azlb"></a> [HAProxy to Azure LB](#tb-haproxy2azlb) (not measured)
       - <a name="azlb2browser"></a> [Azure LB to Browser](#tb-azlb2browser) (not measured)
1. <a name="renderpage"></a> [**Render Page**](#tb-renderpage)
    1. <a name="browser-firstbyte"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/example_company-web-status?refresh=1m&panelId=14&fullscreen&orgId=1&from=now-90d&to=now) [**First Byte**](#tb-browser-firstbyte)
      - The time when the browser receives the first byte.
      In addition to everything in the backend, this also depends on network speed.
      In the dashboard linked to by the tachometer above, First Byte is measured
      from a Digital Ocean box in the US with relatively little network lag thus
      representing an estimate of _internal_ First Byte. Past performance on
      first byte is recorded [elsewhere on this page](#external).
      - For any page, you can use your browser's "inspect" tool to look at "TTFB" (time to first byte).
      - [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/)
      `First Byte - External` is measured for a hand selected number of URLs using [SiteSpeed](https://www.sitespeed.io/)
    1. <a name="reaching-speed-index"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/) [**Speed Index**](#tb-reaching-speed-index)
      - Browser parses the HTML blob and sends out further requests
      to Example Company.com to fetch assets such as javascript bundles, CSS, images, and
      webfonts.
      - The timing of this step depends (amongst other things) on the number and
      the size of assets, as well as network speed. For _each_ static asset, there is a
      round-trip of:
            - for cached assets: browser <i class="fas fa-long-arrow-alt-right fa-fw"
           aria-hidden="true"></i> nginx <i class="fas fa-long-arrow-alt-right fa-fw"
           aria-hidden="true"></i> nginx confirms cached asset is still valid <i
           class="fas fa-long-arrow-alt-right fa-fw" aria-hidden="true"></i> browser
            - for non-cached or expired cached assets: browser <i class="fa
           fa-long-arrow-right fa-fw" aria-hidden="true"></i> workhorse <i class="fa
           fa-long-arrow-right fa-fw" aria-hidden="true"></i> workhorse grabs asset
           from local cache <i class="fas fa-long-arrow-alt-right fa-fw"
         aria-hidden="true"></i> browser.
            - for a page that is served through Example Company Pages: browser <i class="fa
           fa-long-arrow-right fa-fw" aria-hidden="true"></i> pages daemon
           (independent service in the architecture) <i class="fas fa-long-arrow-alt-right
           fa-fw" aria-hidden="true"></i> browser.
      - Stylesheets can block page rendering by default, which can lead to
      unnecessary delays in page rendering.
      - Starting in 9.5, scripts won't block rendering anymore as they are
      loaded with `defer="true"`, so they are parsed and executed in the same
      order as they are called but only after html + css has been rendered.
      - Enough meaningful content is rendered on screen to calculated the "Speed Index".
    1. <a name="reaching-fullyloaded"></a> [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/) [Fully Loaded](#tb-reaching-fullyloaded)
      - When the scripts are loaded, Javascript compiles and evaluates them within the page.
      - On some pages, we use AJAX to allow for async loading. The AJAX call can
      be triggered by all kinds of things; for example a frontend element (button)
      or e.g. the `DOMContentLoaded` event. The new call is for a new URL, and such requests are routed either
      through the Web or API workers, invoke their respective Rails controllers
      on the backend, and return the requested files (HTML, JSON, etc).
      For example, the calendar and activity feeds on a username page `example_company.com/username`
      are two separate AJAX calls, triggered by `DOMContentLoaded`. (The
      `DOMContentLoaded` event "marks the point when both the [DOM](https://css-tricks.com/dom/)
      is ready and there are no stylesheets that are blocking JavaScript
      execution" (taken from an article about the [critical rendering path](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/measure-crp))).
      The alternative to using AJAX would be to include the full Rails code to
      generate the calendar and activity feed within the same controller that
      is called by the example_company.com/username URL; which would lead to slower First
      Paint since it simply involves more calls to the database etc.

---

### Git Commit Push

First read about the [steps in a web request](#web-request) above, then pick up the thread here.

After pushing to a repository, e.g. from the _web UI_:

1. In a web browser, make an edit to a repo file, type a commit message, and hit "Commit"
1. NGINX receives the git commit and passes it to Workhorse
1. Workhorse launches a `git-receive-pack` process (on the workhorse machine) to save the new commit to NFS
1. On the workhorse machine, `git-receive-pack` fires a [git hook](https://docs.example_company.com/ee/administration/server_hooks.html) to trigger `Example Company Shell`.
   - Example Company Shell accepts Git payloads pushed over SSH and acts upon them (e.g. by checking if you're authorized to perform the push, scheduling the data for processing, etc).
   - In this case, Example Company Shell provides the `post-receive` hook, and the `git-receive-pack` process passes along details of what was pushed to the repo to the `post-receive` hook. More specifically, it passes a list of three items: old revision, new revision, and ref (e.g. tag or branch) name.
1. Workhorse then passes the `post-receive` hook to Redis, which is the Sidekiq queue.
   - Workhorse informed that the push succeeded or failed (could have failed due to the repo not available, Redis being down, etc.)
1. Sidekiq picks up the job from Redis and removes the job from the queue
1. Sidekiq updates PostgreSQL
1. Unicorn can now query PostgreSQL.

---

## Goals

### Web Request

Consider the scenario of a user opening their browser, and surfing to their favorite URL on `Example Company.com`. The steps are described in the section on ["web request"](#web-request). In this table, the steps are measured and goals for improvement are set.

Guide to this table:

- All times are reported in milliseconds.
- `# per request` : average number of times this step occurs per request. For instance, an average "transaction" may require [0.2 SQL calls, 0.4 git calls, 1 call to cache](https://docs.google.com/spreadsheets/d/15mhXjwkx2lOXJps7lsp_o0zbwGSyOdYOTc8-McwBy0A/pubhtml), and 30 nested views to be built.
- `p99 Q2-17`: the p99 timing (in milliseconds) at the end of Q2, 2017
- `p99 Now`: link to the dashboard that displays the _current_ p99 timing
- `p99 Q3-17`: the target for the p99 timing by the end of Q3, 2017
- Numbers in _italics_ are _per event_  and/or _in parallel_  with other timings, and therefore do not sum to the (sub)totals. The non-italic numbers _do_ sum to the (sub)totals.

<a name="web-goals-table"></a>

| Step                                                    | # per request | p99 Q2-17 | p99 Now | p99 Q3-17 goal | Issue links and impact |
|---------------------------------------------------------|--------------:|--------:|--------:|-------------:|------------------------|
| <a name="tb-request-reaches-be"></a>[**USER REQUEST**](#request-reaches-be) |               |         |         |              |                        |
| <a name="tb-lookup-ip"></a>[Lookup IP in DNS](#lookup-ip)                          |     1         |~10| ? |~10|  [Use a second DNS provider](https://example_company.com/example_company-com/infrastructure/issues/1711)  |
| <a name="tb-browser2azlb"></a>[Browser to Azure LB](#browser2azlb)                    |     1         |~10| ? |~10|                        |
| <a name="tb-backend-processes"></a>[**BACKEND PROCESSES**](#backend-processes) |    |         |         |              | [Extend monitoring horizon](https://example_company.com/example_company-com/infrastructure/issues/1879) |
|<a name="tb-azlb2haproxy"></a>[Azure LB to HAProxy](#azlb2haproxy)                     |     1         |~2| ? |~2|                        |
|<a name="tb-haproxy-ssl"></a>[HAProxy SSL with Browser](#haproxy-ssl)                 |     1         |~10| ? |~10| [Speed up SSL](https://example_company.com/example_company-com/infrastructure/issues/2321) |
|<a name="tb-haproxy2nginx"></a>[HAProxy to NGINX](#haproxy2nginx)              |     1         |~2| ? |~2|                        |
|<a name="tb-nginx-buffer"></a>[NGINX buffers request](#nginx-buffer)                   |     1         |~10| ? |~10|                        |
|[<a name="tb-nginx2workhorse"></a>[NGINX to Workhorse](#nginx2workhorse)          |     1         |~2|  ? |~2|                        |
|<a name="tb-workhorse2various"></a>[Workhorse distributes request](#workhorse2various)      |     1         |         |         |      | [Adding monitoring to workhorse](https://example_company.com/example_company-com/infrastructure/issues/2025) |
|<a name="tb-workhorse2unicorn"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Workhorse to Unicorn_](#workhorse2unicorn) | 1 | 18  | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=13&fullscreen&orgId=1) | 10 | [Adding Unicorns](https://example_company.com/example_company-com/infrastructure/issues/1883) |
|<a name="tb-workhorse2gitaly"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Workhorse to Gitaly_](#workhorse2gitaly)   | |     | ?  |     |   |
|<a name="tb-workhorse2nfs"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Workhorse to NFS_](#workhorse2nfs)         | |     | ?  |     |   |
|<a name="tb-workhorse2redis"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Workhorse to Redis_](#workhorse2redis)      | |     | ?  |     |   |
|<a name="tb-unicorn2various"></a>[Unicorn calls services](#unicorn2various)          |  1  |  2500       | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=2&fullscreen&orgId=1)  |  1000 | [Allow more Example Company internals monitoring](https://example_company.com/example_company-org/example_company-ce/issues/28465)    |
|<a name="tb-unicorn2db"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Unicorn_ <i class="fas fa-arrows-alt-h fa-fw" aria-hidden="true"></i> _Postgres_](#unicorn2db)      | | _250_ |[<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=9&fullscreen&orgId=1)| _100_ | [Speed up slow queries](https://example_company.com/example_company-org/example_company-ce/issues/34535)  |
|<a name="tb-unicorn2nfs"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Unicorn <i class="fas fa-arrows-alt-h fa-fw" aria-hidden="true"></i> NFS_](#unicorn2nfs)          | | _460_ | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/daily-overview?panelId=14&fullscreen&orgId=1)  | _200_ | [Move to Gitaly](https://example_company.com/example_company-org/gitaly/issues/313) - [sample result](https://example_company.com/example_company-com/infrastructure/issues/1912#note_31368476) |
|<a name="tb-unicorn2redis"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Unicorn <i class="fas fa-arrows-alt-h fa-fw" aria-hidden="true"></i> Redis_](#unicorn2redis)       | |  _18_ | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/daily-overview?panelId=13&fullscreen&orgId=1) |     |   |
|<a name="tb-unicorn-views"></a>[Unicorn constructs Views](#unicorn-views) |  | 1500   | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=8&fullscreen&orgId=1)  |  |       |
|<a name="tb-unicorn2html"></a>[Unicorn makes HTML](#unicorn2html) |  |    |   |  |       |
|<a name="tb-html2browser"></a>[HTML to Browser](#html2browser) |  |    |   |  |       |
|<a name="tb-unicorn2workhorse"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Unicorn to Workhorse_](#unicorn2workhorse) | 1 | ~2 | ?  | ~2  |  |
|<a name="tb-workhorse2nginx"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Workhorse to NGINX_](#workhorse2nginx)             |      1        | ~2| ? |~2|                        |
|<a name="tb-nginx2haproxy"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_NGINX to HAProxy_](#nginx2haproxy)                 |      1        |~2| ? |~2| [Compress HTML in NGINX](https://example_company.com/example_company-org/example_company-ce/issues/33719)  |
|<a name="tb-haproxy2azlb"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_HAProxy to Azure LB_](#haproxy2azlb)               |      1        |~2| ? |~2|                        |
|<a name="tb-azlb2browser"></a>&nbsp;&nbsp;&nbsp;&nbsp;[_Azure LB to Browser_](#azlb2browser)               |      1        |~20| ? |~20|                        |
|<a name="tb-renderpage"></a>[**RENDER PAGE**](#renderpage) |  |         |         |              |                        |
|<a name="tb-browser-firstbyte"></a> [**FIRST BYTE**](#browser-firstbyte) (see [note 1][^1])]  |   | **1080 - 6347** |   [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](https://dashboards.example_company.net/dashboard/db/example_company-web-status)      | **1000**  |                        |
|<a name="tb-reaching-speed-index"></a>[**SPEED INDEX**](#reaching-speed-index) (see [note 2][^2]) |  | **3230 - 14454** | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/)  |   **2000**     | [Remove inline scripts](https://example_company.com/example_company-org/example_company-ce/issues/34903), [Defer script loading when possible](https://example_company.com/example_company-org/example_company-ce/merge_requests/12759), [Lazy load images](https://example_company.com/example_company-org/example_company-ce/issues/34361), [Set up a CDN for faster asset loading](https://example_company.com/example_company-com/infrastructure/issues/2092), [Use image resizing in CDN](https://example_company.com/example_company-org/example_company-ce/issues/34364) |
|<a name="tb-reaching-fullyloaded"></a>[Fully Loaded](#reaching-fullyloaded) (see [note][^3]) |  |   6093 - 14003   |  [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/)  |  not specified  |   [Enable webpack code splitting](https://example_company.com/example_company-org/example_company-ce/issues/33391) |
|---------------------------------------------------------|---------------|---------|---------|--------------|------------------------|

**Notes:**

[^1]: 1\. <a name="note-blackbox"></a> The range here corresponds to the range in First Byte times of the 4 sample URLs provided in the First Byte [table](#first-byte). However, based on all _non-staging_ URL's measured in [this dashboard](https://dashboards.example_company.net/dashboard/db/example_company-web-status?refresh=1m&panelId=14&fullscreen&orgId=1&from=now-90d&to=now), between 2017-03-30 and 2017-06-28, the number would be 3,833 ms.
[^2]: 2\. <a name="note-fp-times"></a> The range here corresponds to the range in Speed Indices of the 4 sample URLs provided in the Speed Index table.
[^3]: 3\. <a name="note-fl-time"></a> The range here corresponds to the range in Fully Loaded times of the 4 sample URLs provided in the Speed Index table.

### Git Commit Push

_Table to be built; merge requests welcome!_

## Modifiers

For any performance metric, the following modifiers can be applied:

- **User**: how a _real_  Example Company user would experience and measure the time.
- **Internal**: the time as measured from _inside_  Example Company.com's infrastructure (the boundary is defined as being at the "network | Azure load balancer" interface).
- **External**: the time as measured from any specified point outside Example Company.com's infrastructure; for example a DO box with Prometheus monitoring or a browser in a specified geo-region on a specified network speed.

## First byte

### External

Timing history for First Byte are listed in the table below (click on the tachometer icons for _current_ timings). All times are in milliseconds.

| Type |  End of Q4-17 | Now |
|------|--------------:|-------------:|-------------:|-----|
| Issue: [Example Company CE #4058](https://example_company.com/example_company-org/example_company-ce/issues/4058) | [857](http://207.154.197.115/gl/sitespeed-result/example_company.com/2017-12-27-19-26-37/pages/example_company.com/example_company-org/example_company-ce/issues/4058/index.html) | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/) |
| Merge request: [Example Company CE !9546](https://example_company.com/example_company-org/example_company-ce/merge_requests/9546) | [18673](http://207.154.197.115/gl/sitespeed-result/example_company.com/2017-12-27-19-26-37/pages/example_company.com/example_company-org/example_company-ce/merge_requests/9546/index.html) | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/) |
| Pipeline: [Example Company CE pipeline 9360254] | [1529](http://207.154.197.115/gl/sitespeed-result/example_company.com/2017-12-27-19-26-37/pages/example_company.com/example_company-org/example_company-ce/pipelines/9360254/index.html) | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/) |
| Repo: [Example Company CE repo](https://example_company.com/example_company-org/example_company-ce/tree/master) | [1076](http://207.154.197.115/gl/sitespeed-result/example_company.com/2017-12-27-19-26-37/pages/example_company.com/example_company-org/example_company-ce/tree/master/index.html) | [<i class="fas fa-tachometer-alt fa-fw" aria-hidden="true"></i>](http://207.154.197.115/gl/sitespeed-result/example_company.com/) |

### Internal {#first-byte-internal}

To go a little deeper and measure performance of the application & infrastructure without consideration for frontend and network aspects, we look at "transaction timings" [as recorded by Unicorn](#unicorn2various). These timings can be seen on the
[Rails Controller dashboard](https://dashboards.example_company.net/d/web-rails-controller/web-rails-controller?orgId=1&var-PROMETHEUS_DS=Global&var-environment=gprd&var-stage=main&var-controller=Projects::MergeRequestsController&var-action=show) _per URL that is accessed_ .

## Availability and Performance labels {#availability-performance-labels}

### Availability

This section has been moved to [Availability severity](/handbook/engineering/infrastructure/engineering-productivity/issue-triage#availability).

### Performance

To clarify the priority of issues that relate to Example Company.com's performance you should add the `~performance` label, as well as a "Severity"

label. There are two factors that influence which severity label you should
pick:

1. How frequently something is used.
2. How likely it is for something to cause an outage.

For strictly performance related work you can use the [Controller Timings Overview](https://dashboards.example_company.net/dashboard/db/controller-timings-overview?)
Grafana dashboard. This dashboard categorises data into three different
categories, each with their associated severity label:

1. Frequently Used: `~severity::2`
2. Commonly Used: `~severity::3`
3. Rarely Used: `~severity::4`

This means that if a controller (e.g. `UsersController#show`) is in the
"Frequently Used" category you assign it the `~severity::2` label.

For database related timings you can also use the
[SQL Timings Overview](https://dashboards.example_company.net/dashboard/db/sql-timings-overview?orgId=1).
This is the dashboard primarily used by the Database Team to determine the AP
label to use for database related performance work.

## Database Performance

Some general notes about parameters that affect database performance, at a very crude level.

- From whitebox monitoring,
  - Of time spent on/by Rails controllers, this much is spent in the database: <https://dashboards.example_company.net/d/web-rails-controller/web-rails-controller?viewPanel=13864&orgId=1> (for a specific Rails controller / page)
  - _Global_ SQL timings: <https://dashboards.example_company.net/dashboard/db/transaction-overview?panelId=9&fullscreen&orgId=1&from=now-2d&to=now>
- A single HTTP request will execute a single controller. A controller in turn will usually only use one available database connection, though it may use 2 if first a read was performed, followed by a write.
  - pgbouncer allows up to 150 concurrent PostgreSQL connections. If this limit
is reached it will block pgbouncer connections until a PostgreSQL connection becomes available.
  - PostgreSQL allows up to 300 connections (connected, whether they're active or not doesn't matter). Once this limit is reached new connections will be rejected, resulting in an error in the application.
  - When the number of processes > number of cores available on the database servers, the CPU constantly switches cores to run the requested processes; this contention for cores can lead to degraded performance.
- As long as the database CPU load < 100% (<https://dashboards.example_company.net/dashboard/db/postgresql-overview?refresh=5m&orgId=1&from=now%2Fw&to=now&panelId=13&fullscreen>), then in theory the database can handle more load without adding latency. In practice database specialists like to keep CPU load below 50%.
  - As an example of how load is determined by underlying application design:
       DB CPU percent used to be lower (20%, prior to 9.2, then up to 50-75% [when 9.2 RC1 went live](https://example_company.com/example_company-org/example_company-ce/issues/32536), then back down to 20% by the time 9.2 was released.
- pgbouncer
  - What it does: pgbouncer maps _N_ incoming connections to _M_ PostreSQL connections, with _N_ >= _M_ (_N_ < _M_ would make no sense). For example, you can map 1024 incoming connections to 10 PostgreSQL connections. This is mostly influenced by the number of concurrent queries you want to be able to handle. For example, for Example Company.com our primary rarely goes above 100 (usually it sits around 20-30), while secondaries rarely go above 20-30 concurrent queries. The more secondaries you add, the more you can spread load and thus require fewer connections (at the
  cost of having more servers).
  - Analogy: pgbouncer is a bartender serving drinks to many customers. Instead of making the drinks himself she instructs 1 out of 20 "backend" bartenders to do so. While one of these bartenders is working on a drink the other 19 (including the "main" one) are available for new orders. Once a drink is done one of the 20 "backend" bartenders gives it to the main bartender, which in turn gives it to the customer that requested the drink. In this analogy, the _N_ incoming connections are the patrons of the bar, and there are _M_ "backend"
   bartenders.
  - Pgbouncer frontend connections (= incoming ones) are very cheap, and you have lots of these (e.g. thousands). Typically you want _N_ >= _A_ with _N_ being the pgbouncer connection limit, and _A_ being the number of connections needed for your application.
  - PostgreSQL connections are much more expensive resource wise, and ideally you have no more than the number of CPU cores available per server (e.g. 32). Depending on your load this may not always be sufficient, e.g. a primary in our setup will need to allow 100-150 connections at peak.
  - Pgbouncer can be configured to terminate PostgreSQL connections when idle for a certain time period, conserving resources.
