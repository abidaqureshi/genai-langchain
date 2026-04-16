from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_obj = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)
result = embedding_obj.embed_query("Islamabad is the capital of Pakistan")
print(str(result))