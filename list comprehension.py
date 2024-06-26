numbers=[1,2,3,4,5]
squares=[n**2 for n in numbers]
print(squares)

evens=[n for n in numbers if n%2==0]
print(evens)

ip_list=["192.168.1.1","10.0.0.256","172.16.0.1","256.0.0.1"]
valid_ips=[ip for ip in ip_list if all(0<=int(octet)<=255 for octet in ip.split('.'))]
print(valid_ips)

interfaces=[f"GigabitEthernet0/{i}" for i in range(0,5)]
print(interfaces)

subnets=[["192.168.1.1","192.168.1.2"],["10.0.0.1","10.0.0.2"]]
all_ips=[ip for subnet in subnets for ip in subnet]
print(all_ips)


numbers=[1,2,3,4,5]
squares={n:n**2 for n in numbers}
print(squares)

even_squares={n:n**2 for n in numbers if n%2==0}
print(even_squares)

devices=["Router1","Switch1","Router2"]
ips=["192.168.1.1","192.168.1.2","192.168.1.3"]
ip_device_map={ips[i]:devices[i] for i in range(len(devices))}
print(ip_device_map)

interfaces=["Gig0/0","Gig0/1","Fa0/0"]
speeds=["1Gbps","1Gbps","100Mbps"]
interface_speed={interfaces[i]:speeds[i] for i in range(len(interfaces))}
print(interface_speed)


device_types={"Router1":"Router","Switch1":"Switch","Router2":"Router"}

routers_only={device:type for device, type in device_types.items() if type=="Router"}
print(routers_only)