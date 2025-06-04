#!/bin/bash
echo "[!] Killing nginx, clearing logs, restarting firewall..."
sudo systemctl restart nginx
sudo ufw reload
sudo truncate -s 0 /var/log/nginx/access.log
