import pandas as pd
import uiautomation
from Bydlogger import get_logger
from logCounts import get_logCounts
import pyautogui
import time
logger=get_logger('scanCommState','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\scanCommState.log')
class scanCommStates:
    def __init__(self):
        #定义各通信正常时位置坐标
        self.scanCommsuccPosition=(1313,43)
        self.scanTubesuccPosition=(1366,50)
        self.scanDetecsuccPosition=(1413,48)
        self.scanSafelocksuccPosition=(1461,50)
        self.scanExposuresuccPosition=(1573,40)
        self.scanCommsuccCmp=pyautogui.pixelMatchesColor(1313,43,(18,93,17))
        self.scanTubesuccCmp = pyautogui.pixelMatchesColor(1366,50,(21,107,20))
        self.scanDetecsuccCmp = pyautogui.pixelMatchesColor(1413,48,(25,129,23))
        self.scanSafelocksuccCmp= pyautogui.pixelMatchesColor(1461,50,(25,129,23))
        self.scanExposuresuccCmp=pyautogui.pixelMatchesColor(1573,40,(189, 161, 12))
        #定义各通信连接失败时位置坐标
        self.scanCommfailPosition=(1313,43)
        self.scanTubefailPosition=(1366,50)
        self.scanDetecfailPosition=(1413,48)
        self.scanSafelockfailPosition=(1461,50)
        self.scanExposuresuccPosition=(1573,40)
        self.scanCommfailCmp=pyautogui.pixelMatchesColor(1313,43,(108, 116, 128))
        self.scanTubefailCmp = pyautogui.pixelMatchesColor(1366,50,(108, 116, 128))
        self.scanDetecfailCmp = pyautogui.pixelMatchesColor(1413,48,(108, 116, 128))
        self.scanSafelockfailCmp = pyautogui.pixelMatchesColor(1461,50,(108, 116, 128))
        self.scanExposurefailCmp=pyautogui.pixelMatchesColor(1573,40,(68, 57, 17))
        #定义各通信连接异常时位置坐标
        self.scanCommExcepPosition=(1313,43)
        self.scanTubeExcepPosition=(1366,50)
        self.scanDetecExcepPosition=(1413,48)
        self.scanSafelockExcepPosition=(1461,50)
        self.scanCommExcepcmp=pyautogui.pixelMatchesColor(1313,43,(139,27,27))
        self.scanTubeExcepCmp = pyautogui.pixelMatchesColor(1366,50,(139,27,27))
        self.scanDetecExcepCmp = pyautogui.pixelMatchesColor(1413,48,(139,27,27))
        self.scanSafelockExcepCmp = pyautogui.pixelMatchesColor(1461,50,(139,27,27))
        self.scanExposureExcepCmp=pyautogui.pixelMatchesColor(1573,40,(68, 57, 17))
        # self.sysSelfcheck=uiautomation.TextControl()
    def test(self):
      # pyautogui.click(self.scanCommsuccPosition)
      # pyautogui.click(self.scanTubesuccPosition)
      # pyautogui.click(self.scanDetecsuccPosition)
      # pyautogui.click(self.scanSafelocksuccPosition)
      pyautogui.click(self.scanExposuresuccPosition)
      time.sleep(2)
      # pyautogui.click('测试门联锁位置',self.scanCommsuccPosition)
    def all_scanCommnormal(self):
        for i in range(3):
            try:
                   pyautogui.click(self.scanCommsuccPosition)
                   # print('测试通过')
                   # print(self.scanCommsuccCmp)
                   # print(self.scanTubesuccCmp)
                   # print(self.scanDetecsuccCmp)
                   # print(self.scanSafelocksuccCmp)
                   # print('系统扫描通信连接正常测试')
                   if self.scanCommsuccCmp and self.scanTubesuccCmp and self.scanDetecsuccCmp and self.scanSafelocksuccCmp:
                       # 调试
                       print(self.scanCommsuccCmp)
                       print(self.scanTubesuccCmp)
                       print(self.scanDetecsuccCmp)
                       print(self.scanSafelocksuccCmp)
                       print('系统扫描通信连接正常')
                       break
                   else:
                     pyautogui.click(self.scanCommfailPosition)
                     if self.scanCommfailCmp:
                         # 调试
                         print(self.scanCommfailCmp)
                         print('系统扫描通信连接失败:', get_logCounts('scanCommfailCount'), '次')
                         logger.info('系统扫描通信连接失败日志:%s次', get_logCounts('scanCommfaillogCount'))
                     elif self.scanCommExcepcmp:
                         # 调试
                         print(self.scanCommExcepcmp)
                         print('系统扫描通信连接异常:', get_logCounts('scanCommExcepCount'), '次')
                         logger.info('系统扫描通信连接异常日志:%s次', get_logCounts('scanCommExceplogCount'))
                     pyautogui.click(self.scanTubefailPosition)
                     if self.scanTubefailCmp:
                         # 调试
                         print(self.scanTubefailCmp)
                         print('系统扫描球管连接失败:', get_logCounts('scanTubefailCount'), '次')
                         logger.info('系统扫描球管连接失败日志:%s次', get_logCounts('scanTubefaillogCount'))
                     elif self.scanTubeExcepCmp:
                         print(self.scanTubeExcepCmp)
                         print('系统扫描球管连接异常:', get_logCounts('scanTubeExcepCount'), '次')
                         logger.info('系统扫描球管连接异常日志:%s次', get_logCounts('scanTubeExceplogCount'))
                     pyautogui.click(self.scanDetecfailPosition)
                     if self.scanDetecfailCmp:
                         # 调试
                         print(self.scanDetecfailCmp)
                         print('系统扫描平板连接失败:', get_logCounts('scanDetectfailCount'), '次')
                         logger.info('系统扫描平板连接失败日志:%s次', get_logCounts('scanDetectfaillogCount'))
                     elif self.scanDetecExcepCmp:
                         print(self.scanDetecExcepCmp)
                         print('系统扫描平板连接异常:', get_logCounts('scanDetectExcepCount'), '次')
                         logger.info('系统扫描平板连接异常日志:%s次', get_logCounts('scanDetectExceplogCount'))
                     pyautogui.click(self.scanSafelockfailPosition)
                     # print('打印门联锁扫描失败状态',self.scanSafelockfailCmp)
                     if self.scanSafelockfailCmp:
                         # 调试
                         print(self.scanSafelockfailCmp)
                         print('系统扫描门联锁连接失败:', get_logCounts('scanSafelockfailCount'), '次')
                         logger.info('系统扫描门联锁连接失败日志:%s次', get_logCounts('scanSafelockfaillogCount'))
                     elif self.scanSafelockExcepCmp:
                         print(self.scanSafelockExcepCmp)
                         print('系统扫描门联锁连接异常:', get_logCounts('scanSafelockExcepCount'), '次')
                         logger.info('系统扫描门联锁连接异常日志:%s次', get_logCounts('scanSafelockExceplogCount'))
            except Exception as e:
                logger.error('处理all_commnormal 异常：%s', str(e))
            if self.scanCommfailCmp or self.scanCommExcepcmp or self.scanTubefailCmp or self.scanTubeExcepCmp or self.scanDetecfailCmp or self.scanDetecExcepCmp or self.scanSafelockfailCmp or self.scanSafelockExcepCmp:
                continue
            time.sleep(3)
    def startscanExposure(self):
        try:
            pyautogui.click(self.scanExposuresuccPosition)
            if self.scanExposuresuccCmp:
                print('开始曝光成功')
            else:
                print('开始曝光失败:',get_logCounts('startscanExposurefailCount'),'次')
                logger.info('开始曝光失败日志:%s次', get_logCounts('startscanExposurefaillogCount'))
        except Exception as e:
            logger.error('开始曝光失败异常：%s', str(e))
# scanCommStatesobj=scanCommStates()
# scanCommStatesobj.startscanExposure()
# # scanCommStatesobj.test()
# scanCommStatesobj.all_scanCommnormal()
# print('测试通过')