from django.db import models

class Candidate(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    skills = models.TextField(blank=True)

    resume = models.FileField(upload_to="resumes/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name or "Unnamed Candidate"
    
class Project(models.Model):
    candidate = models.ForeignKey(
        "Candidate",
        on_delete=models.CASCADE,
        related_name="projects"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    technologies = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

