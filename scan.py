import socket
import sys

class Scanner:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def scan(self):
        try:
            ipaddr = socket.gethostbyname_ex(self.host)
            hostname = ipaddr[0]
            ip_addresses = ipaddr[2]

            for ip in ip_addresses:
                result = self.socket.connect_ex((ip, self.port))
                if result == 0:
                    print(f"[+] {self.port} open on {ip} ({hostname})")
                else:
                    print(f"[-] {self.port} false on {ip} ({hostname})")
        except socket.gaierror as e:
            print(f"Error resolving: {e}")
            return

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            port = int(sys.argv[2])
        else:
            print("Port number not provided.")
            sys.exit(1)

        hostname = socket.gethostname()
        print(f"Scanning on: {hostname}")

        scanner = Scanner(host, port)
        scanner.scan()
    else:
        print("address not provided.")
