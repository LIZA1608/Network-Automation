
import socket

if __name__ == '__main__':
    hostname = input("Enter the hostname: ")
    try:
        addr = socket.gethostbyname(hostname)
        print(f'The ip address of the host {hostname} is: {addr}')
    except socket.gaierror as e:
        print(f"Error: Cannot resolve hostname {hostname}. Please enter a valid hostname.")
