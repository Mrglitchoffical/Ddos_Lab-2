#!/bin/bash
watch -n 1 'echo -e "CPU:"; top -bn1 | grep "Cpu"; echo -e "\nConnections:"; netstat -tnp | grep EST | wc -l'
