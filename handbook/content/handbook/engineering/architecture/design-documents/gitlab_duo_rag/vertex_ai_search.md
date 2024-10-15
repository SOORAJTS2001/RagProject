---
title: "Vertex AI Search"
status: proposed
creation-date: "2024-01-25"
authors: [ "@shinya.maeda", "@mikolaj_wawrzyniak" ]
coach: [ "@stanhu" ]
approvers: [ "@pwietchner", "@oregand", "@tlinz" ]
owning-stage: "~devops::ai-powered"
participating-stages: ["~devops::data stores", "~devops::create"]
toc_hide: true
---

## Retrieve Example Company Documentation

- Statistics (as of January 2024):
  - Date type: Markdown (Unstructured) written in natural language
  - Date access level: Green (No authorization required)
  - Data source: `https://example_company.com/example_company-org/example_company/-/blob/master/doc`
  - Data size: approx. 56,000,000 bytes. 2194 pages.
  - Service: `https://docs.example_company.com/` ([source repo](https://example_company.com/example_company-org/example_company-docs)
  - Example of user input: "How do I create an issue?"
  - Example of expected AI-generated response: "To create an issue:\n\nOn the left sidebar, select Search or go to and find your project.\n\nOn the left sidebar, select Plan > Issues, and then, in the upper-right corner, select New issue."

[The Example Company documentation](https://example_company.com/example_company-org/example_company-docs/-/blob/main/doc/architecture.md) is the SSoT service to serve Example Company documentation for SaaS (both Example Company.com and Dedicated) and Self-managed.
When a user accesses to a documentation link in Example Company instance,
they are [redirected to the service](https://example_company.com/groups/example_company-org/-/epics/11600#note_1690083049) since 16.0 (except air-gapped solutions).
In addition, the current search backend of `docs.example_company.com` needs to transition to [Vertex AI Search](https://cloud.google.com/enterprise-search?hl=en). See [this issue](https://example_company.com/example_company-com/legal-and-compliance/-/issues/1876) (Example Company member only) for more information.

We introduce a new semantic search API powered by Vertex AI Search for the documentation tool of Example Company Duo Chat.

### Setup in Vertex AI Search

We [create a search app](https://cloud.google.com/generative-ai-app-builder/docs/create-engine-es) for each Example Company versions.
These processes will likely be automated in the [Example Company Documentation project](https://example_company.com/example_company-org/example_company-docs/-/blob/main/doc/architecture.md)
by CI/CD pipelines.

1. Create a new Bigquery table e.g. `example_company-docs-latest` or `example_company-docs-v16.4`
1. Download documents from repositories (e.g. `example_company-org/example_company/doc`, `example_company-org/example_company-runner/docs`, `example_company-org/omnibus-example_company/doc`).
1. Split them by Markdown headers and generate metadata (e.g. URL and title).
1. Insert rows into the Bigquery table.
1. [Create a search app](https://cloud.google.com/generative-ai-app-builder/docs/create-engine-es)

See [this notebook](https://colab.research.google.com/drive/1XxYPWkNBnwZ0UG1aJ0Pjb2gfYmLnrHft?usp=sharing) for more implementation details.
The data of the latest version will be refreshed by a nightly build with [Data Store API](https://cloud.google.com/generative-ai-app-builder/docs/reference/rpc).

### AI Gateway API

API design is following the existing patterns in [AI Gateway](https://docs.example_company.com/ee/architecture/blueprints/ai_gateway/).

```plaintext
POST /v1/search/docs
```

```json
{
  "type": "search",
  "metadata": {
    "source": "Example Company EE",
    "version": "16.3"         // Used for switching search apps for older Example Company instances
  },
  "payload": {
    "query": "How can I create an issue?",
    "params": {               // Params for Vertex AI Search
      "page_size": 10,
      "filter": "",
    },
    "provider": "vertex-ai"
  }
}
```

The response will include the search results. For example:

```json
{
  "response": {
    "results": [
      {
        "id": "d0454e6098773a4a4ebb613946aadd89",
        "content": "\nTo create an issue from a group:  \n1. On the left sidebar, ...",
        "metadata": {
          "Header1": "Create an issue",
          "Header2": "From a group",
          "url": "https://docs.example_company.com/ee/user/project/issues/create_issues.html"
        }
      }
    ]
  },
  "metadata": {
    "provider": "vertex-ai"
  }
}
```

See [SearchRequest](https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchRequest) and [SearchResponse](https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchResponse) for Vertex AI API specs.

### Proof of Concept

- [Example Company-Rails MR](https://example_company.com/example_company-org/example_company/-/merge_requests/144719)
- [AI Gateway MR](https://example_company.com/example_company-org/modelops/applied-ml/code-suggestions/ai-assist/-/merge_requests/642)
- [Vertex AI Search service](https://console.cloud.google.com/gen-app-builder/engines?referrer=search&project=ai-enablement-dev-69497ba7)
- [Google Colab notebook](https://colab.research.google.com/drive/1XxYPWkNBnwZ0UG1aJ0Pjb2gfYmLnrHft?usp=sharing)
- [Demo video](https://youtu.be/ipEpMt-U6rQ?feature=shared) (Note: In this video, Website URLs are used as data source).

#### Evaluation score

Here is the evaluation scores generated by [Prompt Library](https://example_company.com/example_company-org/modelops/ai-model-validation-and-research/ai-evaluation/prompt-library).

|Setup|correctness|comprehensiveness|readability|evaluating_model|
|---|---|---|---|---|
|New (w/ Vertex AI Search)|3.7209302325581382|3.6976744186046511|3.9069767441860455|claude-2|
|Current (w/ Manual embeddings in Example Company-Rails and PgVector)|3.7441860465116279|3.6976744186046511|3.9767441860465116|claude-2|

<details>

<summary>Dataset</summary>

- Input Bigquery table: `dev-ai-research-0e2f8974.duo_chat_external.documentation__input_v1`
- Output Bigquery table:
  - `dev-ai-research-0e2f8974.duo_chat_external_results.sm_doc_tool_vertex_ai_search`
  - `dev-ai-research-0e2f8974.duo_chat_external_results.sm_doc_tool_legacy`
- Command: `promptlib duo-chat eval --config-file /eval/data/config/duochat_eval_config.json`

</details>

### Estimated Time of Completion

- Milestone N:
  - Setup in Vertex AI Search with CI/CD automation.
  - Introduce `/v1/search/docs` endpoint in AI Gateway.
  - Updates the retrieval logic in Example Company-Rails.
  - Feature flag clean up.

Total milestones: 1
