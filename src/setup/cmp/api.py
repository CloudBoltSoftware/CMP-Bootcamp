import logging

import requests

log = logging.getLogger(__name__)


class CloudBoltConnection():

    def __init__(self, username, password, hostname) -> None:
        self.username = username
        self.password = password
        self.hostname = hostname
        self.base_url = f"https://{hostname}/api/v3/cmp"
        self.token = None
        super().__init__()

    def __enter__(self):
        if self.token:
            return self
        else:
            self.__fetch_token()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __getattr__(self, item: str):
        method = item.upper()
        if method == "GET":
            return lambda url, **kwargs: self._get(url, **kwargs)
        elif method == "POST":
            return lambda url, json, **kwargs: self.__post(url, json, **kwargs)
        elif method == "DELETE":
            return lambda url, **kwargs: self.__delete(url, **kwargs)
        else:
            return item

    def __fetch_token(self):
        url = f"{self.base_url}/apiToken/"
        data = {
            "username": self.username,
            "password": self.password
        }
        response = requests.post(
            url=url,
            json=data,
            headers={"content-type": "application/json"},
            verify=False
        )
        response.raise_for_status()
        self.token = response.json().get("token", None)

    def __get(self, url, **kwargs):
        log.debug(f"GET: {url}")
        return requests.get(
            url=f"{self.base_url}{url}",
            headers={
                "authorization": f"Bearer {self.token}",
                "accept": "application/json"
            },
            verify=False,
            **kwargs
        )

    def __post(self, url, json, **kwargs):
        log.debug(f"POST: {url}")
        return requests.post(
            url=f"{self.base_url}{url}",
            headers={
                "authorization": f"Bearer {self.token}",
                "accept": "application/json",
                "content-type": "application/json",
            },
            json=json,
            verify=False,
            **kwargs
        )

    def __delete(self, url, **kwargs):
        log.debug(f"DELETE: {url}")
        return requests.delete(
            url=f"{self.base_url}{url}",
            headers={
                "authorization": f"Bearer {self.token}",
                "accept": "application/json",
            },
            verify=False,
            **kwargs
        )
