from netmiko import ConnectHandler

# Input variables
switches = input("Enter IP/hostname of the switches (separate multiple entries with comma): ")
switch_list = switches.split(",")
username = input("Enter your SSH username: ")
password = input("Enter your SSH password: ")


# Netmiko device settings
device = {
    "device_type": "cisco_ios",
    "username": username,
    "password": password,
}

# Loop through each switch
for switch in switch_list:
    device["ip"] = switch
    net_connect = ConnectHandler(**device)
    print(f"Logged into {switch}")
    net_connect.send_config_set([
        "command",
        "command",
        "command",
        "command",
        "command",
        "command"

    ])
    print(f"commands configured on {switch}")
    net_connect.disconnect()
