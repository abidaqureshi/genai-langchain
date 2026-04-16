from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system',"You are {domain} expert"),
    ('human',"Explain in simple terms what is, {topic}")
])

prompt = chat_template.invoke({'domain':'cricketer','topic':'Swing'})

print(prompt)
