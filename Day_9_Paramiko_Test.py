import paramiko
import time
import re


def ssh_show(ip, username, password, cmd_show, port=22):
    x = []
    for cmd_str in cmd_show:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(cmd_str)
        x.append(stdout.read().decode())
        time.sleep(3)
    return x


def ssh_config(ip, username, password, cmd_exec, port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    ssh_shell = ssh.invoke_shell()
    for cmd in cmd_exec:
        ssh_shell.send(cmd)
        time.sleep(2)

        print(str(ssh_shell.recv(65535).decode()))


def ssh_get_gateway(ip, username, password, cmd, port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    return stdout.read().decode()


if __name__ == '__main__':
    ssh_info = {'10.196.100.199':
                    {'username': 'wuzp',
                     'password': 'Systec123',
                     'cmd_show': ['show ip int b', 'show vlan b'],
                     'cmd_exec': ['conf t\n', 'vlan 26\n'],
                     'port': 22}
                }
    get_gateway = {'192.168.213.128':
                       {'username': 'root',
                        'password': 'admin123',
                        'cmd': 'route -n'
                        }
                   }

    # for ip_add, info in ssh_info.items():
    #     result = ssh_show(ip_add, info.get('username'), info.get('password'), info.get('cmd_show'))
    #     ssh_config(ip_add, info.get('username'), info.get('password'), info.get('cmd_exec'))
    #
    # for str_info in result:
    #     print(str(str_info))

    for k, v in get_gateway.items():
        result_get_gateway = ssh_get_gateway(k, v.get('username'), v.get('password'), v.get('cmd'))
        for i in re.split('\n', result_get_gateway)[2:]:
            split_result = re.match(r'\d+\.\d+\.\d+\.\d+\s+(\d+\.\d+\.\d+\.\d+)\s+\d+\.\d+\.\d+\.\d+\s+UG.*', i)
            if split_result:
                print('网关为：')
                print(split_result.group(1))
