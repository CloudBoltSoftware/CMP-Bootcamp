from django.shortcuts import render

from extensions.views import report_extension
from infrastructure.models import Server


@report_extension(title="Active Server Report", description="")
def view_active_server_report(request):
    servers = Server.objects.filter(status="ACTIVE").order_by("hostname")
    return render(
        request, 
        "acme_server_reports/templates/server_report.html",
        context={"servers": servers}
        )
