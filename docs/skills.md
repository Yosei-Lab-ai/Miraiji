# bizstack Skills Reference

## Overview

bizstack extends gstack's development pipeline with business design and go-to-market skills. Each skill adopts a specific expert persona and produces structured output that feeds into subsequent skills.

## Pipeline

```
BEFORE BUILD:
/office-hours → /plan-ceo-review → /persona → /pricing → /gtm → /plan-eng-review

AFTER SHIP:
/ship → /launch → /content → /outreach → /measure → /grow → /feedback → /biz-retro
```

---

## Phase 1 Skills (Implemented)

### /persona — UX Researcher

**Why this exists:** You can't build the right product if you don't know who it's for. Not "developers" or "small businesses" — one specific person with a name, a daily routine, and a credit card.

**Persona:** Senior UX Researcher with 15 years of experience in ethnographic studies and persona development.

**5 Forcing Questions:**
1. A day in their life (morning to end-of-day)
2. Current workaround (how they solve/endure the problem today)
3. Willingness to pay (budget, current tool spending)
4. Where they gather online (specific communities, platforms)
5. Reasons NOT to use it (adoption barriers)

**Output:** `~/.bizstack/personas/persona-[NNN].md`
**Feeds into:** `/pricing` (Q3 data), `/gtm` (Q4 data), `/plan-eng-review` (Q5 data)

---

### /pricing — CFO

**Why this exists:** The price determines the architecture. A free tool doesn't need auth. A $10/mo SaaS needs Stripe, usage limits, and tier management. Decide the price before you design the system.

**Persona:** Startup CFO, ruthlessly numbers-driven, allergic to "we'll figure it out later."

**Framework:**
1. Pricing model selection (free / freemium / subscription / one-time / usage-based)
2. Competitive pricing landscape
3. Willingness-to-pay vs. market position
4. Tier design (Free / Pro / Enterprise)
5. Break-even analysis
6. Free tier limit design → engineering spec

**Output:** `~/.bizstack/pricing/pricing-[NNN].md`
**Reads:** `/persona` willingness-to-pay data
**Feeds into:** `/plan-eng-review` (auth, billing, limits engineering requirements)

---

### /gtm — CMO

**Why this exists:** Building a great product is necessary but not sufficient. You need a repeatable, solo-executable strategy for getting it into the hands of users.

**Persona:** Startup CMO, specialist in solo-founder go-to-market, allergic to "leverage social media."

**Framework:**
1. Positioning statement
2. Messaging framework (one-liner, elevator pitch, full description)
3. Channel strategy (3 channels max, prioritized)
4. Content strategy overview
5. Launch plan overview
6. First 100 users strategy (specific, actionable tactics)

**Output:** `~/.bizstack/gtm/gtm-[NNN].md`
**Reads:** `/persona` (where users gather), `/pricing` (price point for CAC calculation)
**Feeds into:** `/launch`, `/content`, `/outreach`

---

## Phase 2 Skills (Coming Soon)

### /market-scan — Business Development
Competitive analysis and positioning. Maps direct competitors, indirect alternatives, and market gaps. Outputs a positioning map.

### /bizplan — Business Planner
Synthesizes all prior skill outputs into a cohesive business plan with 12-month P&L projection.

### /launch — Launch Manager
Turns GTM strategy into execution: platform-specific materials, T-14 to T+7 timeline, launch day checklist.

### /content — Content Marketer
Sustainable content engine: calendars, blog drafts, social batches, email sequences, SEO targets.

### /outreach — Community Manager
Manual user acquisition: community engagement, DM templates, beta recruitment, partnerships.

### /measure — Growth Analyst
KPI design: North Star Metric, funnel architecture, dashboard wireframe, A/B test framework.

### /grow — Growth Hacker
Growth experiments: ICE scoring, backlog management, result tracking, channel analysis.

### /feedback — Customer Success
Feedback loops: collection channels, triage framework, NPS/CSAT, feedback-to-product pipeline.

### /biz-retro — COO
Business retrospective: unified dashboard combining engineering metrics (gstack), business metrics (bizstack), and life metrics (lifestack).
