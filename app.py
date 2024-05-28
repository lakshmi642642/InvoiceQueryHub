from flask import Flask, request, jsonify, render_template
import base64
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/impira/layoutlm-invoices"
headers = {"Authorization": "Bearer <ENTER_ACCESS_TOKEN>"}

app = Flask(__name__)

def query(payload):
    try:
        with open(payload["image_path"], "rb") as f:
            img = f.read()
            payload["image"] = base64.b64encode(img).decode("utf-8")
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/extract', methods=['POST'])
def extract():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    question = request.form.get('question', 'What is the Total Amount?')
    file_path = f"/tmp/{file.filename}"
    file.save(file_path)

    output = query({
        "image_path": file_path,
        "question": question
    })

    os.remove(file_path)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
