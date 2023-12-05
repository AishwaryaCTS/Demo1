from flask import Flask, render_template,request,jsonify
import os
import vertexai
from vertexai.preview.language_models import ChatModel

from vertexai.preview.language_models import ChatModel, InputOutputTextPair, ChatMessage #

# Get the directory of the current script
dir_path = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path of the credentials file in the secrets directory
credentials_path = os.path.join(dir_path, 'secrets', 'credentials.json')

# Set the environment variable to the credentials file path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

app=Flask(__name__)

CORS(app)   #allows outside requests

# Initialize Vertex AI
vertexai.init(project=os.environ.get("PROJECT_ID"), location=os.environ.get("VERTEX_REGION"))

@app.route('/')
def welcome():
    return render_template('demo1.html')

 
@app.route('/process_question',methods=['POST'])
def process_question():
    data = request.get_json()
    question = data.get('question')
    print(question)
    # Process the question (replace this with your actual processing logic)
    answer = f'This is the answer to: {question}'

    # Return the answer as JSON
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)