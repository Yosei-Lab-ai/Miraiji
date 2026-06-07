# miraiji

**gstack ships your code. miraiji ships it to users.**

A Claude Code skill pack that fills the business gaps in your development pipeline. Built to extend [gstack](https://github.com/garrytan/gstack), not replace it.

---

## The Problem

Solo developers and indie hackers share the same bottleneck: **you can build it, but you can't ship it to the people who need it.**

gstack gives you a world-class sprint cycle:
Think → Plan → Build → Review → Test → Ship → Reflect

But gstack's pipeline has two blind spots:

**Blind Spot 1: After CEO Review, Before Engineering**
You know *what* to build, but not *for whom*, *at what price*, or *through what channel*. Without these answers, you can't even design your auth system correctly.

**Blind Spot 2: After Ship**
Your code is released, but nobody knows it exists. You need launch strategy, marketing, user acquisition, and growth measurement.

miraiji fills both gaps.

---

## The Extended Pipeline

```
BEFORE BUILD (Business Design — after CEO review, before engineering):
/office-hours → /plan-ceo-review → /persona → /pricing → /gtm → /plan-eng-review

AFTER SHIP (Go-to-Market — after release):
/ship → /launch → /content → /outreach → /measure → /grow → /feedback → /biz-retro
```

---

## Quick Start

```bash
# Clone
git clone https://github.com/7da11/miraiji.git

# Install (symlinks skills to ~/.claude/skills/miraiji/)
cd miraiji && bash setup
```

After installation, use any skill in Claude Code:

```
> /persona      # Define your target user
> /pricing      # Design your price structure
> /gtm          # Plan your go-to-market strategy
```

---

## Skills

### Phase 1 — Business Design (Available Now)

| Skill | Persona | What it does |
|-------|---------|-------------|
| `/persona` | UX Researcher | Defines your target user through 5 forcing questions. Outputs a concrete persona document. |
| `/pricing` | CFO | Designs your pricing model, tier structure, and break-even analysis. Outputs engineering requirements for billing & limits. |
| `/gtm` | CMO | Creates your go-to-market strategy: positioning, messaging, channel strategy, and first-100-users plan. |

### Phase 2 — Go-to-Market (Coming Soon)

| Skill | Persona | What it does |
|-------|---------|-------------|
| `/launch` | Launch Manager | Creates launch playbooks and materials for Product Hunt, HN, Reddit, X. |
| `/content` | Content Marketer | Designs content calendars, blog outlines, social posts, email sequences. |
| `/outreach` | Community Manager | Strategies for acquiring your first 100 users through communities and outreach. |

### Phase 3 — Growth (Coming Soon)

| Skill | Persona | What it does |
|-------|---------|-------------|
| `/measure` | Growth Analyst | KPI design, funnel setup, dashboard architecture. |
| `/grow` | Growth Hacker | Growth experiment design with ICE scoring and prioritization. |
| `/feedback` | Customer Success | Feedback collection, triage, and product improvement loops. |
| `/market-scan` | Biz Dev | Competitive analysis, market sizing, positioning maps. |
| `/bizplan` | Biz Planner | Full business plan: vision → strategy → 12-month P&L. |
| `/biz-retro` | COO | Weekly/monthly business retrospective with unified metrics. |

---

## The Three Stacks

miraiji is designed to coexist with gstack and lifestack:

```
~/.claude/skills/
├── gstack/       # Software development (build it)
├── miraiji/     # Business & marketing (ship it to users)
└── lifestack/    # Personal growth (become who you are)
```

| Stack | Domain | Core Question |
|-------|--------|---------------|
| lifestack | Self | "Who am I becoming?" |
| gstack | Product | "What do I build?" |
| miraiji | Business | "How do I deliver it?" |

---

## Data Storage

All data is stored locally. No cloud, no telemetry.

```
~/.miraiji/
├── personas/      # Target user personas
├── pricing/       # Pricing design documents
├── gtm/           # Go-to-market strategies
├── market/        # Competitive analysis
├── plans/         # Business plans
├── launch/        # Launch playbooks & materials
├── content/       # Content calendars
├── growth/        # Growth experiments
├── feedback/      # User feedback logs
└── retros/        # Business retrospectives
```

---

## Privacy

miraiji stores everything in `~/.miraiji/` on your local machine. Nothing is uploaded, tracked, or shared. Your business strategy stays yours.

---

## License

MIT — Copyright (c) 2026 Sho
