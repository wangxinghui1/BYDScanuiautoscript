import subprocess
import os
import uiautomation
from Bydlogger import get_logger
from logCounts import get_logCounts
logger=get_logger('bydconnect','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\bydconnect.log')
def connectApp():
    try:
        # connect byd
        # close bydsoftware
        os.system('taskkill /F /IM LiBOL.exe')
        # open bydsoftware
        subprocess.Popen('D:\\TestAutoProject\\Byd\\venv\\simdeploy\\simdeploy\\LiBOL.exe')
        # Determine whether to enter the login page
        # loginName = uiautomation.ButtonControl(Name='登 陆')
        if uiautomation.ButtonControl(Name='登 陆').Exists():
            print('应用程序打开成功:',get_logCounts('connCountsuccess'),'次')
            logger.info('应用程序打开成功日志:%s次',get_logCounts('connCountlogsuccess'))
        else:
            raise Exception('应用程序打开失败')
    except Exception as e:
        print('未能进入登陆页面，应用程序打开失败:', get_logCounts('connCountfail'), '次')
        logger.info('应用程序打开失败日志:%s次', get_logCounts('connCountlogfail'))
for i in range(1):
    connectApp()

