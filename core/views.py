from django.shortcuts import render, redirect
from candidates.parser import parse_resume, extract_projects
from candidates.models import Candidate, Project


def upload_resume(request):
    if request.method == "POST":
        resume = request.FILES.get("resume")

        candidate = Candidate(resume=resume)
        candidate.save()

        parsed = parse_resume(candidate.resume.path)

        candidate.full_name = parsed.get("full_name", "")
        candidate.email = parsed.get("email")
        candidate.phone = parsed.get("phone")
        candidate.skills = parsed.get("skills", "")
        candidate.save()

        resume_text = parsed.get("text", "")
        projects = extract_projects(resume_text)

        for project in projects:
            Project.objects.create(
                candidate=candidate,
                title=project["title"][:255],
                description=project["description"].strip(),
                technologies=project.get("technologies", ""),
            )

        return redirect("upload")

    return render(request, "upload.html")
