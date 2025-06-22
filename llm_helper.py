
from dotenv import load_dotenv
load_dotenv()
import os

from langchain_groq import ChatGroq

llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model="llama-3.3-70b-versatile")

if __name__=="__main__":
    response=llm.invoke("What are the two main ingredient in samosa")
    print(response)

