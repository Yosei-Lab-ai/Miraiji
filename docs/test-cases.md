# bizstack Test Cases & Usage Scenarios

## Introduction

**For gstack users:** You already know the sprint cycle — Think → Plan → Build → Review → Test → Ship. bizstack fills the gap between `/plan-ceo-review` and `/plan-eng-review` (who are you building for? at what price? through what channel?) and the gap after `/ship` (how do you get it to users?). Run `/persona → /pricing → /gtm` before engineering, and `/launch → /outreach → /measure` after shipping.

**For business beginners:** You can code but you've never sold software. bizstack walks you through the three decisions you must make before building: who's your user, what's your price, and how will you reach them. Each skill is an expert who asks you tough questions and won't let you skip the hard parts.

---

## Scenario 1: gstack User's First bizstack Session

### Context

Sho has been using gstack for months. He just finished `/office-hours` and `/plan-ceo-review`, which confirmed the idea: **an AI-powered segmentation plugin for Adobe Premiere Pro**. He's about to jump into `/plan-eng-review` — but he realizes he can't design the auth system without knowing the pricing model, and he can't design the pricing without knowing the user.

### Prerequisites

- gstack installed and `/plan-ceo-review` completed
- bizstack installed (`bash setup` done)
- `~/.bizstack/` directory exists

### Step 1: `/persona`

```
> /persona
```

> **Researcher:** I'm your UX Researcher. Before you write a single line of code, we need to know exactly who we're building for — not a market segment, not a demographic, one specific person. Let's find them.
>
> First question: **Tell me about the person who needs this product most. What does their day look like?** Walk me through their morning to end-of-day. What's their job title? What tools do they open first? What frustrates them before lunch?

**Sho:** Video editors who use Premiere Pro. They do a lot of manual masking and rotoscoping work.

> **Researcher:** "Video editors who use Premiere Pro" is a market, not a person. I need one human being. Are they a freelancer editing YouTube videos in a home studio, or a junior editor at a post-production house cutting broadcast commercials? Are they in LA, Tokyo, London? How old are they? What's on their desk right now?
>
> Give me one specific person.

**Sho:** OK. He's a freelance video editor, early 30s, living in Tokyo. He mainly edits corporate promo videos and YouTube content for small businesses. He learned Premiere in vocational school and has been using it ever since.

> **Researcher:** Now I can see him. Let me call him Kenji.
>
> Kenji, 32, freelance editor in Shibuya. Opens Premiere Pro around 9am with a canned coffee from the conbini. Morning is rough cuts — syncing audio, trimming clips, building the story. He's fast at this, it's his craft. But around 2pm, the client emails: "Can you make me pop off the background for the thumbnail and the intro?" Kenji's stomach drops. He knows that means 2-3 hours of frame-by-frame masking for a 30-second clip of a CEO who won't stop gesturing.
>
> Sound right? Anything off?

**Sho:** Yeah that's pretty accurate. He's always under deadline pressure too — clients want everything "by tomorrow morning."

> **Researcher:** Good. The pain isn't just tedium — it's tedium under deadline.
>
> **Question 2: How is Kenji solving this problem today?** What's his current workaround?

**Sho:** He uses Premiere's built-in masking tools which are fully manual. Sometimes he dynamic-links to After Effects and uses Rotobrush, but the round-trip is slow and breaks his flow. He's tried a couple of free browser-based tools but the quality isn't client-grade.

> **Researcher:** Three workarounds, all broken:
>
> 1. **Manual masking in Premiere** — works but 2-3 hours per clip
> 2. **After Effects Rotobrush via Dynamic Link** — better AI but 20-30 min round-trip overhead, and Dynamic Link is notoriously unstable
> 3. **Free browser tools** — fast but output quality gets him yelled at by clients
>
> The pattern: he's forced to choose between quality and speed every single time. Your plugin needs to deliver both, inside Premiere.
>
> **Question 3: How much would Kenji pay to make this problem disappear?** What does he currently spend on tools?

**Sho:** He pays about ¥7,000/month for Creative Cloud. He's bought plugins before — things like FilmConvert Nitrate for around ¥8,000 as a one-time purchase. Magic Bullet Looks was about ¥12,000. He wouldn't want another big subscription on top of CC.

> **Researcher:** Let me map his spending:
>
> - Adobe Creative Cloud: ¥7,000/mo
> - Plugin purchases: ¥8,000-¥12,000 one-time (FilmConvert, Magic Bullet)
> - Total tool budget: roughly ¥10,000-15,000/mo including amortized purchases
>
> Key insight: Kenji **buys plugins as one-time purchases**. He's subscription-fatigued from Adobe. But here's the math: if your plugin saves him 2-3 hours per project, and he does 8+ projects/month, that's 16-24 hours saved. At his freelance rate of ¥3,000-5,000/hr, that's ¥48,000-120,000/mo in recaptured billable time.
>
> Willingness-to-pay: ¥2,000-5,000/mo subscription or ¥15,000-25,000 one-time.
>
> **Question 4: Where does Kenji hang out online?** Which accounts does he follow, what communities is he in?

**Sho:** Twitter/X for sure — the Japanese video editing community is active there. Reddit probably — r/premiere and r/VideoEditing. He watches YouTube tutorials from channels like Casey Faris and Premiere Gal. He probably checks Vook, which is a Japanese video production media site.

> **Researcher:** Pinning it down:
>
> - **X/Twitter:** Japanese video editing community. Follows @premierepro_jp, Vook account, individual creators who share tips
> - **Reddit:** r/premiere (87k), r/VideoEditing (196k), r/AfterEffects
> - **YouTube:** Casey Faris, Premiere Gal, Japanese tutorial channels (サンゼスタジオ etc.)
> - **Japanese communities:** Vook.vc (video production media + community), Adobe Community Forums JP
> - **Discovery path:** YouTube tutorial → Adobe Exchange search → X/Twitter recommendation
>
> This is your GTM map. His discovery path starts on YouTube.
>
> **Last question — the most important one: What would stop Kenji from using your plugin?**

**Sho:** Quality. If the AI segmentation looks janky on edges — hair, fingers, motion blur — he won't use it on client work. Also workflow integration: if it doesn't work natively in Premiere's timeline, he won't bother. And subscription pricing — he'd resist another monthly fee.

> **Researcher:** Three barriers, ranked:
>
> 1. **Quality trust** (Primary): "Will this look professional?" He's been burned by free tools. Your demo must show client-grade output on real footage — hair detail, hand gestures, motion blur.
> 2. **Workflow integration**: Must be a Premiere panel/plugin. No exports, no round-trips, no new apps. If it adds friction, he'll go back to manual.
> 3. **Pricing model**: Subscription fatigue. One-time purchase or annual-with-discount strongly preferred.
>
> Product implications:
> - Demo content must be real-world footage, not tech demos with clean studio backgrounds
> - Plugin must operate on timeline clips directly
> - Offer a one-time purchase option
>
> Let me synthesize Kenji's persona.

**Output saved to `~/.bizstack/personas/persona-001.md`:**

```markdown
# Persona: Kenji

**Created:** 2026-03-25
**Product:** AI Segmentation Plugin for Premiere Pro

## Profile
- **Name:** Kenji
- **Age:** 32
- **Location:** Shibuya, Tokyo
- **Role:** Freelance Video Editor (solo)
- **Experience:** 8 years in video editing, self-employed for 4

## A Day in Their Life
Kenji starts his day around 9am at his home studio in Shibuya, opening Premiere Pro
with a canned coffee. His morning is productive — rough cuts, audio sync, story
structure. He's good at this and moves fast. By early afternoon, client requests
start coming in: "Can you isolate me from the background for the intro?" His mood
shifts. He knows he's about to spend 2-3 hours on frame-by-frame masking for a
30-second clip. Under constant deadline pressure ("can you finish by tomorrow
morning?"), he either rushes through manual masking with mediocre results or
dynamic-links to After Effects, breaking his flow for 30+ minutes of round-trip.

## The Problem
- **Pain point:** Manual segmentation/masking is tedious, slow, and error-prone
- **Frequency:** 3-5 times per week across client projects
- **Impact:** 10-15 hours/week of low-value work; missed deadlines; quality compromises

## Current Workaround
- **What he does now:** Manual masking in Premiere + occasional AE Rotobrush
- **Tools he uses:** Premiere Pro masking tools, After Effects Rotobrush, free browser tools
- **What's broken:** No option delivers both speed and client-grade quality

## Willingness to Pay
- **Budget range:** ¥2,000-5,000/mo or ¥15,000-25,000 one-time
- **Current spending:** CC ¥7,000/mo, plugins ¥8,000-12,000 one-time
- **Price sensitivity:** Medium-high (freelancer, subscription-fatigued)

## Where They Are
- **Social:** X/Twitter (Japanese video editing community)
- **Communities:** r/premiere, r/VideoEditing, Vook.vc, Adobe Forums JP
- **Content:** Casey Faris, Premiere Gal, サンゼスタジオ on YouTube

## Adoption Barriers
- **Primary barrier:** Quality trust — will AI output pass client scrutiny?
- **Secondary barriers:** Must be native Premiere plugin; subscription fatigue
- **What would overcome them:** Real-footage demo, free trial, one-time purchase option
```

> **Researcher:** Your persona is saved. Next recommended step: `/pricing` to design your price structure based on Kenji's willingness to pay, or `/gtm` to plan how to reach him.

### Step 2: `/pricing`

```
> /pricing
```

> **CFO:** I'm your CFO. The price determines the architecture — what you charge changes what you build. Let's get this right before you write code.
>
> I've read Kenji's persona. He currently spends ¥7,000/mo on CC and buys plugins in the ¥8,000-12,000 range. His ceiling is ¥2,000-5,000/mo or ¥15,000-25,000 one-time. He has subscription fatigue.
>
> **Step 1: Pricing model.** Here are your options for a Premiere Pro plugin:

| Model | Fit | Pros | Cons |
|-------|-----|------|------|
| Free / OSS | Poor | Fast adoption | Zero revenue; if AI runs server-side, free users cost money |
| Freemium | Strong | Low friction trial, upsell path | Must define clear free/paid boundary |
| Subscription | Moderate | Recurring revenue, predictable | Kenji has subscription fatigue |
| One-time | Strong | Matches Kenji's buying pattern | No recurring revenue stream |
| Usage-based | Weak | Fair per-clip pricing | Complex billing, UX friction |

> My recommendation: **Freemium with both subscription and one-time purchase options.** The free tier drives trial (critical for overcoming quality trust barrier), subscription for ongoing users, and one-time for Kenji's tribe who hate monthly fees.
>
> What's your instinct?

**Sho:** I was thinking freemium too. Free tier with some limit, then paid for full features. Is having both subscription AND one-time too complicated?

> **CFO:** Not if you keep it simple. Many plugin makers do this: monthly, annual, and lifetime. The math actually works in your favor — the lifetime price is just the annual price × 2-3, so you get cash upfront.
>
> Critical question before tier design: **does the AI inference run locally or server-side?**

**Sho:** Locally on the user's GPU. No server costs.

> **CFO:** That's the best possible answer. Free users cost you nothing. Freemium economics are clean.
>
> **Step 2: Competitive landscape:**

| Competitor | Price | Model | Limitation |
|-----------|-------|-------|------------|
| Rotobrush (AE built-in) | ¥0 (in CC) | Bundled | Requires AE round-trip |
| RunwayML | $15-76/mo | Cloud subscription | Cloud upload, not in Premiere |
| Topaz Video AI | $299 one-time | Desktop app | Not a Premiere plugin |
| Boris FX Silhouette | $1,695 one-time | Pro license | Enterprise pricing, overkill |
| Free browser tools | ¥0 | Free | Low quality, not integrated |

> You're in a gap: **better than free tools, integrated into Premiere (unlike everything else), affordable (unlike Boris).** Strong position.
>
> **Step 3: Tier design:**

```
FREE TIER: "Starter"
├── AI segmentation on clips up to 30 seconds
├── 720p max output resolution
├── Small watermark: "Made with [Plugin]"
└── Goal: let Kenji prove quality on a real project

PRO TIER: ¥2,980/mo or ¥29,800/year (¥2,483/mo effective — 17% savings)
├── Unlimited clip length
├── Full resolution up to 8K
├── No watermark
├── Batch processing (multiple clips at once)
├── Priority model updates
└── Upsell trigger: first time user hits 30s limit on a real project

LIFETIME: ¥59,800 (one-time, current major version)
├── Same as Pro
├── Free updates within v1.x
├── Major version upgrades at 50% discount
└── For Kenji's tribe who hate subscriptions
```

> **Step 4: Break-even:**

```
Monthly fixed costs:
  Apple Developer Program:  ¥1,083/mo (¥12,999/yr)
  Domain + landing page:    ¥1,500/mo
  Adobe Exchange fee:       15% of revenue
  Code signing cert:        ¥833/mo (¥10,000/yr)
  Total fixed:              ~¥3,416/mo

Per-user economics (monthly subscription):
  Price:                    ¥2,980/mo
  Adobe Exchange cut (15%): ¥447/mo
  Net per user:             ¥2,533/mo

Break-even:        ¥3,416 ÷ ¥2,533 = 2 paying subscribers
Ramen profit (¥200k/mo):   79 paying subscribers
Comfortable (¥500k/mo):    198 paying subscribers
```

> 2 subscribers to break even. 79 for ramen profitability. These are excellent numbers.
>
> **Step 5: Free tier engineering spec** — this goes directly to `/plan-eng-review`:

```
FREE TIER LIMITS (→ /plan-eng-review input):
─────────────────────────────────────────────
Clip length:    30 seconds max
                → Hard limit. Show upgrade prompt when exceeded.
                → Implementation: check clip duration before processing.

Resolution:     720p max output
                → Downscale output if source > 720p.
                → Free users see "Upgrade to Pro for full resolution" overlay.

Watermark:      Small corner watermark composited in final render
                → Applied post-segmentation, not removable.
                → Easy to implement: overlay PNG at render stage.

Batch:          Single clip only (no batch processing)
                → Disable batch UI for free tier.

LICENSING:
Auth method:    License key validation (no user accounts needed)
Billing:        Gumroad or Paddle (handles Japanese payments well)
                → Stripe also viable but more integration work.
Key delivery:   Email after purchase → enter in plugin settings panel
Validation:     Online check on first activation, then periodic (30 days)
                → Offline grace period: 7 days

NO server infrastructure needed (local inference).
```

**Output saved to `~/.bizstack/pricing/pricing-001.md`**

> **CFO:** Pricing design saved. The engineering requirements section has your billing, auth, and limit specs for `/plan-eng-review`. Next step: `/gtm` to figure out how to reach those 79 paying users.

### Step 3: `/gtm`

```
> /gtm
```

> **CMO:** I'm your CMO. You've got a product and a price. Now we need to get it in front of the right people.
>
> I've read Kenji's persona. He discovers plugins through YouTube tutorials, Adobe Exchange browsing, and X/Twitter recommendations. He's in r/premiere, Vook.vc, and Adobe forums.
>
> Your pricing: freemium with Pro at ¥2,980/mo. Net ¥2,533/user after Exchange cut. You need 79 paying users for ramen profitability. Let's get there.
>
> **Positioning.** Let's build your statement.

**Sho:** "AI segmentation for Premiere Pro that just works."

> **CMO:** "Just works" is what every tool claims. What makes you different from Rotobrush? From Runway? Let me sharpen this:
>
> For **freelance video editors** who **lose hours to manual masking**, **[Plugin]** is a **Premiere Pro plugin** that **segments subjects in one click with AI, right on your timeline**. Unlike **After Effects Rotobrush**, you **never leave Premiere**. Unlike **cloud tools**, your **footage stays on your machine**.
>
> Two differentiators: **no round-trip** and **local processing**. These are Kenji's actual pain points.

**Sho:** That's good. I like "never leave Premiere" — that's the core promise.

> **CMO:** That's your tagline. Now messaging:
>
> **One-liner:** One-click AI masking. Never leave Premiere.
>
> **Elevator Pitch (30s):**
> Freelance editors waste hours on frame-by-frame masking — or break their flow round-tripping to After Effects. [Plugin] brings AI segmentation directly into your Premiere Pro timeline. Select a clip, click segment, done. Runs on your GPU, footage never leaves your machine. Free to try.
>
> **Channel strategy.** Based on Kenji's persona, your top 3:

### Channel 1: YouTube — PRIMARY

> - **Why:** Kenji's #1 plugin discovery channel. Tutorial content compounds — a video posted today gets views for years.
> - **Content:** Before/after demos, "I masked this in 10 seconds" reaction-style videos, Premiere Pro workflow tutorials that naturally feature your plugin
> - **Frequency:** 1 video every 2 weeks (realistic for a solo dev)
> - **First action this week:** Record a 90-second side-by-side: manual masking (time-lapse showing 2 hours) vs. your plugin (real-time, 10 seconds). No fancy editing needed. Raw and honest.
> - **Success metric:** Views → Adobe Exchange click-through

### Channel 2: Reddit — SECONDARY

> - **Why:** r/premiere has 87k members actively asking "how do I mask/rotoscope?" High-intent users.
> - **Content:** Helpful comments on masking questions, before/after showcase posts, "I built this" launch post
> - **Frequency:** 3-4 comments/week + 1 post/month
> - **First action this week:** Search r/premiere for "mask" "rotoscope" "segment" in the last month. Leave genuinely helpful replies on 5 posts. Don't mention your plugin yet — build karma first.
> - **Success metric:** Upvotes, DMs, installs from Reddit referral

### Channel 3: X/Twitter (Japanese community) — TERTIARY

> - **Why:** Japanese video editing community is tight-knit on X. One retweet from a respected editor can drive 50 installs.
> - **Content:** Build-in-public updates in Japanese, 15-second demo clips, before/after comparisons
> - **Frequency:** 3-5 tweets/week in Japanese
> - **First action this week:** Post a 15-second screen recording of the AI segmentation in action. Japanese caption. Tag @Vook_vc.
> - **Success metric:** Retweets, followers, DMs

> **First 100 users:**

```
FIRST 10 (Manual — Week 1-2):
1. Post before/after demo in r/premiere             → 3-5 installs
2. DM 20 r/VideoEditing users who asked about masks → 2-3 installs
3. Share in 3 Japanese FB groups for video editors   → 2-3 installs
4. Ask 3 editor friends to beta test                 → 3 installs

USERS 11-50 (Community — Week 3-6):
5. YouTube tutorial: "One-Click Masking in Premiere" → 10-15 installs
6. Answer 15 Adobe Forum threads about masking       → 5-8 installs
7. "Show HN: AI segmentation for Premiere Pro"       → 5-10 installs
8. Reach out to 3 Premiere YouTubers for reviews     → 5-10 each

USERS 51-100 (Content + WoM — Week 7-12):
9.  2nd YouTube video: workflow tutorial              → 10-15 installs
10. Cross-post best Reddit demo to X in Japanese      → 5-10 installs
11. Early user testimonials + "tag us" CTA            → 10-20 referrals
12. Adobe Exchange listing SEO (keywords, screenshots) → ongoing organic
```

**Output saved to `~/.bizstack/gtm/gtm-001.md`**

> **CMO:** GTM strategy saved. You now have persona, pricing, and GTM. You're ready for gstack's `/plan-eng-review` — bring the pricing engineering requirements (free tier limits, license key validation, Gumroad/Paddle integration) into your tech design session.

### Step 4: Back to gstack

```
> /plan-eng-review
```

The engineering review now has concrete inputs from bizstack:

- **From /pricing:** Free tier limits (30s clip, 720p, watermark), license key validation, Gumroad/Paddle billing, no server infrastructure needed
- **From /persona:** Must be native Premiere plugin (CEP/UXP panel), local GPU inference, no round-trips
- **From /gtm:** Adobe Exchange listing required (affects build/packaging), demo footage needed (affects test fixtures)

Without bizstack, these engineering decisions would have been guesses.

### Common Mistakes This Flow Corrects

| Mistake | How bizstack corrects it |
|---------|------------------------|
| "I'll build the whole thing then figure out pricing" | /pricing forces price-before-code |
| "My target is video editors" | /persona forces one specific person |
| "I'll just post it on Twitter" | /gtm forces 3 channels with specific actions |
| "I'll make it free at first" | /pricing demands a monetization strategy even for free |
| "I'll add auth later" | /pricing outputs engineering specs for auth/billing upfront |

---

## Scenario 2: Business Beginner Starting from Scratch

### Context

Yuki is a web developer with 3 years of experience. She can build a full-stack app but has never sold software. She has a vague idea: "a tool for freelancers to manage invoices." She doesn't use gstack or lifestack — just heard about bizstack from a tweet and wants to try it.

### Prerequisites

- bizstack installed
- No prior gstack/lifestack data
- No existing `~/.bizstack/` data

### Step 1: `/persona`

```
> /persona
```

> **Researcher:** I'm your UX Researcher. Before you write a single line of code, we need to know exactly who we're building for — not a market segment, not a demographic, one specific person. Let's find them.
>
> **Question 1: Who needs this product most? What does their day look like?**

**Yuki:** Freelancers. They struggle with invoicing and tracking payments. I think designers, developers, writers — anyone who freelances.

> **Researcher:** Stop. "Anyone who freelances" is everyone and therefore no one. A freelance developer invoicing a SaaS company in USD has completely different needs from a freelance illustrator invoicing a local bakery in JPY.
>
> Pick ONE person. Not a category — a human being. Who specifically have you seen struggle with this?

**Yuki:** OK, my friend Mika. She's a freelance graphic designer. She uses Excel to make invoices and sometimes forgets to follow up on unpaid ones.

> **Researcher:** Now we're talking. Tell me about Mika's day. What time does she start? What tools does she open? When does the invoicing pain actually hit?

**Yuki:** She's 28, lives in Osaka. She opens Figma and Slack in the morning to work on client projects. The invoicing pain hits at the end of the month — she spends a whole evening creating invoices in Excel, manually calculating tax, copying bank details, and exporting to PDF. Then she has to remember who paid and who didn't.

> **Researcher:** Good. Mika, 28, freelance graphic designer in Osaka. Morning is creative work in Figma. End-of-month is invoice hell in Excel. The pain is predictable, monthly, and takes an entire evening.
>
> **Question 2: How is Mika solving this today?**

**Yuki:** Excel templates she made herself. She copies last month's invoice, changes the details, exports to PDF, and emails it. For tracking payments, she has a separate spreadsheet. Sometimes she forgets to check it and doesn't realize a payment is 30 days overdue.

> **Researcher:** So Mika's workaround is:
> 1. **Excel template** → manual, error-prone, no automation
> 2. **Separate tracking spreadsheet** → disconnected from invoices, easy to forget
> 3. **Email delivery** → no read receipts, no automatic follow-up
>
> Cost: ~3 hours/month on invoicing itself + unknown revenue lost from forgetting to chase unpaid invoices. That's real money.
>
> **Question 3: How much would Mika pay to make this disappear?**

**Yuki:** I don't know... freelancers don't have much money. Maybe it should be free?

> **Researcher:** Let me push back. "Freelancers don't have much money" is an assumption, not data. Mika is a professional graphic designer charging clients for her work. She has a tool budget.
>
> What does Mika currently pay for? Figma? Adobe CC? A domain? Accounting software?

**Yuki:** She pays for Figma (¥1,800/mo for pro), Adobe CC (¥7,000/mo), her website hosting (¥1,000/mo), and she uses the free version of freee for basic accounting.

> **Researcher:** Mika spends ¥9,800/mo on tools already. She uses free freee for accounting, which means:
> 1. She IS willing to pay for tools that matter to her workflow (Figma, Adobe)
> 2. She defaults to free for things she considers secondary (accounting, invoicing)
> 3. But she's spending 3+ hours/month on manual invoicing — at her rate of ¥4,000-5,000/hr for design work, that's ¥12,000-15,000 of lost productive time
>
> Willingness to pay: ¥500-1,500/mo if you make the value obvious. Or ¥0 with a clear upgrade path.
>
> **Do NOT decide "free" because you assume freelancers are poor. Decide "free" only if it's strategically correct.** We'll resolve this in /pricing.
>
> **Question 4: Where does Mika hang out online?**

**Yuki:** Twitter for sure. And she's in some designer Slack communities. She reads design blogs. Instagram for portfolio stuff.

> **Researcher:** Be specific. Which Slacks? Which blogs?
>
> Let me guess based on the Japanese freelance designer profile:
> - **X/Twitter:** Japanese design community, follows design tool accounts
> - **Slack:** Design Scramble, Boss.design community, local freelance groups
> - **Instagram:** Portfolio, follows other designers (but doesn't discover tools here)
> - **Media:** note.com (Japanese), design blogs
> - **Forums:** Freelance-related threads on はてなブックマーク
>
> Does that match?

**Yuki:** Yeah, that's close. She also reads things on note.com a lot.

> **Researcher:** Discovery path: X/Twitter recommendation → note.com article → try the tool.
>
> **Question 5: What would stop Mika from using your invoicing tool?**

**Yuki:** Switching cost. She already has her Excel templates set up. And trust — she needs to know her invoice data is safe. Also learning curve — she doesn't want to spend time setting up a new tool.

> **Researcher:** Three barriers:
> 1. **Switching cost** (Primary): Her Excel templates are "good enough." You need to make the first invoice faster than copying her Excel template.
> 2. **Data trust**: Financial data is sensitive. Needs to feel secure.
> 3. **Setup friction**: Must be zero-config. Import existing client list, auto-detect tax rate.
>
> Product implication: **your onboarding needs to be "paste your client list, send your first invoice in 2 minutes."** If setup takes longer than one Excel copy-paste, Mika won't switch.

**Output saved to `~/.bizstack/personas/persona-001.md`**

### Step 2: `/pricing`

```
> /pricing
```

> **CFO:** I've read Mika's persona. She pays ¥9,800/mo for tools but uses free freee for accounting. Her invoicing pain costs her ¥12,000-15,000/mo in lost time. Willingness to pay: ¥500-1,500/mo.
>
> Let's talk pricing model.

**Yuki:** I think freemium. Free for basic invoicing, paid for automation features like payment reminders.

> **CFO:** Freemium is the right call here. But let me stress-test your free/paid boundary. What specifically is free and what's paid? This is the hardest decision in freemium and most founders get it wrong by giving away too much.

**Yuki:** Free: create and send invoices, up to maybe 5 clients. Paid: unlimited clients, automatic payment reminders, payment tracking dashboard, recurring invoices.

> **CFO:** Solid instinct. But "5 clients" is tricky — a freelance designer with 5 clients might never upgrade. Let me suggest a different boundary:

```
FREE TIER: "Solo"
├── Unlimited invoices (don't limit the core action)
├── Up to 3 active clients
├── Manual payment tracking
├── bizstack branding on invoice footer
└── Goal: get Mika to send her first invoice and feel the magic

PRO TIER: ¥980/mo (annual: ¥9,800/yr = ¥817/mo)
├── Unlimited clients
├── Automatic payment reminders (3-day, 7-day, 30-day overdue)
├── Payment tracking dashboard
├── Recurring invoice templates
├── Remove branding
├── CSV/PDF export of all data
└── Upsell trigger: Mika's 4th client

Why ¥980/mo:
- Under ¥1,000/mo psychological barrier
- Below her freee premium (¥1,980/mo) — "cheaper than accounting software"
- 3 clients → 4th client is natural growth moment
- Annual discount brings it to daily coffee price (¥27/day)
```

> Break-even:

```
Monthly fixed costs:
  Server (Supabase free tier → Railway): ¥0-2,000/mo
  Domain:                                 ¥100/mo
  Resend (email):                         ¥0 (free tier: 3,000 emails/mo)
  Stripe fees:                            3.6% per transaction
  Total fixed:                            ~¥2,100/mo

Per-user economics:
  Price:           ¥980/mo
  Stripe cut:      ¥35/mo
  Net per user:    ¥945/mo

Break-even:                    3 paying users
Ramen profit (¥200k/mo):      212 paying users
```

> **CFO:** 3 users to break even. 212 for ramen profitability. The unit economics work, but 212 paying users means you need ~4,000-5,000 free users (at 4-5% conversion). That's achievable in the Japanese freelancer market, but it'll take 6-12 months.

**Output saved to `~/.bizstack/pricing/pricing-001.md`**

### Step 3: `/gtm`

```
> /gtm
```

> **CMO:** Your persona is Mika, freelance designer in Japan. Your price is freemium at ¥980/mo. You need 212 paying users, which means ~4,000 free users. Let's design how to get there.
>
> **Channel strategy.** I know what you're going to say — Twitter, Instagram, TikTok, YouTube, a blog, maybe a podcast. Am I right?

**Yuki:** Ha, yeah I was thinking all of those...

> **CMO:** Stop. You're one person. You cannot maintain quality presence on 6 platforms. It's the fastest way to burn out and achieve nothing. **Pick 3. Kill the rest.**
>
> Based on Mika's persona, here's my recommendation:

```
1. X/Twitter (Japanese freelance community) — PRIMARY
   Why: Mika's primary social platform, discovery + word-of-mouth

2. note.com (Japanese blog platform) — SECONDARY
   Why: Mika reads note regularly. SEO + long-form content.
   "フリーランスの請求書管理" articles rank well.

3. Freelancer Slack communities — TERTIARY
   Why: Direct access to Mika's exact peer group. High trust.
```

> **What I'm killing and why:**
> - Instagram: Mika uses it for portfolio, not tool discovery. Wrong context.
> - TikTok: No evidence Mika discovers business tools here.
> - YouTube: Good channel, but you don't have time for video + all the above.
> - Podcast: Audience too small, too much production time.
>
> You can add YouTube later when you have revenue to justify the time investment.

**Yuki:** Makes sense. I was going to spread myself too thin.

> **CMO:** Exactly. Here's your first 100 users plan:

```
FIRST 10 (Week 1-2):
1. Post on X: "フリーランスの請求書、まだExcelで作ってませんか？" with screenshot → 3-5
2. DM 10 freelance designers you know/follow → 2-3
3. Post in 2 freelancer Slack communities → 2-3

USERS 11-50 (Week 3-8):
4. note.com article: "フリーランスデザイナーの請求書管理を自動化した話" → 10-20
5. X thread: "フリーランス3年目で気づいた請求書の失敗5選" (storytelling) → 5-10
6. Answer 10 questions about freelance invoicing on X → 3-5
7. Ask 5 early users for testimonials, quote-tweet them → 5-10

USERS 51-100 (Week 9-16):
8. 2nd note article: "月末の3時間を取り戻す方法" → 10-15
9. Referral program: "友達紹介で1ヶ月無料" → 10-15
10. X spaces: host "フリーランスのお金周り" conversation → 5-10
```

> Weekly time budget:

| Activity | Hours/week |
|----------|-----------|
| X/Twitter (posts + replies) | 1.5h |
| note.com (1 article/2 weeks) | 1h |
| Slack community engagement | 0.5h |
| DMs/outreach | 0.5h |
| **Total** | **3.5h** |

**Output saved to `~/.bizstack/gtm/gtm-001.md`**

### Next Steps

> **CMO:** You have three options from here:
> 1. **If you use gstack:** Run `/plan-eng-review` with your pricing engineering requirements (free tier limits, Stripe integration, email sending)
> 2. **If you don't use gstack:** Start building your MVP manually, targeting Mika's core flow: create invoice → send → track payment
> 3. **Either way:** When your MVP is ready, come back for `/launch` to plan your public launch

### Common Mistakes This Flow Corrects

| What Yuki said | What the skill forced |
|---|---|
| "Freelancers — designers, devs, writers" | One person: Mika, 28, graphic designer, Osaka |
| "Maybe it should be free?" | Free is a strategy, not a default. ¥980/mo with free tier |
| "Twitter, Instagram, TikTok, YouTube, blog, podcast" | 3 channels: X, note.com, Slack communities |
| "I don't know how much she'd pay" | Mapped current spending → derived willingness-to-pay |

---

## Scenario 3: OSS Project (Lifestack)

### Context

Sho built lifestack — a Claude Code skill pack for personal identity and self-growth. It's open-source and MIT-licensed. Nobody knows it exists. He doesn't want to charge for it directly, but he wants: GitHub stars, community, and a foundation for potential future monetization.

### Prerequisites

- bizstack installed
- lifestack repo exists on GitHub
- No prior bizstack data for this project

### Step 1: `/persona`

```
> /persona
```

> **Researcher:** Let's find who lifestack is for. One person.
>
> **Question 1: Who needs this most? What does their day look like?**

**Sho:** Developers who use Claude Code and are interested in self-improvement. They want to be intentional about their personal growth, not just their code.

> **Researcher:** "Developers interested in self-improvement" is still broad. Is this person a 22-year-old junior dev trying to figure out their career? A 35-year-old senior engineer going through a mid-career crisis? A founder who works 80 hours and has no life outside code?
>
> Who specifically did you build this for?

**Sho:** Honestly, me. A solo developer in their late 20s to 30s who can build things but feels like they're just grinding without direction. They've read Atomic Habits and maybe tried journaling apps but nothing stuck.

> **Researcher:** Perfect. Let me call him Taro.
>
> Taro, 31, full-stack developer at a startup in Tokyo. Technically skilled — can ship a feature in a day. But he feels like he's building other people's dreams. He's read Atomic Habits, tried Notion life dashboards, dabbled with journaling apps. Nothing stuck because none of those tools live where he works: the terminal.
>
> He spends 8+ hours/day in Claude Code. If self-reflection happened there, he might actually do it.
>
> **Question 2: Current workaround?**

**Sho:** Scattered Notion pages. A journal app he opens once a month. Sometimes writes reflections in Apple Notes but never reads them back. No system.

> **Researcher:** Workaround: fragmented, disconnected, and never reviewed. The key insight: **Taro's self-reflection tools are separated from his work tools.** He has to context-switch to reflect, which means he never does.
>
> **Question 3: Willingness to pay?**

**Sho:** It's OSS, I don't plan to charge.

> **Researcher:** I hear you. But let me reframe the question: **what would Taro pay if it weren't free?** This matters because it tells us the perceived value, which informs your future monetization and your positioning.
>
> What does Taro currently pay for self-improvement tools?

**Sho:** Maybe Headspace or Calm subscription — ¥600/mo. Books — ¥1,500-2,000 each. He bought an online course once for ¥10,000. But he'd probably expect a CLI tool to be free.

> **Researcher:** Taro's self-improvement spend: ¥2,000-3,000/mo. He expects CLI tools to be free (developer culture), but he pays for content (books, courses) and wellness apps.
>
> This tells us: free tool, but there's a monetization path through **content and services** (coaching, premium content, paid workshops). We'll map this in /pricing.
>
> **Question 4: Where does Taro hang out?**

**Sho:** X/Twitter dev community, Hacker News, r/ClaudeAI, GitHub trending, dev.to maybe. Japanese dev community on X.

> **Researcher:** Pinned:
> - **GitHub:** Browses trending repos, stars tools he finds interesting
> - **X/Twitter:** Japanese dev community, follows Claude/AI accounts
> - **Reddit:** r/ClaudeAI, r/singularity, r/productivity
> - **Hacker News:** Reads daily, occasionally comments
> - **Discovery path:** HN/Reddit post → GitHub repo → star → try it
>
> **Question 5: Adoption barriers?**

**Sho:** "This seems like a gimmick." Self-help + CLI feels weird. Also setup friction — if it takes more than 5 minutes to install, he won't bother. And privacy — he won't put personal reflections in a cloud service.

> **Researcher:** Three barriers:
> 1. **Credibility gap**: "Self-help in a terminal? Really?" Must demonstrate real value quickly.
> 2. **Setup friction**: Must install in under 2 minutes. One command.
> 3. **Privacy**: Must be local-only. No telemetry, no cloud. This is actually a selling point.

**Output saved to `~/.bizstack/personas/persona-001.md`**

### Step 2: `/pricing`

```
> /pricing
```

> **CFO:** OSS project. Revenue = ¥0. But let me be clear: **free does not mean no business model.** If you're investing your time, you need a return — even if it's not direct revenue.
>
> Let me map the value exchange:

```
WHAT YOU INVEST:        WHAT YOU GET BACK:
─────────────────       ──────────────────
Dev time (20h/mo)       GitHub stars (portfolio value)
Support time (5h/mo)    Community (network effects)
                        Reputation (consulting leads)
                        Learning (skills development)
                        User base (future product foundation)
```

> **Monetization paths, ranked by feasibility:**

```
1. GITHUB SPONSORS / Ko-fi (Low effort, low return)
   Expected: ¥5,000-20,000/mo at 500+ stars
   Effort: Add sponsor button, that's it

2. PREMIUM SKILLS (Medium effort, medium return)
   Free: /vision, /checkpoint, /mentor
   Paid: /deep-analysis, /quarterly-review, /team-coaching
   Expected: ¥1,500/mo × 50 users = ¥75,000/mo
   Effort: Build premium skill pack, payment integration

3. WEB APP VERSION (High effort, high return)
   Lifestack as a web app with dashboards, visualizations, history
   Expected: ¥2,980/mo × 200 users = ¥596,000/mo
   Effort: Full product build (6+ months)

4. COACHING / CONSULTING (Low effort, high per-unit return)
   "Lifestack-powered personal coaching" — 1:1 sessions
   Expected: ¥10,000/session × 10 sessions/mo = ¥100,000/mo
   Effort: Your time (doesn't scale, but validates demand)
```

> **My recommendation:** Start with path 1 (sponsors) immediately, design for path 2 (premium skills) as your first monetization milestone, and keep path 3 as the long-term vision.
>
> **OSS "engineering" requirements:**

```
OSS SUSTAINABILITY SPEC:
─────────────────────────
Sponsorship:     GitHub Sponsors enabled, Ko-fi link in README
Premium path:    Skill architecture supports free/premium split
License:         MIT (maximizes adoption)
Contributing:    CONTRIBUTING.md must be excellent (community = moat)
Telemetry:       None. Privacy is a feature.
```

**Output saved to `~/.bizstack/pricing/pricing-001.md`**

### Step 3: `/gtm`

```
> /gtm
```

> **CMO:** OSS GTM is different. You're not selling a product — you're building a movement. Your "conversion" is: discover → star → install → use regularly → contribute/sponsor.
>
> **Positioning:**
> For **developers who live in the terminal** and want to be **intentional about personal growth**, **lifestack** is a **Claude Code skill pack** that brings **identity-based self-reflection into your daily workflow**. Unlike **journaling apps**, it **lives where you already work**. Unlike **productivity tools**, it asks **"who are you becoming?" not "what did you do?"**
>
> **Channel strategy:**

```
1. GitHub + Show HN — PRIMARY
   First impression matters. README is your landing page.
   Launch: Show HN post with compelling personal story.
   Ongoing: Keep README sharp, respond to issues within 24h.

2. r/ClaudeAI + r/productivity — SECONDARY
   Taro is here. Share genuine experiences, not pitches.
   "How I use Claude Code for personal development" = authentic content.

3. X/Twitter (dev community) — TERTIARY
   Build-in-public thread. Share the philosophy, not just the tool.
   "Terminal as a tool for self-reflection" is a provocative, shareable idea.
```

> **First 100 stars strategy (OSS equivalent of first 100 users):**

```
FIRST 20 STARS (Week 1):
1. Show HN post with personal story                     → 10-15 stars
2. Post in r/ClaudeAI with demo                          → 5-10 stars
3. Tweet thread: "I built a self-reflection tool in CLI"  → 3-5 stars

STARS 21-100 (Week 2-6):
4. Cross-post to r/productivity, r/selfimprovement       → 10-15 stars
5. Dev.to article: "Identity-based development"           → 5-10 stars
6. Engage with Claude Code community, mention naturally   → 10-20 stars
7. Ask early users to star if they find it useful         → 5-10 stars
```

> **OSS-specific advice:**
> - **CONTRIBUTING.md is your most important marketing document.** It determines whether one-time users become long-term community members.
> - Stars ≠ users. Track actual installs (GitHub clone stats) and recurring usage.
> - **"User" and "Contributor" are different personas.** Taro uses it; someone else contributes to it. You may need a separate persona for contributors later.

**Output saved to `~/.bizstack/gtm/gtm-001.md`**

### Next Steps

1. Polish the README (it's your landing page)
2. Run `Show HN` when ready
3. After 100 stars: revisit `/pricing` path 2 (premium skills)

### OSS-Specific Takeaways

| Software product assumption | OSS reality |
|---|---|
| Revenue is the goal | Adoption is the goal (revenue comes from adjacent offerings) |
| Price drives architecture | License + contribution model drives architecture |
| CAC matters | Star-to-install conversion matters |
| Churn is the enemy | Contributor drop-off is the enemy |
| Support is a cost center | Issues/PRs are community health signals |

---

## Scenario 4: Physical Product (Cyrus Coffee Lab)

### Context

Sho runs Cyrus Coffee Lab — hand-roasted specialty coffee sold on BASE (Japanese e-commerce platform) and Mercari. His Instagram has been dormant for months. Online discoverability is near zero. Monthly revenue is minimal.

### Prerequisites

- bizstack installed
- Existing BASE shop and Mercari listings
- Dormant Instagram account

### Step 1: `/persona`

```
> /persona
```

> **Researcher:** Let's find who's buying your coffee. One person.
>
> **Question 1: Who needs your coffee most? What does their day look like?**

**Sho:** Coffee lovers who appreciate specialty coffee. People who care about where their beans come from and how they're roasted.

> **Researcher:** That's still a category. Let me split this into two possible personas:
>
> A) **The daily drinker:** Home-brews every morning, owns a hand grinder and a V60, reads about coffee origins for fun
> B) **The gift buyer:** Doesn't know much about coffee but wants an impressive, unique gift for someone who does
>
> These are completely different people with different buying triggers. Which one is your primary customer right now?

**Sho:** Mostly A — people who already know and love specialty coffee. They brew at home and care about roast profiles.

> **Researcher:** Let me build them. I'll call her Rina.
>
> Rina, 34, works in marketing at a mid-size company in Fukuoka. Every morning before work, she grinds beans with her Timemore C2 and brews a V60. It's her ritual — 4 minutes of calm before the chaos. She buys beans from local roasters but has started ordering online because her local options feel repetitive. She follows coffee accounts on Instagram and occasionally splurges on rare single-origins.
>
> **Question 2: How does Rina get coffee today?**

**Sho:** She buys from local roasters, Kaldi sometimes, and has tried ordering from online roasters she found on Instagram. She's tried subscription boxes but didn't like that she couldn't choose.

> **Researcher:** Rina's current coffee sourcing:
> 1. **Local roasters** — her default, but selection is getting stale
> 2. **Kaldi** — convenient but not exciting enough for her palate
> 3. **Instagram-discovered online roasters** — hit-or-miss, hard to judge quality before buying
> 4. **Subscription boxes** — tried, quit. She wants to choose, not be surprised.
>
> Your opportunity: a roaster she discovers on Instagram with a story she connects with, and specific beans she can choose.
>
> **Question 3: Willingness to pay?**

**Sho:** She's used to paying ¥1,500-2,500 for 200g from local roasters. Online she might pay a bit more because of shipping, but she's price-aware.

> **Researcher:** Rina's coffee budget:
> - **200g bag:** ¥1,500-2,500 (local), ¥1,800-3,000 (online, shipping included)
> - **Monthly spend:** 2-3 bags/month = ¥4,000-7,500/mo
> - **Splurge tolerance:** up to ¥4,000 for a rare micro-lot
> - **Shipping sensitivity:** FREE shipping is expected over ¥3,000. Under that, ¥500 shipping is OK but creates friction
>
> Key insight: **your price must include or absorb shipping to feel competitive.** ¥2,200 + ¥500 shipping feels worse than ¥2,500 free shipping, even though it's cheaper.
>
> **Question 4: Where does Rina hang out online?**

**Sho:** Instagram definitely — she follows coffee roasters and latte art accounts. Maybe Twitter a bit. She probably reads coffee blogs. She might be on specialty coffee forums but I'm not sure.

> **Researcher:** Rina's online world:
> - **Instagram:** PRIMARY discovery channel. Follows roasters, checks stories for new bean drops. Hashtags: #スペシャルティコーヒー #ハンドドリップ #自家焙煎
> - **X/Twitter:** Secondary. Japanese coffee community is smaller but engaged
> - **Google Search:** "スペシャルティコーヒー 通販" "手網焙煎 豆" — SEO matters
> - **BASE search:** Browses BASE for unique food items
> - **Discovery path:** Instagram reel → profile → BASE shop link → purchase
>
> **Question 5: Why wouldn't Rina buy your coffee?**

**Sho:** She can't taste it online. She doesn't know if she'll like the roast profile. And there's no brand recognition — she's never heard of Cyrus Coffee Lab. Plus, she already has trusted roasters.

> **Researcher:** Four barriers:
> 1. **Taste uncertainty** (Primary): Can't sample online. Needs detailed roast descriptions and trust signals
> 2. **Brand unknown**: Zero recognition. Needs social proof (reviews, follower count, story)
> 3. **Switching cost**: She has roasters she likes. Your first sale must be "try alongside," not "replace"
> 4. **Convenience**: Reordering must be frictionless
>
> Product implications:
> - Detailed tasting notes and roast profiles on every listing (not just "Ethiopia Yirgacheffe")
> - Customer reviews/photos prominently displayed
> - Sampler set (3× 50g bags) as entry product — low commitment, high discovery
> - LINE or email for reorder reminders

**Output saved to `~/.bizstack/personas/persona-001.md`**

### Step 2: `/pricing`

```
> /pricing
```

> **CFO:** Physical product. Different economics. Your margin is eaten by COGS, not server costs. Let me map it:

```
UNIT ECONOMICS (per 200g bag):
  Green beans:              ¥400-600
  Roasting (time + gas):    ¥200
  Packaging:                ¥150
  Label/sticker:            ¥50
  COGS total:               ¥800-1,000

  Selling price:            ¥2,200
  BASE fee (6.6% + 40):     ¥185
  Shipping (you pay):       ¥500-700 (letter pack/nekopos)
  ──────────────────────
  Net margin:               ¥315-715 per bag (14-32%)

  If customer pays shipping separately:
  Net margin:               ¥1,015-1,215 per bag (46-55%)
```

> **CFO:** Your margins are tight with free shipping. Two strategies:

```
STRATEGY A: Free shipping over ¥3,000
├── Encourages 2-bag orders (¥2,200 × 2 = ¥4,400)
├── Average margin improves because shipping is amortized
└── Rina's expectation: free shipping over ¥3,000 is standard

STRATEGY B: Entry product (sampler set)
├── 3 × 50g sampler set: ¥1,500 (shipping included)
├── COGS: ~¥600, shipping: ¥400, BASE fee: ¥139
├── Net margin: ¥361 (24%) — break even is fine
├── Goal: not profit, but first-time trial → repeat full-size purchase
└── Repeat rate target: 30%+ of sampler buyers order full bags
```

> **Recommended product lineup:**

```
ENTRY:    Sampler Set (3 × 50g)          ¥1,500   shipping included
CORE:     Single Origin 200g             ¥2,200   shipping ¥500 or free over ¥3,000
PREMIUM:  Rare Micro-lot 150g            ¥3,500   free shipping
GIFT:     Gift Box (2 × 200g + card)     ¥5,500   free shipping, gift wrapping
```

> **Monthly revenue targets:**

```
Current:        ~¥10,000/mo (estimate)
Target (3mo):   ¥50,000/mo  → ~25 bags/mo
Target (6mo):   ¥150,000/mo → ~70 bags/mo
Target (12mo):  ¥300,000/mo → ~140 bags/mo

At 140 bags/mo with average margin ¥500/bag = ¥70,000 net profit
(Physical product margins are slim — volume is everything)
```

**Output saved to `~/.bizstack/pricing/pricing-001.md`**

### Step 3: `/gtm`

```
> /gtm
```

> **CMO:** Physical product GTM is visual-first. Rina discovers coffee with her eyes before her taste buds. Here's your channel strategy:

```
1. Instagram (Reels + Stories) — PRIMARY
   Why: Rina's #1 discovery channel for food/coffee.
   Content: Roasting process videos, bean close-ups, brewing tutorials.
   Frequency: 3 Reels/week, daily Stories when roasting.
   First action: Post a 15-second Reel of hand-roasting with the sound
   of crackling beans. Caption: "今日の焙煎。エチオピア イルガチェフェ、
   シティロースト。" Use hashtags: #自家焙煎 #スペシャルティコーヒー
   #ハンドドリップ #コーヒーのある暮らし

2. BASE Shop SEO — SECONDARY
   Why: People search BASE for specialty food.
   Content: Optimized product titles and descriptions.
   "【自家焙煎】エチオピア イルガチェフェ ナチュラル 200g｜フルーティーで
   華やかな浅煎り" > "エチオピア 200g"
   First action: Rewrite all product titles with keywords + tasting notes.

3. Google (SEO via BASE blog or note.com) — TERTIARY
   Why: "スペシャルティコーヒー 通販" has search volume.
   Content: note.com articles about hand-roasting, origin stories, brewing guides.
   Frequency: 1 article/2 weeks.
   First action: Write "手網焙煎の魅力 — 自宅で焙煎を始めて変わったこと"
```

> **First 100 customers:**

```
FIRST 10 CUSTOMERS (Week 1-3):
1. Instagram Reel: roasting process video                → 2-3 orders
2. Offer sampler sets to 5 friends/family at cost        → 5 orders (+ reviews)
3. Post sampler set on Mercari with attractive photos    → 2-3 orders

CUSTOMERS 11-30 (Week 4-8):
4. Daily Instagram Stories: "今日の焙煎" ritual content  → 5-10 orders
5. Reply to #ハンドドリップ posts, build genuine connections → 3-5 orders
6. Ask first 10 customers for reviews + repost their photos → 5-8 orders

CUSTOMERS 31-100 (Month 3-6):
7. note.com article about your roasting journey           → 10-15 orders
8. Collaborate with local café: wholesale 1kg bags        → 20-30 recurring
9. Instagram giveaway: "フォロー&リポストでサンプラーセット" → 10-20 orders
10. Seasonal limited edition (桜ブレンド etc.)             → 10-15 orders
```

> **Physical product–specific advice:**
> - **Photos are everything.** Invest 1 hour in good lighting for product shots. Natural light, clean background, steam rising from a cup.
> - **Unboxing experience = free marketing.** A handwritten thank-you note gets photographed and shared. Include a small card with brewing instructions and your Instagram handle.
> - **Repeat customers are your lifeblood.** After first purchase, send a LINE message or email: "How did you like the beans? I'm roasting [next origin] this weekend." Personal touch at this scale.

**Output saved to `~/.bizstack/gtm/gtm-001.md`**

### Physical Product Takeaways

| Software assumption | Physical product reality |
|---|---|
| Marginal cost ≈ ¥0 | COGS + shipping eat 50-70% of revenue |
| Scale by adding servers | Scale by roasting more (capacity limit: ~200 bags/mo solo) |
| Free tier costs nothing | Free samples cost real money |
| Churn = cancel subscription | Churn = stop reordering (harder to detect) |
| Demo = free trial | Demo = sampler set (you eat the cost) |
| SEO drives traffic | Instagram drives discovery |

---

## Scenario 5: 3-Stack Integrated Flow

### Context

Sho has all three stacks installed: lifestack (personal growth), gstack (software development), and bizstack (business). He's starting a new project — **an AI-powered photo portfolio optimization service** — and wants to run the full pipeline from vision to launch.

### Prerequisites

- lifestack, gstack, and bizstack all installed
- Fresh project with no prior data

### The Full Pipeline

```
PHASE 1: IDENTITY (lifestack)
lifestack /vision

PHASE 2: BUSINESS DESIGN (bizstack)
bizstack /persona → /pricing → /gtm

PHASE 3: BUILD (gstack)
gstack /office-hours → /plan-ceo-review → /plan-eng-review → Build → /ship

PHASE 4: GO-TO-MARKET (bizstack)
bizstack /launch → /outreach → /measure

PHASE 5: RETRO (all three)
bizstack /biz-retro + gstack /retro + lifestack /retro
```

### Connection Point 1: lifestack `/vision` → bizstack `/persona`

```
> /vision
```

**lifestack output:**

```markdown
# Vision Statement
I am a developer who creates at the intersection of AI and photography,
building tools that help artists see their work through new eyes.

Target Date: 2027-03-31
```

**How this connects to bizstack:**

When `/persona` runs, it can reference the vision:

> **Researcher:** I see your lifestack vision: "AI and photography intersection, tools for artists." This anchors who you're building for — you're not building generic AI tools, you're building for people who make visual art. Let's find the specific artist who needs you most.

The vision acts as a **constraint**: /persona won't let you target "anyone who has photos" — it steers toward artists, photographers, and visual creators who align with your identity.

### Connection Point 2: bizstack `/pricing` → gstack `/plan-eng-review`

**bizstack /pricing output (key section):**

```markdown
## Tier Structure

### Free Tier
- 10 photos/month optimization
- Basic quality score (1-10)
- Watermark on exported optimizations

### Pro Tier — $9.99/mo
- Unlimited photos
- Detailed scoring with per-dimension breakdown
- AI-generated improvement suggestions
- No watermark
- Priority processing

## Engineering Requirements
- **Auth:** Required (email + password, or OAuth with Google)
- **Billing:** Stripe Checkout (supports JPY and USD)
- **Usage tracking:** Photo count per user per month (reset on billing date)
- **Feature flags:** quality_score_detail (pro), suggestions (pro), watermark (free)
- **Storage:** User uploads processed and discarded. No persistent storage of user photos.
- **Rate limiting:** Free tier: 10 photos/calendar month. Hard limit with upgrade prompt.
```

**How gstack reads this:**

```
> /plan-eng-review
```

> **Eng Manager:** I've found a bizstack pricing document at `~/.bizstack/pricing/pricing-001.md`. It specifies engineering requirements. Let me incorporate these into the technical design:
>
> **Auth system:** Required. Email/password + Google OAuth. Recommendation: use Supabase Auth (free tier covers initial users, handles both auth methods).
>
> **Billing:** Stripe Checkout. Need: webhook handler for subscription events, customer portal for plan management. Estimated: 2 days integration.
>
> **Usage tracking:** Monthly photo counter per user. Schema:
> ```sql
> usage_tracking (user_id, month, photo_count, limit)
> ```
> Check before processing. Increment after successful processing. Reset handled by cron or billing cycle.
>
> **Feature flags:** 3 flags tied to subscription tier. Store in user record, check at API layer.
>
> Without the bizstack pricing output, I would have asked you "do we need auth?" and "what are the limits?" Now I already know.

### Connection Point 3: gstack `/ship` → bizstack `/launch`

**gstack /ship output:**

```
v0.1.0 released. Deployed to production.
GitHub release created. Changelog updated.
```

**How bizstack picks up:**

```
> /launch
```

> **Launch Manager:** Your code is shipped (v0.1.0 — I can see the gstack release). Now let's get it in front of people. I'm reading your GTM strategy from `~/.bizstack/gtm/gtm-001.md`.
>
> Your GTM says the top channels are: 1x.com community, Reddit r/photography, and X photo community. Let me build the launch playbook:
>
> **T-14 (today):** Start posting your photo optimization results on X. "Built an AI that scores photos like a contest judge. Here's what it thinks of my portfolio." Show the before/after scores.
>
> **T-7:** Post to r/photography: "I've been building an AI tool that analyzes what makes photos score well in contests — here's what I've learned." Share insights, not a pitch.
>
> **T-0 (Launch Day):**
> - Submit to Product Hunt (Tuesday 12:01am PT)
> - Post Show HN with technical deep-dive on the AI model
> - Launch tweet thread with 5 before/after examples

The launch plan builds directly on the GTM channel strategy — no duplication, no contradiction.

### Connection Point 4: Unified 3-Stack Retro

At the end of each week, the three retros combine:

```
> /biz-retro
```

```
+====================================================================+
|              3-STACK WEEKLY RETRO — Week 13                         |
+====================================================================+
| Product: Photo Portfolio Optimizer                                  |
+====================================================================+
| IDENTITY (lifestack)                                                |
| Vision: "AI × Photography tools for artists"                       |
| Alignment Score: 72% (+8pt) | Streak: 12 days                     |
| Note: Shipped the product I said I would. Living the vision.       |
+--------------------------------------------------------------------+
| ENGINEERING (gstack)                                                |
| Commits: 47 | LOC: 3.2k | Test: 38% | PRs: 12                    |
| Ship: v0.1.0 released on schedule                                  |
| Risk: Test coverage below 50% threshold                            |
+--------------------------------------------------------------------+
| BUSINESS (bizstack)                                                 |
| Users: 0 → 12 (+12) | Revenue: ¥0 (free tier only so far)         |
| Waitlist: 45 (+18) | Page views: 340 | Signups: 12 (3.5% CVR)    |
| Top Channel: X/Twitter (8 signups) | DMs sent: 15 | Replies: 4    |
+--------------------------------------------------------------------+
| MARKETING                                                           |
| Posts: 5 | Impressions: 2,340 | Engagement: 4.2%                   |
| Blog: 1 article (872 views) | YouTube: 0 (behind schedule)        |
+--------------------------------------------------------------------+
| INSIGHTS                                                            |
|                                                                     |
| [IDENTITY] Alignment trending up. This project fits who I'm        |
|            becoming. Protect this momentum.                         |
|                                                                     |
| [ENG] Test coverage at 38% is a liability. Before adding features, |
|       write tests for the scoring engine.                           |
|                                                                     |
| [BIZ] X/Twitter → signup CVR is 3.4%, highest of all channels.     |
|       Double down next week. Reddit is underperforming — investigate|
|       whether r/photography was the right subreddit.                |
|                                                                     |
| [BIZ] Zero revenue yet. First paid conversion is the next          |
|       milestone. Consider reaching out to the 12 free users        |
|       personally to understand upgrade triggers.                    |
|                                                                     |
| [LIFE] Missed the YouTube video — energy dipped mid-week.          |
|        Schedule recording for Monday when energy is highest.        |
|                                                                     |
+--------------------------------------------------------------------+
| VERDICT                                                             |
| Engineering momentum is strong. Business needs attention — 12      |
| users is a start but zero revenue means the pricing hypothesis     |
| is untested. Identity alignment trending up — this project fits.   |
| Maintain current actions, shift marketing time toward X/Twitter.   |
+--------------------------------------------------------------------+
| NEXT WEEK PRIORITIES                                                |
|                                                                     |
| 1. [BIZ]  DM all 12 free users — learn what they think             |
| 2. [BIZ]  Double X/Twitter posting cadence (3→5 posts/week)        |
| 3. [ENG]  Increase test coverage to 50%                            |
| 4. [ENG]  Fix scoring edge case reported by user #3                |
| 5. [LIFE] Record YouTube tutorial (Monday morning, fresh energy)   |
|                                                                     |
+====================================================================+
```

### Why the Integrated Flow Matters

Without integration:
- You build features nobody wants (no /persona)
- You design auth wrong (no /pricing before /plan-eng-review)
- You ship to silence (no /launch after /ship)
- You don't know if you're winning (no /biz-retro)

With integration:
- **Identity** anchors what you build (lifestack → bizstack)
- **Business design** shapes engineering decisions (bizstack → gstack)
- **Shipping** triggers go-to-market (gstack → bizstack)
- **Retro** connects all three dimensions (all stacks → unified view)

The three stacks answer three questions every week:
- **lifestack:** "Am I becoming who I want to be?"
- **gstack:** "Am I building well?"
- **bizstack:** "Am I reaching the people who need this?"

When all three are aligned, you're not just writing code — you're building a life.
