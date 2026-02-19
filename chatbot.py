import json
import os
from groq import Groq

# Load university data
with open("data/university_data.json", encoding="utf-8") as f:
    DATA = json.load(f)


def _format_data_for_prompt():
    """Convert the JSON data into a readable text block for the system prompt."""
    lines = []
    for school, school_data in DATA.items():
        lines.append(f"\n## Department of {school.title()}")
        for prog_key, prog in school_data["programs"].items():
            lines.append(f"\n### {prog.get('name', prog_key.upper())}")
            for field, value in prog.items():
                if field == "name":
                    continue
                label = field.replace("_", " ").title()
                if isinstance(value, list):
                    lines.append(f"- {label}: {', '.join(value)}")
                else:
                    lines.append(f"- {label}: {value}")
    return "\n".join(lines)


# System prompt that grounds the AI in the university data
SYSTEM_PROMPT = f"""You are a friendly and helpful admissions assistant chatbot for Scaledown University.

Your role is to help students explore academic programs, eligibility criteria, fees, entrance exams, specializations, duration, and career scope across various departments at Scaledown University.

**RULES:**
1. ONLY answer questions using the university data provided below. Do NOT make up or guess any information.
2. If a student asks something not covered in the data, OR if you cannot understand their message, respond with a friendly reminder of your purpose. For example:
   "I'm the Scaledown University Admissions Assistant! I can help you with:
   • Academic programs and specializations
   • Eligibility criteria
   • Fee structures
   • Entrance exams
   • Career scope and opportunities
   • Duration of programs
   Try asking something like 'Tell me about B.Tech' or 'What are the MBA fees?'"
3. Keep responses concise, clear, and well-formatted.
4. Use bullet points for lists.
5. Be warm and encouraging — like a real university admissions counselor.
6. If the student greets you, introduce yourself as Scaledown University's admissions assistant and suggest what they can ask about.
7. Always frame your responses in the context of Scaledown University.

**UNIVERSITY DATA:**
{_format_data_for_prompt()}
"""


def init_client():
    """Initialize and return the Groq client."""
    api_key = os.environ.get("GROQ_API_KEY", "")
    if not api_key or api_key == "YOUR_GROQ_API_KEY_HERE":
        raise ValueError(
            "GROQ_API_KEY is not set. "
            "Get a free key at https://console.groq.com "
            "and add it to your .env file."
        )
    client = Groq(api_key=api_key)
    return client


# Initialize client at module load
try:
    CLIENT = init_client()
except ValueError as e:
    CLIENT = None
    print(f"⚠️  {e}")


def get_response(user_input, history=None):
    """
    Generate an AI response using Groq (Llama 3), grounded in university data.

    Args:
        user_input: The student's message.
        history: List of {"role": ..., "content": ...} dicts for conversation context.

    Returns:
        The AI-generated response string.
    """
    if CLIENT is None:
        return (
            "⚠️ The AI service is not configured yet. "
            "Please add your Groq API key to the .env file.\n"
            "Get a free key at: https://console.groq.com"
        )

    try:
        # Build messages list
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        if history:
            messages.extend(history)

        messages.append({"role": "user", "content": user_input})

        response = CLIENT.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Groq API error: {e}")
        return (
            "Sorry, I'm having trouble connecting right now. "
            "Please try again in a moment."
        )
