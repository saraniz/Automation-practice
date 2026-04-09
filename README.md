# Automation Practice

Simple Linux automation project that captures system information with Bash and analyzes it with Python.

## Environment

This project is developed in VS Code connected to an Ubuntu VM using SSH (Remote - SSH).

## Project Structure

```text
automation/
├── bash/
│   └── system_info.sh
├── data/
│   └── snapshot.txt
├── python/
│   ├── monitor.py
│   ├── logs/
│   └── reports/
│       └── log.jsonl
└── README.md
```

## What It Does

1. `bash/system_info.sh`
- Creates a system snapshot in `data/snapshot.txt`.
- Collects uptime, memory, disk usage, top memory-heavy processes, and a basic network check.

2. `python/monitor.py`
- Reads `data/snapshot.txt`.
- Collects live CPU and memory percentage using `psutil`.
- Appends JSON lines to `python/reports/log.jsonl` (when run from `python/`).
- Writes alerts or normal status entries to `python/logs/system.log`.

## Requirements

- Ubuntu/Linux
- Python 3
- `pip`
- Python package: `psutil`

Install dependency:

```bash
pip install psutil
```

## How To Run

From the project root:

```bash
cd /home/Amiez/Desktop/automation
bash bash/system_info.sh
cd python
python3 monitor.py
```

## Output Files

- `data/snapshot.txt`: raw Bash snapshot
- `python/reports/log.jsonl`: structured JSON entries
- `python/logs/system.log`: status and alert log

## Optional: Cron Automation

If you want to run this periodically with cron, add entries with:

```bash
crontab -e
```

Example (every 5 minutes):

```cron
*/5 * * * * /bin/bash /home/Amiez/Desktop/automation/bash/system_info.sh
*/5 * * * * cd /home/Amiez/Desktop/automation/python && /usr/bin/python3 monitor.py
```

## Notes

- `monitor.py` writes to relative paths (`logs/` and `reports/`), so run it from the `python/` directory for the expected output locations.