from langchain_openai import OpenAI
from dotenv import load_dotenv  #helps in loading environment variables from a .env file

load_dotenv()

llm = OpenAI(model_name="gpt-4")
result=llm.invoke("What is the capital of India?")

print(result)