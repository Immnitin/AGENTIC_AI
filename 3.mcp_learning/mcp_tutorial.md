## MCP Server
Model Context Protocol:- Model context Protocol is a protocol where we expose the external sources to the llm, which will act on that data and  interact with the external tools, services through a common interface.

## Architecture
- MCP Host
    - this is the application that the user interacts with eg- claude Desktop
- MCP Client 
    - this is the client that speaks the MCP protocol, 
        - it connects to MCP servers
        - Sends requests
        - Checks available tools
        - receives response
- MCP Server
    - this is a program that exposes tools,resources,prompts and capabilities to AI Models using MCP(Acts as a brigde between AI agent and external sources)

## Transport Protocols
communication done using Json messages
it is a communication mechanism that is used by MCP client and MCP server
there are 3 types
- STDIO: This is just a standard input and output, just like how we give inputs and take outputs from the mcp servers. 
    - mostly used in local development.
- HTTP: Communication happens over HTTP requests 
    - used in Cloud-hosted services
- SSE: Allows server to push updates to client
    - used in Real-time updates, streaming responses
- Streamable HTTP: Combines HTTP+Streaming

## Primitives

- Resources: Passive data sources that provide read-only access to information for context, such as file contents, database schemas, or API documentation.
- Prompt: Pre-built instruction templates that tell the model to work with specific tools and resources
- Tools: Functions that your LLM can actively call, and decides when to use them based on user requests. Tools can write to databases, call external APIs, modify files, or trigger other logic.

## Building own MCP server
we will use fastMCP library to build our own mcp servers
- import fastMCP library -> name the mcp -> then build tools for that mcp agent 
    - -> run this file using command uv run mcp dev filename -> this is will open the mcp inspector and from there we can test our mcp tools and performance
    - run this file with command uv run mcp install filename -> this will add this mcp to the claude, you can check this in the claude settings-> developers->edit config

## Building MCP client
we will use mcp-use library to develop mcp-client.

-   from mcp-use we will import MCPAgent,MCPClient

we will create a config file which will consist the details and paths of all the services we provide, this file will give the client, details of all the services and tools present

- client=MCPClient.from_config_file(filename)
- create an llm
-create an MCPAgent(
    client=""
    llm=""
)

this creates an mcpclient and we can this file using while and access the mcp server

