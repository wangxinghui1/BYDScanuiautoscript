import uiautomation
from radiationSources import radiationSource
class scanTypes:
    def __init__(self):
        self.staticdrButton=uiautomation.RadioButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.widget_16.pushButton_DRTab')
        self.largareinsButton=uiautomation.RadioButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.widget_16.pushButton_CheckTab')
        self.tomoButton=uiautomation.RadioButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.widget_16.pushButton_TomoTab')
        self.biasButton=uiautomation.RadioButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.widget_16.pushButton_offsetTab')
        self.ctButton=uiautomation.RadioButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.widget_16.pushButton_CTTab')
        self.spiralButton=uiautomation.RadioButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.widget_16.pushButton_spiralTab')
        self.stadrnumofveyInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_3.widget_28.lineEdit_overlayCount')
        self.lagerstartInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_4.widget_31.lineEdit_startSplice')
        self.lagerendInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_4.widget_31.lineEdit_endSplice')
        self.tomostartInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_9.widget_32.lineEdit_startAngle')
        self.tomoendInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_9.widget_32.lineEdit_endAngle')
        self.tomonumofveyInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_9.widget_34.lineEdit_TomoOverlayCount')
        self.biassizeInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_10.widget_35.lineEdit_EccSize')
        self.biascolInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_10.widget_36.lineEdit_EccAcqCount')
        self.ctcolInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_11.widget_38.lineEdit_CTAcqCount')
        self.spiralstartInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_12.widget_40.lineEdit_startPosSpiral')
        self.spiralendInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_12.widget_40.lineEdit_endPosSpiral')
        self.spiralscspdInput=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_11.widget_15.scrollArea_2.qt_scrollarea_viewport.scrollAreaWidgetContents_2.stackedWidget_scan.page_12.widget_41.lineEdit_SpiralScanSpeed')
        self.previewButton=uiautomation.CheckBoxControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_44.LithiumSportControlWidgetClass.widget_12.checkBox_prview')
    def staticDR(self,spiralscspdpar):
        # radiationSource().Voltage('180')
        # radiationSource().Current('300')
        self.staticdrButton.Click()
        self.stadrnumofveyInput.GetValuePattern().SetValue(' ')
        self.stadrnumofveyInput.GetValuePattern().SetValue(spiralscspdpar)

    def largareiNS(self,startpar,endpar):
        self.largareinsButton.Click()
        self.lagerstartInput.GetValuePattern().SetValue(' ')
        self.lagerstartInput.GetValuePattern().SetValue(startpar)
        self.lagerendInput.GetValuePattern().SetValue(' ')
        self.lagerendInput.GetValuePattern().SetValue(endpar)
    def Tomo(self,startpar,endpar,numofveypar):
        self.tomoButton.Click()
        self.tomostartInput.GetValuePattern().SetValue(' ')
        self.tomostartInput.GetValuePattern().SetValue(startpar)
        self.tomoendInput.GetValuePattern().SetValue(' ')
        self.tomoendInput.GetValuePattern().SetValue(endpar)
        self.tomonumofveyInput.GetValuePattern().SetValue(' ')
        self.tomonumofveyInput.GetValuePattern().SetValue(numofveypar)
    def Bais(self,biassizepar,biasscolpar):
        self.biasButton.Click()
        self.biassizeInput.GetValuePattern().SetValue(' ')
        self.biassizeInput.GetValuePattern().SetValue(biassizepar)
        self.biascolInput.GetValuePattern().SetValue(' ')
        self.biascolInput.GetValuePattern().SetValue(biasscolpar)
    def CT(self,ctcolpar):
        self.ctButton.Click()
        self.ctcolInput.GetValuePattern().SetValue(' ')
        self.ctcolInput.GetValuePattern().SetValue(ctcolpar)
    def Spiral(self,spistapar,spiendpar,spisppar):
        self.spiralButton.Click()
        self.spiralstartInput.GetValuePattern().SetValue(' ')
        self.spiralstartInput.GetValuePattern().SetValue(spistapar)
        self.spiralendInput.GetValuePattern().SetValue(' ')
        self.spiralendInput.GetValuePattern().SetValue(spiendpar)
        self.spiralscspdInput.GetValuePattern().SetValue(' ')
        self.spiralscspdInput.GetValuePattern().SetValue(spisppar)

scanStaticDR=scanTypes()
# scanStaticDR.staticDR('600')
scanStaticDR.Tomo('1','360','1800')