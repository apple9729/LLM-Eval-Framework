import os
import openai

class OpenAIClient:
    def __init__(self, key=None):
        api_key = key or os.environ.get('OPENAI_API_KEY')
        openai.api_key = api_key

    def generate(self, prompt, max_tokens=8192, temperature=0.0):
        try:
            resp = openai.ChatCompletion.create(
                model='gpt-4o' if hasattr(openai, 'ChatCompletion') else 'gpt-3.5-turbo',
                messages=[{'role':'user','content':prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            if isinstance(resp, dict):
                choices = resp.get('choices', [])
                if choices:
                    content = choices[0].get('message', {}).get('content') or choices[0].get('text', '')
                    return content.strip()
            return str(resp)
        except Exception:
            return ""
