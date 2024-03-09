from flask import Flask, request
import os
from gradio_client import Client
app = Flask(__name__)
@app.route('/', methods=['POST'])
def convert_string_to_array():
    return Client("edge37/embed", hf_token=os.environ.get("HF")).predict(request.get_data(as_text=True), api_name="/predict")
if __name__ == '__main__':
    app.run(debug=True)