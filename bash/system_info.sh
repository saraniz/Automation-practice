#!/bin/bash

BASE="/home/Amiez/Desktop/automation"

mkdir -p "$BASE/data"

echo "System Metric Snapshot - $(date)" > "$BASE/data/snapshot.txt"

echo "Uptime:" >> "$BASE/data/snapshot.txt"
uptime >> "$BASE/data/snapshot.txt"

#h mean human-readable format
echo "Memory:" >> "$BASE/data/snapshot.txt"
free -h >> "$BASE/data/snapshot.txt"

echo "Disk Usage:" >> "$BASE/data/snapshot.txt"
df -h >> "$BASE/data/snapshot.txt"

#ps aux lists all processes, --sort=-%mem sorts by memory usage, head -5 shows top 5
echo "Top Processes:" >> "$BASE/data/snapshot.txt"
ps aux --sort=-%mem | head -5 >> "$BASE/data/snapshot.txt"

echo "Network Check:" >> "$BASE/data/snapshot.txt"
# Label for network connectivity check

ping -c 1 google.com > /dev/null \
&& echo "Internet OK" >> "$BASE/data/snapshot.txt" \
|| echo "Internet DOWN" >> "$BASE/data/snapshot.txt" # Sends 1 ping request to google.com
# > /dev/null hides ping output (we only care about success/failure)
# && means: if ping succeeds → print "Internet OK"
# || means: if ping fails → print "Internet DOWN"