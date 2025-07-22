import os
import requests
os.environ['HF_TOKEN']='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'
API_URL = "https://router.huggingface.co/hf-inference/models/tabularisai/multilingual-sentiment-analysis"
headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "I like you. I love you",
})
print(output)