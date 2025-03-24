# OpenAI-Compatible Gateway for Amazon Bedrock

## 🔧 Features
- Compatible with OpenAI SDK (ChatCompletion, Embeddings, /v1/models)
- Bearer Token authentication
- Stream and non-stream Claude chat
- Titan Embedding support
- Docker deployable

## 🚀 Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## 🐳 Run via Docker

```bash
docker build -t bedrock-gateway .
docker run -p 5000:5000 -e AWS_ACCESS_KEY_ID=xxx -e AWS_SECRET_ACCESS_KEY=xxx bedrock-gateway
```

## 🔐 Example (Python OpenAI SDK)

```python
import openai

openai.api_base = "http://localhost:5000/v1"
openai.api_key = "your-token-123"

resp = openai.ChatCompletion.create(
  model="claude-3-sonnet",
  messages=[{"role": "user", "content": "讲个冷笑话"}]
)
print(resp["choices"][0]["message"]["content"])
```