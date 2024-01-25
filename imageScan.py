# -*- coding: utf-8 -*-
import uiautomation
import pyautogui
import time
from Bydlogger import get_logger
from logCounts import get_logCounts
import pyautogui
from scanCommState import scanCommStates
logger=get_logger('imageScans','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\imageScans.log')
class imageScans:
    def __init__(self):
        self.preview=uiautomation.CheckBoxControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_12.checkBox_prview')
        self.scanButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_10.pushButton_startScan')
        self.cancelButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_10.pushButton_cancleScan')
    def imageScan(self):
        try:
           self.preview.Click()
           self.scanButton.Click()
           self.cancelButton.Click()
           time.sleep(3)
           self.scanButton.Click()
           scanCommStatesobj=scanCommStates()
           scanCommStatesobj.startscanExposure()
           if scanCommStatesobj.scanExposurefailCmp:
               #开始曝光失败后重新开始扫描曝光三次后继续执行扫描
               for i in range(5):
                   self.scanButton.Click()
                   scanCommStatesobj = scanCommStates()
                   scanCommStatesobj.startscanExposure()
           else:
            #曝光成功后等待扫描结果
            time.sleep(15)
           if test==True:
               print('扫描图像结果正确:',get_logCounts('imageScansuccCount'), '次',)
               logger.info('扫描图像结果正确日志:%s次', get_logCounts('imageScansucclogCount'))
           else:
               print('扫描图像结果错误:',get_logCounts('imageScanfailCount'), '次',)
               logger.info('扫描图像结果错误日志:%s次', get_logCounts('imageScanfaillogCount'))
        except Exception as e:
            print('扫描图像抛出错误异常')
imagesanObj=imageScans()
imagesanObj.imageScan()