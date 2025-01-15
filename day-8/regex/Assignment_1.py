# Create a program that:
# Validates a user-provided IPv4 address.
import re
def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    # pattern = r'/^([0-9]+(\.|$)){4}/'
    if re.match(pattern, ip):
        parts = ip.split('.')
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False

ip_input = input("Enter an ipv4 address: ")
if is_valid_ip(ip_input):
    print(f"the ipv4 address is valid.")
else:
    print(f"the ipv4 address is invalid.")