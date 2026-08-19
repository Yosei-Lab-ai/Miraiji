# Miraiji Bounded Hypothesis Contract

`/persona`, `/pricing`, and `/gtm` produce decision inputs, not permission to launch.
Each output must distinguish observed evidence from inference and attach a small,
bounded test to its riskiest assumption.

## Required hypothesis fields

```yaml
status: hypothesis
evidence_status: observed | inferred | unknown
decision: ready_to_run | measurement_repair | revise | adopt | reject
execution_mode: internal_autorun | external_approval_required
resume_from: next skill or concrete next question
external_action_authorized: false
```

Every output must state:

1. **Specific situation** — who is experiencing the problem, in what context, and when.
2. **Problem** — the current cost or friction and the workaround used today.
3. **Promise** — the bounded change being tested, without unsupported outcome claims.
4. **Proof status** — observed evidence, source, contradictions, and what remains unknown.
5. **Riskiest assumption** — the single assumption most likely to invalidate the proposal.

## Minimal test fields

| Field | Requirement |
|---|---|
| Method | Smallest test that can falsify the riskiest assumption. |
| Execution mode | `internal_autorun` for read-only/local evidence collection; `external_approval_required` for a public or customer-facing action. |
| Audience and sample | Exact target situation and bounded sample size. |
| Timebox | Start/end or maximum duration. |
| Budget | Maximum approved test cost; zero if no spend is authorized. |
| Pass | Numeric or directly observable threshold. |
| Fail | Numeric or directly observable threshold that rejects the hypothesis. |
| Inconclusive | Missing-data or sample-quality condition. Set `decision: measurement_repair` and name the next collection or correction; do not end at hold. |
| Stop condition | Safety, cost, response-quality, or policy condition that ends the test. |
| Experiment record | Save the executable plan and results at `~/.miraiji/experiments/{id}.md`. |
| Next decision | Execute internal test, request one external approval, adopt, revise, reject, or repair measurement; never auto-launch. |

## Execution rule

Use `internal_autorun` when the test only reads existing authorized data, compares
local artifacts, calculates metrics, or produces a private draft. Create the experiment
record and continue in the same session when the required inputs and tools exist.

Use `external_approval_required` only when the test posts, publishes, messages a person,
spends money, changes an account, or changes a customer-facing price. Prepare the exact
action, audience, cost cap, and rollback first; after one explicit approval, execute the
approved test without asking again for each mechanical substep.

An inconclusive result is not a terminal state. Route it to `measurement_repair` with a
concrete missing field, collection method, and next run, or revise the bounded test.

## Approval boundary

Planning an experiment does not authorize publishing, posting, outreach, reservations,
billing, purchases, account changes, price changes, or customer-facing edits. Set
`external_action_authorized: false` unless the user separately approves the exact action.
This boundary does not block `internal_autorun` work. Save the latest resume point in
`~/.miraiji/state/current.md` and the executable record in `~/.miraiji/experiments/`.
