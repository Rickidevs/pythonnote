import socket

ip = input("Enter the IP address you want to scan: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    
    if result == 0:
        print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")
    
    sock.close()
