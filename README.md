https://www.youtube.com/watch?v=sw7_aEafJJg - How to scan for open ports in python | Kali Hacking




This Python script is designed to perform port scanning on a specified target IP address. It utilizes the socket module for network communication to check for open ports within the given IP address range.


-


Setting Target IP: Modify the target_ip variable in the script to the desired IP address that you want to scan for open po
target_ip = '192.168.1.1'  # Replace with your target IP address


-


Adjusting Timeout: The script utilizes a timeout of 0.1 seconds for each port connection attempt. You can adjust this timeout value within the check_port function as needed.
sock.settimeout(0.1)  # Adjust the timeout as required


-


Running the Script:
python port_scanner.py


-



check_port(target_ip, port): Checks if a specific port is open on the given target IP address. It attempts to establish a TCP connection and prints a message if the port is open.

scan_ports(target_ip): Initiates a full port scan on the specified target IP address, checking for open ports within the range of 1 to 65535.





-




Port scanning may be subject to legal restrictions and could be considered intrusive or malicious if performed without proper authorization. 
Ensure you have appropriate permissions before scanning any IP addresses that do not belong to you or are not under your authority.
