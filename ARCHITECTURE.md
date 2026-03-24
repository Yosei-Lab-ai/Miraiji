# Architecture

## Repository Structure

```
bizstack/
├── README.md              # Project overview and quick start
├── LICENSE                 # MIT License
├── VERSION                 # Semantic version
├── CLAUDE.md               # Claude Code configuration
├── ETHOS.md                # Design philosophy ("Seller Ethos")
├── ARCHITECTURE.md         # This file
├── CHANGELOG.md            # Release history
├── CONTRIBUTING.md         # Contribution guidelines
├── setup                   # Installation script
├── .gitignore
├── docs/
│   └── skills.md           # Detailed skill documentation
├── [skill-name]/
│   └── skill.md            # Skill definition (Claude Code format)
└── templates/
    ├── persona.md           # Persona output template
    ├── pricing.md           # Pricing output template
    └── gtm-strategy.md     # GTM output template
```

## Design Decisions

### 1. One directory per skill

Each skill lives in its own directory (`persona/`, `pricing/`, `gtm/`, etc.) with a single `skill.md` file. This matches the Claude Code skill convention and keeps skills isolated.

### 2. Templates separate from skills

Templates in `templates/` define the output format. Skills reference these templates but the templates can be updated independently.

### 3. Local data storage in ~/.bizstack/

All user data is stored in `~/.bizstack/`, not in the repository. This keeps business-sensitive data out of version control and allows multiple projects to share persona/pricing data.

### 4. Skill-to-skill communication via filesystem

Skills communicate by reading each other's output files from `~/.bizstack/`. There is no runtime dependency — each skill can run independently, but produces better results when prior skills have been run.

### 5. Persona-based switching

Following gstack's pattern, each skill adopts a specific expert persona. This constrains the AI's behavior to the relevant domain expertise and produces more focused, opinionated outputs.

## Data Flow

```
/persona ──→ ~/.bizstack/personas/persona-NNN.md
                │
                ├──→ /pricing (reads willingness-to-pay, current spending)
                │       │
                │       └──→ ~/.bizstack/pricing/pricing-NNN.md
                │               │
                │               └──→ /plan-eng-review (billing, auth, limits)
                │
                └──→ /gtm (reads user locations, communities)
                        │
                        └──→ ~/.bizstack/gtm/gtm-NNN.md
                                │
                                └──→ /launch (reads channel strategy)
```

## Installation

The `setup` script creates:
1. A symlink from `~/.claude/skills/bizstack/` to the repo's skill directories
2. The `~/.bizstack/` data directory with all subdirectories
