import os
from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from the .env file
load_dotenv()

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
# Enable CORS for all routes and origins
CORS(app)

# This is the API endpoint your front end will call
@app.route("/api/chat", methods=["POST"])
def chat():
    # Get the entire JSON payload from the front end
    data = request.json
    
    # Check if the 'messages' list is in the data
    messages = data.get("messages")

    if not messages:
        return jsonify({"error": "No messages provided"}), 400

    try:
        # Call the OpenAI Chat Completions API with the messages list directly
        response = client.chat.completions.create(
            model="gpt-4o",  # The model to use
            messages=messages  # Pass the list of messages directly
        )
        
        # Extract the AI's response text
        ai_response = response.choices[0].message.content
        return jsonify({"reply": ai_response})

    except Exception as e:
        # This will now give you a more specific error if something else goes wrong
        print("An error occurred:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
