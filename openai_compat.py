import json, time, uuid
import boto3
from flask import Response, jsonify
from config import DEFAULT_CHAT_MODEL, DEFAULT_EMBEDDING_MODEL
from model_router import invoke_chat, invoke_embedding, model_route
client = boto3.client("bedrock-runtime", region_name="us-east-1")

def chat_completions(req):
    data = req.get_json()
    # messages = data.get("messages", [])
    stream = data.get("stream", False)
    model_id = data.get("model", DEFAULT_CHAT_MODEL)

    if stream:
        pass
        # def generate():
        #     stream_body = invoke_chat(model_id, body, stream=True)
        #     for event in stream_body:
        #         chunk = json.loads(event["chunk"]["bytes"].decode())
        #         delta = chunk.get("delta", {}).get("text", "")
        #         if delta:
        #             yield f"data: {json.dumps({ 'id': f'chatcmpl-{uuid.uuid4()}', 'object': 'chat.completion.chunk', 'created': int(time.time()), 'model': model_id, 'choices': [ { 'delta': { 'content': delta }, 'index': 0, 'finish_reason': None } ] })}\n\n"
        #     yield "data: [DONE]\n\n"
        # return Response(generate(), content_type="text/event-stream")
    else:
        response_text = model_route(data)
        # print({"maxTokens": data.get("max_tokens", 1024), "temperature": data.get("temperature", 0.7), "topP": 0.9})
        # response = client.converse(
        # modelId=model_id,
        # messages=messages,
        # inferenceConfig={"maxTokens": data.get("max_tokens", 1024), "temperature": data.get("temperature", 0.7), "topP": 0.9}
        # )
        # result = invoke_chat(model_id, body)
        # text = result["content"][0]["text"]
        return jsonify({
            "id": f"chatcmpl-{uuid.uuid4()}",
            "object": "chat.completion",
            "created": int(time.time()),
            "model": model_id,
            "choices": [{
                "index": 0,
                "message": {"role": "assistant", "content": response_text},
                "finish_reason": "stop"
            }]
        })

def embeddings(req):
    data = req.get_json()
    model_id = DEFAULT_EMBEDDING_MODEL
    input_texts = data.get("input", [])
    if isinstance(input_texts, str):
        input_texts = [input_texts]
    body = { "inputText": input_texts[0] }  # Titan 目前只支持单条
    result = invoke_embedding(model_id, body)
    vector = result["embedding"]
    return jsonify({
        "object": "list",
        "data": [{
            "object": "embedding",
            "embedding": vector,
            "index": 0
        }],
        "model": model_id,
        "usage": {"prompt_tokens": 0, "total_tokens": 0}
    })

def list_models():
    return jsonify({
        "object": "list",
        "data": [
            {"id": DEFAULT_CHAT_MODEL, "object": "model", "owned_by": "bedrock"},
            {"id": DEFAULT_EMBEDDING_MODEL, "object": "model", "owned_by": "bedrock"}
        ]
    })