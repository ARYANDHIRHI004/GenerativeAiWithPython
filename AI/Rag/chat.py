# read pdf 
from openai import OpenAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

# Vector Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
  google_api_key=os.getenv("GEMINI_API_KEY"),
  model="models/gemini-embedding-001"
)

# vactor db connection
vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

# take user quere
user_quere = input("ask something")

search_result = vector_store.similarity_search(query=user_quere)

context = "\n\n\n".join([f"Page Content: {result.page_content}\nPageNumber: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_result])

SYSTEM_PROMPT = f"""
    You are a helpfull AI Assistent who answers user query based on the available data
    context retreved from a PDF file along with page contents and page number.

    You should only answer the user based on the following content and navigate the user to open the right page number ot know more.
    
    Context: 
    {context}


"""

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},     
        {"role": "user", "content": user_quere},
    ]
)

print(response.choices[0].message.content)
