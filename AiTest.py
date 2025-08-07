#%%
import requests

def ask_ollama(prompt, model='deepseek-r1'):
    response = requests.post(
        'http://192.168.2.137:11434/api/generate',
        json={
            'model': model,
            'prompt': prompt,
            'stream': False  # Set to True if you want streaming responses
        }
    )
    # return response.json()['response']
    print(response.json()['response'])
# %%
