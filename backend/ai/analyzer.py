from ai.openrouter import ask_ai
import json

def analyze_company(company_data):

    prompt = f"""

Analyze this company information:


{company_data}


You are an expert company research analyst.

Using the provided company information, return ONLY valid JSON.

Extract or infer:

- company_name
- website
- phone
- address
- products_services (array)
- pain_points (array of 3–6 items)
- competitors (array)

For each competitor return:
- name
- website

Rules:
- Return ONLY JSON.
- Do not include Markdown.
- If information is unavailable, use an empty string or empty array.
- Do not invent phone numbers or addresses. Only use publicly available information or leave them blank.

"""


    result = ask_ai(prompt)

    try:
       return json.loads(result)
    except json.JSONDecodeError:
        return {
        "error": "AI returned invalid JSON",
        "raw_response": result
        }