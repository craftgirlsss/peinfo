import subprocess
import os

def clear_terminal():
    if os.name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)


def get_latency(target_host):
    result = subprocess.run(["nmap", "-p", "80", "-T4", "-v", target_host], capture_output=True, text=True)
    output = result.stdout

    # Parse the output to extract the RTT
    for line in output.splitlines():
        if "RTT" in line:
            rtt_str = line.split()[3]
            rtt_ms = float(rtt_str[:-2])  # Remove the 'ms' suffix
            print(rtt_ms)
            return rtt_ms

    return None