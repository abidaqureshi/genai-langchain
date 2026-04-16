from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Islamabad is capital of Lahore",
    "Lisbon is capital of Portugal",
    "Tallinn is capital of Estonia"
]

result = embeddings.embed_documents(documents)
print(str(result))