from google import genai
from getpass import getpass

api_key = getpass("Enter Gemini API Key: ")
client = genai.Client(api_key=api_key)

print("SMART STUDY NOTES GENERATOR")
print("-"*40)

subject = input("Enter subject: ")
topic = input("Enter topic: ")
level = input("Enter level (Basic / Detailed): ")
style = input("Enter style (Bullet points / Paragraph): ")

prompt = f"""
Generate study notes.

Subject: {subject}
Topic: {topic}
Level: {level}
Style: {style}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)
