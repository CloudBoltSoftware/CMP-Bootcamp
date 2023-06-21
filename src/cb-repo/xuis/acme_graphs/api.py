import requests

from utilities.decorators import json_view
from utilities.logger import ThreadLogger
from utilities.rest import RestConnection
from resourcehandlers.models import ResourceHandler

logger = ThreadLogger(__name__)


@json_view
def fetch_data_from_api(request):
	results = []
	rhs = ResourceHandler.objects.all()
	for rh in rhs:
		results.append({
			"name": rh.name,
			"y": rh.server_set.count(),
			"id": rh.id
		})	
	return results	
