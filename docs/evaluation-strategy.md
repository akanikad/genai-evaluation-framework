# Evaluation Strategy

## Offline
Use a versioned golden set to compare models, prompts, retrieval settings, and agent workflows.

## Online
Track production signals such as completion rate, escalation rate, retrieval confidence, latency, cost, and user feedback.

## Release gate
A model/prompt change should not be promoted solely because a benchmark score improved. It must pass workflow-level regression tests and business-risk thresholds.

## High-risk workflows
For clinical, financial, eligibility, or authorization-related decisions, define explicit human-review conditions and audit evidence requirements.
