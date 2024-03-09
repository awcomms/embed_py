from flask import Flask, request
from sentence_transformers import SentenceTransformer
app = Flask(__name__)
@app.route('/', methods=['POST'])
def convert_string_to_array():
    return SentenceTransformer("jinaai/jina-embedding-s-en-v1").encode(request.get_data(as_text=True))[0]
if __name__ == '__main__':
    import bjoern
    bjoern.run(app, '0.0.0.0', 10000)