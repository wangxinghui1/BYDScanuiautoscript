import pandas as pd
import uiautomation
from Bydlogger import get_logger
from logCounts import get_logCounts
import pyautogui
import time
logger=get_logger('systemSelfcheck','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\systemSelfcheck.log')
class systemSelfcheck:
    def __init__(self):
        #定义各通信恢复正常点击按钮
        self.commButton=uiautomation.ButtonControl(AutomationId='BlurredBackground.lithiumSystemCheckWidget.widget.widget_3.pushButton_systemCheckMcu')
        self.mechaButton=uiautomation.ButtonControl(AutomationId='BlurredBackground.lithiumSystemCheckWidget.widget.widget_4.pushButton_systemCheckMot')
        self.tubeButton=uiautomation.ButtonControl(AutomationId='BlurredBackground.lithiumSystemCheckWidget.widget.widget_5.pushButton_systemCheckTube')
        self.detecButton=uiautomation.ButtonControl(AutomationId='')
        #判断系统自检弹窗是否存在
        self.selfchecklabExist=uiautomation.TextControl(AutomationId='BlurredBackground.lithiumSystemCheckWidget.widget.widget_2.label_2')
        self.selfchecknameExist=uiautomation.TextControl(Name='系统自检')
        #系统自检关闭按钮
        self.selfcheckClose=uiautomation.ButtonControl(AutomationId='BlurredBackground.lithiumSystemCheckWidget.widget.pushButton_SystemCheck_Close')
        #定义各通信正常时位置坐标
        self.commsuccPosition=(1057,406)
        self.mechasuccPosition=(1057,467)
        self.tubesuccPosition=(1056,526)
        self.detecsuccPosition=(1057,586)
        self.commsuccCmp=pyautogui.pixelMatchesColor(1057,406,(29,139,27))
        self.mechsuccCmp = pyautogui.pixelMatchesColor(1057,467,(29,139,27))
        self.tubesuccCmp = pyautogui.pixelMatchesColor(1057,526,(29,139,27))
        self.detecsuccCmp = pyautogui.pixelMatchesColor(1057,586,(29,139,27))
        #定义各通信异常时位置坐标
        self.commfailPosition=(1059,402)
        self.mechafailPosition=(1059,462)
        self.tubefailPosition=(1059,522)
        self.detecfailPosition=(1059,582)
        self.commfailCmp=pyautogui.pixelMatchesColor(1059,402,(139,27,27))
        self.mechfailCmp = pyautogui.pixelMatchesColor(1059,462,(139,27,27))
        self.tubefailCmp = pyautogui.pixelMatchesColor(1059,522,(139,27,27))
        self.detecfailCmp = pyautogui.pixelMatchesColor(1059,582,(139,27,27))
        # self.sysSelfcheck=uiautomation.TextControl()
    def all_commnormal(self):
        for i in range(3):
             try:
                 if self.selfchecknameExist.Exists():
                     print('系统自检弹窗存在')
                     if self.commsuccCmp and self.mechsuccCmp and self.tubesuccCmp and self.detecsuccCmp:
                         # 调试
                         print(self.commsuccCmp)
                         print(self.mechsuccCmp)
                         print(self.tubesuccCmp)
                         print(self.detecsuccCmp)
                         print('系统自检通信正常')
                         self.selfcheckClose.Click()
                         break
                     else:
                         if self.commfailCmp:
                             # 调试
                             print(self.commfailCmp)
                             self.commButton.Click()
                             print('系统自检通信异常:', get_logCounts('commfailCount'), '次')
                             logger.info('系统自检通信异常日志:%s次', get_logCounts('commfaillogCount'))
                         if self.mechfailCmp:
                             # 调试
                             print(self.mechfailCmp)
                             self.mechaButton.Click()
                             print('系统自检机械轴异常:', get_logCounts('mechfailCount'), '次')
                             logger.info('系统自检机械轴异常日志:%s次', get_logCounts('mechfaillogCount'))
                         if self.tubefailCmp:
                             # 调试
                             print(self.tubefailCmp)
                             self.tubeButton.Click()
                             logger.info('系统自检球管异常日志:%s次', get_logCounts('tubefaillogCount'))
                         if self.detecfailCmp:
                             # 调试
                             print(self.detecfailCmp)
                             self.detecButton.Click()
                             print('系统自检平板异常:', get_logCounts('detecfailCount'), '次')
                             logger.info('系统自检平板异常日志:%s次', get_logCounts('detecfaillogCount'))
                 else:
                     print('系统自检弹窗不存在:', get_logCounts('slchecknotExitCount'), '次')
                     logger.info('系统自检弹窗不存在日志:%s次', get_logCounts('slchecknotExitlogCount'))
                     break
                     print('测试break成功')
             except Exception as e:
                 logger.error('处理all_commnormal 异常：%s', str(e))
             if self.commfailCmp or self.mechfailCmp or self.tubefailCmp or self.detecfailCmp:
                 continue
             time.sleep(3)

systemSelfcheck().all_commnormal()