from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import tempfile
import logging

from utils.text_extractor import extract_text, sanitize_text, ALLOWED_EXTENSIONS
# from summarizer import summarize_text
from utils.length_mapper import map_length

app = Flask(__name__)
CORS(app, resources={r"/summarize": {"origins": ["http://localhost:5173", "http://localhost:5000"]}})
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # Limit file uploads to 5 MB 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m-%d-%Y %H:%M:%S'
)

@app.route("/health", methods=['GET'])
def health_check():
    logging.info('Starting server health check')
    return jsonify({ 
        "status": "ok",
        "message": "Cyberskool Companion is running"
    })

@app.route("/test_preprocessor", methods=['GET'])
def test_text_extractor():
    logging.info('Testing text extractor logic')
    from utils.text_extractor import extract_text
    import os
    file_path = os.path.join(os.getcwd(), 'docs/test_data.txt')
    try:
        text = extract_text(file_path)
        logging.info('Text extracted successfully')
        return jsonify({
            'status': "OK",
            'data': text[:100]
        }), 200
    except Exception as e:
        logging.error(f'Text extraction failed: {e}')
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

# @app.route("/test_model", methods=['GET'])
# def test_model():
#     logging.info('Starting AI model test')
#     from summarizer import summarize_text
#     text = """Cyberskool Companion Standard Features
#      These are the essential capabilities expected 
#     from any reliable AI summarizer. Core 
#     Summarization Automatic Summarization: 
#     Generates a condensed version of the input text.
#      Extractive Summarization: Selects key sentences
#      directly from the original text. Length 
#     Control: Allows customization of summary 
#     length (short, medium, long). Single Document 
#     Summarization: Handles summarization of one 
#     document at a time."""
#     try:
#         logging.info('Attempting text summary')
#         summary = summarize_text(text)
#         logging.info('Summarization successful')
#         return jsonify({
#             'status': "OK",
#             'data': summary
#         }), 200
#     except Exception as e:
#         logging.error(f'Summarization failed: {e}')
#         return jsonify({
#             'status': 'error',
#             'message': str(e)
#         })
    
# @app.route("/summarize", methods=['POST'])
# def summarize():
#     try:
#         min_len = int(request.form.get("min_length", 30))
#         max_len = int(request.form.get("max_length", 30))

#         # Plain text input
#         if "text" in request.form:
#             raw_text = sanitize_text(request.form["text"])
#             summary = summarize_text(raw_text, min_len, max_len)
#             return jsonify({
#                 'status': "OK",
#                 'data': summary
#             })
        
#         # File input
#         if "file" in request.form:
#             file = request.files["file"]
#             filename = secure_filename(file.filename) # Block path traversal
#             ext = os.path.splitext(filename)[1].lower()
#             if ext not in ALLOWED_EXTENSIONS:
#                 return jsonify({
#                     'status': "error",
#                     'message': f"Unsupported file type: {ext}"
#                 }), 400
            
#             with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
#                 file.save(tmp.name)
#                 tmp_path = tmp.name

#                 try:
#                     text = extract_text(tmp_path)
#                     summary = summarize_text(text, min_len, max_len)
#                     return jsonify({
#                         'status': "OK",
#                         'data': summary
#                     })
#                 finally:
#                     os.remove(tmp_path)
#         return jsonify({
#             'status': "error",
#             'message': f"No valid 'file' or 'text' input provided"
#         }), 400
#     except Exception as e:
#         return jsonify({
#             'status': "error",
#             'message': {str(e)}
#         }), 500

@app.route("/", methods=['GET', 'POST'])
def index():
    summary = "Cyberskool Companion Standard Features These are the essential capabilities expected from any reliable AI summarizer."
    if request.method == 'POST':
        model_name = request.form.get("model", "sshleifer/distilbart-cnn-12-6")
        min_len, max_len = map_length(request.form.get("length", "medium"))

        # Plain text input
        if "text" in request.form and request.form["text"].strip():
            raw_text = sanitize_text(request.form["text"])
            # summary = summarize_text(raw_text, min_len, max_len)
        
        # File input
        if "file" in request.files and request.files["file"].filename:
            file = request.files["file"]
            filename = secure_filename(file.filename) # Block path traversal
            ext = os.path.splitext(filename)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                summary = f"Unsupported file type: {ext}"
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
                file.save(tmp.name)
                tmp_path = tmp.name

                try:
                    text = extract_text(tmp_path)
                    # summary = summarize_text(text, min_len, max_len)
                finally:
                    os.remove(tmp_path)
    return render_template('index.html', summary=summary)

if __name__ == "__main__":
    app.run(debug=True)