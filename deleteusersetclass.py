import pandas as pd
import pyautogui
import uiautomation
class deletesetUserInfo:
    def __init__(self):
        self.delete=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_20.widget_24.widget_26.pushButton_bydSetting_Delete')
    def deleteUserInfo(self):
        adminposition = uiautomation.DataItemControl(Name='admin')
        while adminposition.Exists() != True:
            uiautomation.TableControl(
                AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_5.widget_18.widget_19.widget_22.tableWidget_bydSetting_UserList').Click()
            uiautomation.WheelUp()
        addIndex = 3
        while uiautomation.DataItemControl(foundIndex=addIndex).Exists()==True:
            uiautomation.DataItemControl(foundIndex=addIndex).Click()
            self.delete.Click()
        print('用户已全部删除完成')
        print(addIndex)
        # exit('用户已全部删除完成，退出脚本执行程序')
deletesetUserInfo().deleteUserInfo()