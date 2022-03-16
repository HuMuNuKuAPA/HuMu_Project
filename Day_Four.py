import os
import re
ifconfig_result = 'ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST> mtu 1500 \
              inet 172.16.66.166 netmask 255.255.255.0  broadcast 172.16.66.255 \
              inet6 fe80::250:56ff:feab:59bd prefixlen 64 scopeid 0x20<link> \
              ether 00:50:56:ab:59:bd txqueuelen 1000 (Ethernet) \
              RX packets 174598769 bytes 1795658527217 (1.6 TiB) \
              RX errors 1 dropped 24662 overruns 0 frame 0 \
              TX packets 51706604 bytes 41788673420 (38.9 GiB) \
              TX errors 0 dropped 0 overruns 0 carrier 0 collisions 0'

ipv4_add = re.findall(r'\b(?:25[0-4]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-4]|2[0-4]\d|[01]?\d\d?)\b',
                      ifconfig_result, re.S)
netmask = re.findall(r'(?:255)(?:\.(?:25[245]|24[08]|224|192|128|0)){3}', ifconfig_result, re.S)
broadcast = re.findall(r'\b(?:25[0-4]\.|2[0-4]\d\.|[01]?\d\d?\.){3}255\b', ifconfig_result, re.S)
mac_address = re.findall(r'(?:[0-9a-f][0-9a-f]:){5}[0-9a-f][0-9a-f]', ifconfig_result)
ipv4_gw = '10.66.1.254'

ping_result = os.popen('ping ' + ipv4_gw + ' -n 1').read()

ipv4_add_str = 'ipv4_add'
netmask_str = 'netmask'
broadcast_str = 'broadcast'
mac_address_str = 'mac_address'

print(f'{ipv4_add_str:<12}:', ipv4_add[0])
print(f'{netmask_str:<12}:', netmask[0])
print(f'{broadcast_str:<12}:', broadcast[0])
print(f'{mac_address_str:<12}:', mac_address[0])
ping_result_re = re.findall(r'时间=\d+ms', ping_result)

if ping_result_re:
    print('\n', '网关可达!')
else:
    print('\n', '网关不可达')
