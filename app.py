from flask import Flask, render_template, request, redirect, send_from_directory
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

tracks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        author = request.form["author"]
        price = request.form["price"]

        if file:
            filename = f"{uuid.uuid4()}_{file.filename}"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            tracks.append({
                "id": filename,
                "filename": file.filename,
                "author": author,
                "price": price
            })

            return redirect("/success")

    return render_template("index.html", tracks=tracks)

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/download/<track_id>")
def download(track_id):
    return send_from_directory(UPLOAD_FOLDER, track_id, as_attachment=True)

if __name__ == "__main__":
    app.run()
