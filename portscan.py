import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def main():
    target = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    print(f"Scanning {target}...")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port+1):
            executor.submit(scan_port, target, port)

    print("Scan complete")

if __name__ == "__main__":
    main()
