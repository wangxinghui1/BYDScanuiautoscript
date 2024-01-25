import time
import subprocess
import os
import uiautomation
from Bydlogger import get_logger
from logCounts import get_logCounts
# from systemSelfcheck import systemSelfcheck
import pandas as pd
logger=get_logger('newSamplelog','D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\log\\newsample.log')
df = pd.read_excel('D:\\TestAutoProject\\Byd\\venv\\Function_module\\Data\\testfile\\newsample1.xlsx')
class newSamples:
    def __init__(self):
        #新建样品表是否存在
        self.sampleList=uiautomation.TableControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_12.widget_13.widget_14.widget_46.tableWidget_sampleInfo')
        self.txbu_newSample=uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_12.widget_13.widget_14.widget_27.pushButton_newSample')
        self.sampleName=uiautomation.EditControl(AutomationId='mainAppWidget.newSampleWidget.frame.widget.lineEdit_newSampleEndName')
        self.serial=uiautomation.EditControl(AutomationId='mainAppWidget.newSampleWidget.frame.widget_2.lineEdit_newSampleEndNumber')
        self.bu_newSample=uiautomation.ButtonControl(AutomationId='mainAppWidget.newSampleWidget.frame.pushButton_newSampleEnd')
        self.sampleJumpPage=uiautomation.EditControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_12.widget_13.widget_14.widget_16.widget_47.mpPageChange_Widget.widget_2.lineEdit_JumpPage')
    def newSample(self,sampleName,serial):
        self.txbu_newSample.Click()
        self.sampleName.GetValuePattern().SetValue(' ')
        self.sampleName.GetValuePattern().SetValue(sampleName)
        self.serial.GetValuePattern().SetValue(' ')
        self.serial.GetValuePattern().SetValue(serial)
        self.bu_newSample.Click()
    def readSample(self):
        for i in df.index:
            # print('打印表格中的样品所有的行数:',df.index)
            # print('打印新建样品的行值:',i)
            for j in range(len(df.columns) - 1):
                # print('打印新建样品的列值:',j)
                self.newSample(df.iloc[i,j], df.iloc[i,j+1])
                if uiautomation.TextControl(Name='插入失败',time=0.2).Exists():
                    uiautomation.ButtonControl(Name='确定').Click()
                    print('新建样品序列号重复')
                    break
                #单个样品判断是否新建成功
                # sampleNamelist = self.sampleList.GetGridPattern().GetItem(k,l).Name
                # serialList = self.sampleList.GetGridPattern().GetItem(k,l+1).Name
                # print("打印新建后页面读取样品名称：",sampleNamelist, serialList)
                # if sampleNamelist and serialList is None:
                #     stop_flag = True
                #     break
                # if sampleNamelist in df.values and serialList in df.values:
                #     print((sampleNamelist, serialList), '已新建成功，且存在于excel')
                #     logger.info("(%s,%s),已新建成功，且存在于excel：%s 次", sampleNamelist, serialList,get_logCounts('newsamplesuccesCount'))
                # else:
                #     print((sampleNamelist, serialList), '已新建失败,且不存在于excel')
                #     logger.error("(%s,%s),已新建失败，且不存在于excel：%s 次", sampleNamelist, serialList,get_logCounts('newsamplefailCount'))
                #     if k == 1:
                #             uiautomation.ButtonControl(AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_12.widget_13.widget_14.widget_16.widget_47.mpPageChange_Widget.widget.pushButton_NextPage').Click()
                #     continue


    def cmpnewsam(self):
        stop_flag = False
        count = 0
        length = len(df.index) / 10
        print(length)
        try:
            while count < length and not stop_flag:
                count += 1
                print('打印count的值:',count)
                for i in range(10):
                    print('打印10个i的值:',i)
                    for j in range(1):
                        try:
                            if self.sampleList.GetGridPattern().GetItem(i, j) is None:
                                stop_flag = True
                                break
                            sampleNamelist =self.sampleList.GetGridPattern().GetItem(
                                i, j).Name
                            serialList = self.sampleList.GetGridPattern().GetItem(
                                i, j + 1).Name
                            # print(test3, test4)
                            if sampleNamelist in df.values and serialList in df.values:
                                print((sampleNamelist,serialList),'已新建成功，且存在于excel')
                                logger.info("(%s,%s),已新建成功，且存在于excel：%s 次",sampleNamelist,serialList,get_logCounts('newsamplesuccesCount'))
                            else:
                                print((sampleNamelist,serialList),'已新建失败,且不存在于excel')
                                logger.error("(%s,%s),已新建失败，且不存在于excel：%s 次",sampleNamelist,serialList,get_logCounts('newsamplefailCount'))
                            if i ==9:
                                uiautomation.ButtonControl(
                                    AutomationId='mainAppWidget.stackedWidget_main.page_2.widget_7.widget_12.widget_13.widget_14.widget_16.widget_47.mpPageChange_Widget.widget.pushButton_NextPage').Click()
                            continue
                        except Exception as e:
                            print('内层循环发生异常:',e)
                    # print('测试continue:',stop_flag)
                    if stop_flag:
                        break
                # print('测试stop_flag:',stop_flag)
                if stop_flag:
                    break
        except Exception as e:
            print('外层循环发生异常:',e)

    def deleteSample(self):
        # sampleNamelist = self.sampleList.GetGridPattern().GetItem(0, 2)
        # while sampleNamelist.Exists():
        #     sampleNamelist.Click()
        #     uiautomation.RightClick(315,240)
        #     uiautomation.RightClick(342,261)
        # 获取第一个网格元素
        # 等待元素出现并进行循环操作
        self.sampleJumpPage.Click()
        self.sampleJumpPage.SendKeys('{Ctrl}{A}')
        self.sampleJumpPage.SendKeys('{delete}')
        self.sampleJumpPage.SendKeys('1')
        self.sampleJumpPage.SendKeys('{enter}')
        # print('test1')
        try:
            if self.sampleJumpPage.GetValuePattern().Value == '1':
                print('当前处于第一页')
                try:
                    n=0
                    while True:
                        # 等待元素出现
                        if self.sampleList.GetGridPattern().GetItem(0,1) is None:
                            print('测试样品全部被删除成功')
                            break
                        elif self.sampleList.GetGridPattern().GetItem(0,1).Exists():
                                #获取此时第一行的样品
                                sampleNamelistnow=self.sampleList.GetGridPattern().GetItem(0,1).Name
                                serialListnow=self.sampleList.GetGridPattern().GetItem(0,2).Name
                                print('打印样品列表名称和样品序列号:',sampleNamelistnow,serialListnow)
                                # 点击元素并打开右键菜单
                                self.sampleList.GetGridPattern().GetItem(0,1).Click()
                                uiautomation.RightClick(315, 240)
                                uiautomation.RightClick(342,261)
                                if sampleNamelistnow and serialListnow not in df.values:
                                    # print('当前第',get_logCounts('newsampledeletesuccesCount'),'个样品列表名称和样品序列号:',sampleNamelistnow,serialListnow,'被删除成功')
                                    logger.info("当前第(%s)个样品列表名称和样品序列号:'(%s,%s),被删除成功", get_logCounts('newsampledeletesuccesCount'),sampleNamelistnow,serialListnow)
                                else:
                                    # print('当前第',get_logCounts('newsampledeletefailCount'),'个样品列表名称和样品序列号:',sampleNamelistnow,serialListnow,'删除失败')
                                    logger.error("当前第(%s)个样品列表名称和样品序列号:'(%s,%s),被删除失败", get_logCounts('newsampledeletefailCount'),sampleNamelistnow,serialListnow)

                        n+=1
                    print('一共删除了:',n,'个扫描样品')
                except Exception as e:
                    print('删除样品失败:',e)
            else:
                print('当前页面不是第一页')
        except Exception as e:
            print('当前页面不是第一页:',e)



objnewsmp=newSamples()
objnewsmp.readSample()
objnewsmp.cmpnewsam()
objnewsmp.deleteSample()
