import re
slb_server_name1 = 'TongHuaShun'       #定义real server
slb_server_ip1 = '10.168.98.96'        #定义real server的IP

slb_server_name2 = 'TongHuaShun2'
slb_server_ip2 = '10.168.98.97'

slb_server_name3 = ''
slb_server_ip3 = ''

slb_server_name4 = ''
slb_server_ip4 = ''

slb_server_name5 = ''
slb_server_ip5 = ''

protocal = 'tcp'                       #定义使用的协议
slb_virtual_server = '162.14.141.10'   #定义所需映射的公网IP
port1 = '1001'                         #定义real server的端口
port2 = '1002'
port3 = ''
port4 = ''
port5 = ''

list_x = [1, 2, 3, 4, 5, 6]

slb_server_ip_list1 = []
slb_server_ip_list2 = []
slb_server_ip_list3 = []
slb_server_ip_list4 = []
slb_server_ip_list5 = []

slb_server_nameip1 = []
slb_server_nameip2 = []
slb_server_nameip3 = []
slb_server_nameip4 = []
slb_server_nameip5 = []

slb_service_group1 = []
slb_service_group2 = []
slb_service_group3 = []

#配置slb server
for a in list_x:
    if slb_server_ip1 != '' and a == 1:
        slb_server_ip_list1 = re.split('\.', slb_server_ip1)
        slb_server_nameip1 = '(' + slb_server_ip_list1[2] + '.' + slb_server_ip_list1[3] + ')'
        print('slb server ', slb_server_name1+slb_server_nameip1, slb_server_ip1)
        if port1 != '':
            print('  ', 'port ', port1, protocal)
        if port2 != '':
            print('  ', 'port ', port2, protocal)
        if port3 != '':
            print('  ', 'port ', port3, protocal)
        if port4 != '':
            print('  ', 'port ', port4, protocal)
        if port5 != '':
            print('  ', 'port ', port5, protocal)

    elif slb_server_ip2 != '' and a == 2:
        slb_server_ip_list2 = re.split('\.', slb_server_ip2)
        slb_server_nameip2 = '(' + slb_server_ip_list2[2] + '.' + slb_server_ip_list2[3] + ')'
        print('slb server ', slb_server_name2 + slb_server_nameip2, slb_server_ip2)
        if port1 != '':
            print('  ', 'port ', port1, protocal)
        if port2 != '':
            print('  ', 'port ', port2, protocal)
        if port3 != '':
            print('  ', 'port ', port3, protocal)
        if port4 != '':
            print('  ', 'port ', port4, protocal)
        if port5 != '':
            print('  ', 'port ', port5, protocal)
    elif slb_server_ip3 != '' and a == 3:
        slb_server_ip_list3 = re.split('\.', slb_server_ip3)
        slb_server_nameip3 = '(' + slb_server_ip_list3[2] + '.' + slb_server_ip_list3[3] + ')'
        print('slb server ', slb_server_name3 + slb_server_nameip3, slb_server_ip3)
        if port1 != '':
            print('  ', 'port ', port1, protocal)
        if port2 != '':
            print('  ', 'port ', port2, protocal)
        if port3 != '':
            print('  ', 'port ', port3, protocal)
        if port4 != '':
            print('  ', 'port ', port4, protocal)
        if port5 != '':
            print('  ', 'port ', port5, protocal)
    elif slb_server_ip4 != '' and a == 4:
        slb_server_ip_list4 = re.split('\.', slb_server_ip4)
        slb_server_nameip4 = '(' + slb_server_ip_list4[2] + '.' + slb_server_ip_list4[3] + ')'
        print('slb server ', slb_server_name4 + slb_server_nameip4, slb_server_ip4)
        if port1 != '':
            print('  ', 'port ', port1, protocal)
        if port2 != '':
            print('  ', 'port ', port2, protocal)
        if port3 != '':
            print('  ', 'port ', port3, protocal)
        if port4 != '':
            print('  ', 'port ', port4, protocal)
        if port5 != '':
            print('  ', 'port ', port5, protocal)
    elif slb_server_ip5 != '' and a == 5:
        slb_server_ip_list5 = re.split('\.', slb_server_ip5)
        slb_server_nameip5 = '(' + slb_server_ip_list5[2] + '.' + slb_server_ip_list5[3] + ')'
        print('slb server ', slb_server_name5 + slb_server_nameip5, slb_server_ip5)
        if port1 != '':
            print('  ', 'port ', port1, protocal)
        if port2 != '':
            print('  ', 'port ', port2, protocal)
        if port3 != '':
            print('  ', 'port ', port3, protocal)
        if port4 != '':
            print('  ', 'port ', port4, protocal)
        if port5 != '':
            print('  ', 'port ', port5, protocal)
    else:
        break

#配置slb service-group
if port1 != '':
    slb_service_group1 = slb_server_name1 + '_Server' + '(' + port1 + ')'
    print('slb service-group ', slb_service_group1, protocal)
    if slb_server_ip1 != '':
        print('  ', 'member ', slb_server_name1 + slb_server_nameip1, port1)
    if slb_server_ip2 != '':
        print('  ', 'member ', slb_server_name2 + slb_server_nameip2, port1)
    if slb_server_ip3 != '':
        print('  ', 'member ', slb_server_name3 + slb_server_nameip3, port1)
    if slb_server_ip4 != '':
        print('  ', 'member ', slb_server_name4 + slb_server_nameip4, port1)
    if slb_server_ip5 != '':
        print('  ', 'member ', slb_server_name5 + slb_server_nameip5, port1)

if port2 != '':
    slb_service_group2 = slb_server_name1 + '_Server' + '(' + port2 + ')'
    print('slb service-group ', slb_service_group2, protocal)
    if slb_server_ip1 != '':
        print('  ', 'member ', slb_server_name1 + slb_server_nameip1, port2)
    if slb_server_ip2 != '':
        print('  ', 'member ', slb_server_name2 + slb_server_nameip2, port2)
    if slb_server_ip3 != '':
        print('  ', 'member ', slb_server_name3 + slb_server_nameip3, port2)
    if slb_server_ip4 != '':
        print('  ', 'member ', slb_server_name4 + slb_server_nameip4, port2)
    if slb_server_ip5 != '':
        print('  ', 'member ', slb_server_name5 + slb_server_nameip5, port2)

if port3 != '':
    slb_service_group3 = slb_server_name1 + '_Server' + '(' + port3 + ')'
    print('slb service-group ', slb_service_group3, protocal)
    if slb_server_ip1 != '':
        print('  ', 'member ', slb_server_name1 + slb_server_nameip1, port3)
    if slb_server_ip2 != '':
        print('  ', 'member ', slb_server_name2 + slb_server_nameip2, port3)
    if slb_server_ip3 != '':
        print('  ', 'member ', slb_server_name3 + slb_server_nameip3, port3)
    if slb_server_ip4 != '':
        print('  ', 'member ', slb_server_name4 + slb_server_nameip4, port3)
    if slb_server_ip5 != '':
        print('  ', 'member ', slb_server_name5 + slb_server_nameip5, port3)
#配置slb virtual-server
if port1 != '':
    print('slb virtual-server ', slb_virtual_server, slb_virtual_server)
    print('  ', 'port', port1, protocal)
    print('    ', 'name', slb_service_group1)
    print('    ', 'ha-conn-mirror')
    print('    ', 'service-group', slb_service_group1)
    print('    ', 'use-rcv-hop-for-resp')
    if port2 != '':
        print('  ', 'port', port2, protocal)
        print('    ', 'name', slb_service_group2)
        print('    ', 'ha-conn-mirror')
        print('    ', 'service-group', slb_service_group2)
        print('    ', 'use-rcv-hop-for-resp')
    if port3 != '':
        print('  ', 'port', port3, protocal)
        print('    ', 'name', slb_service_group3)
        print('    ', 'ha-conn-mirror')
        print('    ', 'service-group', slb_service_group3)
        print('    ', 'use-rcv-hop-for-resp')





