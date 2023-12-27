import socket  # Importing the socket module for network communication

target_ip = '192.168.1.1'  # Define the target IP address

# Function to check if a specific port is open on the target IP
def check_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a TCP socket
        sock.settimeout(0.1)  # Setting a timeout for the connection attempt (adjustable)
        result = sock.connect_ex((target_ip, port))  # Attempting to connect to the target IP and port
        if result == 0:  # If the result is 0, the connection was successful
            print(f"Port {port} is open")  # Print that the port is open
        sock.close()  # Close the socket connection
    except socket.error:  # Handling socket errors
        pass

# Function to scan ports on the target IP
def scan_ports(target_ip):
    print(f"Scanning ports for {target_ip}...")  # Printing a message indicating the start of the scan
    for port in range(1, 65536):  # Iterating through ports from 1 to 65535
        check_port(target_ip, port)  # Checking each port using the check_port function

# Initiating the port scanning process for the specified target IP
scan_ports(target_ip)
