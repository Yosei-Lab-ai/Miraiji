# miraiji — Claude Code Configuration

## Overview

miraiji is a Claude Code skill pack for business design and go-to-market execution.
It extends gstack's development pipeline with business strategy skills.

## Skills

### Phase 1 (Implemented)
- `/persona` — Target user definition (UX Researcher persona)
- `/pricing` — Price structure design (CFO persona)
- `/gtm` — Go-to-market strategy (CMO persona)
- `/copy` — Landing page & sales copy, Caples-school direct response (Direct Response Copywriter persona)

### Phase 2 (Stubs)
- `/market-scan` — Competitive analysis
- `/bizplan` — Business plan creation
- `/launch` — Launch execution planning
- `/content` — Content strategy & production
- `/outreach` — User acquisition
- `/measure` — KPI design & tracking
- `/grow` — Growth experiment design
- `/feedback` — User feedback loops
- `/biz-retro` — Business retrospective

## Common Patterns

### Persona-Based Switching
Each skill adopts a specific expert persona (UX Researcher, CFO, CMO, etc.).
The persona determines the questions asked, frameworks used, and output format.

### Skill-to-Skill Data Flow
Skills read each other's outputs automatically:
```
/persona → /pricing (reads willingness-to-pay from persona)
/persona → /gtm (reads user locations from persona)
/pricing → /plan-eng-review (passes billing & limit requirements)
/gtm → /launch (passes channel strategy)
/persona + /pricing + /gtm → /copy (reader, offer, positioning inputs)
/copy → /launch, /content, /outreach (headlines & messaging reuse)
```

### Data Storage
All outputs are saved to `~/.miraiji/`:
```
~/.miraiji/
├── personas/      # /persona outputs
├── pricing/       # /pricing outputs
├── gtm/           # /gtm outputs
├── copy/          # /copy outputs
├── market/        # /market-scan outputs
├── plans/         # /bizplan outputs
├── launch/        # /launch outputs
├── content/       # /content outputs
├── growth/        # /grow outputs
├── feedback/      # /feedback outputs
└── retros/        # /biz-retro outputs
```

### ID Convention
Files use incrementing IDs: `persona-001.md`, `pricing-001.md`, etc.
When creating a new file, check existing files and increment the ID.

## Integration with gstack

miraiji fills the gaps in gstack's pipeline:
- BEFORE BUILD: `/plan-ceo-review` → **miraiji** → `/plan-eng-review`
- AFTER SHIP: `/ship` → **miraiji** → `/retro`

## Language

- Public documentation: English
- Skill interactions: Support both English and Japanese
