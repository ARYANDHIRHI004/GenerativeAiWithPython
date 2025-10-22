# read pdf 
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os

load_dotenv()


pdf_path = Path(__file__).parent/"nodejs.pdf"
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# split the docs
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=300
)
chunks = text_splitter.split_documents(documents=docs)

# Vector Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
  google_api_key=os.getenv("GEMINI_API_KEY"),
  model="models/gemini-embedding-001"
)

# vactor db connection
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url="http://localhost:6333",
    collection_name="learning_rag",
)

