import pdfplumber
import re

SKILLS_LIST = [
    "python", "django", "flask", "fastapi",
    "java", "c++", "c", "javascript", "typescript",
    "react", "angular", "vue",
    "html", "css", "bootstrap", "tailwind",
    "sql", "postgresql", "mysql", "mongodb",
    "git", "github", "docker", "kubernetes",
    "aws", "azure", "gcp",
    "pandas", "numpy", "scikit-learn",
    "machine learning", "deep learning",
    "data analysis", "data science",
]

def parse_resume(path):
    text = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text().lower() + "\n"

    email = re.search(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.search(r"\+?\d[\d\s\-]{8,}", text)

    found_skills = []
    for skill in SKILLS_LIST:
        if skill in text:
            found_skills.append(skill)

    return {
        "full_name": text.split("\n")[0].strip().title() if text else "",
        "email": email.group(0) if email else None,
        "phone": phone.group(0) if phone else None,
        "skills": ", ".join(sorted(set(found_skills))),
        "text": text,
    }

import re


def extract_projects(resume_text):
    """
    Level-1 project extraction:
    - Finds Projects section
    - Extracts multiple projects
    """

    projects = []
    text = resume_text.replace("\r", "")

    match = re.search(
        r"(projects|academic projects|personal projects)\s*(.*?)(experience|education|skills|certifications|$)",
        text,
        re.IGNORECASE | re.DOTALL,
    )

    if not match:
        return projects

    section_text = match.group(2).strip()
    lines = [line.strip() for line in section_text.split("\n") if line.strip()]

    current_project = None

    for line in lines:
        if len(line) < 80 and not line.startswith("-"):
            if current_project:
                projects.append(current_project)

            current_project = {
                "title": line,
                "description": "",
                "technologies": "",
            }
        else:
            if current_project:
                current_project["description"] += line + " "

    if current_project:
        projects.append(current_project)

    return projects
