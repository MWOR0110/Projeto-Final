import os
import subprocess
from datetime import datetime

# Function to run shell command and return the output
def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return result.stderr
    except Exception as e:
        return str(e)

# Function to log network policies
def log_wifi_network_policies():
    log_file = "wifi_network_policies_log.txt"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "w") as log:
        log.write(f"Wi-Fi Network Policies Log - {current_time}\n")
        log.write("="*50 + "\n\n")

        # Linux network policies
        if os.name == 'posix':
            log.write("Fetching network policies (Linux):\n")

            # Get Wi-Fi status
            wifi_status = run_command("nmcli -t -f active,ssid dev wifi")
            log.write("Active Wi-Fi SSID:\n" + wifi_status + "\n")

            # Get routing table
            routing_table = run_command("ip route")
            log.write("Routing Table:\n" + routing_table + "\n")

            # Get firewall policies (iptables)
            firewall_policies = run_command("sudo iptables -L")
            log.write("Firewall Policies (iptables):\n" + firewall_policies + "\n")

            # Get DNS settings
            dns_settings = run_command("systemd-resolve --status | grep 'DNS Servers'")
            log.write("DNS Servers:\n" + dns_settings + "\n")

        # Windows network policies
        elif os.name == 'nt':
            log.write("Fetching network policies (Windows):\n")

            # Get Wi-Fi status
            wifi_status = run_command("netsh wlan show interfaces")
            log.write("Wi-Fi Status:\n" + wifi_status + "\n")

            # Get routing table
            routing_table = run_command("route print")
            log.write("Routing Table:\n" + routing_table + "\n")

            # Get firewall policies
            firewall_policies = run_command("netsh advfirewall show allprofiles")
            log.write("Firewall Policies (netsh firewall):\n" + firewall_policies + "\n")

            # Get DNS settings
            dns_settings = run_command("ipconfig /all | findstr /C:\"DNS Servers\"")
            log.write("DNS Servers:\n" + dns_settings + "\n")

        log.write("="*50 + "\n")
    
    print(f"Wi-Fi network policies logged to {log_file}")

if __name__ == "__main__":
    log_wifi_network_policies()
