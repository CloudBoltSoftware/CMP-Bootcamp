import json
import logging

import prov_instance_blueprint
from cmp.api import CloudBoltConnection
from settings import STUDENT_NAMES, STUDENT_EMAILS, CB_UID, CB_PWD, CB_HOST

log = logging.getLogger(__name__)

GROUP = "/api/v3/cmp/groups/GRP-f1pfjtyx/"
ACCOUNT = "Martin Marietta"


def parse_response(response):
    deployment_items = response.json().get("deploymentItems")
    resource_name = deployment_items[0].get("resourceName")
    return resource_name


def main():
    roster = zip(STUDENT_NAMES, STUDENT_EMAILS)
    assignments = []

    with CloudBoltConnection(CB_UID, CB_PWD, CB_HOST) as conn:
        for name, email in roster:
            json_payload = json.loads(prov_instance_blueprint.JSON)
            json_payload["parameters"]["cbpl__account"] = ACCOUNT
            json_payload["parameters"]["cbpl__contact_name"] = f"{name}/{email}"
            json_payload["group"] = GROUP
            try:
                response = conn.post(
                    url="/blueprints/BP-615goe7r/deploy/",
                    json=json_payload
                )
                response.raise_for_status()
                resource_name = parse_response(response)
            except Exception as ex:
                if response:
                    log.error(response.text)
                else:
                    raise ex
                exit(1)

            assignments.append({
                "name": name,
                "email": email,
                "instance": f"{resource_name}.poc.cloudbolt.io",
            })

    log.info(assignments)
    for assignment in assignments:
        print(
            assignment['name'],
            f"https://{assignment['instance']}",
            assignment['email'],
            sep='\t')


if __name__ == '__main__':
    main()
