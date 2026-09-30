# Example: LangGraph Tool Agent

## User Query
Create a LangGraph agent that can call a search tool and then summarize the result.

## How The Skill Should Help
- Separate reasoning, tool execution, and summarization.
- Track tool outputs in state.
- Add a validation step before final response.
- Keep the workflow easy to inspect.

## Response Pattern
1. Describe the graph stages.
2. Provide the implementation.
3. Explain how tool results move through state.
