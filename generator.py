from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def generate_report(raw_notes: str):
    prompt = f"""
You are an operations analyst. Take the raw notes below and turn them into a 
clean weekly status report in markdown format.

Use these four sections:
1. Summary — 2 to 3 sentences covering the week overall
2. Accomplishments — bullet points of what got done
3. Blockers — anything that is stuck or waiting on someone else
4. Next Week — priorities and planned work for the coming week

Rules:
- Write in third person professional tone
- Be specific, not vague
- If something is not mentioned, do not make it up
- Keep it concise — this is a status update, not an essay

--- RAW NOTES ---
{raw_notes}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)
