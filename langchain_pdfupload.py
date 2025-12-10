import os
from google.colab import userdata

os.environ["GOOGLE_API_KEY"]=userdata.get('GOOGLE_API_KEY')

import time
from google import genai
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


client = genai.Client()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

myfile = client.files.upload(file="attention.pdf")

while myfile.state.name == "PROCESSING":
    time.sleep(2)
    myfile = client.files.get(name=myfile.name)

# Reference by file_id in FileContentBlock
message = HumanMessage(
    content=[
        {"type": "text", "text": "What is in the document?"},
        {
            "type": "file",
            "file_id": myfile.uri,  # or myfile.name
            "mime_type": "application/pdf",
        },
    ]
)
response = model.invoke([message])
print(response)
