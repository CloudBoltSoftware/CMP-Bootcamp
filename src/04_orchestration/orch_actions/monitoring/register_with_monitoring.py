if __name__ == "__main__":
    import os, sys
    sys.path.extend(['/opt/cloudbolt', '/var/opt/cloudbolt/proserv'])
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

    import django
    django.setup()


from common.methods import set_progress
from jobs.models import Job


def run(job, server, **kwargs):
    msg = ""
    if server.acme_enable_monitoring:
        msg = f"Registered {server.hostname} with monitoring."
        set_progress(msg)
    return "SUCCESS", msg, ""


if __name__ == "__main__":
    job = Job.objects.get(id=348)
    server = job.server_set.first()
    print(run(job, server))
