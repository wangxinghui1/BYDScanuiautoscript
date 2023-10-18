import pyautogui
import uiautomation
import subprocess
import time
import logging
logger = logging.getLogger()
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s')
file_handler = logging.FileHandler('D:\\BYDscanTest\\bydscript\\Data\\log\\byd2.log')
file_handler.setLevel(level=logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#1.单击一次打开门锁不再次关闭门锁
signalsaftylock1 = 0
signalsaftylock2 = 0
signalsaftylock3=0
safty1and2lock=0
safty1and3lock=0
safty2and3lock=0
safty1an2and3lock=0
def openSafetyLock():
    #1.关闭设置页面安全锁1图标颜色,坐标(537, 516)，RGB(79, 231, 194)
    #2.打开设置页面安全锁1图标颜色,坐标(537, 516)，RGB(113, 155, 219)
    #3.打开设置页面安全锁1后整个页面上方通讯安全锁1图标颜色,坐标(617,67)，RGB(234, 17, 29)
    # 4.关闭设置页面安全锁2图标颜色,坐标(684,515)，RGB(79, 231, 194)
    # 5.打开设置页面安全锁2图标颜色,坐标(684,515)，RGB(113, 155, 219)
    # 6.打开设置页面安全锁2后整个页面上方通讯安全锁2图标颜色,坐标（618,65），RGB(234, 17, 29)
    # 7.关闭设置页面安全锁3图标颜色,坐标(829, 514)，RGB(79, 231, 194)
    # 8.打开设置页面安全锁3图标颜色,坐标(829, 514)，RGB(113, 155, 219)
    # 9.打开设置页面安全锁3后整个页面上方通讯安全锁3图标颜色,坐标(617,67)，RGB(234, 17, 29)
    #10.高压图标颜色，坐标（357，61），RGB（0，255，0）
    #11.平板图标颜色，坐标（420，64），RGB（0，255，0）
    #12.通信图标颜色，坐标（487，66），RGB（0，255，0）
    #13.机械臂图标颜色，坐标（552，64），RGB（0，255，0）
    # get_tubePixel=pyautogui.pixel(618,65)
    # print(get_tubePixel)
    # print('执行过了3')
    safetylock1 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_6.widget_10.widget_11.pushButton_bydSetting_doorlock_1')
    safetylock2 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_6.widget_10.widget_12.pushButton_bydSetting_doorlock_2')
    safetylock3 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_6.widget_10.widget_13.pushButton_bydSetting_doorlock_3')
    Scanbutton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_16.pushButton_bydCT_Scan')
    #1.单次点击门锁1
    safetylock1.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #2.打开安全锁1颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(113, 155, 219))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(79, 231, 194))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(234,17,29))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(0,255,0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))
    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面安全锁1打开成功')
    else:
        print('设置页面安全锁1打开失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftylock1
    #此时曝光了，颜色为黄色
    if tubeexposePixel & exposurePiexl==True:
        signalsaftylock1+=1
        print('安全锁1机制出现错误，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftylock1)+'.png')
        logger.debug('安全锁1机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftylock1)
        # exit('安全锁1机制出现错误，此时不可被曝光')
    else:
        print('安全锁1已打开，禁止曝光')
    #2.单次点击门锁2
    safetylock2.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #2.打开安全锁2颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(79, 231, 194))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(113, 155, 219))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(0,255,0))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(234,17,29))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面安全锁2打开成功')
    else:
        print('设置页面安全锁2打开失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftylock2
    if tubeexposePixel & exposurePiexl==True:
        signalsaftylock2+=1
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftylock2)+'.png')
        print('安全锁2机制出现错误，此时不可被曝光')
        logger.debug('安全锁1机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftylock2)
        # exit('安全锁2机制出现错误，此时不可被曝光')
    else:
        print('安全锁2已打开，禁止曝光')
    #3.单次点击门锁3
    safetylock3.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #2.打开安全锁3颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(79, 231, 194))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(79, 231, 194))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(113, 155, 219))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(0,255,0))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(0,255,0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(234,17,29))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面安全锁3打开成功')
    else:
        print('设置页面安全锁3打开失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftylock3
    if tubeexposePixel &exposurePiexl==True:
        signalsaftylock3+=1
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\imagegenerateimage'+str(signalsaftylock3)+'.png')
        print('安全锁3机制出现错误，此时不可被曝光')
        logger.debug('安全锁1机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftylock3)
        # exit('安全锁3机制出现错误，此时不可被曝光')
    else:
        print('安全锁3已打开，禁止曝光')
    #4.同时点击门锁1和门锁2
    safetylock1.Click()
    safetylock2.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #2.打开安全锁1和安全锁2颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(113, 155, 219))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(113, 155, 219))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(234, 17, 29))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(234, 17, 29))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面安全锁1和门锁2打开成功')
    else:
        print('设置页面安全锁1和门锁2打开失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global safty1and2lock
    if tubeexposePixel &exposurePiexl==True:
        print('安全锁1和安全锁2机制出现错误，此时不可被曝光')
        safty1and2lock+=1
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(safty1and2lock)+'.png')
        # exit('安全锁1和安全锁2机制出现错误，此时不可被曝光')
        logger.debug('安全锁1和2机制出现错误，此时不可被曝光,但曝光了%s次',safty1and2lock)
    else:
        print('安全锁1和安全锁2已打开，禁止曝光')
    # 5.同时点击门锁1和门锁3
    safetylock1.Click()
    safetylock3.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61, (0, 255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    # 2.打开安全锁1和安全锁3颜色
    saftylock1color = pyautogui.pixelMatchesColor(537, 516, (113, 155, 219))
    saftylock2color = pyautogui.pixelMatchesColor(684, 515, (79, 231, 194))
    saftylock3color = pyautogui.pixelMatchesColor(829, 514, (113, 155, 219))
    communicationsaftylock1color = pyautogui.pixelMatchesColor(617, 67, (234, 17, 29))
    communicationsaftylock2color = pyautogui.pixelMatchesColor(618, 65, (0, 255, 0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(234, 17, 29))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel == True:
        print('设置页面安全锁1和门锁3打开成功')
    else:
        print('设置页面安全锁1和门锁3打开失败')
    # 直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global safty1and3lock
    if tubeexposePixel & exposurePiexl == True:
        safty1and3lock+=1
        print('安全锁1和安全锁3机制出现错误，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(safty1and3lock)+'.png')
        logger.debug('安全锁1和3机制出现错误，此时不可被曝光,但曝光了%s次',safty1and3lock)
        # exit('安全锁1和安全锁3机制出现错误，此时不可被曝光')
    else:
        print('安全锁1和安全锁3已打开，禁止曝光')
    # 6.同时点击门锁2和门锁3
    safetylock2.Click()
    safetylock3.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61, (0, 255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    # 2.打开安全锁2和安全锁3颜色
    saftylock1color = pyautogui.pixelMatchesColor(537, 516, (79, 231, 194))
    saftylock2color = pyautogui.pixelMatchesColor(684, 515, (113, 155, 219))
    saftylock3color = pyautogui.pixelMatchesColor(829, 514, (113, 155, 219))
    communicationsaftylock1color = pyautogui.pixelMatchesColor(617, 67, (0, 255, 0))
    communicationsaftylock2color = pyautogui.pixelMatchesColor(618, 65, (234, 17, 29))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(234, 17, 29))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel == True:
        print('设置页面安全锁2和门锁3打开成功')
    else:
        print('设置页面安全锁2和门锁3打开失败')
    # 直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global safty2and3lock
    if tubeexposePixel & exposurePiexl == True:
        safty2and3lock+=1
        print('安全锁2和安全锁3机制出现错误，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(safty2and3lock)+'.png')
        logger.debug('安全锁2和3机制出现错误，此时不可被曝光,但曝光了%s次',safty2and3lock)
        # exit('安全锁2和安全锁3机制出现错误，此时不可被曝光')
    else:
        print('安全锁2和安全锁3已打开，禁止曝光')
    # 7.同时点击门锁1，门锁2和门锁3
    safetylock1.Click()
    safetylock2.Click()
    safetylock3.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61, (0, 255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    # 2.打开安全锁2和安全锁3颜色
    saftylock1color = pyautogui.pixelMatchesColor(537, 516, (113, 155, 219))
    saftylock2color = pyautogui.pixelMatchesColor(684, 515, (113, 155, 219))
    saftylock3color = pyautogui.pixelMatchesColor(829, 514, (113, 155, 219))
    communicationsaftylock1color = pyautogui.pixelMatchesColor(617, 67, (234, 17, 29))
    communicationsaftylock2color = pyautogui.pixelMatchesColor(618, 65, (234, 17, 29))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(234, 17, 29))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel == True:
        print('设置页面安全锁1,安全锁2和门锁3打开成功')
    else:
        print('设置页面安全锁1,安全锁2和门锁3打开失败')
    # 直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global safty1an2and3lock
    if tubeexposePixel & exposurePiexl == True:
        safty1an2and3lock+=1
        print('安全锁1,安全锁2和安全锁3机制出现错误，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(safty1an2and3lock)+'.png')
        logger.debug('安全锁1和2,3机制出现错误，此时不可被曝光,但曝光了%s次',safty1an2and3lock)
        # exit('安全锁1,安全锁2和安全锁3机制出现错误，此时不可被曝光')
    else:
        print('安全锁1,安全锁2和安全锁3已打开，禁止曝光')

#2.单击一次打开门锁后再次关闭门锁
signalsaftycl1=0
signalsaftycl2=0
signalsaftycl3=0
signalsaftycl1nd2=0
signalsaftycl1nd3=0
signalsaftycl2nd3=0
signalsaftycl1nd2nd3=0
def closeSafetyLock():
    #1.关闭设置页面安全锁1图标颜色,坐标(537, 516)，RGB(79, 231, 194)
    #2.打开设置页面安全锁1图标颜色,坐标(537, 516)，RGB(113, 155, 219)
    #3.打开设置页面安全锁1后整个页面上方通讯安全锁1图标颜色,坐标(617,67)，RGB(234, 17, 29)
    # 4.关闭设置页面安全锁2图标颜色,坐标(684,515)，RGB(79, 231, 194)
    # 5.打开设置页面安全锁2图标颜色,坐标(684,515)，RGB(113, 155, 219)
    # 6.打开设置页面安全锁2后整个页面上方通讯安全锁2图标颜色,坐标（618,65），RGB(234, 17, 29)
    # 7.关闭设置页面安全锁3图标颜色,坐标(829, 514)，RGB(79, 231, 194)
    # 8.打开设置页面安全锁3图标颜色,坐标(829, 514)，RGB(113, 155, 219)
    # 9.打开设置页面安全锁3后整个页面上方通讯安全锁3图标颜色,坐标(617,67)，RGB(234, 17, 29)
    #10.高压图标颜色，坐标（357，61），RGB（0，255，0）
    #11.平板图标颜色，坐标（420，64），RGB（0，255，0）
    #12.通信图标颜色，坐标（487，66），RGB（0，255，0）
    #13.机械臂图标颜色，坐标（552，64），RGB（0，255，0）
    # get_tubePixel=pyautogui.pixel(618,65)
    # print(get_tubePixel)
    # print('执行过了3')
    safetylock1 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_6.widget_10.widget_11.pushButton_bydSetting_doorlock_1')
    safetylock2 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_6.widget_10.widget_12.pushButton_bydSetting_doorlock_2')
    safetylock3 = uiautomation.CheckBoxControl(
        AutomationId='bydQWidgetPlatformClass.mpUserSettingName.widget.widget_3.widget_4.widget_6.widget_10.widget_13.pushButton_bydSetting_doorlock_3')
    Scanbutton=uiautomation.ButtonControl(AutomationId='bydQWidgetPlatformClass.stackedWidgetPlatfotm.page_Scan.bydQWidgetScanClass.widget.widget_3.widget_6.widget_9.widget_10.widget_16.pushButton_bydCT_Scan')
    #1.单次点击门锁1后再次点击门锁1
    safetylock1.Click()
    time.sleep(1)
    safetylock1.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #2.打开安全锁1颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(79, 231, 194))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(79, 231, 194))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(0,255,0))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(0,255,0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))
    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面安全锁1打开成功后再次成功关闭')
    else:
        print('设置页面安全锁1打开成功后再次关闭失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftycl1
    if tubeexposePixel & exposurePiexl!=True:
        signalsaftycl1+=1
        print('设置页面安全锁1打开失败')
        print('设置页面安全锁1打开成功后再次关闭失败，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftycl1)+'.png')
        logger.debug('安全锁1机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftycl1)
        # exit()
    else:
        print('设置页面安全锁1打开成功后再次关闭成功，此时可被曝光')
    #2.单次点击门锁2
    safetylock2.Click()
    time.sleep(1)
    safetylock2.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #2.打开安全锁2颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(79, 231, 194))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(79, 231, 194))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(0,255,0))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(0,255,0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面安全锁2打开成功后再次成功关闭')
    else:
        print('设置页面安全锁2打开成功后再次关闭失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftycl2
    if tubeexposePixel & exposurePiexl!=True:
        signalsaftycl2+=1
        print('设置页面安全锁2打开失败')
        print('设置页面安全锁2打开成功后再次关闭失败，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftycl2)+'.png')
        logger.debug('安全锁2机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftycl2)
        # exit()
    else:
        print('设置页面安全锁2打开成功后再次关闭成功，此时可被曝光')
    #3.单次点击门锁3
    safetylock3.Click()
    time.sleep(1)
    safetylock3.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #2.打开安全锁3颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(79, 231, 194))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(79, 231, 194))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(0,255,0))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(0,255,0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面安全锁3打开成功后再次成功关闭')
    else:
        print('设置页面安全锁3打开失败')
        print('设置页面安全锁3打开成功后再次关闭失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftycl3
    if tubeexposePixel & exposurePiexl!=True:
        signalsaftycl3+=1
        print('设置页面安全锁3打开成功后再次关闭失败，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftycl3)+'.png')
        logger.debug('安全锁3机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftycl3)
        # exit()
    else:
        print('设置页面安全锁3打开成功后再次关闭成功，此时可被曝光')
    #4.同时点击门锁1和门锁2
    safetylock1.Click()
    safetylock2.Click()
    time.sleep(1)
    safetylock1.Click()
    safetylock2.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #2.打开安全锁1和安全锁2颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(79, 231, 194))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(79, 231, 194))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(0, 255, 0))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(0, 255, 0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面安全锁1和门锁2打开成功后再次关闭成功')
    else:
        print('设置页面安全锁1和门锁2打开失败')
        print('设置页面安全锁1和门锁2打开成功后再次关闭失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftycl1nd2
    if tubeexposePixel & exposurePiexl!=True:
        signalsaftycl1nd2+=1
        print('设置页面门锁1和门锁2打开成功后再次关闭失败，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftycl1nd2)+'.png')
        logger.debug('安全锁1,2机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftycl1nd2)
        # exit()
    else:
        print('设置页面门锁1和门锁2打开成功后再次曝光成功，此时可被曝光')
    # 5.同时点击门锁1和门锁3
    safetylock1.Click()
    safetylock3.Click()
    time.sleep(1)
    safetylock1.Click()
    safetylock3.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #5.打开门锁1和门锁3颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(79, 231, 194))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(79, 231, 194))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(0, 255, 0))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(0, 255, 0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面门锁1和门锁3打开成功后再次关闭成功')
    else:
        print('设置页面门锁1和门锁3打开失败')
        print('设置页面门锁1和门锁3打开成功后再次关闭失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftycl1nd3
    if tubeexposePixel & exposurePiexl!=True:
        signalsaftycl1nd3+=1
        print('设置页面门锁1和门锁3打开成功后再次关闭失败，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftycl1nd3)+'.png')
        logger.debug('安全锁1,3机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftycl1nd3)
        # exit()
    else:
        print('设置页面门锁1和门锁3打开成功后再次曝光成功，此时可被曝光')
    # 6.同时点击门锁2和门锁3
    safetylock2.Click()
    safetylock3.Click()
    time.sleep(1)
    safetylock2.Click()
    safetylock3.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61,(0,255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    #5.打开门锁1和门锁3颜色
    saftylock1color=pyautogui.pixelMatchesColor(537, 516,(79, 231, 194))
    saftylock2color=pyautogui.pixelMatchesColor(684,515,(79, 231, 194))
    saftylock3color=pyautogui.pixelMatchesColor(829, 514,(79, 231, 194))
    communicationsaftylock1color=pyautogui.pixelMatchesColor(617,67,(0, 255, 0))
    communicationsaftylock2color=pyautogui.pixelMatchesColor(618,65,(0, 255, 0))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(0,255,0))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel==True:
        print('设置页面门锁2和门锁3打开成功后再次关闭成功')
    else:
        print('设置页面门锁2和门锁3打开失败')
        print('设置页面门锁2和门锁3打开成功后再次关闭失败')
    #直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    signalsaftycl2nd3=0
    if tubeexposePixel & exposurePiexl!=True:
        signalsaftycl2nd3+=1
        print('设置页面门锁2和门锁3打开成功后再次关闭失败，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftycl2nd3)+'.png')
        logger.debug('安全锁2,3机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftycl2nd3)
        # exit()
    else:
        print('设置页面门锁2和门锁3打开成功后再次曝光成功，此时可被曝光')
    # 7.同时点击门锁1，门锁2和门锁3
    safetylock1.Click()
    safetylock2.Click()
    safetylock3.Click()
    time.sleep(1)
    safetylock1.Click()
    safetylock2.Click()
    safetylock3.Click()
    tubePixel = pyautogui.pixelMatchesColor(357, 61, (0, 255, 0))
    dectectorPixel = pyautogui.pixelMatchesColor(420, 64, (0, 255, 0))
    commPixel = pyautogui.pixelMatchesColor(487, 66, (0, 255, 0))
    machinalPixel = pyautogui.pixelMatchesColor(552, 64, (0, 255, 0))
    # 2.打开门1和门锁2和安全锁3颜色
    saftylock1color = pyautogui.pixelMatchesColor(537, 516, (79, 231, 194))
    saftylock2color = pyautogui.pixelMatchesColor(684, 515, (79, 231, 194))
    saftylock3color = pyautogui.pixelMatchesColor(829, 514, (79, 231, 194))
    communicationsaftylock1color = pyautogui.pixelMatchesColor(617, 67, (234, 17, 29))
    communicationsaftylock2color = pyautogui.pixelMatchesColor(618, 65, (234, 17, 29))
    # communicationsaftylock3color=pyautogui.pixelMatchesColor(618,65,(234, 17, 29))

    if saftylock1color & saftylock2color & saftylock3color & communicationsaftylock1color & communicationsaftylock2color & tubePixel & dectectorPixel & commPixel & machinalPixel == True:
        print('设置页面安全锁1,安全锁2和门锁3打开成功后再次关闭成功')
    else:
        print('设置页面安全锁1,安全锁2和门锁3打开失败')
        print('设置页面安全锁1,安全锁2和门锁3打开成功后再次关闭失败')
    # 直接点击扫描按钮
    Scanbutton.Click()
    tubeexposePixel = pyautogui.pixelMatchesColor(357, 61, (228, 249, 2))
    exposurePiexl = pyautogui.pixelMatchesColor(1023, 66, (228, 249, 2))
    global signalsaftycl1nd2nd3
    if tubeexposePixel & exposurePiexl != True:
        signalsaftycl1nd2nd3+=1
        print('设置页面安全锁1,安全锁2和门锁3打开成功后再次关闭失败，此时不可被曝光')
        pyautogui.screenshot('D:\\BYDscanTest\\bydscript\\Data\\image\\generateimage'+str(signalsaftycl1nd2nd3)+'.png')
        logger.debug('安全锁1,2,3机制出现错误，此时不可被曝光,但曝光了%s次',signalsaftycl1nd2nd3)
        # exit()
    else:
        print('设置页面安全锁1,安全锁2和门锁3打开成功后再次关闭成功，此时可被曝光')
openSafetyLock()
closeSafetyLock()