from netmiko import ConnectHandler

Router = {
    "device_type": "cisco_ios",
    "ip": "devnetsandboxiosxe.cisco.com",
    "username": "admin",
    "password": "C1sco12345"
        }

dev_connect = ConnectHandler(**Router)
command = dev_connect.send_command("show version")
print(command)

dev_connect.disconnect()