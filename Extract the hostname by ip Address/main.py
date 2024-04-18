

import socket

if __name__ == '__main__':
  ip_address = input("Enter the IP address: ")
  try:
      hostname = socket.gethostbyaddr(ip_address)
      print(f'The hostname of the IP address {ip_address} is: {hostname[0]}')
  except socket.herror as e:
      print(f"Error: Cannot resolve IP address {ip_address}. Please enter a valid IP address.")
