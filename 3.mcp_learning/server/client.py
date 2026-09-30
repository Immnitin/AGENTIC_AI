import os
from langchain_groq import ChatGroq
from mcp_use import MCPAgent,MCPClient
from dotenv import load_dotenv
import asyncio

async def memory_chat():
    '''Run a chat using MCP built in conversation memory'''
    load_dotenv()
    os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY') 

    config_file='../server/mcp_config.json'

    print('Initializing Chat')

    client=MCPClient.from_config_file(config_file)
    llm=ChatGroq(model='qwen/qwen3-32b')

    agent=MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True 
    )

    print('Interactive Chatbot')

    try:
        while True:
            user_input=input('\n You')

            print('Assistant',end="",flush=True)

            try:
                response=await agent.run(user_input)
                print(response)
            except Exception:None
    finally:
        if client and client.sessions:
            client.close_all_sessions()

if __name__=='__main__':
    asyncio.run(memory_chat())