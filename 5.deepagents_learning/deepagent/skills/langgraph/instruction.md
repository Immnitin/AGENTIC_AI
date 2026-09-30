# LangGraph Skill Instructions

## Core Behavior
When this skill is active, the agent should:
- Think in terms of state, nodes, transitions, and termination.
- Make the graph design explicit before writing code.
- Keep state minimal but sufficient for routing and validation.
- Prefer understandable node responsibilities over overly clever graphs.

## Design Guidance
- Define the graph goal first.
- Identify what state must persist between nodes.
- Use conditional edges for routing decisions.
- Use dedicated nodes for planning, execution, tool use, validation, and response formatting when needed.
- Keep side effects isolated to specific nodes.

## Common LangGraph Patterns
- Router graph for branching by intent.
- Planner/executor graph for multistep tasks.
- Tool-calling graph for retrieval or API work.
- Supervisor graph for coordinating specialized subagents.

## Output Preferences
- Explain graph structure before code.
- Name nodes clearly.
- Show the state schema.
- Explain how execution starts and stops.
- Mention observability or debugging tips if the workflow is complex.

## Avoid
- Mixing unrelated responsibilities into one node.
- Storing unnecessary raw data in shared state.
- Creating loops without explicit exit conditions.
