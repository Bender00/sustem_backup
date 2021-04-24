#вивод актуальної дати
def now_date():
    from datetime import datetime


    now = datetime.now()
    datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
    return now

#Виводить MAC-адрес
def mac_address():
    import uuid # Для виводу MAC - адресу

    # print ("The MAC address in formatted way is : ", end="mac")
    mac = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
    for ele in range(0,8*6,8)][::-1]))
    return mac

# Збор інформації про систему
def info_machines():
    import os

    
    
    info_machines = {
        'sysname' : os.uname().sysname,
        'nodename' : os.uname().nodename,
        'releace' : os.uname().release,
        'version' : os.uname().version
    }
    for i,n in info_machines.items():
        print(i,n)
        

    return info_machines, i,n