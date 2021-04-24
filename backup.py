import uuid # Для виводу MAC - адресу
from datetime import datetime
import os

#вивод актуальної дати
def now_date():
    now = datetime.now()
    datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    return now

#Виводить MAC-адрес
def mac_address():
    # print ("The MAC address in formatted way is : ", end="mac")
    mac = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))
    return mac

# Збор інформації про систему
def info_machines():
    info_machines = {
        'mac_address' : mac_address(),
        'sysname' : os.uname().sysname,
        'nodename' : os.uname().nodename,
        'releace' : os.uname().release,
        'version' : os.uname().version
    }

    save_info(info_machines)

    return info_machines

def save_info(info_machines):
    file_info = open("info_machines.txt", mode='a', encoding='utf-8')
    file_info.write(mac_address() + '\t' + str(now_date()) + '\n')

    for i,n in info_machines.items():    
        file_info.write('\t' + i + ': ' + n + '\n')

    file_info.close()


info_machines()