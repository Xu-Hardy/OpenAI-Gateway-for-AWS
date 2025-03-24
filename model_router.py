import json
from model_invoke import invoke_deepseek

def model_route(data):
    mode_name = data.get("model")
    if mode_name == "us.deepseek.r1-v1:0":
        return invoke_deepseek(data)

def invoke_chat(model_id, body, stream=False):
    pass
    # if stream:
    #     response = client.invoke_model_with_response_stream(
    #         modelId=model_id,
    #         body=json.dumps(body),
    #         contentType="application/json",
    #         accept="application/json"
    #     )
    #     return response["body"]
    # else:
    #     response = client.invoke_model(
    #         modelId=model_id,
    #         body=json.dumps(body),
    #         contentType="application/json",
    #         accept="application/json"
    #     )
    #     return json.loads(response["body"].read())

def invoke_embedding(model_id, body):
    pass
    # response = client.invoke_model(
    #     modelId=model_id,
    #     body=json.dumps(body),
    #     contentType="application/json",
    #     accept="application/json"
    # )
    # return json.loads(response["body"].read())