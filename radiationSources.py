import uiautomation
class radiationSource:
    def __init__(self):
        self.inputVoltage=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_29.LithiumXRayWidgetClass.widget.widget_2.lineEdit_TubekV')
        self.inputCurrent=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_29.LithiumXRayWidgetClass.widget.widget_3.lineEdit_TubemA')
        self.addVoltage=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_29.LithiumXRayWidgetClass.widget.widget_2.pushButton_kvAdd')
        self.reduceVoltage=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_29.LithiumXRayWidgetClass.widget.widget_2.pushButton_kvDecrease')
        self.addCurrent=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_29.LithiumXRayWidgetClass.widget.widget_3.pushButton_maAdd')
        self.reduceCurrent=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_40.stackedWidget_RightBar.page_13.widget_22.widget_29.LithiumXRayWidgetClass.widget.widget_3.pushButton_maDecrease')
    def Voltage(self,inputvoltage):
        self.inputVoltage.GetValuePattern().SetValue(' ')
        self.inputVoltage.GetValuePattern().SetValue(inputvoltage)
        self.addVoltage.Click()
        self.reduceVoltage.Click()
    def Current(self,inputcurrent):
        self.inputCurrent.GetValuePattern().SetValue(' ')
        self.inputCurrent.GetValuePattern().SetValue(inputcurrent)
        self.addCurrent.Click()
        self.reduceCurrent.Click()
# radiationSource().Voltage('180')
# radiationSource().Current('300')