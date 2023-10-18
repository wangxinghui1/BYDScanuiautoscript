import uiautomation
import subprocess
import time
import logging
import pandas
logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')
file_handler = logging.FileHandler('D:\\log\\bydconfigset.log')
file_handler.setLevel(level=logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
opensetting = 0
def setpsdVif():
    global opensetting
    settingbutton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_8.widget_44.widget_46.widget_52.pushButton_bydCT_Setting')
    settingbutton.Click()
    inputpsd=uiautomation.TextControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.mpPasswordValidation.widget.widget_3.widget_5.label_2')
    if inputpsd.Name!='请输入密码':
        opensetting+=1
        logger.debug('打开设置输入密码页面失败%s次',opensetting)
        # exit('退出执行测试脚本')
    else:
        print('设置输入密码页面打开成功')
inputpassword=0
def inputpassword():
    global inputpassword
    inputpass=uiautomation.EditControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.mpPasswordValidation.widget.widget_3.widget_5.widget_7.lineEdit_bydManagerPassword')
    # inputpass.SendKeys('123')
    inputpass.GetValuePattern().SetValue('123')
    okButton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.mpPasswordValidation.widget.widget_3.widget_6.pushButton_bydPassWord_Vailidation')
    okButton.Click()
    pasvalid=uiautomation.TextControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_2.label')
    if pasvalid.Name!='密码验证':
        inputpassword+=1
        logger.debug('输入密码失败，打开设置页面失败了%s次',inputpassword)
    else:
        print('进入设置页面成功')
openlocal=0
def storage():
    global openlocal
    browsebutton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_7.widget_15.pushButton_bydSetting_PathView')
    browsebutton.Click()
    if uiautomation.EditControl(AutomationId='1152').Exists()!=True:
        openlocal+=1
        logger.debug('打开本地文件夹失败,失败了%s次',openlocal)
    else:
        print('打开本地文件夹成功')
    inputfile=uiautomation.EditControl(AutomationId='1152',Name='文件夹:')
    inputfile.SendKeys('D:\\SVNsoftwarePackageRelease\\BYDCollectExe_2023_07_19\\res\\Data\\Testdata')
    if uiautomation.EditControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_7.widget_15.lineEdit_bydSetting_Path').GetValuePattern()!='D:/SVNsoftwarePackageRelease/...':
        openlocal+=1
        logger.debug('选择保存的路径与实际选择的路径不一致了%s次',openlocal)
    else:
        print('选择保存的路径与实际选择的路径一致')
    # saveButton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_7.widget_16.pushButton_bydSetting_PathSave')
    savefileButton=uiautomation.ButtonControl(Name='选择文件夹')
    savefileButton.Click()
def aircorrection():
    aircorbutton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_31.widget_33.pushButton_bydSetting_AirCalibration')
    aircorbutton.Click()
def GeometricCorrection():
    GeoCorbutton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_31.widget_33.pushButton_bydSetting_GeometricCorrection')
    GeoCorbutton.Click()
def PlateCorrection():
    PlateCorbutton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_31.widget_33.pushButton_bydSetting_PlateCorrection')
    PlateCorbutton.Click()
setpsdVif()
time.sleep(2)
inputpassword()
time.sleep(2)
storage()
time.sleep(2)
# aircorrection()
# time.sleep(2)
# GeometricCorrection()
# time.sleep(2)
# PlateCorrection()