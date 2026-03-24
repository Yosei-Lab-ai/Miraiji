# Contributing to bizstack

## Adding a New Skill

1. Create a directory: `mkdir skill-name/`
2. Create `skill-name/skill.md` following the existing skill format
3. If the skill produces output, create a template in `templates/`
4. Add an entry to `docs/skills.md`
5. Update `CLAUDE.md` with the new skill
6. Update `README.md` skill table

## Skill Format

Every `skill.md` must include:

- **Frontmatter**: `name`, `description`, `persona`
- **System prompt**: The expert persona and behavior instructions
- **Forcing questions**: Numbered questions asked one at a time
- **Output format**: What gets saved and where
- **Constraints**: What the skill must NOT do

## Design Principles

- Each skill has one clear expert persona
- Skills ask questions one at a time, never all at once
- Skills read prior skill outputs when available
- All outputs save to `~/.bizstack/`
- Strategies must be solo-developer executable
- No cloud dependencies

## Naming

- Skill directories use kebab-case: `market-scan/`, `biz-retro/`
- Output files use the pattern: `type-NNN.md` (e.g., `persona-001.md`)
- Templates match skill names: `templates/persona.md`

## Testing

Run a skill manually in Claude Code and verify:
1. The persona is adopted correctly
2. Questions are asked one at a time
3. Prior skill outputs are read when available
4. Output is saved to the correct `~/.bizstack/` path
5. Output follows the template format
