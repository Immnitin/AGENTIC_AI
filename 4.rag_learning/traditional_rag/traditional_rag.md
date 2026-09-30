# Traditional Rag

# RAG(Retrieval Augemented Generation):
This is a optimization technique, where we can make the llms give an authorized access to the data and, the llm will give the output with the context of that data, that will give authorized output.
The relevant information is retrieved from an external datasource like Vector Database, documents.
This allows model to answer upto date and domain specific information without retraining.

Generally, without rag when we ask llms upto date information or any other domain specific answers, the llms tend to hallucinate(Hallucinate means, llm doesnt have an answer, but it tries to giev and answer and make us believe in it).

we could solve this problem using fine tuning. (Fine tuning is the process of retraining already trained model with our own data so that it becomes better at specific task,domain,behaviour).
But this takes a lot of time and, it is expensive.

To tackle this we use Rag

RAG Pipelines:
- Data Ingestion pipeline:
    - this pipeline mostly foucses on the data,
        - data ingestion -> data parsing -> dividing into chunks -> apply embedding models -> store those embeddings in Vector DataBase.
- Retrieval pipeline:
    - This pipeline focuses on tasks like retrieving data from Vector Database that is similar to the prompt given.
    - user prompts -> embedding is applied to it -> then the information similar to those embeddings is retrieved from database -> this information is sent to the llm as context -> this context and prompt is used by llm to respond. 

This will not totally remove hallucination, but reduces it.

 