import socket

def get_ip_address():
  """Gets the IP address of the local device."""
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))  # Connect to a public server (Google DNS)
  ip = s.getsockname()[0]
  s.close()
  return ip


ip_address = get_ip_address()

with open('ip.log', 'w') as f:
  f.write(f"Device IP address: {ip_address}\n")

print(f"IP address logged to 'ip.log': {ip_address}")
