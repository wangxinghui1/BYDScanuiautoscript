from bydconnect import connectApp
from Bydlogger import get_logger
from logCounts import get_logCounts
from login import userLogin
from newSample import newSamples
from scanType import scanTypes
#login class
for i in range(1):
    connectApp()
    userLogin().readuser()
    objnewsmp = newSamples()
    objnewsmp.readSample()
    objnewsmp.cmpnewsam()
    # 静态DR的扫描
    scanStaticDR=scanTypes()
    scanStaticDR.staticDR(600)

