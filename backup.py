from datetime import datetime
import os
import sys
import uuid # Для виводу MAC - адресу

#вивод актуальної дати
def now_date():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    return now


#Виводить MAC-адрес
def mac_address():
    print ("The MAC address in formatted way is : ", end="mac")
    mac = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))
    return mac

mac = mac_address()

# інфа про систему
OS = os.uname()
info_machines = {
    'sysname' : OS.sysname,
    'nodename' : OS.nodename,
    'releace' : OS.release,
    'version' : OS.version
}


file_info = open("info_machines.txt", mode='a', encoding='utf-8')

file_info.write('\n' + str(mac) + '\t' + str(now_date()) + '\n' + '\t' + str(info_machines))

#with file_info as file:
#    for item in info_machines:
#        print(item, file=file)

#   print(info_machines, file=file)

#for item in info_machines:
#    file_info.write("%s\n" % item)

file_info.close()

if OS.sysname == 'Linux' :
    print('linux')
    print(os.uname())
else:
    print('Ти рак на вінді')