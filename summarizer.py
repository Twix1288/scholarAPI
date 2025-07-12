import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str, length: str = "short"):
    if not text or len(text.strip()) == 0:
        return "No input text provided."

    prompt = f"Please summarize the following text in a {length} format:\n\n{text}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error during summarization: {str(e)}"