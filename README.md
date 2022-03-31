# hetzner_api

---
An API wrapper for the Hetzner Robot API.
Based on the popular client library requests bundled with pydantic models.

---
The library is currently in alpha status. Pull requests are welcome.

### Implemented:
* Server(partial: list, detail)
* Failover

### Not Implemented:
* Server
* IP
* Subnet
* Reset
* Failover
* Wake on LAN
* Boot-Configuration
* Reverse DNS
* Traffic
* SSH-Keys
* Server Order
* Storage Box
* Firewall
* vSwitch

### Example:
```python
import logging
import sys

from hetzner_api.robot.Robot import Robot

failover_ip_str = "1.2.3.4"
local_node_ip_str = "10.8.0.1"

if __name__ == '__main__':
    robot = Robot(username="hetzner_username", password="hetzner_password")

    failover_ip = robot.failover().detail(failover_ip=failover_ip_str)
    
    if failover_ip.active_server_ip == local_node_ip_str:
        logging.info(f"Failover IP is already routed to this node.")
        sys.exit(0)

    logging.info(f"Setting Failover IP to this node({local_node_ip_str}).")
    failover_ip = robot.failover().set_route(failover_ip=failover_ip, active_server_ip=local_node_ip_str)
    if failover_ip.active_server_ip == local_node_ip_str:
        logging.info("Success!")
        sys.exit(0)
    sys.exit(1)

```
