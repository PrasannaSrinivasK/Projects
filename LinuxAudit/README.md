## Linux Hardening Audit Tool

The Linux Hardening Audit Tool is a command-line utility written in Python to evaluate the security posture of a Linux system. It performs common audit checks like firewall status, SSH configuration, file permissions, suspicious directories, and service listing, then generates a report with a final hardening score.


## Features

- Detects if UFW firewall is active
- Checks SSH configuration (PermitRootLogin, PasswordAuthentication)
- Verifies permissions of critical system files (`/etc/passwd`, `/etc/shadow`)
- Identifies running services (top 5 non-essential)
- Scans for known suspicious directories (basic rootkit signs)
- Calculates final audit score out of 100
- Saves a full report in results/audit_report.txt


## Technologies Used

| Tool/Library                  |    Purpose                                  |
|-------------------------------|---------------------------------------------|
| Python 3.13.5                 |    Core programming                         |
| subprocess / os               |    System command execution and file checks |
| datetime                      |    Timestamped audit logs                   |
| systemctl / ufw / sshd_config |    Core Linux system config sources         |


## Folder Structure

LinuxAudit/
├── linux_audit.py
├── results/
│ └── audit_report.txt
├── screenshots/
└── README.md


## How to Run

1. Make sure Python 3 is installed (preferably 3.10+)

2. Run the script:

python3 linux_audit.py

View the output:

cat results/audit_report.txt


## Sample Checks Performed
Firewall: Whether UFW is active or not

SSH Config: Is root login allowed? Is password auth enabled?

Permissions: Should be 644 for /etc/passwd, 640 for /etc/shadow

Services: Lists 5 non-essential running services

Rootkit Paths: Checks for known suspicious folders

Scoring: Displays passed/total and a score out of 100


## Output Example
========== Linux Hardening Audit Report ==========
Generated on: 2025-06-26 14:31:00.923401

[+] Firewall Status (UFW):
 ❌ UFW is installed but inactive

[+] SSH Configuration (/etc/ssh/sshd_config):
 🔍 PermitRootLogin yes
 ❌ Root login over SSH is enabled (should be disabled)

[+] Critical File Permission Check:
 🔍 /etc/passwd - Found: 644, Expected: 644
 ✅ Correct permissions

[+] Final Audit Score:
 ✅ Passed: 5 / 8
 📊 Score: 62/100


## Disclaimer
This tool is intended for educational and internal audit purposes only. It should not be used on systems you do not own or have permission to audit.


## Author
Created as part of a cybersecurity internship project submission.
