def greet():
    print("Hello, Network Engineer!")

greet()

def configure_inteface(interface_name,ip_address):
    print(f"Configuring {interface_name} with {ip_address}")

configure_inteface("GigabitEthernet0/1","192.168.1.1")

configure_inteface(ip_address="192.168.1.1",
interface_name="GigabitEthernet0/1")

def calculate_metrics(bytes_transmitted,bytes_received):
    tx_rate=bytes_transmitted/60
    rx_rate=bytes_received/60
    return tx_rate, rx_rate

tx,rx=calculate_metrics(3000,5000)
print(f"Transmit rate: {tx} Bps, receive rate: {rx} Bps")



def ping(host="8.8.8.8",count=4):
    print(f"Pinging {host} {count} times...")
    return "Ping successful"

print(ping())
print(ping("192.168.1.1"))
print(ping(count=8))

