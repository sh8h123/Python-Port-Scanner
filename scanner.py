import socket
target = input("Enter an IP address: ")
ports = [21, 22, 23, 53, 80, 443, 8080]
print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: closed")

    sock.close()

print("\nScan finished.")

