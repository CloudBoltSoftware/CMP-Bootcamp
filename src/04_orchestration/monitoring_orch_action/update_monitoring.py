if __name__ == "__main__":
    import os, sys
    sys.path.extend(['/opt/cloudbolt', '/var/opt/cloudbolt/proserv'])
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

    import django
    django.setup()


from common.methods import set_progress
from jobs.models import Job


def run(job, server, old_value, new_value, **kwargs):
    msg = ""

    if new_value == True:
        msg = f"Enable monitoring for {server.hostname}."
    else:
        msg = f"Disable monitoring for {server.hostname}"

    return "SUCCESS", msg, ""


if __name__ == "__main__":
    job = Job.objects.get(id=348)
    server = job.server_set.first()
    print(run(job, server))
