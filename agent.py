import os, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("HF_API_KEY")

def hf_generate(model, prompt):
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, headers=headers, json={"inputs": prompt})

    print("\n🔍 RAW RESPONSE:", response.status_code)
    print(response.json())  # <-- Print full JSON for debugging

    result = response.json()
    if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
        return result[0]["generated_text"]
    elif isinstance(result, dict) and "error" in result:
        raise ValueError(f"Hugging Face API error: {result['error']}")
    else:
        raise ValueError("Unexpected API response format")


def plan_task(user_query):
    with open("prompts/planner.txt") as f:
        base = f.read()
    prompt = base.replace("{query}", user_query)
    return hf_generate("tiiuae/falcon-rw-1b", prompt)

def generate_final_answer(user_query, retrieved_docs, tool_results):
    with open("prompts/answer.txt") as f:
        base = f.read()
    prompt = base.format(
        retrieved_docs="\n".join(retrieved_docs),
        tool_results=str(tool_results),
        user_query=user_query
    )
    return hf_generate("mistralai/Mistral-7B-Instruct-v0.2", prompt)