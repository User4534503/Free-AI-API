import asyncio
import warnings
import sys
import platform
import os
from flask import Flask, request, jsonify
from g4f.client import Client
from flask_cors import CORS

# Only set the Windows-specific asyncio policy if we're on Windows.
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Suppress warnings to keep the console clean.
warnings.simplefilter("ignore")

# Redirect errors to null to hide them.
# Note: Windows uses 'nul', while Unix-like systems use '/dev/null'.
if platform.system() == "Windows":
    sys.stderr = open('nul', 'w', encoding='utf-8')
else:
    sys.stderr = open('/dev/null', 'w', encoding='utf-8')

# Initialize the Flask app.
app = Flask(__name__)

# Enable CORS for all routes (adjust for specific domains if needed).
CORS(app)

# Create an instance of the client.
client = Client()

@app.route('/chat', methods=['POST'])
def chat():
    """API Endpoint for Chat Completions"""
    try:
        data = request.get_json()
        user_message = data.get("message", "Hello")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_message}],
            web_search=False
        )

        # Return the response from the AI model.
        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        # If something goes wrong, send back an error message.
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Render provides the port via an environment variable.
    port = int(os.environ.get("PORT", 1836))
    app.run(host='0.0.0.0', port=port, debug=False)
