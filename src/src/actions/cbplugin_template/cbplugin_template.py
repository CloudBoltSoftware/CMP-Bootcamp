if __name__ == '__main__':
    import os
    import sys
    import django
    sys.path.extend(['/opt/cloudbolt', '/var/opt/cloudbolt/proserv'])
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
    django.setup()


from infrastructure.models import Server
from common.methods import set_progress

from utilities.logger import ThreadLogger
logger = ThreadLogger(__name__)


def run():
    servers = Server.objects.filter(status="ACTIVE")
    for server in servers:
        msg = f"{server.id}, {server.hostname}"
        set_progress(msg)  # output to job progress
        logger.info(msg)   # output to job log

    return "SUCCESS", msg, ""  # output message to job results

if __name__ == '__main__':
    run()

