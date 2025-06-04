#!/bin/bash
echo "🔰 DDoS Lab Ultimate 🔰"
echo "1. Run Layer 7 HTTP Flood"
echo "2. Run Layer 4 Socket Flood"
echo "3. Monitor Panel (CPU + Conn)"
echo "4. Emergency Recovery"
read -p "Choose Option: " opt

case $opt in
  1) python3 attacks/layer7_flood.py ;;
  2) python3 attacks/layer4_socket.py ;;
  3) bash monitor/monitor.sh ;;
  4) bash monitor/recovery.sh ;;
  *) echo "❌ Invalid";;
esac
