# DeepAgent Skills

This folder stores reusable context packs for DeepAgent.

Each skill lives in its own folder and contains:
- `skill.md` for activation rules and intent matching
- `instruction.md` for detailed guidance and constraints
- one or more `example*.md` files for concrete patterns

Suggested runtime behavior:
1. Match user intent to one or more skills.
2. Load `skill.md` first.
3. Load `instruction.md` for the matched skill.
4. Load only the most relevant example file(s) to keep context compact.

Available skills:
- `python`
- `langgraph`
- `aws`
- `report_writer`
