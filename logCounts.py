logCounts={'connCountsuccess':0,'connCountfail':0,'connCountlogsuccess':0,'connCountlogfail':0,'loginCountsuccess':0,
           'loginCountfail':0,'loginCountlogsuccess':0,'loginCountlogfail':0,'commfailCount':0,'mechfailCount':0,
           'tubefailCount':0,'detecfailCount':0,'slchecknotExitCount':0,'commfaillogCount':0,'mechfaillogCount':0,
           'tubefaillogCount':0,'detecfaillogCount':0,'slchecknotExitlogCount':0,'newsamplesuccesCount':0,
           'newsamplefailCount':0,'newsamplesuccesCount':0,'newsamplefailCount':0,'newsampledeletesuccesCount':0,
           'newsampledeletefailCount':0,'CommsuccessCount':0,'CommfailCount':0,'expsucCount':0,'expfailCount':0,
           'commstCmpCount':0,'CommstfailCount':0,'mechstCmpCount':0,'MechstfailCount':0,'tubestCmpCount':0,
           'TubestfailCount':0,'DetecstfailCount':0,'scanCommfailCount':0,'scanCommfaillogCount':0,'scanTubefailCount':0,'scanTubefaillogCount':0,
           'scanDetectfailCount':0,'scanDetectfaillogCount':0,'scanSafelockfailCount':0,'scanSafelockfaillogCount':0,'scanCommExcepCount':0,'scanCommExceplogCount':0,
           'scanTubeExcepCount':0,'scanTubeExceplogCount':0,'scanDetectExcepCount':0,'scanDetectExceplogCount':0,'scanSafelockExcepCount':0,'scanSafelockExceplogCount':0,
            'rotatutabsfail':0,'rotatutabslogfail':0,'tubdetcdissfail':0,'tubdetcdisslogfail':0,'tubtutadissfail':0,'tubtutadisslogfail':0,'detechighsfail':0,'detechighslogfail':0,
            'tubehighsfail':0,'tubehighslogfail':0,'detecfobacksfail':0,'detecfobackslogfail':0,'turtabfobacksfail':0,'turtabfobackslogfail':0,'startscanExposurefailCount':0,
            'startscanExposurefaillogCount':0,'imageScansuccCount':0,'imageScansucclogCount':0,'imageScanfailCount':0,'imageScanfaillogCount':0,
}

def get_logCounts(logCountParam):
    global logCounts
    logCounts[logCountParam]+=1
    return logCounts[logCountParam]
# print(get_logCounts('connCount'))