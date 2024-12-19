from openai import OpenAI
import json
import re
from typing import Dict, Any

class BaseProcessor:
    def __init__(self, api_key: str, base_url: str, model: str, config: dict):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.config = config

    def _call_openai(self, prompt: str, temperature: float = 0.3) -> str:
        """Generic method to call OpenAI API"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
        )
        return response.choices[0].message.content

    def _extract_json(self, content: str) -> Dict[str, Any]:
        """Generic method to extract JSON content from response"""
        json_pattern = r'\{.*?\}'
        match = re.search(json_pattern, content, re.DOTALL)
        
        if match:
            try:
                return json.loads(match.group(0))
            except json.JSONDecodeError:
                print("Failed to parse JSON from the extracted content.")
        
        print("No valid JSON found in the response.")
        return {} 