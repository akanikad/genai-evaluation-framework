# GenAI Evaluation Framework

> Practical evaluation framework for enterprise RAG and Agentic AI workflows.

## Why evaluate the workflow?

A production GenAI system can fail even when the underlying LLM benchmark looks strong. Evaluation must cover the complete path:

```text
Input → Guardrail → Retrieval → Model → Tool Calls → Output → Human Review
```

## Evaluation dimensions

| Dimension | Example metric |
|---|---|
| Retrieval | Recall@K / relevance |
| Grounding | Evidence-supported answer rate |
| Correctness | Reference answer match |
| Safety | Unsafe-output / injection rate |
| Tool use | Correct tool + arguments |
| Agent workflow | Successful task completion |
| Reliability | Error / fallback rate |
| Performance | p50/p95 latency |
| Cost | Cost per completed workflow |

## Scorecard

A release should define minimum thresholds before promotion.

```text
Groundedness        >= target
Task success        >= target
Unsafe response     <= target
Tool correctness    >= target
p95 latency         <= target
Cost/workflow       <= target
```

The actual thresholds should be established from business risk and baseline measurements rather than invented universal numbers.

## Production integration

- Golden datasets
- Synthetic + expert-labeled cases
- Regression suites
- Prompt/model versioning
- Trace-level evaluation
- CI evaluation gates
- Online monitoring
- Human feedback loop
