from ipaddress import IPv4Address

from requests.auth import HTTPBasicAuth

from .ApiRoute import ApiRoute
from .models import ServerMin, ServerDetail, FailoverIp

BASE_URL = "https://robot-ws.your-server.de"


class Robot:
    class _Server(ApiRoute):
        def list(self) -> list[ServerMin]:
            return self._do_request(
                sub_url=f"/",
                target_class=ServerMin,
                method=ApiRoute._Methods.GET
            )

        def detail(self, server_number: int) -> ServerDetail:
            return self._do_request(
                sub_url=f"/{server_number}",
                target_class=ServerDetail,
                method=ApiRoute._Methods.GET
            )

    class _Failover(ApiRoute):
        def list(self) -> list[FailoverIp]:
            return self._do_request(
                sub_url=f"/",
                target_class=FailoverIp,
                method=ApiRoute._Methods.GET
            )

        def detail(self, failover_ip: IPv4Address) -> FailoverIp:
            return self._do_request(
                sub_url=f"/{failover_ip}",
                target_class=FailoverIp,
                method=ApiRoute._Methods.GET
            )

        def set_route(self, failover_ip: IPv4Address, active_server_ip: IPv4Address) -> FailoverIp:
            return self._do_request(
                sub_url=f"/{failover_ip}",
                target_class=FailoverIp,
                method=ApiRoute._Methods.POST,
                data={"active_server_ip": active_server_ip}
            )

        def delete_route(self, failover_ip: IPv4Address) -> FailoverIp:
            return self._do_request(
                sub_url=f"/{failover_ip}",
                target_class=FailoverIp,
                method=ApiRoute._Methods.DELETE
            )

    def __init__(self, username: str, password: str):
        self._auth = HTTPBasicAuth(username, password)

    def server(self):
        return self._Server(auth=self._auth, url=f"{BASE_URL}/server")

    def failover(self):
        return self._Failover(auth=self._auth, url=f"{BASE_URL}/failover")
