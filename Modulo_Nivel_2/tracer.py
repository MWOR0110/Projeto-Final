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

# Function to check for proxy settings
def check_proxy_settings():
    proxy_info = ""
    
    if os.name == 'posix':  # Linux
        proxy_info = run_command("env | grep -i proxy")
    elif os.name == 'nt':  # Windows
        proxy_info = run_command("reg query \"HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" | findstr Proxy")
    
    if proxy_info:
        return "Proxy detected:\n" + proxy_info
    else:
        return "No proxy detected."

# Function to check for sniffers (basic check for suspicious network interfaces in promiscuous mode)
def check_sniffers():
    sniffer_info = ""
    
    if os.name == 'posix':  # Linux
        sniffer_info = run_command("ip link | grep PROMISC")
    elif os.name == 'nt':  # Windows
        sniffer_info = run_command("netsh interface show interface")
    
    if "PROMISC" in sniffer_info or "monitor" in sniffer_info:
        return "Suspicious interface detected in promiscuous mode:\n" + sniffer_info
    else:
        return "No sniffers detected in promiscuous mode."

# Function to log the connection route to Google
def log_google_trace():
    log_file = "google_connection_log.txt"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "w") as log:
        log.write(f"Google Connection Trace Log - {current_time}\n")
        log.write("="*50 + "\n\n")

        # Ping Google to check response time
        if os.name == 'posix':  # Linux
            log.write("Pinging google.com (Linux):\n")
            ping_output = run_command("ping -c 4 google.com")
            log.write("Ping Output:\n" + ping_output + "\n")

            # Traceroute to Google
            log.write("Tracing route to google.com (Linux - traceroute):\n")
            trace_output = run_command("traceroute google.com")
            log.write("Traceroute Output:\n" + trace_output + "\n")

        elif os.name == 'nt':  # Windows
            log.write("Pinging google.com (Windows):\n")
            ping_output = run_command("ping -n 4 google.com")
            log.write("Ping Output:\n" + ping_output + "\n")

            # Tracert to Google
            log.write("Tracing route to google.com (Windows - tracert):\n")
            trace_output = run_command("tracert google.com")
            log.write("Tracert Output:\n" + trace_output + "\n")

        # Check for proxy settings
        log.write("\nChecking for Proxy Settings:\n")
        proxy_info = check_proxy_settings()
        log.write(proxy_info + "\n")

        # Check for sniffers or promiscuous mode interfaces
        log.write("\nChecking for Sniffers or Suspicious Interfaces:\n")
        sniffer_info = check_sniffers()
        log.write(sniffer_info + "\n")

        log.write("="*50 + "\n")
    
    print(f"Google connection trace logged to {log_file}")

if __name__ == "__main__":
    log_google_trace()
