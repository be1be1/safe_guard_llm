import requests
import json
from config import AI_MODEL_API_URL, AI_MODEL_API_KEY

class AIDecisionMaker:
    def __init__(self):
        self.api_url = AI_MODEL_API_URL
        self.api_key = AI_MODEL_API_KEY

    def make_decision(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        data = {
            "prompt": prompt,
            "max_tokens": 500
        }

        response = requests.post(self.api_url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['text'].strip()
        else:
            raise Exception(f"API request failed with status code {response.status_code}")
