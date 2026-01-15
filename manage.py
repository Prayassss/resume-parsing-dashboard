#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    try:
        import django
        from django.core.management import execute_from_command_line
        django.setup()
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc

    # ✅ RUN MIGRATIONS AUTOMATICALLY ON RENDER
    if os.environ.get("RENDER"):
        execute_from_command_line(["manage.py", "migrate", "--noinput"])

        # ✅ AUTO-CREATE SUPERUSER (FREE TIER)
        from django.contrib.auth import get_user_model

        User = get_user_model()
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if username and password and not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
