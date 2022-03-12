from ipaddress import IPv4Address
from typing import Any, Optional

from pydantic import BaseModel


class Subnet(BaseModel):
    ip: str
    mask: str


class ServerMin(BaseModel):
    def __init__(self, **data: Any):
        if "server" in data:
            data = data["server"]
        super().__init__(**data)

    server_ip: str  # Haupt-IP-Adresse des Servers
    server_ipv6_net: str  # Haupt-IPv6-Netz des Servers
    server_number: int  # ID des Servers
    server_name: str  # Name des Servers
    product: str  # Produktname
    dc: str  # Rechenzentrum
    traffic: str  # Freitraffic, 'unlimited' im Fall einer Flatrate
    status: str  # Bestellstatus ("ready" oder "in process")
    cancelled: bool  # Zeigt an, ob der Server zur Kündigung vorgemerkt ist
    paid_until: str  # Bezahlt-bis Datum
    ip: list[str]  # Array aller zugehörigen Einzel-IP-Adressen


class ServerDetail(ServerMin):
    subnet: list[Subnet]  # Array aller zugehörigen Subnetze
    reset: bool  # Zeigt an, ob ein Reset möglich ist
    rescue: bool  # Zeigt an, ob das Rescuesystem verfügbar ist
    vnc: bool  # Zeigt an, ob die VNC-Installation verfügbar ist
    windows: bool  # Zeigt an, ob die Windows-Installation verfügbar ist
    plesk: bool  # Zeigt an, ob die Plesk-Installation verfügbar ist
    cpanel: bool  # Zeigt an, ob die cPanel-Installation verfügbar ist
    wol: bool  # Zeigt an, ob Wake on Lan verfügbar ist
    hot_swap: bool  # Zeigt an, ob Hot-Swap verfügbar ist
    linked_storagebox: Optional[int]  # ID der zugehörigen Storage Box


class FailoverIp(BaseModel):
    def __init__(self, **data: Any):
        if "failover" in data:
            data = data["failover"]
        super().__init__(**data)

    ip: IPv4Address  # Failover Netz-Adresse
    netmask: IPv4Address  # Failover Netzmaske
    server_ip: IPv4Address  # Haupt-IP-Adresse des zugehörigen Servers
    server_number: int  # ID des Servers
    active_server_ip: Optional[IPv4Address]  # Haupt-IP-Adresse des derzeitigen Ziel-Servers
