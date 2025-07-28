from flask import Flask, render_template, request
from utils.parser import extract_text
from utils.scorer import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files["resume"]
        job_desc = request.form["job_desc"]

        if resume_file:
            file_path = "uploads/" + resume_file.filename
            resume_file.save(file_path)

            resume_text = extract_text(file_path)
            analysis = analyze_resume(resume_text, job_desc)

            return render_template("result.html", analysis=analysis)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
