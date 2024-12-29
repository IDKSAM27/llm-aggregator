from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = ""

@app.route('/query', methods=['POST']) #called decorator
def query():
    """
    Aggregates requests and queries GPT-4 API.
    Expected JSON input: {"model": "gpt-4", "prompt": "Your prompt here", "max_tokens": 100}
    """
    data = request.json

    if not data or 'prompt' not in data:
        return jsonify({"error": "Missing prompt"}), 400
    
    try:
        # Qeury gpt4 api
        response = openai.ChatCompletion.create(
            model = data.get("model", "gpt-4"),
            messages = [{"role": "user", "content": data["prompt"]}],
            max_tokens = data.get("max_tokens", 100)
        )
        return jsonify({"response": response.choices[0].message["content"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
# The api's which are paid cannot be used, hence this project is paused for a good reason