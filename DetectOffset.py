import pandas as pd
import uiautomation
from Bydlogger import get_logger
from logCounts import get_logCounts
import pyautogui
import time
logger=get_logger('DetectOffset','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\DetectOffset.log')
class scanCommStates:
    def __init__(self):
        #�����ƽ�������ť
        self.detectOffsetButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_Tab.page_3.LithiumSystemCorrectWidgetClass.widget_10.widget_7.widget_8.widget_37.widget_9.pushButton_offsetCalib')
        self.detectDefectButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_Tab.page_3.LithiumSystemCorrectWidgetClass.widget_10.widget_7.widget_8.widget_37.widget_9.pushButton_gainCalib')
        self.detectGainButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_Tab.page_3.LithiumSystemCorrectWidgetClass.widget_10.widget_7.widget_8.widget_37.widget_9.pushButton_defectCalib')
        #�����ƽ��̽������������ʱλ������
        self.detectOffsetsuccPosition=(1829,251)
        self.detectDefectsuccPosition=(1828,280)
        self.detectGainsuccPosition=(1829,313)
        self.detectOffsetsuccCmp=pyautogui.pixelMatchesColor(1829,251,(124,222,0))
        self.detectDefectsuccCmp = pyautogui.pixelMatchesColor(1828,280,(124,222,0))
        self.detectGainsuccCmp = pyautogui.pixelMatchesColor(1829,313,(124,222,0))
        #�����ƽ��̽��������ʧ��ʱλ������
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
      # pyautogui.click('����������λ��',self.scanCommsuccPosition)
    def all_detecOffsetnormal(self):
        for i in range(3):
            try:
               pyautogui.click(self.detectOffsetsuccPosition)
               if self.detectOffsetsuccCmp and self.detectDefectsuccCmp and self.detectGainsuccCmp:
                   # ����
                   print(self.detectOffsetsuccCmp)
                   print(self.detectDefectsuccCmp)
                   print(self.detectGainsuccCmp)
                   print('ϵͳƽ���������')
                   break
               else:
                 pyautogui.click(self.detectOffsetfailPosition)
                 if self.detectOffsetfailCmp:
                     # ����
                     print(self.detectOffsetfailCmp)
                     print('ϵͳƽ��offset����ʧ��:', get_logCounts('detectOffsetfailCount'), '��')
                     logger.info('ϵͳƽ��offset����ʧ����־:%s��', get_logCounts('detectOffsetfaillogCount'))
                     self.detectOffsetButton.Click()
                 pyautogui.click(self.detectDefectfailPosition)
                 if self.detectDefectfailCmp:
                     # ����
                     print(self.detectDefectfailCmp)
                     print('ϵͳƽ��Defect����ʧ��:', get_logCounts('detectDefectfailCount'), '��')
                     logger.info('ϵͳƽ��Defect����ʧ����־:%s��', get_logCounts('detectDefectfaillogCount'))
                     self.detectDefectButton.Click()
                 pyautogui.click(self.detectGainfailPosition)
                 if self.detectGainfailCmp:
                     # ����
                     print(self.detectGainfailCmp)
                     print('ϵͳƽ��Gain����ʧ��:', get_logCounts('detectGainfailCount'), '��')
                     logger.info('ϵͳƽ��Gain����ʧ����־:%s��', get_logCounts('detectGainfaillogCount'))
                     self.detectGainButton.Click()
            except Exception as e:
                logger.error('ϵͳƽ������׳��쳣��%s', str(e))
            if self.detectOffsetfailCmp or self.detectDefectfailCmp or self.detectGainfailCmp:
                continue
            time.sleep(3)
# scanCommStatesobj=scanCommStates()
# scanCommStatesobj.startscanExposure()
# # scanCommStatesobj.test()
# scanCommStatesobj.all_scanCommnormal()
# print('����ͨ��')