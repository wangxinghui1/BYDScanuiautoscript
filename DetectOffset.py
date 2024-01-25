import pandas as pd
import uiautomation
from Bydlogger import get_logger
from logCounts import get_logCounts
import pyautogui
import time
logger=get_logger('DetectOffset','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\DetectOffset.log')
class scanCommStates:
    def __init__(self):
        #定义各平板矫正按钮
        self.detectOffsetButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_Tab.page_3.LithiumSystemCorrectWidgetClass.widget_10.widget_7.widget_8.widget_37.widget_9.pushButton_offsetCalib')
        self.detectDefectButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_Tab.page_3.LithiumSystemCorrectWidgetClass.widget_10.widget_7.widget_8.widget_37.widget_9.pushButton_gainCalib')
        self.detectGainButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_Tab.page_3.LithiumSystemCorrectWidgetClass.widget_10.widget_7.widget_8.widget_37.widget_9.pushButton_defectCalib')
        #定义各平板探测器矫正正常时位置坐标
        self.detectOffsetsuccPosition=(1829,251)
        self.detectDefectsuccPosition=(1828,280)
        self.detectGainsuccPosition=(1829,313)
        self.detectOffsetsuccCmp=pyautogui.pixelMatchesColor(1829,251,(124,222,0))
        self.detectDefectsuccCmp = pyautogui.pixelMatchesColor(1828,280,(124,222,0))
        self.detectGainsuccCmp = pyautogui.pixelMatchesColor(1829,313,(124,222,0))
        #定义各平板探测器矫正失败时位置坐标
        self.detectOffsetfailPosition=(1829,251)
        self.detectDefectfailPosition=(1828,280)
        self.detectGainfailPosition=(1829,313)
        self.detectOffsetfailCmp=pyautogui.pixelMatchesColor(1829,251,(108,116,128))
        self.detectDefectfailCmp = pyautogui.pixelMatchesColor(1828,280,(108,116,128))
        self.detectGainfailCmp = pyautogui.pixelMatchesColor(1829,313,(108,116,128))
        # self.sysSelfcheck=uiautomation.TextControl()
    def test(self):
      # pyautogui.click(self.scanCommsuccPosition)
      # pyautogui.click(self.scanTubesuccPosition)
      # pyautogui.click(self.scanDetecsuccPosition)
      # pyautogui.click(self.scanSafelocksuccPosition)
      pyautogui.click(self.scanExposuresuccPosition)
      time.sleep(2)
      # pyautogui.click('测试门联锁位置',self.scanCommsuccPosition)
    def all_detecOffsetnormal(self):
        for i in range(3):
            try:
               pyautogui.click(self.detectOffsetsuccPosition)
               if self.detectOffsetsuccCmp and self.detectDefectsuccCmp and self.detectGainsuccCmp:
                   # 调试
                   print(self.detectOffsetsuccCmp)
                   print(self.detectDefectsuccCmp)
                   print(self.detectGainsuccCmp)
                   print('系统平板矫正正常')
                   break
               else:
                 pyautogui.click(self.detectOffsetfailPosition)
                 if self.detectOffsetfailCmp:
                     # 调试
                     print(self.detectOffsetfailCmp)
                     print('系统平板offset矫正失败:', get_logCounts('detectOffsetfailCount'), '次')
                     logger.info('系统平板offset矫正失败日志:%s次', get_logCounts('detectOffsetfaillogCount'))
                     self.detectOffsetButton.Click()
                 pyautogui.click(self.detectDefectfailPosition)
                 if self.detectDefectfailCmp:
                     # 调试
                     print(self.detectDefectfailCmp)
                     print('系统平板Defect矫正失败:', get_logCounts('detectDefectfailCount'), '次')
                     logger.info('系统平板Defect矫正失败日志:%s次', get_logCounts('detectDefectfaillogCount'))
                     self.detectDefectButton.Click()
                 pyautogui.click(self.detectGainfailPosition)
                 if self.detectGainfailCmp:
                     # 调试
                     print(self.detectGainfailCmp)
                     print('系统平板Gain矫正失败:', get_logCounts('detectGainfailCount'), '次')
                     logger.info('系统平板Gain矫正失败日志:%s次', get_logCounts('detectGainfaillogCount'))
                     self.detectGainButton.Click()
            except Exception as e:
                logger.error('系统平板错误抛出异常：%s', str(e))
            if self.detectOffsetfailCmp or self.detectDefectfailCmp or self.detectGainfailCmp:
                continue
            time.sleep(3)
# scanCommStatesobj=scanCommStates()
# scanCommStatesobj.startscanExposure()
# # scanCommStatesobj.test()
# scanCommStatesobj.all_scanCommnormal()
# print('测试通过')