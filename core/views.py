from django.shortcuts import render, redirect
from candidates.models import Candidate
from candidates.parser import parse_resume

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

        return redirect("upload")

    return render(request, "upload.html")
