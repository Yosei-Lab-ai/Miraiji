# bizstack Skills — Deep Dive

## Overview

bizstack extends gstack's development pipeline with business design and go-to-market skills. Each skill adopts a specific expert persona and produces structured output that feeds into subsequent skills.

```
BEFORE BUILD:
/office-hours → /plan-ceo-review → /persona → /pricing → /gtm → /plan-eng-review

AFTER SHIP:
/ship → /launch → /content → /outreach → /measure → /grow → /feedback → /biz-retro
```

---

# Phase 1 Skills

---

## /persona — Senior UX Researcher

### Why This Skill Exists

Every product failure can be traced back to a misunderstanding of the user. Not the market, not the technology — the user. Specifically, the failure to define one concrete person who desperately needs what you're building.

"Developers" is not a persona. "Small businesses" is not a persona. "Content creators" is not a persona. A persona is a person with a name, a morning routine, a tool budget, and a specific frustration they hit at 2pm on a Tuesday.

/persona exists because founders skip this step. They start coding because coding feels productive. But building for a vague audience means every design decision is a guess. /persona turns guesses into informed decisions.

### How It Works

The skill adopts the persona of a Senior UX Researcher — someone who has conducted hundreds of user interviews and refuses to accept vague answers. It asks 5 forcing questions, one at a time, and pushes back when answers are too broad.

The output is a persona document that subsequent skills read automatically:
- `/pricing` reads willingness-to-pay (Q3)
- `/gtm` reads online presence (Q4)
- `/plan-eng-review` reads adoption barriers (Q5)

### Example Dialogue

**Scenario:** Building an AI-powered segmentation plugin for Adobe Premiere Pro.

---

> **Researcher:** I'm your UX Researcher. Before you write a single line of code, we need to know exactly who we're building for — not a market segment, not a demographic, one specific person. Let's find them.
>
> First question: **Tell me about the person who needs this product most. What does their day look like?** Walk me through their morning to end-of-day. What's their job title? What tools do they open first? What frustrates them before lunch?

**User:** It's for video editors who use Premiere Pro. They spend a lot of time manually masking and rotoscoping subjects in their footage.

> **Researcher:** "Video editors who use Premiere Pro" is a market, not a person. Let me push you harder. Is this person a freelancer editing YouTube videos in their apartment, or a staff editor at a post-production house cutting Netflix shows? Those are completely different people with different workflows, different budgets, and different pain thresholds.
>
> Give me one specific person. Name them. Where do they live? What kind of projects do they work on?

**User:** OK. He's a freelance video editor, maybe early 30s, based in Tokyo. He mainly edits corporate promotional videos and YouTube content for small businesses. He uses Premiere Pro because that's what he learned in school.

> **Researcher:** Good. Now I can see him. Let me call him Kenji.
>
> Kenji, 32, freelance editor in Tokyo. Opens Premiere Pro at 9am with a flat white. His morning is about rough cuts — syncing audio, arranging clips, getting the story structure right. That part he enjoys. But by early afternoon, the client asks for "that thing where the person pops off the background" — and Kenji's heart sinks because he knows he's about to spend 3 hours frame-by-frame masking a talking head that keeps moving their hands.
>
> Does that feel right? Anything to adjust before we move on?

**User:** Yeah, that's pretty accurate. He's also under time pressure because clients always want it "by tomorrow."

> **Researcher:** Perfect. Kenji's pain isn't just the tedium — it's the tedium under deadline pressure.
>
> **Question 2: How is Kenji solving this problem today?** What's his current workaround? What tools or techniques does he use for segmentation right now?

**User:** He uses Premiere's built-in masking tools, which are manual and frame-by-frame. Sometimes he sends clips to After Effects for Rotobrush, but the round-trip is slow. Occasionally he uses a free online tool but the quality isn't great.

> **Researcher:** So Kenji has three workarounds, all bad:
> 1. **Manual masking in Premiere** — tedious, 2-3 hours per clip
> 2. **After Effects Rotobrush** — better results but the round-trip kills his flow
> 3. **Free online tools** — fast but quality is unacceptable for client work
>
> The pattern is clear: he's choosing between quality and speed every single time. Your plugin would need to give him both — inside Premiere, no round-trip.
>
> **Question 3: How much would Kenji pay to make this problem disappear?** What similar tools or plugins is he already paying for? What's his monthly tool budget?

**User:** He pays for Creative Cloud which is about ¥7,000/month. He's bought a few plugins before — things like FilmConvert for ¥8,000 one-time. He probably wouldn't pay a huge subscription fee since he's freelance.

> **Researcher:** Let me map Kenji's spending:
> - Adobe Creative Cloud: ~¥7,000/mo (~$47)
> - Plugin purchases: ¥5,000-¥10,000 one-time (based on FilmConvert precedent)
> - Total tool budget: probably ¥10,000-15,000/mo including amortized plugin costs
>
> Key insight: Kenji is **accustomed to one-time plugin purchases** in the ¥5,000-¥10,000 range. A subscription would need to be justified by ongoing value. But if your plugin saves him 2-3 hours per project, and he does 8-10 projects per month, that's 20+ hours saved. Even at his freelance rate of ¥3,000-5,000/hour, that's ¥60,000+ in recaptured billing time.
>
> The willingness-to-pay is likely: ¥3,000-5,000/mo subscription or ¥15,000-25,000 one-time.
>
> **Question 4: Where does Kenji hang out online?** What Twitter/X accounts does he follow? What subreddits, Discord servers, or forums is he part of?

**User:** Definitely Twitter/X — he follows a lot of Japanese video creators. He's probably on r/premiere and r/VideoEditing on Reddit. YouTube channels like Casey Faris for Premiere tips. Maybe some Japanese-language forums or Facebook groups for video editors.

> **Researcher:** Let me be more specific:
> - **X/Twitter:** Japanese video editing community, follows accounts like @premierepro_jp, Vook.vc, and individual Japanese creators
> - **Reddit:** r/premiere (87k members), r/VideoEditing (196k), r/AfterEffects
> - **YouTube:** Casey Faris, Premiere Gal, and Japanese tutorial channels
> - **Communities:** Vook (Japanese video production community), Adobe Community Forums
> - **Marketplaces:** Adobe Exchange (where he'd discover plugins)
>
> This is gold for GTM. His discovery path is: YouTube tutorial → Adobe Exchange → X/Twitter recommendation from another editor.
>
> **Final question — and this is the most important one for your product design:**
> **What would stop Kenji from using your plugin?** What's the adoption barrier?

**User:** Probably trust — will AI segmentation actually be good enough for client work? And also workflow disruption — if it doesn't integrate smoothly into Premiere, he won't bother. And maybe price if it's a subscription.

> **Researcher:** Three barriers, in order of severity:
> 1. **Quality trust** (Primary): "Will this actually look professional?" He's burned by free tools. Needs to see proof on real footage.
> 2. **Workflow integration**: Must work inside Premiere's timeline. No round-trips, no exports. If it adds steps, he'll go back to manual masking.
> 3. **Pricing model friction**: Subscription fatigue. He already pays for Creative Cloud and resents monthly fees.
>
> These directly inform your product strategy:
> - Quality trust → Your demo content must show client-grade output, not tech demos
> - Workflow → Must be a native Premiere plugin, not a standalone tool
> - Pricing → Consider one-time purchase or annual with heavy discount

After all 5 questions, the researcher synthesizes the persona into a structured document and saves it to `~/.bizstack/personas/persona-001.md`.

### Output Example

```markdown
# Persona: Kenji

**Created:** 2026-03-25
**Product:** AI Segmentation Plugin for Premiere Pro

## Profile
- **Name:** Kenji
- **Age:** 32
- **Location:** Tokyo, Japan
- **Role:** Freelance Video Editor (solo)
- **Experience:** 7 years in video editing

## A Day in Their Life
Kenji starts his day at 9am, opening Premiere Pro with a flat white. His morning
is productive — rough cuts, audio sync, story structure. He's good at this and
enjoys it. But by early afternoon, the client requests "pop the subject off the
background" and his mood drops. He knows he's about to spend 2-3 hours on
frame-by-frame masking for a 30-second clip. Under deadline pressure ("can you
have this by tomorrow?"), he either rushes through manual masking with mediocre
results or sends the clip to After Effects, breaking his flow for 30 minutes of
round-trip overhead.

## The Problem
- **Pain point:** Manual segmentation/masking is tedious and slow
- **Frequency:** 3-4 times per week across client projects
- **Impact:** 8-12 hours/week of low-value work; missed deadlines; compromised quality

## Current Workaround
- **What he does now:** Manual masking in Premiere or Rotobrush round-trip to AE
- **Tools he uses:** Premiere Pro masking, After Effects Rotobrush, occasional free online tools
- **What's broken:** Quality/speed tradeoff — no option gives both

## Willingness to Pay
- **Budget range:** ¥3,000-5,000/mo or ¥15,000-25,000 one-time
- **Current spending:** Creative Cloud ¥7,000/mo, occasional plugins ¥5,000-10,000
- **Price sensitivity:** Medium-high (freelancer, subscription-fatigued)

## Where They Are
- **Social:** X/Twitter (Japanese video editing community)
- **Communities:** r/premiere, r/VideoEditing, Vook.vc, Adobe Forums
- **Content:** Casey Faris, Premiere Gal, Japanese tutorial YouTubers

## Adoption Barriers
- **Primary barrier:** Quality trust — will AI output be client-grade?
- **Secondary barriers:** Workflow integration (must be native Premiere), pricing model (prefers one-time)
- **What would overcome them:** Demo on real footage, free trial, one-time purchase option
```

---

## /pricing — Startup CFO

### Why This Skill Exists

"Price before you code" is not a slogan — it's an engineering requirement.

The price determines the architecture. Consider:
- **Free tool:** No auth needed. No billing. No usage tracking. Ship it.
- **$10/mo SaaS:** Needs user accounts, Stripe integration, usage limits, upgrade prompts, tier management.
- **$500/yr enterprise:** Needs seat-based licensing, admin dashboard, SSO, invoicing, SLA.

These are fundamentally different products. If you don't decide the price before you start engineering, you'll either over-build (auth system for a free tool) or under-build (no billing for a product you want to charge for).

/pricing exists to force this decision before a line of code is written.

### How It Works

The skill adopts the persona of a Startup CFO — numbers-driven, allergic to hand-waving. It reads the persona's willingness-to-pay data and walks through a structured pricing framework:

1. Pricing model selection with pros/cons
2. Competitive pricing landscape
3. Willingness-to-pay cross-reference
4. Tier design with engineering specs
5. Break-even analysis
6. Free tier limit design (directly feeds /plan-eng-review)

### Example Dialogue

**Scenario:** Pricing the AI segmentation plugin for Adobe Premiere Pro. Persona (Kenji) already exists.

---

> **CFO:** I'm your CFO. The price determines the architecture — what you charge changes what you build. Let's get this right before you write code.
>
> I've read Kenji's persona. He currently spends ¥7,000/mo on Creative Cloud and has bought plugins in the ¥5,000-10,000 range. His budget ceiling is around ¥3,000-5,000/mo or ¥15,000-25,000 one-time. He has subscription fatigue.
>
> Let's start with the pricing model. Here are your options:

| Model | Fit for Plugin | Pros | Cons |
|-------|---------------|------|------|
| **Free / OSS** | Poor | Fast adoption | No revenue. AI inference costs will eat you alive |
| **Freemium** | Good | Low friction, upsell path | Must define clear free/paid boundary |
| **Subscription** | Moderate | Recurring revenue | Kenji has subscription fatigue. High churn risk |
| **One-time purchase** | Strong | Matches plugin buying behavior. No churn | No recurring revenue. Must sell new versions for growth |
| **Usage-based** | Moderate | Fair for variable usage | Complex billing. Unpredictable for user |

> My recommendation: **One-time purchase with major version upgrades** — this matches how Kenji already buys plugins (FilmConvert model). But I want to hear your instinct first.

**User:** I was thinking freemium — free tier with limited exports, paid for full quality. But one-time purchase is interesting too.

> **CFO:** Freemium is defensible, but let me stress-test it. You said this is a Premiere Pro plugin that runs AI segmentation. Two questions:
>
> 1. **What does "limited" look like?** Watermark on free output? Resolution cap? Clip length limit? Each of these is a different engineering requirement.
> 2. **What's your AI inference cost?** If you're running a model per frame, free users cost you money on every use. Unlike a SaaS where free users cost near-zero, an AI plugin with server-side inference has real marginal costs.
>
> If inference runs locally (on-device), freemium is viable because free users don't cost you anything. If it's server-side, freemium could bankrupt you.

**User:** It would run locally using the GPU. No server costs. So free users are basically free to serve.

> **CFO:** That changes everything. Local inference means free users cost you nothing. Freemium is viable. Let me map the competitive landscape.
>
> **Competitive pricing for Premiere Pro plugins:**
>
> | Plugin | Price | Model | Notes |
> |--------|-------|-------|-------|
> | Rotobrush (built-in AE) | Included in CC | Bundled | Requires AE round-trip |
> | RunwayML | $15-76/mo | Subscription | Cloud-based, general purpose |
> | Topaz Video AI | $299 one-time | One-time + upgrades | Desktop app, not a plugin |
> | Boris FX Silhouette | $1,695 | One-time (pro) | Enterprise-grade, overkill for Kenji |
> | Free online tools | $0 | Free | Low quality, not integrated |
>
> You're sitting in a gap: **better than free tools, cheaper than Topaz, integrated into Premiere (unlike everything else)**. This is a strong position.
>
> Given Kenji's ¥15,000-25,000 willingness-to-pay and the competitive landscape, here's my tier design:

```
FREE TIER: "Starter"
- AI segmentation on clips up to 30 seconds
- 720p max output resolution
- Watermark: small "Made with [Plugin]" in corner
- Goal: let Kenji try it on a real project and see the quality

PRO TIER: ¥2,480/mo or ¥19,800/year (¥1,650/mo effective)
- Unlimited clip length
- Full resolution output (up to 8K)
- No watermark
- Priority model updates
- Batch processing

ONE-TIME OPTION: ¥24,800 (lifetime license for current major version)
- Same as Pro
- Free minor updates (1.x)
- Major version upgrades at 50% discount
```

> **Break-even analysis:**

```
Monthly fixed costs:
  Apple Developer: ¥1,250/mo (amortized)
  Domain + hosting: ¥1,500/mo
  Adobe Exchange fee: 15% of revenue
  Total fixed:       ~¥2,750/mo

Per-user economics (subscription):
  Price per user:     ¥2,480/mo
  Adobe Exchange cut: ¥372/mo (15%)
  Net per user:       ¥2,108/mo

Break-even: ¥2,750 ÷ ¥2,108 = 2 paying subscribers
Ramen profitability (¥200,000/mo): 95 paying subscribers
```

> **CFO:** 2 subscribers to break even. 95 to live on. Those are good numbers. With a free tier driving trial and local inference keeping costs at zero, the economics work.
>
> Now, the engineering spec for your free tier limits:

```
FREE TIER LIMITS (→ /plan-eng-review input):
- Clip length: 30 seconds max (hard limit, show upgrade prompt)
- Resolution: 720p max output (downscale if source is higher)
- Watermark: composited in final render, not removable
- Enforcement: local license check, no server validation needed
- Tracking: none required (local inference, no server)
- Auth: license key validation (Gumroad/Paddle) for Pro tier
```

Output is saved to `~/.bizstack/pricing/pricing-001.md`.

---

## /gtm — Startup CMO

### Why This Skill Exists

Distribution is a skill, not a task. "Post it on Twitter and see what happens" is not a go-to-market strategy. A GTM strategy answers: who are we talking to, what are we saying, where are we saying it, and how do we get the first 100 users?

/gtm exists because the gap between "code shipped" and "users acquired" is where most indie products die. Not from bad code — from invisibility.

### How It Works

The skill adopts the persona of a Startup CMO who specializes in solo-founder launches. It reads both the persona (where users gather) and pricing (CAC constraints) to build a strategy that one person can actually execute.

Key constraint: **3 channels maximum.** A solo developer cannot maintain presence on 7 platforms. Pick 3, dominate them, ignore the rest.

### Example Dialogue

**Scenario:** GTM strategy for the AI segmentation plugin. Persona (Kenji) and pricing already exist.

---

> **CMO:** I'm your CMO. You've got a product and a price. Now we need to get it in front of the right people. Let's build a GTM strategy you can execute solo.
>
> I've read Kenji's persona. He discovers plugins through YouTube tutorials, Adobe Exchange browsing, and X/Twitter recommendations from other editors. He hangs out in r/premiere, Vook.vc, and Adobe forums.
>
> Your pricing is freemium with a Pro tier at ¥2,480/mo. With Adobe Exchange taking 15%, your net is ¥2,108/user/mo. You need 95 paying users for ramen profitability. Let's design how to get there.
>
> **Step 1: Positioning.** Let's build your statement.

**User:** Something like "AI-powered video segmentation that works inside Premiere Pro"?

> **CMO:** That's a feature description, not positioning. Let me push you. Positioning answers "why you and not the alternative?" Here:
>
> For **freelance video editors** who **waste hours on manual masking**, **[Plugin Name]** is a **Premiere Pro plugin** that **segments subjects in one click with AI**. Unlike **After Effects Rotobrush**, it **works directly in your Premiere timeline with no round-trip**.
>
> The key differentiator isn't "AI" — every tool claims AI. It's **"no round-trip, stays in Premiere."** That's what Kenji cares about.
>
> **Step 2: Messaging.**

**One-liner:**
> One-click AI masking, inside Premiere.

**Elevator Pitch (30s):**
> Video editors spend hours on frame-by-frame masking — or they round-trip to After Effects and break their flow. [Plugin Name] brings AI-powered subject segmentation directly into the Premiere Pro timeline. Select a clip, click segment, done. Free to try, pro license for full resolution.

**Full Description (2min):**
> Every video editor knows the pain: the client wants the subject isolated from the background. In 2026, this still means either tedious manual masking in Premiere, or exporting to After Effects for Rotobrush and losing 30 minutes in the round-trip.
>
> [Plugin Name] solves this with AI segmentation that runs natively inside Premiere Pro. No round-trips, no external tools, no cloud uploads. Select your clip, click "Segment," and the AI generates a precise mask of your subject — even with hand gestures, hair, and motion blur. It runs on your local GPU, so your footage never leaves your machine.
>
> Free tier lets you try it on clips up to 30 seconds at 720p. Pro license unlocks unlimited length, full resolution up to 8K, and batch processing. Used by freelancers who'd rather spend their afternoon on creative work than frame-by-frame masking.

> **CMO:** Now channels. Based on Kenji's persona, here are my top 3:

### Channel 1: YouTube — PRIMARY
- **Why:** Kenji's #1 discovery channel for Premiere Pro tools. Tutorial content has a long shelf life and compounds.
- **Content type:** Before/after demo videos, "5-minute masking in Premiere" tutorials
- **Frequency:** 1 video every 2 weeks
- **First action this week:** Record a 2-minute side-by-side comparison: manual masking (sped up, showing 2 hours) vs. your plugin (real-time, 10 seconds). Post to YouTube with title "I just saved 2 hours of masking in Premiere Pro"
- **Success metric:** Views, click-through to Adobe Exchange listing

### Channel 2: Reddit (r/premiere, r/VideoEditing) — SECONDARY
- **Why:** Active communities where Kenji asks questions and discovers tools. High-intent users.
- **Content type:** "Show-off" posts with before/after, answering masking questions with your plugin as the solution
- **Frequency:** 2-3 posts/week (mix of helpful comments and showcase posts)
- **First action this week:** Find 3 recent posts asking about masking/rotoscoping in r/premiere. Leave genuinely helpful comments. Don't pitch yet — build reputation first.
- **Success metric:** Post upvotes, DMs, traffic to listing

### Channel 3: X/Twitter (Japanese video community) — TERTIARY
- **Why:** Kenji's social network. Word-of-mouth amplifier. Japanese video editing community is tight-knit.
- **Content type:** Build-in-public thread, short demo clips (< 30s), tips
- **Frequency:** 3-5 tweets/week
- **First action this week:** Post a 15-second screen recording of AI segmentation in action with Japanese caption. Tag Vook.vc.
- **Success metric:** Retweets, followers, DMs from editors

> **CMO:** And the most important part — your first 100 users:

```
FIRST 10 USERS (Manual — Week 1-2):
1. Post in r/premiere with before/after demo → expect 3-5 installs
2. DM 20 active members of r/VideoEditing who've posted about masking → expect 2-3
3. Share in 2 Japanese video editing Facebook groups → expect 2-3
4. Ask 3 video editor friends to try it and give honest feedback → 3

USERS 11-50 (Community — Week 3-6):
5. Publish YouTube tutorial "One-Click Masking in Premiere Pro" → 10-15
6. Answer 10 masking-related questions on Adobe Forums with genuine help + plugin mention → 5-8
7. Post "Show HN: AI segmentation plugin for Premiere Pro" → 5-10
8. Reach out to 3 Premiere Pro tutorial YouTubers for review → 5-10 each

USERS 51-100 (Content + Word-of-Mouth — Week 7-12):
9. Second YouTube video: "5 Things I Learned Launching a Premiere Pro Plugin" → 10-15
10. Cross-post best Reddit demo to X/Twitter in Japanese → 5-10
11. Early users sharing their results (encourage with "tag us" CTA) → 10-20
12. Adobe Exchange listing optimization (keywords, screenshots, reviews) → ongoing organic
```

> **CMO:** Weekly marketing time budget:

| Activity | Hours/week |
|----------|-----------|
| YouTube (scripting, recording, editing) | 2h |
| Reddit (posting, commenting) | 1h |
| X/Twitter (posting, engaging) | 0.5h |
| DMs/outreach | 0.5h |
| **Total** | **4h** |

> That leaves you 36+ hours for building. GTM strategy saved. You now have your persona, pricing, and go-to-market plan. You're ready for `/plan-eng-review` — bring the pricing engineering requirements and this GTM context to your engineering planning session.

---

# Phase 2 Skills

---

## /market-scan — Business Development Strategist

### Design Overview

/market-scan maps the competitive landscape before you commit to a strategy. Most founders either say "there's no competition" (wrong — there's always competition, even if it's manual processes) or get paralyzed by competitors they find.

The skill produces:
- **Direct competitors** (same problem, same approach)
- **Indirect competitors** (same problem, different approach)
- **Substitute solutions** (manual workarounds, existing tool combinations)
- **Pricing landscape** across all competitors
- **2-axis positioning map** (ASCII) showing where you fit
- **Your USP** (unique selling proposition) derived from the gaps

**Intended use:** Run after /persona, before /pricing. Feeds competitive pricing data into /pricing.

---

## /bizplan — Business Planner

### Design Overview

/bizplan synthesizes everything from /persona, /market-scan, /pricing, and /gtm into a single cohesive business plan. It's optimized for solo developers and bootstrapped founders — not a 40-page investor pitch, but a practical document that answers "can this sustain me?"

Key sections:
- Executive summary (1 paragraph — forces clarity)
- 12-month P&L projection (revenue, costs, break-even trajectory)
- Milestone timeline (tied to user count, not feature count)
- Risk assessment with specific mitigations
- KPI definitions (what to measure and when to worry)

**Intended use:** Run after all other business design skills. The "final check" before /plan-eng-review.

---

## /launch — Launch Manager

### Design Overview

Launching is a 3-week campaign, not a single post. /launch takes the channel strategy from /gtm and turns it into an executable playbook with platform-specific materials.

For each platform (Product Hunt, Hacker News, Reddit, X/Twitter, etc.), it generates:
- Optimized copy (title, subtitle, description, thread)
- Timing recommendations (day of week, time of day)
- Warm-up strategy (T-14 to T-1)
- Launch day checklist
- Follow-up sequence (T+1 to T+7)

**Intended use:** Run after /gtm, when you're ready to launch. The bridge between strategy and execution.

---

## /content — Content Marketer

### Design Overview

Solo developers don't have time for a content treadmill. /content focuses on the "write once, distribute many" principle: create one substantial piece of content per week and repurpose it across all channels.

The core workflow:
1. One blog post or tutorial per week (SEO-optimized, evergreen)
2. Extract 3-5 social media posts from it
3. Create an email newsletter digest monthly
4. Repurpose best performers into video scripts

/content also handles onboarding email sequences, which are the highest-leverage content for conversion.

**Intended use:** Run after /launch for ongoing content strategy. Reads /gtm channel priorities.

---

## /outreach — Community Manager

### Design Overview

The first 100 users are earned, not acquired. /outreach provides the templates, scripts, and strategies for manual user acquisition that doesn't feel spammy.

Core principle: **give before you ask.** Spend 2 weeks being helpful in communities before mentioning your product. Build reputation first, then introduce your tool as a natural part of helping.

Includes:
- Community participation playbook (which communities, what to say, when to pitch)
- DM/email templates that respect people's time
- Beta tester recruitment strategy
- Partnership outreach for complementary tools/creators

**Intended use:** Run in parallel with /launch for the first-100-users push.

---

## /measure — Growth Analyst

### Design Overview

"What gets measured gets managed" — but what gets measured badly gets managed badly. /measure designs a minimal, decision-driving measurement system.

The framework:
1. **North Star Metric** — the one number that best represents value delivery (e.g., "clips segmented per week")
2. **Funnel stages** — Awareness → Interest → Trial → Purchase → Retention
3. **One metric per stage** — no dashboard with 47 charts
4. **Tool recommendations** — GA4, Plausible, Supabase, Stripe Dashboard, etc.
5. **Review cadence** — what to check daily, weekly, monthly

Anti-pattern: tracking everything. /measure forces you to pick 5-7 metrics that actually change decisions.

**Intended use:** Run after first users arrive. Sets up the infrastructure for /grow and /biz-retro.

---

## /grow — Growth Hacker

### Design Overview

Growth without a system is random marketing. /grow provides the ICE framework for systematic experimentation:

- **Impact:** How many users will this affect? (1-10)
- **Confidence:** How sure are we this will work? (1-10)
- **Ease:** How easy is this to implement? (1-10)

Score = (I + C + E) / 3. Run the highest-scoring experiments first.

Each experiment has:
- Hypothesis: "If we [action], then [metric] will [change] because [reason]"
- Success criteria: defined before running
- Timeline: 1-2 weeks max
- Result: what happened, what we learned

**Intended use:** Run after /measure establishes baseline metrics. Ongoing growth cycle.

---

## /feedback — Customer Success Manager

### Design Overview

Feedback without a system becomes noise. /feedback creates structured channels and a triage process:

1. **Collection:** In-app feedback widget, email follow-ups, social monitoring, post-cancel survey
2. **Classification:** Bug / Feature request / UX issue / Praise / Churn signal
3. **Triage:** Must-fix (retention risk) / Should-do (high demand) / Nice-to-have / Won't-do
4. **Action:** Connect prioritized items to your development backlog
5. **Close the loop:** Tell users when their feedback ships

The key insight: the fastest way to reduce churn is to respond to feedback within 24 hours, even if you can't fix it yet.

**Intended use:** Run after first users. Ongoing feedback loop.

---

## /biz-retro — COO

### Design Overview

/biz-retro is the business counterpart to gstack's /retro. While /retro measures engineering health, /biz-retro measures business health. The ultimate vision is a **3-stack retro** — a unified weekly dashboard across engineering, business, and life.

### The 3-Stack Retro Vision

```
+============================================================================+
|                    UNIFIED WEEKLY RETRO — Week 13                          |
|                    Product: Premiere Pro AI Plugin                          |
+============================================================================+

+--- ENGINEERING (gstack /retro) ----+--- BUSINESS (bizstack /biz-retro) ---+
|                                     |                                      |
|  Commits:    47  (+12 vs last wk)   |  Users:     0 → 12  (+12)           |
|  LOC added:  3.2k                   |  Revenue:   ¥0                      |
|  Test cover: 38%  (▲ from 31%)      |  Waitlist:  45  (+18)               |
|  PRs merged: 12                     |  Signups:   12  (3.5% CVR)          |
|  Bugs fixed: 8                      |  Churn:     0  (no paid yet)        |
|  Ship:       v0.3.0 released        |  NPS:       n/a (too early)         |
|                                     |                                      |
+-------------------------------------+--------------------------------------+

+--- MARKETING ----------------------------+--- LIFE (lifestack /retro) ----+
|                                           |                                |
|  Posts published:  5                      |  Identity score:  7.2/10       |
|  Impressions:      2,340                  |  Top habit:       coding 6/7   |
|  Engagement rate:  4.2%                   |  Energy:          ████████░░   |
|  Top channel:      X/Twitter (8 signups)  |  Focus:           ██████░░░░   |
|  DMs sent:         15                     |  Mood:            ████████░░   |
|  DM reply rate:    26.7% (4/15)           |  Exercise:        4/5 days     |
|  Blog posts:       1                      |  Sleep avg:       6.8h         |
|  YT videos:        0 (behind schedule)    |                                |
|                                           |                                |
+-------------------------------------------+--------------------------------+

+--- INSIGHTS & ACTIONS ---------------------------------------------------+
|                                                                           |
|  [BIZ]  X/Twitter → signup CVR is highest (3.4%). Double down next week.  |
|  [BIZ]  Waitlist growth slowing. Test new channel: YouTube tutorial.      |
|  [BIZ]  Top user request: "Japanese UI" — consider for v0.4.0.           |
|  [ENG]  Test coverage still below 50%. Block: need test fixtures for AI.  |
|  [ENG]  v0.3.0 shipped on time. First public release.                    |
|  [LIFE] Missed YouTube video — energy dip mid-week. Adjust schedule.     |
|  [LIFE] Coding consistency strong. Protect this habit.                    |
|                                                                           |
+--- NEXT WEEK PRIORITIES ------------------------------------------------+
|                                                                           |
|  1. [BIZ]  Record first YouTube tutorial (overdue)                        |
|  2. [BIZ]  Convert 3 waitlist users to beta testers                       |
|  3. [ENG]  Increase test coverage to 50%                                  |
|  4. [ENG]  Start v0.4.0 planning (Japanese UI?)                           |
|  5. [LIFE] Protect Wednesday afternoon for rest                           |
|                                                                           |
+---------------------------------------------------------------------------+
```

This unified view answers three questions every week:
- **Engineering:** "Am I building well?"
- **Business:** "Am I reaching users?"
- **Life:** "Am I sustaining myself?"

When all three are healthy, you're on track. When one drops, the retro surfaces it before it becomes a crisis.

**Intended use:** Weekly ritual. Reads data from gstack /retro, bizstack metrics, and lifestack /retro when available.

---

# Skill Data Flow

```
                    ┌─────────┐
                    │ /persona │
                    └────┬────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          ▼
        ┌──────────┐ ┌────────┐ ┌─────┐
        │/market-  │ │/pricing│ │/gtm │
        │  scan    │ │        │ │     │
        └────┬─────┘ └───┬────┘ └──┬──┘
             │           │         │
             └─────┬─────┘         │
                   ▼               │
             ┌──────────┐          │
             │ /bizplan  │          │
             └──────────┘          │
                                   │
         ┌────────────┬────────────┤
         ▼            ▼            ▼
    ┌─────────┐ ┌──────────┐ ┌──────────┐
    │ /launch │ │ /content │ │/outreach │
    └─────────┘ └──────────┘ └──────────┘
                                   │
                    ┌──────────────┤
                    ▼              ▼
              ┌──────────┐  ┌──────────┐
              │ /measure │  │/feedback │
              └────┬─────┘  └──────────┘
                   │
                   ▼
              ┌──────────┐
              │  /grow   │
              └────┬─────┘
                   │
                   ▼
            ┌────────────┐
            │ /biz-retro │
            └────────────┘
```
