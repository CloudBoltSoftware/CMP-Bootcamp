from django.urls import path

from xui.acme_graphs.api import fetch_data_from_api

API_BASE = "xui/acme_graphs/api"

xui_urlpatterns = [
    path(f"{API_BASE}/data", fetch_data_from_api),
]
