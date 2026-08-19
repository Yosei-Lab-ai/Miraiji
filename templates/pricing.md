# Pricing Design: [Product Name]

**Created:** [date]
**Persona:** [Link to persona file if exists]
**Status:** Hypothesis
**Evidence status:** [Observed | Inferred | Unknown]
**Execution mode:** [internal_autorun | external_approval_required]
**External action authorized:** No

## Pricing Model
**Selected:** [Model name]
**Rationale:** [Why this model fits]

## Competitive Landscape
| Competitor | Price | Model | Notes |
|-----------|-------|-------|-------|
| ... | ... | ... | ... |

**Positioning:** [Premium / Match / Undercut] — [reasoning]

## Tier Structure

### Free Tier
- **Included:** [features]
- **Limits:** [specific limits]
- **Goal:** [acquisition / trial / community]

### Pro Tier — $[X]/mo
- **Included:** [features above free]
- **Target conversion:** [X]% of free users
- **Upsell trigger:** [what makes users upgrade]

### [Additional tiers if applicable]

## Break-Even Analysis
- **Monthly fixed costs:** $[X]
- **Margin per paid user:** $[X]
- **Break-even:** [N] paying users
- **Target timeline:** [X] months

## Engineering Requirements
- **Auth:** [Required / Not required] — [system recommendation]
- **Billing:** [Stripe / Paddle / Gumroad / etc.]
- **Usage tracking:** [What to track, storage approach]
- **Feature flags:** [What to gate]
- **Free tier enforcement:** [Soft / Hard limits, implementation approach]

## Key Risks
- [Risk 1 and mitigation]
- [Risk 2 and mitigation]

## Bounded Hypothesis
- **Specific situation:** [Buyer context and purchase trigger]
- **Problem hypothesis:** [Current economic or workflow cost]
- **Promise under test:** [Bounded paid outcome]
- **Proof status:** [Evidence and sources]
- **Riskiest assumption:** [One falsifiable pricing assumption]

## Minimal Test
- **Method:** [Smallest test]
- **Experiment record:** [~/.miraiji/experiments/{id}.md]
- **Audience and sample:** [Exact target and sample size]
- **Timebox:** [Maximum duration]
- **Budget cap:** [Approved cap or zero]
- **Pass:** [Threshold]
- **Fail:** [Threshold]
- **Inconclusive:** [Missing-data condition]
- **Inconclusive next action:** [measurement_repair step or revised test]
- **Stop condition:** [When to stop]
- **Next decision:** [Execute internal | Request external approval | Adopt | Revise | Reject | Repair measurement]
