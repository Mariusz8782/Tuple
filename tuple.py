device={"Router","192.168.1.","Cisco"}
print(device)

interface="GigabitEthernet0","up",1000 #interface name, status, speed
print (interface)

try:
    device[1]="192.168.2.1"
except TypeError as e:
    print(e)

name, ip, brand=device

print(f"Name: {name}, IP: {ip}, Brand: {brand}")

device_info=("Router1","172.16.0.1","Juniper",22)

endpoint=("10.10.10.1",443)

device={
    "hostname":"Router1",
    "ip":"192.168.1.1",
    "model":"Cisco 2901",
    "interfaces":["GigabitEthernet0","GigabitEhternet1"]
}
print(device)

ip_address=device["ip"]
print(f"Device IP Address: {ip_address}")

device["location"]="Data Center A"
print(device)

device["ip"]="192.168.2.1"
print(device)

del device["model"]
location=device.pop("location") #Using pop, also retrieves the value
print(device)


for key in device.keys():
    print (key)

for value in device.values():
    print(value)

for key,value in device.items():
    print(f"{key}: {value}")

routing_table={
    "10.0.0.0/24":"192.168.1.1",
    "172.16.0.0/16":"192.168.2.1"
}
for network, next_hop in routing_table.items():
    print(f"Destination: {network}, Next hop: {next_hop}")

