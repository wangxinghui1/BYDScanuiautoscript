import uiautomation
from Bydlogger import get_logger
from logCounts import get_logCounts
logger=get_logger('rotatutabs','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\rotatutabs.log')
# -*- coding: utf-8 -*-
class motionControls:
    def __init__(self):
        self.rotatutabButton=uiautomation.TextControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDZ.label_6')
        self.rotatutabTarget=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDZ.lineEdit_DDZDest')
        self.rotatutabStep=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDZ.lineEdit_DDZStep')
        self.rotatutabCurr=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDZ.lineEdit_Mot_Cur_DDR')

        self.tubdetcdisButton=uiautomation.TextControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetY.label_7')
        self.tubdetcdisTarget = uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetY.lineEdit_DetYDest')
        self.tubdetcdisStep = uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetY.lineEdit_DetYStep')
        self.tubdetcdisCurr = uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetY.lineEdit_Mot_Cur_DetY')

        self.tubtutadisButton = uiautomation.TextControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDY.label_8')
        self.tubtutadisTarget = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDY.lineEdit_DDYDest')
        self.tubtutadisStep = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDY.lineEdit_DDYStep')
        self.tubtutadisCurr = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDY.lineEdit_Mot_Cur_DDY')

        self.detechighButton = uiautomation.TextControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetZ.label_10')
        self.detechighTarget = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetZ.lineEdit_DetZDest')
        self.detechighStep = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetZ.lineEdit_DetZStep')
        self.detechighCurr = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetZ.lineEdit_Mot_Cur_DetZ')

        self.tubehighButton = uiautomation.TextControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_TubeZ.label_11')
        self.tubehighTarget = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_TubeZ.lineEdit_TubeZDest')
        self.tubehighStep = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_TubeZ.lineEdit_TubeZStep')
        self.tubehighCurr = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_TubeZ.lineEdit_Mot_Cur_TubeZ')

        self.detecfobackButton = uiautomation.TextControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetX.label_12')
        self.detecfobackTarget = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetX.lineEdit_DetXDest')
        self.detecfobackStep = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetX.lineEdit_DetXStep')
        self.detecfobackCurr = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DetX.lineEdit_Mot_Cur_DetX')

        self.turtabfobackButton = uiautomation.TextControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDX.label_13')
        self.turtabfobackTarget = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDX.lineEdit_DDXDest')
        self.turtabfobackStep = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDX.lineEdit_DDXStep')
        self.turtabfobackCurr = uiautomation.EditControl(
            AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_2.scrollArea.qt_scrollarea_viewport.scrollAreaWidgetContents.widget_DDX.lineEdit_Mot_Cur_DDX')
        self.moveButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_9.pushButton_motStart')
        self.stopButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_9.pushButton_motStop')
        self.forwardButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_9.pushButton_motLeft')
        self.backforwardButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_9.pushButton_motRight')
        self.clwiserotButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_9.pushButton_motUnclock')
        self.couclwisroButton=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_9.pushButton_motClock')

    def rotatutabs(self,rotatutabTargetparas,rotatutabStepparas):
        try:
            self.rotatutabButton.Click()
            # self.rotatutabCurr.GetValuePattern().SetValue(' ')
            # self.rotatutabCurr.GetValuePattern().SetValue(rotatutabCurrparas)
            self.rotatutabTarget.GetValuePattern().SetValue(' ')
            self.rotatutabTarget.GetValuePattern().SetValue(rotatutabTargetparas)
            self.rotatutabStep.GetValuePattern().SetValue(' ')
            self.rotatutabStep.GetValuePattern().SetValue(rotatutabStepparas)
            if self.rotatutabCurr.GetValuePattern().Value=='1200.000':
                print('转台旋转度数设置成功')
            else:
                print('转台旋转度数设置失败',get_logCounts('rotatutabsfail'), '次')
                logger.info('转台旋转度数设置失败日志:%s次', get_logCounts('rotatutabslogfail'))
        except Exception as e:
            print('转台旋转度数设置失败',str(e))

    def tubdetcdiss(self,tubdetcdisTargetparas,tubdetcdisStepparas):
        try:
            self.tubdetcdisButton.Click()
            # self.tubdetcdisCurr.GetValuePattern().SetValue(' ')
            # self.tubdetcdisCurr.GetValuePattern().SetValue(tubdetcdisCurrparas)
            self.tubdetcdisTarget.GetValuePattern().SetValue(' ')
            self.tubdetcdisTarget.GetValuePattern().SetValue(tubdetcdisTargetparas)
            self.tubdetcdisStep.GetValuePattern().SetValue(' ')
            self.tubdetcdisStep.GetValuePattern().SetValue(tubdetcdisStepparas)
            if self.tubdetcdisCurr.GetValuePattern().Value=='1200.000':
                print('sdd球管到平板的距离设置成功')
            else:
                print('sdd球管到平板的距离设置失败:',get_logCounts('tubdetcdissfail'), '次')
                logger.info('sdd球管到平板的距离设置失败日志:%s次', get_logCounts('tubdetcdisslogfail'))
        except Exception as e:
            print('sdd球管到平板的距离设置失败日志',str(e))
    def tubtutadiss(self,tubtutadisTargetparas,tubtutadisStepparas):
        try:
            self.tubtutadisButton.Click()
            # self.tubtutadisCurr.GetValuePattern().SetValue(' ')
            # self.tubtutadisCurr.GetValuePattern().SetValue(tubtutadisCurrparas)
            self.tubtutadisTarget.GetValuePattern().SetValue(' ')
            self.tubtutadisTarget.GetValuePattern().SetValue(tubtutadisTargetparas)
            self.tubtutadisStep.GetValuePattern().SetValue(' ')
            self.tubtutadisStep.GetValuePattern().SetValue(tubtutadisStepparas)
            if self.tubtutadisCurr.GetValuePattern().Value=='1200.000':
                print('sid球管到转台距离设置成功')
            else:
                print('sid球管到转台距离设置失败:',get_logCounts('tubtutadissfail'), '次')
                logger.info('sid球管到转台距离设置失败日志:%s次', get_logCounts('tubtutadisslogfail'))
        except Exception as e:
            print('sid球管到转台距离设置失败',str(e))
    def detechighs(self,detechighTargetparas,detechighStepparas):
        try:
            self.detechighButton.Click()
            # self.detechighCurr.GetValuePattern().SetValue(' ')
            # self.detechighCurr.GetValuePattern().SetValue(detechighCurrparas)
            self.detechighTarget.GetValuePattern().SetValue(' ')
            self.detechighTarget.GetValuePattern().SetValue(detechighTargetparas)
            self.detechighStep.GetValuePattern().SetValue(' ')
            self.detechighStep.GetValuePattern().SetValue(detechighStepparas)
            if self.detechighCurr.GetValuePattern().Value=='1200.000':
                print('平板高度设置成功')
            else:
                print('平板高度设置失败日志:',get_logCounts('detechighsfail'), '次')
                logger.info('平板高度设置失败日志:%s次', get_logCounts('detechighslogfail'))
        except Exception as e:
            print('平板高度设置失败',str(e))
    def tubehighs(self,tubehighsTargetparas,tubehighsStepparas):
        try:
            self.tubehighButton.Click()
            # self.tubehighCurr.GetValuePattern().SetValue(' ')
            # self.tubehighCurr.GetValuePattern().SetValue(tubehighsCurrparas)
            self.tubehighTarget.GetValuePattern().SetValue(' ')
            self.tubehighTarget.GetValuePattern().SetValue(tubehighsTargetparas)
            self.tubehighStep.GetValuePattern().SetValue(' ')
            self.tubehighStep.GetValuePattern().SetValue(tubehighsStepparas)
            if self.tubehighCurr.GetValuePattern().Value=='1200.000':
                print('球管高度设置成功')
            else:
                print('球管高度设置失败:',get_logCounts('tubehighsfail'), '次')
                logger.info('球管高度设置失败日志:%s次', get_logCounts('tubehighslogfail'))
        except Exception as e:
            print('球管高度设置失败日志',str(e))
    def detecfobacks(self,detecfobackTargetparas,detecfobackStepparas):
        try:
            self.detecfobackButton.Click()
            # self.detecfobackCurr.GetValuePattern().SetValue(' ')
            # self.detecfobackCurr.GetValuePattern().SetValue(detecfobackCurrparas)
            self.detecfobackTarget.GetValuePattern().SetValue(' ')
            self.detecfobackTarget.GetValuePattern().SetValue(detecfobackTargetparas)
            self.detecfobackStep.GetValuePattern().SetValue(' ')
            self.detecfobackStep.GetValuePattern().SetValue(detecfobackStepparas)
            if self.detecfobackCurr.GetValuePattern().Value=='1200.000':
                print('平板前后移动设置成功')
            else:
                print('平板前后移动设置失败:',get_logCounts('detecfobacksfail'), '次')
                logger.info('平板前后移动设置失败日志:%s次', get_logCounts('detecfobackslogfail'))
        except Exception as e:
            print('平板前后移动设置失败日志',str(e))
    def turtabfobacks(self,turtabfobacksTargetparas,turtabfobacksStepparas):
        try:
            self.turtabfobackButton.Click()
            # self.turtabfobackCurr.GetValuePattern().SetValue(' ')
            # self.turtabfobackCurr.GetValuePattern().SetValue(turtabfobacksCurrparas)
            self.turtabfobackTarget.GetValuePattern().SetValue(' ')
            self.turtabfobackTarget.GetValuePattern().SetValue(turtabfobacksTargetparas)
            self.turtabfobackStep.GetValuePattern().SetValue(' ')
            self.turtabfobackStep.GetValuePattern().SetValue(turtabfobacksStepparas)
            if self.turtabfobackCurr.GetValuePattern().Value=='1200.000':
                print('转台前后移动设置成功')
            else:
                print('转台前后移动设置失败',get_logCounts('turtabfobacksfail'), '次')
                logger.info('转台前后移动设置失败日志:%s次', get_logCounts('turtabfobackslogfail'))
        except Exception as e:
            print('转台前后移动设置失败',str(e))
# motionControlobj=motionControls()
# motionControlobj.rotatutabs('1200','1400')
# motionControlobj.moveButton.Click()
# motionControlobj.tubdetcdiss('1200','1401')
# motionControlobj.moveButton.Click()
# motionControlobj.tubtutadiss('1200','1402')
# motionControlobj.moveButton.Click()
# motionControlobj.detechighs('1200','1403')
# motionControlobj.moveButton.Click()
# motionControlobj.tubehighs('1200','1404')
# motionControlobj.moveButton.Click()
# motionControlobj.detecfobacks('1200','1405')
# motionControlobj.moveButton.Click()
# motionControlobj.turtabfobacks('1200','1406')
# motionControlobj.moveButton.Click()




