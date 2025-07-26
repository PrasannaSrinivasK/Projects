import os
import subprocess
from datetime import datetime

report = []

def write_report():
    os.makedirs("results", exist_ok=True)
    with open("results/audit_report.txt", "w") as f:
        for line in report:
            f.write(line + "\n")
    print("\n✅ Report saved to results/audit_report.txt")

def header():
    report.append("========== Linux Hardening Audit Report ==========")
    report.append(f"Generated on: {datetime.now()}")
    report.append("--------------------------------------------------")

def check_os_info():
    report.append("\n[+] OS Info:")
    try:
        info = subprocess.getoutput("lsb_release -a")
        report.append(info)
    except:
        report.append(" ❌ Could not fetch OS info")

def check_ufw():
    report.append("\n[+] Firewall Status (UFW):")
    try:
        status = subprocess.getoutput("ufw status")
        if "inactive" in status:
            report.append(" ❌ UFW is installed but inactive")
        elif "Status: active" in status:
            report.append(" ✅ UFW is active")
        else:
            report.append(" ⚠️ UFW not properly configured or unknown output")
        report.append(status)
    except Exception as e:
        report.append(f" ❌ Error checking UFW: {e}")

def check_ssh_config():
    report.append("\n[+] SSH Configuration (/etc/ssh/sshd_config):")
    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            lines = f.readlines()
            found_root_login = False
            found_password_auth = False
            for line in lines:
                line = line.strip()
                if line.startswith("PermitRootLogin"):
                    report.append(f" 🔍 {line}")
                    if "yes" in line:
                        report.append(" ❌ Root login over SSH is enabled (should be disabled)")
                    else:
                        report.append(" ✅ Root login is restricted")
                    found_root_login = True
                if line.startswith("PasswordAuthentication"):
                    report.append(f" 🔍 {line}")
                    found_password_auth = True
            if not found_root_login:
                report.append(" ⚠️ 'PermitRootLogin' not explicitly set")
            if not found_password_auth:
                report.append(" ⚠️ 'PasswordAuthentication' not explicitly set")
    except Exception as e:
        report.append(f" ❌ Failed to read SSH config: {e}")

def check_file_permissions():
    report.append("\n[+] Critical File Permission Check:")
    files = {
        "/etc/passwd": "644",
        "/etc/shadow": "640"
    }
    for filepath, expected in files.items():
        try:
            stat = os.stat(filepath)
            perm = oct(stat.st_mode)[-3:]
            report.append(f" 🔍 {filepath} - Found: {perm}, Expected: {expected}")
            if perm == expected:
                report.append(" ✅ Correct permissions")
            else:
                report.append(" ❌ Permissions should be fixed")
        except Exception as e:
            report.append(f" ❌ Cannot access {filepath}: {e}")

def check_running_services():
    report.append("\n[+] Running Services (Top 5 Non-Essential):")
    try:
        output = subprocess.getoutput("systemctl list-units --type=service --state=running")
        services = [line for line in output.split('\n') if '.service' in line and not 'systemd' in line]
        report.append(" ⚠️ Services detected:")
        for line in services[:5]:
            report.append(" 🔍 " + line)
    except Exception as e:
        report.append(f" ❌ Error checking services: {e}")

def check_rootkit_signs():
    report.append("\n[+] Rootkit Sign Check (Basic):")
    suspicious_paths = ["/dev/.udev", "/dev/.init", "/dev/.tmp"]
    for path in suspicious_paths:
        if os.path.exists(path):
            report.append(f" ❌ Suspicious directory exists: {path}")
        else:
            report.append(f" ✅ No suspicious path: {path}")

def calculate_score():
    report.append("\n[+] Final Audit Score:")
    passed = sum(1 for line in report if line.startswith(" ✅"))
    total = sum(1 for line in report if line.startswith(" ✅") or line.startswith(" ❌"))
    score = int((passed / total) * 100) if total else 0
    report.append(f" ✅ Passed: {passed} / {total}")
    report.append(f" 📊 Score: {score}/100")

if __name__ == "__main__":
    header()
    check_os_info()
    check_ufw()
    check_ssh_config()
    check_file_permissions()
    check_running_services()
    check_rootkit_signs()
    calculate_score()
    write_report()
