import os
import json
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

api_str=None
                   
try:                   
    with open('apis.json', 'r') as file:
            api_str = json.load(file)
except:
      print("API failed to load!!")


if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = api_str["Google_api_key"]

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

def chat_with_gemini(input_):
    global model
    return model.invoke([HumanMessage(content=input_)])
    # return model.invoke()

if __name__=="__main__":
    print("Type any one ['Bye', 'Stop' or 'Quit'] to end the chat!!")
    count=1
    while True:
        print("###############Prompt {}!###############".format(count))
        user_input= input("Type your prompt: ")
        if user_input.lower() in ["bye","stop","quit"]:
            break
        result=chat_with_gemini(user_input)
        print(result.content)
        count+=1
    print("Thank you! Nice to chat with you.")    
    