from django.shortcuts import render

from extensions.views import report_extension
from utilities.logger import ThreadLogger

logger = ThreadLogger(__name__)


@report_extension(
    title="Servers By Resource Handler",
    description="",
    thumbnail="report_preview.png")
def rh_server_report_view(request, **kwargs):
    return render(request, template_name='acme_graphs/templates/servers_by_rh.html')

