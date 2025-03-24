import boto3
import json


def invoke_deepseek(data):

    model_id = data.get("model")
    messages = data.get('messages')
    region_name = data.get("region_name", "us-east-1")

    client = boto3.client("bedrock-runtime", region_name=region_name)

    response = client.converse(
        modelId=model_id,
        messages=messages,
        inferenceConfig={"maxTokens": data.get("max_tokens", 1024), "temperature": data.get("temperature", 0.7), "topP": 0.9}
        )
    return response["output"]["message"]["content"][0]["text"]