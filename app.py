from flask import Flask, request
from gradio_client import Client
app = Flask(__name__)
@app.route('/convert', methods=['POST'])
def convert_string_to_array():
    return Client("edge37/embed").predict(request.get_data(as_text=true), api_name="/predict")

if __name__ == '__main__':
    app.run(debug=True)