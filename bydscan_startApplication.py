import os
import pyautogui
import uiautomation
import subprocess
import logging
import time
# 添加ctypes.c_void_p
logger = logging.getLogger('bydtest')
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')
file_handler = logging.FileHandler('D:\\log\\bydscanmain.log')
file_handler.setLevel(level=logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# stream_handler = logging.StreamHandler()
# stream_handler.setLevel(level=logging.DEBUG)
# stream_handler.setFormatter(formatter)
openprocess = 0
def startApplication():
    global openprocess
    os.system('taskkill /F /IM bydFrontEndGui.exe')
    # time.sleep(2)
    subprocess.Popen("D:\\SVNsoftwarePackageRelease\\bydScan20230725\\bydFrontEndGui.exe")
    # subprocess.Popen("D:\\SVNsoftwarePackageRelease\\bydScan20230725\\bydFrontEndGui.exe")
    loginExist=uiautomation.ButtonControl(Name='登录')
    time.sleep(3)
    if loginExist.Name!='登录':
        openprocess+=1
        logger.debug('软件程序打开错误%s次',openprocess)
        # exit('退出执行测试脚本')
    else:
        print('程序打开成功')
userdenglu=0
def userlogin():
    global userdenglu
    input_username = uiautomation.EditControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Login.bydQWidgetLoginClass.widget.widget_2.widget_3.lineEdit_bydLoginUsername')
    input_username.SendKeys('admin')
    input_password = uiautomation.EditControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Login.bydQWidgetLoginClass.widget.widget_2.widget_4.lineEdit_bydLoginPassword')
    input_password.SendKeys('admin')
    logbutton = uiautomation.ButtonControl(
        Name='登录')
    logbutton.Click()
    time.sleep(3)
    scanExist=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_16.pushButton_bydCT_Scan')
    if scanExist.Name!='  扫描':
        userdenglu+=1
        logger.debug('用户登录错误%s次',userdenglu)
        # exit('登录错误，退出执行测试脚本')
    else:
        print('用户登录成功')
communication=0
def connectState():
    global communication
    # get_tubePixel=pyautogui.pixel(357,61)
    # print(get_tubePixel)
    # print(uiautomation.ImageControl.GetPixelColor(357,61))
    # test=uiautomation.ImageControl()
    # get_dectectorPixel=pyautogui.pixel(420,64)
    # get_commPixel=pyautogui.pixel(487,66)
    # get_machinalPixel=pyautogui.pixel(552,64)
    # get_safetyPixel1=pyautogui.pixel(616,64)
    # get_safetyPixel2=pyautogui.pixel(681,63)
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    # print('testtubePixel')
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    # print('dectectorPixel')
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    # print('commPixel')
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    # print('machinalPixel')
    safetyPixel1 = pyautogui.pixelMatchesColor(616, 64, (0, 255, 0))
    # print('safetyPixel1')
    safetyPixel2 = pyautogui.pixelMatchesColor(681, 63, (0, 255, 0))
    # print('safetyPixel2')
    if tubePixel & dectectorPixel & commPixel & machinalPixel & safetyPixel1 & safetyPixel2 != True:
        communication+=1
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\communication'+str(communication)+'.png')
        # return "通讯连接失败"
        # prinLogging(coummunication)
        logger.debug('通讯连接失败错误%s次',communication)
        # exit('通讯连接失败，退出执行测试脚本')
        # logger.debug("通讯连接失败")
    else:
        # return "通讯连接正常"
        print("通讯连接正常")
def ele_volcurInput(elevolparam,elecurparam):
    input_elevol=uiautomation.EditControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_14.lineEdit_bydCT_kv')
    input_elevol.SendKeys('{CTRL}''a')
    input_elevol.SendKeys('{BACK}')
    input_elevol.SendKeys(elevolparam)
    Sub_elevol=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_14.pushButton_bydCT_kvSub').Click()
    Add_elevol=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_14.pushButton_bydCT_kvAdd').Click()
    input_elecur=uiautomation.EditControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_15.lineEdit_bydCT_ma')
    input_elecur.SendKeys('{CTRL}''a')
    input_elecur.SendKeys('{BACK}')
    input_elecur.SendKeys(elecurparam)
    Add_elecur=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_15.pushButton_bydCT_maAdd').Click()
    Sub_elecur=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_15.pushButton_bydCT_maSub').Click()
tubeexpose=0
def start_exposureState():
    global tubeexpose
    tubeexposePixel=pyautogui.pixelMatchesColor(357,61,(228,249,2))
    exposurePiexl=pyautogui.pixelMatchesColor(1023,66,(228,249,2))
    if tubeexposePixel & exposurePiexl!=True:
        tubeexpose=tubeexpose+1
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\tubeexpose'+str(tubeexpose)+'.png')
        logger.debug('开始曝光失败错误%s次',tubeexpose)
        # exit('曝光失败，退出执行测试脚本')
    else:
        print("开始曝光成功")
stoptubeexpose=0
def stop_exposureState():
    global stoptubeexpose
    tubeexposePixel=pyautogui.pixelMatchesColor(357,61,(0,255,0))
    exposurePiexl=pyautogui.pixelMatchesColor(1023,66,(204,204,204))
    if tubeexposePixel & exposurePiexl!=True:
        stoptubeexpose+=1
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\stoptubeexpose'+str(stoptubeexpose)+'.png')
        logger.debug('停止曝光失败错误%s次',stoptubeexpose)
        # exit('停止曝光失败，退出执行测试脚本')
    else:
        print('停止曝光成功完成，请进行下一步')
# def tubePreheat():
#     #判断通讯连接状态
#     connectState()
#     ele_volcurInput('100','100')
#     scanButton = uiautomation.ButtonControl(
#         AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_16.pushButton_bydCT_Scan')
#     scanButton.Click()
#     #确认开始预热
#     #判断是否有预热弹窗
#     confirmpreheatButton=uiautomation.TextControl(Name='需要预热15分钟，高压灯变绿可以开始扫描。')
#     global confirmpreheatglobal
#     #如果有预热弹窗
#     confirmpreheatglobal = confirmpreheatButton.Exists()
#     if confirmpreheatButton.Exists():
#         uiautomation.ButtonControl(Name='OK').Click()
#         #判断是否开始曝光
#         time.sleep(1)
#         start_exposureState()
#         time.sleep(1)
#         #判断是否成功完成曝光
#         stop_exposureState()
def imageScan():
    #判断通讯连接状态
    connectState()
    ele_volcurInput('100','100')
    # 重新开始点击扫描按钮进行扫描
    scanButton = uiautomation.ButtonControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_16.pushButton_bydCT_Scan')
    scanButton.Click()
    #判断是否有预热弹窗
    confirmpreheatButton=uiautomation.TextControl(Name='需要预热15分钟，高压灯变绿可以开始扫描。')
    global confirmpreheatglobal
    #如果有预热弹窗
    confirmpreheatglobal = confirmpreheatButton.Exists()
    if  confirmpreheatglobal:
        uiautomation.ButtonControl(Name='OK').Click()
        #判断是否开始曝光
        time.sleep(1)
        start_exposureState()
        time.sleep(1)
        #判断是否成功完成曝光
        stop_exposureState()
        time.sleep(1)
    # scanButton = uiautomation.ButtonControl(
    #     AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_16.pushButton_bydCT_Scan')
    # scanButton.Click()
    #判断是否开始曝光
    start_exposureState()
    time.sleep(1)
    #判断是否成功完成曝光
    stop_exposureState()
    #设置等待扫描出图结果花费时间
    time.sleep(1)
def stopScan():
    stopScan=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_16.pushButton_bydCT_pause')
    stopScan.Click()
generateimage=0
def scanResult():
    global generateimage
    angle1Text=uiautomation.TextControl(AutomationId='')
    if angle1Text.Name!='角1':
        generateimage += 1
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(generateimage)+'.png')
        logger.debug('生成扫描图像错误%s次', generateimage)
        # exit('生成扫描图像错误，退出执行测试脚本')
        # return 'error'
    else:
        print('生成图像成功')
def start_Stopscan():
    scanButton = uiautomation.ButtonControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_16.pushButton_bydCT_Scan')
    scanButton.Click()
    # 判断是否开始曝光
    start_exposureState()
    time.sleep(10)
    #执行暂停曝光
    stopScan()
    # 判断是否暂停曝光成功
    stop_exposureState()
    #再次进行曝光扫描
    imageScan()

def operateWindowsWith(point_x1, point_y1, point_x2, point_y2):
        uiautomation.MoveTo(point_x1, point_y1, waitTime=0.2)
        temp = [point_x1 - 10, point_x1 + 10, point_x1 + 52, point_x1 + 72, point_x1 + 105]
        local = point_x1
        for i in range(len(temp)):
            uiautomation.DragDrop(x1=local, y1=point_y1, x2=temp[i], y2=point_y1, waitTime=1)
            if temp[i] < point_x1:
                local = point_x1
            elif temp[i] > point_x2:
                local = point_x2
            else:
                local = temp[i]
def operateWindowsPosition(point_x1, point_y1, point_x2, point_y2):
    uiautomation.MoveTo(point_x1, point_y1, waitTime=0.2)
    temp = [point_x1 - 10, point_x1 + 10, point_x1 + 52, point_x1 + 72, point_x1 + 105]
    local = point_x1
    for i in range(len(temp)):
        uiautomation.DragDrop(x1=local, y1=point_y1, x2=temp[i], y2=point_y1, waitTime=1)
        if temp[i] < point_x1:
            local = point_x1
        elif temp[i] > point_x2:
            local = point_x2
        else:
            local = temp[i]
def baofuMeasure():
    baofumeasureButton=uiautomation.CheckBoxControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_12.widget_40.widget_41.pushButton_btdCT_Wrapping')
    baofumeasureButton.Click()
    #1.直接右键单击，左键单击
    baofumeasureButton.Click(159,288)
    baofumeasureButton.Click(301,480)

def distanceMeasure():
    distancemeasureButton=uiautomation.CheckBoxControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_12.widget_40.widget_41.pushButton_btdCT_Distance')
    distancemeasureButton.Click()
def angleMeasure():
    AnglemeasureButton = uiautomation.CheckBoxControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_12.widget_40.widget_41.pushButton_btdCT_Angle')
    AnglemeasureButton.Click()
# def exitApplication():
#     closeApplication=uiautomation.ButtonControl(searchDepth=3,Name='关闭')
#     closeApplication.Click()
def angleSwith():
    angleButton1 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_12.widget_40.widget_42.pushButton_bydCT_1')
    angleButton2 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_12.widget_40.widget_42.pushButton_bydCT_2')
    angleButton3 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_12.widget_40.widget_42.pushButton_bydCT_3')
    angleButton4 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_12.widget_40.widget_42.pushButton_bydCT_4')
    angleButton5 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_12.widget_40.widget_42.pushButton_bydCT_0')
    All_angleButton = [angleButton1, angleButton2, angleButton3, angleButton4, angleButton5]
    # names = ['角1', '角2', '角3', '角4', '全部角']
    for i in range(len(All_angleButton) - 1):
        All_angleButton[i].Click()
        # 在此判断是否进入角i页面
        anglepageExist = All_angleButton[i].Exists()
        if anglepageExist == True:
            operateWindowsWith(1621, 763, 1724, 763)
            operateWindowsPosition(1799, 763, 1899, 763)
            baofuMeasure()
            distanceMeasure()
            angleMeasure()
        for j in range(i + 1, len(All_angleButton)):
            All_angleButton[j].Click()

# if __name__=='__main__':
# testprocess=0
#打开应用程序
print('执行打开应用程序')
startApplication()
#用户登录
print('执行用户登录')
userlogin()
#执行包含球管预热的流程
print('执行球管预热')
# tubePreheat()
#执行扫描
print('执行扫描')
imageScan()
#判断扫描结果是否出图
# scanResult()
#测试各个图像页面工具测量
print('角页面切换')
angleSwith()
#单独测试开始扫描和暂停扫描
print('执行扫描和暂停切换按钮测试')
start_Stopscan()
# operateWindowsWith(1621,763,1724,763)
# operateWindowsPosition(1799,763,1899,763)
# exitApplication()
# testprocess=testprocess+1
# logger.debug('测试了%s次',testprocess)
# connectState()
