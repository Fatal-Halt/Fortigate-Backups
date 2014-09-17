import subprocess
from datetime import datetime

#Each set of (,) represents a firewall, add its common name and its IP.
firewalls = [('<FirewallName>','<FirewallIP>'),('<FirewallName2>','<FirewallIP2>')]#Add more as needed

timestamp = datetime.now().strftime('%m-%d-%Y %H-%M-%S')

for loc,ip in firewalls:
    process = subprocess.Popen(['pscp.exe', '-P', '<PORT>', '-i', '<PRIVATE KEY>', '<USERNAME>@'+ip+':fgt-config', 'c:\config\\'+loc+'\\'+timestamp+'.conf'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(b'<PASSWORD>\r\n')
    print(process.communicate())


