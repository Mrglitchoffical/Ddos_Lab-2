git clone https://github.com/Mrglitchoffical/Ddos_Lab-2.git

cd Ddos_Lab-2

apt install python -y

pip install -r requirements.txt

## Attacks

### TCP Flood
```bash
cd attack
python3 tcp_flood.py 192.168.0.100 80 200 0.01
