import subprocess

data=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifiname=[line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifiname:
    result=subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi, 'key=clear']).decode('utf-8').split('\n')
    result=[line.split(':')[1][1:-1] for line in result if "Key Content" in line]
    try:
        print(f'WIFINAME:-  {wifi}  PASSWORD:-  {result[0]}')
    except IndexError:
        print(f'WIFINAME:-  {wifi}  PASSWORD:-  Could not read')