from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Fake baza (za MVP)
tracks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        author = request.form["author"]
        price = request.form["price"]

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            tracks.append({
                "name": file.filename,
                "author": author,
                "price": price,
                "paid": False
            })

        return redirect(url_for("index"))

    return render_template("index.html", tracks=tracks)

@app.route("/buy/<int:track_id>")
def buy(track_id):
    if 0 <= track_id < len(tracks):
        tracks[track_id]["paid"] = True
    return redirect(url_for("index"))

@app.route("/download/<int:track_id>")
def download(track_id):
    track = tracks[track_id]
    if not track["paid"]:
        return "License not purchased", 403
    return send_from_directory(UPLOAD_FOLDER, track["name"], as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)