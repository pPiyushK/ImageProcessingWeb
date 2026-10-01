from flask import Flask, render_template, request, redirect, url_for, redirect
import os
from werkzeug.utils import secure_filename

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
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for("uploaded_file", filename=filename))
    return render_template("index.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return render_template("index.html", filename=filename)

if __name__ == "__main__":
    app.run(debug=True)