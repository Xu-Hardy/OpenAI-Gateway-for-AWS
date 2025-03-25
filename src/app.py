from flask import Flask, request, jsonify
from openai_compat import chat_completions, embeddings, list_models
from auth import verify_token

app = Flask(__name__)

# @app.before_request
# def auth_middleware():
#     if not verify_token(request):
#         return jsonify({"errors": "Unauthorized"}), 401

@app.route("/v1/chat/completions", methods=["POST"])
def handle_chat():
    return chat_completions(request)

@app.route("/v1/embeddings", methods=["POST"])
def handle_embeddings():
    return embeddings(request)

@app.route("/v1/models", methods=["GET"])
def handle_models():
    # print("mode")
    return list_models()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)