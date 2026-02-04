import os
from openai import OpenAI

class LLMAgent:
    def __init__(self):
        self.enabled = os.getenv("ENABLE_LLM", "false").lower() == "true"
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) if self.enabled else None

    def respond(self, payload: dict, analysis: dict):
        if not self.enabled:
            return "LLM disabled"

        prompt = f"""
You are a defensive honeypot agent.
Incoming payload: {payload}
Detection result: {analysis}

Respond like a vulnerable system but never give real data.
"""

        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=80,
            )
            return resp.choices[0].message.content
        except Exception as e:
            return f"LLM_ERROR: {str(e)}"
