import subprocess
import os 
filename = 'T_bot.py'
os.chdir(r'C:\Users\TelegramBot\test_bot-main')
while True:
    p=subprocess.Popen('python '+filename, shell = True).wait()
    if p!=0:
        continue
    else:
        break
