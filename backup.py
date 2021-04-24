<<<<<<< Updated upstream
bender = 1
=======
from function import *

# вивод актуальної дати
# now_date()

# Виводить MAC-адрес
# mac_address()

# інфа про систему
# info_machines()

# Відкриття(створення) файла
file_info = open("info_machines.txt", mode='a', encoding='utf-8')

# Записує у файл дані із змінної OS та з функції mac_address() + now_date()
file_info.write('\n' + str(mac_address()) + '\t' + str(now_date()) + '\n' + '\t' + str(info_machines()))

#with file_info as file:
#    for item in info_machines:
#        print(item, file=file)

#   print(info_machines, file=file)

#for item in info_machines:
#    file_info.write("%s\n" % item)

file_info.close()
>>>>>>> Stashed changes
