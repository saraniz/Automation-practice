import json
import datetime
import os
import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

#function to read file
# here with ensure automatically file is closed
# open() opens a file and 'r' mean it is only read mode
# return f.read() mean read entire file as a string
def read_snapshot():
    base_dir = "/home/Amiez/Desktop/automation"
    path = os.path.join(base_dir, "data/snapshot.txt")

    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""

os.makedirs("reports", exist_ok=True)
os.makedirs("logs", exist_ok=True)

snapshot = read_snapshot()
cpu = get_cpu_usage()
memory = get_memory_usage()
timestamp = datetime.datetime.now()

data = {
    "timestamp": str(timestamp),
    "raw_snapshot": snapshot
}

# a mean append file
# json.dump mean conver the data into json format and write directly into the file
with open("reports/log.jsonl", "a") as f:
    json.dump(data, f)
    f.write("\n")

#alert system
alerts = []

if cpu > 80:
    alerts.append(f"High CPU usage: {cpu}%\n")

if memory > 80:
    alerts.append(f"High Memory usage: {memory}%\n")

#search 'down' in snapshot
#snapshot.lower() convert the text into lowercase
# += append text to existing string
if "down" in snapshot.lower():
    alerts.append("Network issue detected")

alert = "\n".join(alerts)

# if alert exist write it into system.log file
# if it is not write to logs system health as OK status
if alert:
    with open("logs/system.log", "a") as f:
        f.write(f"[ALERT] {data['timestamp']}\n{alert}\n")
    print("Alert triggered")
else:
    with open("logs/system.log", "a") as f:
        f.write(f"[OK] {data['timestamp']} System normal\n")

print("Analysis completed")