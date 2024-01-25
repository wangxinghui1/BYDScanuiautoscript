# 打开应用程序
from bydconnect import connectApp
# 登录应用程序
from login import userLogin
# 系统自检功能
from systemSelfcheck import systemSelfcheck
#新建样品功能
from newSample import newSamples
# 扫描状态判断
from scanCommState import scanCommStates
#输入电源
from radiationSources import radiationSource
radiationSource().Voltage('180')
radiationSource().Current('300')
# 输入平板参数
from Detector import FrameRates
FrameRates().framerates('30')
FrameRates().pixelMerges1()
# 输入运动控制参数
from motionControl import motionControls
motionControlobj=motionControls()
motionControlobj.rotatutabs('1200','1400')
motionControlobj.moveButton.Click()
motionControlobj.tubdetcdiss('1200','1401')
motionControlobj.moveButton.Click()
motionControlobj.tubtutadiss('1200','1402')
motionControlobj.moveButton.Click()
motionControlobj.detechighs('1200','1403')
motionControlobj.moveButton.Click()
motionControlobj.tubehighs('1200','1404')
motionControlobj.moveButton.Click()
motionControlobj.detecfobacks('1200','1405')
motionControlobj.moveButton.Click()
motionControlobj.turtabfobacks('1200','1406')
motionControlobj.moveButton.Click()
# 输入扫描类型
from scanType import scanTypes
scanStaticDR=scanTypes()
scanStaticDR.staticDR('600')
from imageScan import imageScans
imagesanObj=imageScans()
imagesanObj.imageScan()
