# Python Skill Instructions

## Core Behavior
When this skill is active, the agent should:
- Prefer clear, maintainable, idiomatic Python.
- Use small functions and descriptive names.
- Add error handling for file, network, parsing, and runtime risks.
- Prefer standard library solutions unless a framework or package is explicitly requested.
- Include brief setup steps when external packages are required.

## Coding Guidance
- Target Python 3.11+ unless the project states otherwise.
- Use type hints for non-trivial functions.
- Prefer `pathlib` over raw path strings.
- Prefer `logging` over excessive print statements in production-style code.
- Keep notebook examples concise and cell-friendly.

## Problem-Solving Pattern
1. Restate the objective internally.
2. Identify inputs, outputs, and constraints.
3. Choose the simplest Python design that solves the task.
4. Implement the core logic.
5. Add validation or tests when useful.
6. Return code plus a short explanation.

## Output Preferences
- For scripts: provide runnable code.
- For APIs: show project structure, endpoint logic, and dependencies.
- For debugging: explain root cause, then show the fix.
- For data tasks: explain assumptions about schema and edge cases.

## Avoid
- Overengineering simple utilities.
- Using advanced metaprogramming unless necessary.
- Hiding assumptions about versions, packages, or file formats.
