from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")  # replace this

def get_llm_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
