import bydscan_startApplication
import configtest
import setusermanagement
import setsafetylock
for testprocess in range(10):
    #打开应用程序
    print('执行打开应用程序')
    bydscan_startApplication.startApplication()
    #用户登录
    print('执行用户登录')
    bydscan_startApplication.userlogin()
    #执行包含球管预热的流程
    print('执行球管预热')
    # bydscan_startApplication.tubePreheat()
    #执行扫描
    print('执行扫描')
    bydscan_startApplication.imageScan()
    #判断扫描结果是否出图
    # bydscan_startApplication.scanResult()
    #测试各个图像页面工具测量
    print('角页面切换')
    bydscan_startApplication.angleSwith()
    #单独测试开始扫描和暂停扫描
    print('执行扫描和暂停切换按钮测试')
    bydscan_startApplication.start_Stopscan()
    # operateWindowsWith(1621,763,1724,763)
    # operateWindowsPosition(1799,763,1899,763)
    # exitApplication()
    testprocess=testprocess+1
    bydscan_startApplication.logger.debug('测试了%s次',testprocess)
#执行设置新建用户管理
obj=setusermanagement.setusernameManagement()
for i in range(10):
    configtest.setpsdVif()
    configtest.inputpassword()
    configtest.storage()
    # configtest.aircorrection()
    # configtest.GeometricCorrection()
    # configtest.PlateCorrection()
    obj.deleteUserInfo()
    obj.readUserInfo()
    obj.getIndexvalue()
    obj.readeditUserInfo()
    obj.getIndexvalue()
    # 执行安全锁操作
    setsafetylock.openSafetyLock()
    setsafetylock.closeSafetyLock()
    i+=1
    setusermanagement.logger.debug('测试了%s次',i)