# SentinelEye
SentinelEye: Real-Time Directory Integrity Monitor
SentinelEye is a lightweight, Python-based security utility designed to monitor file system activities in real-time. Whether you are tracking unauthorized access, debugging software file changes, or performing basic malware analysis, SentinelEye provides instant visibility into every action occurring within a specified directory.

🚀 Features
Comprehensive Event Tracking: Monitors file creation, modification, deletion, moving, and access events.

Deep Inspection: Detects when files are opened or closed, helping identify which processes are interacting with your data.

Dynamic Path Selection: Supports monitoring of any directory via command-line arguments.

Lightweight & Fast: Built using the watchdog library for high-performance asynchronous monitoring.

Cross-Platform: Works on Windows, macOS, and Linux (with enhanced event support on Linux).

🛠️ Installation
Clone the Repository:

Bash
git clone https://github.com/prajapatiHardik2008/SentinelEye.git
cd SentinelEye
Install Dependencies:

Bash
pip install watchdog
💻 Usage
Run the script by providing the path to the directory you wish to monitor. If no path is provided, it defaults to the current directory.

Bash
python sentineleye.py /path/to/your/folder
Example Output:
Plaintext
[+] Monitoring started on: /home/user/documents...
[+] File created on /home/user/documents/new_log.txt
[!] Modified: /home/user/documents/config.yaml
[-] File Deleted from /home/user/documents/temp.tmp
[+] File opened! /home/user/documents/notes.txt
📂 Technical Overview
The core of SentinelEye utilizes the Observer Pattern. The Observer class runs in a background thread, listening for signals from the Operating System's file system API. When an event occurs, it dispatches a signal to the custom MyHandler class, which processes and logs the event type and source path.

🛡️ Use Cases
Intrusion Detection: Monitor sensitive system folders for unexpected changes.

Development: Track which files your build system or application is modifying in real-time.

Forensics: Log file access and movement during security audits.

📄 License
Distributed under the MIT License. See LICENSE for more information.
