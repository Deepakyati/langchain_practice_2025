import os
from google.colab import userdata

# 1. Retrieve the secret value using the name you set in the Secrets manager.
try:
    API_KEY = userdata.get('GOOGLE_API_KEY')
    
    # 2. Set the environment variable so LangChain can automatically find it.
    os.environ['GOOGLE_API_KEY'] = API_KEY
    
    print("✅ GOOGLE_API_KEY loaded successfully from Colab Secrets.")
except Exception as e:
    print("❌ ERROR: Could not load API key from Secrets.")
    print("Please check the secret name and access toggle on the sidebar.")

# Optional: Install LangChain dependency
!pip install -q langchain-google-genai langchain-core

#Integrating Gemini with LangChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

#Create a Prompt Template: Define a prompt template for your interactions. 

prompt = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful AI Assistant"),
    ("user" ,"{input}")                                       
])

#Chain Components: Combine the prompt, LLM, and an output parser using LangChain Expression Language (LCEL) to create a chain.

output_parser=StrOutputParser()
chain = prompt | llm | output_parser

#Invoke the Chain: Pass your input to the chain to get a response from Gemini.

response = chain.invoke({"input": "What is the capital of France?"})
print(response)
