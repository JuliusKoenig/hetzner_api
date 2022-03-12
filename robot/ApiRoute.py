from enum import Enum
from typing import Any, Union

import requests
from requests.auth import HTTPBasicAuth


class ApiRoute:
    class _Methods(str, Enum):
        GET = "GET"
        POST = "POST"
        PUT = "PUT"
        DELETE = "DELETE"

    def __init__(self, auth: HTTPBasicAuth, url: str):
        self._auth = auth
        self._url = url

    def _do_request(self, sub_url: str, target_class: Any, method: _Methods = _Methods.GET, data: dict = None) -> Union[Any, list[Any]]:
        if data is None:
            data = {}
        url = self._url + sub_url

        if method == "GET":
            response = requests.get(url=url, auth=self._auth, data=data)
        elif method == "POST":
            response = requests.post(url=url, auth=self._auth, data=data)
        elif method == "PUT":
            response = requests.put(url=url, auth=self._auth, data=data)
        elif method == "DELETE":
            response = requests.delete(url=url, auth=self._auth, data=data)
        else:
            raise AttributeError("Method unknown.")

        response.raise_for_status()
        response_json = response.json()

        if type(response_json) == list:
            target_objects = []
            for r in response_json:
                target_object = target_class(robot=self, **r)
                target_objects.append(target_object)
            return target_objects
        else:
            target_object = target_class(robot=self, **response_json)
            return target_object
