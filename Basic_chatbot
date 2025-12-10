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

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# The model initialization reads the environment variable set in Step 2.
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Example usage
response = llm.invoke([
    HumanMessage(content="Explain the concept of Retrieval-Augmented Generation (RAG) in one sentence.")
])

print("\n--- LLM Response ---")
print(response.content)
