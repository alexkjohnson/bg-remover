from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")  # Serves an HTML form for file upload

# Route for file upload and processing
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file uploaded", 400
    file = request.files["file"]
    input_image = file.read()
    output_image = remove(input_image)
    return send_file(io.BytesIO(output_image), mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)

