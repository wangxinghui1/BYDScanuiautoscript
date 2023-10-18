import time
import pandas as pd
import uiautomation
import logging
logger = logging.getLogger('setusertest')
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')
file_handler = logging.FileHandler('D:\\log\\bydconfigsetuser.log')
file_handler.setLevel(level=logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
class setusernameManagement:
    def __init__(self):
        self.currentvalue=''
        self.nextvalue=''
        self.userlistinfo=[]
        self.account=uiautomation.EditControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_20.widget_24.widget_25.widget_28.lineEdit_bydSerring_UserCode')
        self.password=uiautomation.EditControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_20.widget_24.widget_25.widget_29.lineEdit_bydSerring_UserPassword')
        self.confirmpassword=uiautomation.EditControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_20.widget_24.widget_25.widget_30.lineEdit_bydSerring_UserPasswordConfirmation')
        self.username=uiautomation.EditControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_20.widget_24.widget_25.widget_27.lineEdit_bydSerring_UserName')
        self.saveas=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_20.widget_24.widget_26.pushButton_bydSetting_Other')
        self.repeat=uiautomation.TextControl(Name= '该账号已存在，无法创建！')
        self.table=uiautomation.TableControl(searchDepth=12,AutomationId="bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_19.widget_22.tableWidget_bydSetting_UserList")
        self.delete=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_20.widget_24.widget_26.pushButton_bydSetting_Delete')
        self.save=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_20.widget_24.widget_26.pushButton_bydSetting_Save')
    def newUser(self, account, password, confirmpassword, username):
        self.account.GetValuePattern().SetValue(' ')
        self.account.GetValuePattern().SetValue(account)
        self.password.GetValuePattern().SetValue(' ')
        self.password.GetValuePattern().SetValue(password)
        self.confirmpassword.GetValuePattern().SetValue(' ')
        self.confirmpassword.GetValuePattern().SetValue(confirmpassword)
        self.username.GetValuePattern().SetValue(' ')
        self.username.GetValuePattern().SetValue(username)
        self.saveas.Click()
        if self.repeat.Exists():
            exit('账号重复，退出程序')
    def readUserInfo(self):
        df = pd.read_excel('D:\\SVNsoftwarePackageRelease\\BYDCollectExe_2023_07_19\\res\\Data\\login.xlsx')
        for i in df.index:
            self.newUser(df.iloc[i].values[0], df.iloc[i].values[1],df.iloc[i].values[2], df.iloc[i].values[3])
        for i in range(1, self.table.GetGridPattern().RowCount):
            self.userlistinfo.append(self.table.GetGridPattern().GetItem(i, 0).Name)
            self.userlistinfo.append(self.table.GetGridPattern().GetItem(i, 1).Name)
        print(self.userlistinfo)
    def editUser(self, account, password, confirmpassword, username):
        self.account.GetValuePattern().SetValue(' ')
        self.account.GetValuePattern().SetValue(account)
        self.password.GetValuePattern().SetValue(' ')
        self.password.GetValuePattern().SetValue(password)
        self.confirmpassword.GetValuePattern().SetValue(' ')
        self.confirmpassword.GetValuePattern().SetValue(confirmpassword)
        self.username.GetValuePattern().SetValue(' ')
        self.username.GetValuePattern().SetValue(username)
        self.save.Click()
        if self.repeat.Exists():
            exit('账号重复，退出程序')
    def readeditUserInfo(self):
        df = pd.read_excel('D:\\SVNsoftwarePackageRelease\\BYDCollectExe_2023_07_19\\res\\Data\\edituser.xlsx')
        for i in range(1, self.table.GetGridPattern().RowCount):
            if i > 8:
                uiautomation.WheelDown()
                time.sleep(1)
            self.table.GetGridPattern().GetItem(i, 1).Click()
            self.editUser(df.iloc[i-1].values[0], df.iloc[i-1].values[1],df.iloc[i-1].values[2], df.iloc[i-1].values[3])
        for i in range(1,self.table.GetGridPattern().RowCount):
            self.userlistinfo.append(self.table.GetGridPattern().GetItem(i, 0).Name)
            self.userlistinfo.append(self.table.GetGridPattern().GetItem(i, 1).Name)
        print(self.userlistinfo)
    def confirmUser(self,lst,current_param,next_param):
        for index in range(0,len(lst),2):
            current_element =lst[index]
            if index < len(lst)-1:
                next_element =lst[index + 1]
                # print('current_element:',current_element, 'next_element:',next_element)
            else:
                # print(current_element)
                next_element=' '
            if current_element==current_param and next_element==next_param:
                print('新建成功')
                break
            else:
                print('新建失败')
    def getIndexvalue(self):
        df = pd.read_excel('D:\\SVNsoftwarePackageRelease\\BYDCollectExe_2023_07_19\\res\\Data\\login.xlsx')
        j=0
        for i in df.index:
            currentvalue = df.iloc[i].values[0]
            nextvalue = df.iloc[i].values[3]
            # print('打印文件读取的currentvalue:',currentvalue)
            # print('打印文件读取的nextvalue:',nextvalue)
            if j<len(self.userlistinfo):
                self.confirmUser(self.userlistinfo[j:],currentvalue,nextvalue)
                j+=2
            else:
                break
    def deleteUserInfo(self):
        adminposition = uiautomation.DataItemControl(Name='admin')
        while adminposition.Exists() != True:
            self.table.Click()
            uiautomation.WheelUp()
        addIndex = 3
        while uiautomation.DataItemControl(foundIndex=addIndex).Exists()==True:
            uiautomation.DataItemControl(foundIndex=addIndex).Click()
            self.delete.Click()
        print('用户已全部删除完成')
obj=setusernameManagement()
for i in range(10):
    obj.deleteUserInfo()
    obj.readUserInfo()
    obj.getIndexvalue()
    obj.readeditUserInfo()
    obj.getIndexvalue()
    i+=1
    print(i)
    logger.debug('测试了%s次',i)