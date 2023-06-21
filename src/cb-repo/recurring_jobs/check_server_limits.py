THRESHOLD = int({{ THRESHOLD }})
# THRESHOLD = 10.0

if __name__ == "__main__":
    import os
    import sys
    sys.path.extend(['/opt/cloudbolt', '/var/opt/cloudbolt/proserv'])
    os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
    import django
    django.setup()

from utilities.logger import ThreadLogger
from accounts.models import Group
from alerts.methods import alert


logger = ThreadLogger(__name__)


def run(*args, **kwargs):    
    msg = ""
    for group in Group.objects.all():
        curr_limit = group.quota_set.vm_cnt.limit
        curr_usage = group.quota_set.vm_cnt.total_used
        pct = int(curr_usage / curr_limit * 100)
        print(group, curr_usage, curr_limit, pct)
        if pct >= THRESHOLD:
            alert("rak", f"RAK: Group {group.name} has exceeded {THRESHOLD}%. Current usage: {pct}%")

    return "SUCCESS", "", ""

if __name__ == "__main__":
    run()
