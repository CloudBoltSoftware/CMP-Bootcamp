from infrastructure.models import Server, CustomField
from orders.models import CustomFieldValue
from common.methods import set_progress
import time

FETCH_JENKINS_PW_SCRIPT = """
echo $(sudo docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword)
"""


def run(job, resource, logger, **kwargs):
    server = resource.server_set.first()

    # Fetch the intial password from jenkins
    result = server.execute_script(script_contents=FETCH_JENKINS_PW_SCRIPT, run_with_sudo=True)
    result = result.strip()
    tries = 20

    while ('No such file or directory' in result or len(result) == 0) and tries > 0:
        time.sleep(5)
        result = server.execute_script(script_contents=FETCH_JENKINS_PW_SCRIPT)
        result = result.strip()
        set_progress('Response from container: [{}]'.format(result))
        tries -= 1

    if not result:
        return 'WARNING', 'Unable to fetch unlock key.', ''
        
    cf, _ = CustomField.objects.get_or_create(name='acme_initial_unlock_key',
                                              label='Initial Unlock Key',
                                              type='STR',
                                              show_as_attribute=True)
    pattern = re.compile('[\d\w]{30,}')
    matches = pattern.findall(result)
    resource.acme_initial_unlock_key = matches[0]
    
    return 'SUCCESS', '', ''
