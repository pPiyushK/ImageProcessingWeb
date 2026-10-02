from flask import Flask, render_template, request, redirect, url_for, redirect
import os
from werkzeug.utils import secure_filename
from processing.image_opertains import grayscale

app = Flask(__name__)
app.secret_key = "123456"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif","webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "image" not in request.files:
            return "No file selected"
        file = request.files["image"]
        if file.filename == "":
            return "No file selected"
        if not allowed_file(file.filename):
            return "File type not allowed"
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(input_path)
        name,extension = os.path.splitext(filename)
        output_filename = f"{name}_grayscale{extension}"
        output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
        grayscale(input_path, output_path)
        return render_template("index.html", Original=output_filename,processed=output_filename)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)