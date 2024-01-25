import time

import pandas as pd
import uiautomation
from Bydlogger import get_logger
from logCounts import get_logCounts
logger=get_logger('userlogin','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\userlogin.log')
class userLogin:
    def __init__(self):
        self.username=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page.widget_loginBack.widget_loginCenter.widget.widget_2.lineEdit_loginAccount')
        self.password=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page.widget_loginBack.widget_loginCenter.widget.widget_3.lineEdit_loginPassword')
        self.login=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page.widget_loginBack.widget_loginCenter.widget.pushButton_login')
        self.errorOk=uiautomation.ButtonControl(Name='OK')
        # self.errorClose=uiautomation.ButtonControl(Name='关闭')
    def Login(self,username,password):
            self.username.GetValuePattern().SetValue(' ')
            self.username.GetValuePattern().SetValue(username)
            self.password.Click()
            self.password.SendKeys('{Ctrl}{A}')
            self.password.SendKeys('{delete}')
            self.password.SendKeys(password)
            self.login.Click()

    def readuser(self):
        df=pd.read_excel('D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\testfile\\loginuser1.xlsx')
        for i in df.index:
            for j in range(len(df.columns)-1):
                try:
                    if uiautomation.ButtonControl(Name='OK').Exists():
                        uiautomation.ButtonControl(Name='OK').Click()
                    else:
                        self.Login(df.iloc[i,j],df.iloc[i,j+1])
                    if uiautomation.TextControl(Name='          样品管理').Exists():
                        print('用户登录成功:', get_logCounts('loginCountsuccess'), '次')
                        logger.info('用户登录成功日志:%s次', get_logCounts('loginCountlogsuccess'))
                        #登录成功后直接结束跳出循环
                        break
                    else:
                        # print('未能进入样品管理页面，用户登录失败:', get_logCounts('loginCountfail'), '次')
                        # logger.info('未能进入样品管理页面，用户登录失败:%s次', get_logCounts('loginCountlogfail'))
                        raise Exception('登录失败')
                except Exception as e:
                        print('未能进入样品管理页面，用户登录失败:', get_logCounts('loginCountfail'), '次')
                        # logger.exception('未能进入样品管理页面，用户登录失败:%s次，原因：%s',get_logCounts('loginCountlogfail'), e)
                        logger.exception('未能进入样品管理页面，用户登录失败日志:%s次:', get_logCounts('loginCountlogfail'))
            else:
                #内层循环结束后继续外层循环
                continue
            break #内层循环被跳出后直接跳出外层循环



ob=userLogin().readuser()
print(ob)
# def readuser(self):
#     df = pd.read_excel('D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\testfile\\loginuser.xlsx')
#     for i in df.index:
#         for j in range(len(df.columns) - 1):
#             if uiautomation.ButtonControl(Name='OK').Exists():
#                 uiautomation.ButtonControl(Name='OK').Click()
#             else:
#                 self.Login(df.iloc[i, j], df.iloc[i, j + 1])
#             if uiautomation.TextControl(Name='          样品管理').Exists():
#                 print('用户登录成功:', get_logCounts('loginCountsuccess'), '次')
#                 logger.info('用户登录成功:%s次', get_logCounts('loginCountlogsuccess'))
#                 break  # 登录成功后直接跳出循环
#             else:
#                 print('未能进入样品管理页面，用户登录失败:', get_logCounts('loginCountfail'), '次')
#                 logger.info('未能进入样品管理页面，用户登录失败:%s次', get_logCounts('loginCountlogfail'))
#         else:
#             continue  # 内层循环结束后继续外层循环
#         break  # 内层循环被跳出后跳出外层循环