# Example: LangGraph Router

## User Query
Build a LangGraph workflow that routes user requests to either a research node, coding node, or summary node.

## How The Skill Should Help
- Define a state object with user input, route, and result.
- Use a router node to classify intent.
- Add conditional edges to specialized nodes.
- End after the selected node returns an answer.

## Response Pattern
1. Describe the nodes and state.
2. Show the LangGraph code.
3. Explain the routing logic.
