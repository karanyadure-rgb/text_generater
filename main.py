from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import re
import os

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPEN_API_KEY")

)

topic = input("Topic:")
content_type =input("Type(artical,summary,post,etc..):")
audience = input("Audience(expert,begineer,etc):")
tone = input("Tone(casual,formal,simple):")
system_prompt=f"""you are expert{content_type} writer to indian audience write a structured{topic}
Audience ={audience}
Tone={tone}
keep it under 300"""
response=client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role":"system",
         "content":system_prompt
        },
        {"role":"user",
         "content":f"write {content_type} about {topic}"
        },
    ],
    max_tokens =400,
    temperature=0.7

)
result = response.choices[0].message.content

print(result)
filename=topic.lower()+".txt"
with open(filename,"w")as f:
    f.write(result)

print("response saved in file"+filename)