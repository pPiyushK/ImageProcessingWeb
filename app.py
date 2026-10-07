from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from processing.image_opertains import grayscale, brightness

app = Flask(__name__)
app.secret_key = "123456"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

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
        operation = request.form.get("operation")
        name, extension = os.path.splitext(filename)

        if operation == "grayscale":
            output_filename = f"{name}_grayscale{extension}"
            output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
            grayscale(input_path, output_path)

        elif operation in {"bright", "dark"}:
            factor = 1.4 if operation == "bright" else 0.6
            suffix = "bright" if operation == "bright" else "dark"
            output_filename = f"{name}_{suffix}{extension}"
            output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
            brightness(input_path, output_path, factor)

        else:
            return "Invalid operation"

        return render_template(
            "index.html",
            original=filename,
            processed=output_filename
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
