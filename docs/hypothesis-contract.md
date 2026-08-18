# Miraiji Bounded Hypothesis Contract

`/persona`, `/pricing`, and `/gtm` produce decision inputs, not permission to launch.
Each output must distinguish observed evidence from inference and attach a small,
bounded test to its riskiest assumption.

## Required hypothesis fields

```yaml
status: hypothesis
evidence_status: observed | inferred | unknown
decision: pending
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
| Audience and sample | Exact target situation and bounded sample size. |
| Timebox | Start/end or maximum duration. |
| Budget | Maximum approved test cost; zero if no spend is authorized. |
| Pass | Numeric or directly observable threshold. |
| Fail | Numeric or directly observable threshold that rejects the hypothesis. |
| Inconclusive | Missing-data or sample-quality condition requiring another decision. |
| Stop condition | Safety, cost, response-quality, or policy condition that ends the test. |
| Next decision | Adopt, revise, reject, or gather evidence; never auto-launch. |

## Approval boundary

Planning an experiment does not authorize publishing, posting, outreach, reservations,
billing, purchases, account changes, price changes, or customer-facing edits. Set
`external_action_authorized: false` unless the user separately approves the exact action.
Save the latest resume point in `~/.miraiji/state/current.md`.
