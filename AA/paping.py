import socket
import time
import sys

def tcp_ping(target_ip, target_port, interval=0.5, timeout=1): 
    while True:
        try:
            start_time = time.time()
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(timeout)
            client_socket.connect((target_ip, target_port))
            client_socket.close()
            end_time = time.time()
            response_time = (end_time - start_time) * 1000
            print(f"\x1b[38;5;160mConnected to \x1b[38;5;255m{target_ip}\033[97m: \x1b[38;5;160mtime=\x1b[38;5;255m{response_time:.2f}ms \x1b[38;5;160mprotocol=\x1b[38;5;255mTCP \x1b[38;5;160mport=\x1b[38;5;255m{target_port}")
        except Exception as e:
            print("\x1b[38;5;160mConnection timed out")

        time.sleep(interval)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 paping.py ip port")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    interval = 0.5
    timeout = 0.7  # Adjust this value as needed
    tcp_ping(target_ip, target_port, interval, timeout)
    # Paping by D4XG
