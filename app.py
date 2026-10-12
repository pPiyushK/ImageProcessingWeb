from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from processing.image_opertains import contrast, grayscale, brightness, rotate, flip, resize, crop

app = Flask(__name__)
app.secret_key = "123456"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def render_message(message):
    return render_template("index.html", message=message)

def form_int(name, default=None):
    value = request.form.get(name)
    if value in (None, ""):
        if default is not None:
            return default
        raise ValueError(f"{name.capitalize()} is required.")
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{name.capitalize()} must be a number.") from exc

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        if "image" not in request.files:
            return render_message("No file selected.")
        
        file = request.files["image"]

        if file.filename == "":
            return render_message("No file selected.")
        
        if not allowed_file(file.filename):
            return render_message("File type not allowed. Please upload PNG, JPG, JPEG, GIF, or WEBP.")
        
        filename = secure_filename(file.filename)
        if not filename:
            return render_message("Invalid file name.")

        input_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(input_path)
        operation = request.form.get("operation")
        name, extension = os.path.splitext(filename)

        try:
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

            elif operation == "contrast":
                factor = 1.5
                output_filename = f"{name}_contrast{extension}"
                output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
                contrast(input_path, output_path, factor)

            elif operation in {"rotate", "rotate90", "rotate180", "rotate270"}:
                angle = form_int("angle", 0) if operation == "rotate" else int(operation.replace("rotate", ""))
                output_filename = f"{name}_rotate{angle}{extension}"
                output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
                rotate(input_path, output_path, angle)

            elif operation in {"flip", "flip_horizontal", "flip_vertical"}:
                mode = request.form.get("mode", "horizontal") if operation == "flip" else operation.replace("flip_", "")
                output_filename = f"{name}_flip_{mode}{extension}"
                output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
                flip(input_path, output_path, mode)

            elif operation == "resize":
                width = form_int("width")
                height = form_int("height")
                if width <= 0 or height <= 0:
                    raise ValueError("Width and height must be greater than zero.")
                output_filename = f"{name}_resize_{width}x{height}{extension}"
                output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
                resize(input_path, output_path, width, height)

            elif operation == "crop":
                left = form_int("left")
                upper = form_int("top")
                right = form_int("right")
                lower = form_int("bottom")
                if right <= left or lower <= upper:
                    raise ValueError("Crop right/bottom values must be greater than left/top values.")
                output_filename = f"{name}_crop_{left}_{upper}_{right}_{lower}{extension}"
                output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_filename)
                crop(input_path, output_path, left, upper, right, lower)

            else:
                return render_message("Please choose a valid image operation.")

        except Exception as e:
            return render_message(f"Error processing image: {str(e)}")
        
        return render_template(
            "index.html",
            original=filename,
            processed=output_filename
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
