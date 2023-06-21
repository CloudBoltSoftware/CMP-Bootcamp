from common.methods import set_progress
from infrastructure.models import CustomField


RESOURCE_URL = "{{ RESOURCE_URL }}"


def run(job, resource, **kwargs):
    cf, _ = CustomField.objects.get_or_create(
        name="acme_resource_url",
        label="Resource URL",
        type="URL",
        show_as_attribute=True,
    )
    
    resource.acme_resource_url = RESOURCE_URL
    set_progress(f"Resource available at: {RESOURCE_URL}")
    
    return "SUCCESS", RESOURCE_URL, ""
