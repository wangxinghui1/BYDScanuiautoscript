# -*- coding: utf-8 -*-
import os
import subprocess
import time
import psutil
from threading import Thread
class Processkill:
    def __init__(self):
        pass
    def get_process_by_name(self, process_name):
        processes = list(psutil.process_iter())
        for proc in processes:
            name = proc.name()
            brt= name.lower() == process_name.lower()
            print(name)
            if brt:
              return True
        return False
    def run_testset(self):
        os.system('python D:\\TestAutoProject\\Byd\\venv\\Function_module\\applicationStaticDR.py')
obj=Processkill()
while True:
    time.sleep(1)
    if obj.get_process_by_name('LiBOL.exe'):
        continue
    else:
        print('杀死正在运行的测试脚本')
        process_name = "applicationStaticDR.py"
        command = f'taskkill /F /IM python.exe /FI "WINDOWTITLE eq {process_name}"'
        subprocess.run(command, shell=True)
        #重新开启测试脚本
        print('开始执行applicationStaticDR脚本')
        thread = Thread(target=obj.run_testset)
        thread.start()
        time.sleep(2)