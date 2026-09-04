from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=0.7, max_completion_tokens=100)  #temperature controls randomness in the output, how diverse or predictable the responses are. A higher temperature (e.g., 0.8) will result in more diverse and creative responses, while a lower temperature (e.g., 0.2) will produce more focused and deterministic outputs.

result = model.invoke("What is the capital of India?")

print("Response:")
print(result.content)