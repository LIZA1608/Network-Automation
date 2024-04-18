
import socket

if __name__ == '__main__':
    hostname = input("Enter the hostname: ")
    try:
        addr = socket.gethostbyname(hostname)
        print(f'The ip address of the host {hostname} is: {addr}')
    except socket.gaierror as e:
        print(f"Error: Cannot resolve hostname {hostname}. Please enter a valid hostname.")



# here 
# __name__ -> it is a special variable that stores the name of the current module or script
# In the context of the code snippet you provided, if __name__ == '__main__': is a common idiom used to check if the Python script is being run directly by the interpreter. If the script is being executed directly, the __name__ variable will be set to '__main__'. This is useful when you have code that you only want to run when the script is executed directly, not when it is imported into another script.
# So, by checking if __name__ == '__main__':, you ensure that the code block underneath it will only run when the Python script is directly executed, not when it is imported into another script.
