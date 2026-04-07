from flask import Flask, render_template, request
import os

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from job_matcher import match_job_role

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Analyze resume
@app.route("/analyze", methods=["POST"])
def analyze():

    file = request.files["resume"]

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Extract text from resume
    text = extract_resume_text(filepath)

    # DEBUG: Show extracted resume text
    print("\n===== RESUME TEXT =====\n")
    print(text)
    print("\n=======================\n")

    # Extract skills from resume
    resume_skills = extract_skills(text)

    # DEBUG: Show detected skills
    print("\n===== SKILLS FOUND =====\n")
    print(resume_skills)
    print("\n========================\n")

    # Match job role
    role, score, matched, missing = match_job_role(resume_skills)

    # If no role detected
    if role is None:
        role = "No matching job role found"

    return render_template(
        "result.html",
        skills=resume_skills,
        role=role,
        score=round(score, 2),
        matched=matched,
        missing=missing
    )


if __name__ == "__main__":
    app.run(debug=True)