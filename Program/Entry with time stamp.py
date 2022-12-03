import os
import datetime
os.chdir("/Users/iarv/This PC/Code Resource/My Codes/Python/Program")

# f = open('diary.txt', 'a')
# date = str(datetime.datetime.now())
# f.write('\n')
# f.write(f'{date}\n')
# f.writelines(input())
# f.close()

with open('diary.txt', 'a') as f:
    edit_time = str(datetime.datetime.now())
    f.write('\n')
    f.write(f'{edit_time}\n')
    f.writelines(input())
