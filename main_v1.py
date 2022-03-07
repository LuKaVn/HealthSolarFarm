import sys
import time
import platform
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from ui import Ui_MainWindow

from PyQt5.QtCore import QTimer

import subprocess as sp
#pyuic5 -x mainui.ui -o ui.py
#pyrcc5 -o icon_rc.py icon.qrc
from config import *
from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
from PyQt5.QtCore import QRunnable, QThreadPool, QTimer, pyqtSlot

_key_thread=0
buf_1_time=0 # bien tam doc du lieu 1 lan.
interval = 2
connect=["NO","NO","NO","NO","NO","NO","NO","NO","NO","NO","NO","NO","NO","NO","NO","NO"]
_key_readINmain=0

#--------------------------------------10/01/2021 
sys.path.append(".")
from test import *
from thread1_read_mobus import *
#--------------------------------------11/01/2021
_key_sql=0
_key_setting=0
#--------------------------------------14/01/2021
_key_thread1=0
_key_thread2=0
_data=[("a","b"),]
#---------------------------------------16/01/2021
from thread2_read_sql import *
_key_control=0
from datetime import datetime

class MainWindow(QMainWindow):
    global ip
    global name_ip
    global connect
    global _key_sql
    global _key_setting
    global _key_thread1
    global _key_thread2
    global _key_control
    
    global _data
    def __init__(self):
        global _key_thread
        super().__init__()
        #-------------------------------
        #function.export()
        self.threadpool = QThreadPool()
        print(
            "Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()
        )
        #-------------------------------
        self.buf_1_time=0
        self.ui_import = Ui_MainWindow()
        self.ui_import.setupUi(self)
        #self.threadpool.start(Worker(keywords=1))
        self.ui_import.btn_main.clicked.connect(lambda : self.main_layout())
        self.ui_import.btn_setup.clicked.connect(lambda : self.setting_layout())
        self.ui_import.btn_history.clicked.connect(lambda : self.history_layout())
        self.ui_import.btn_info.clicked.connect(lambda : self.infor_layout())
        
        
        #lock-----------------------------16/01
        self.timer = QTimer()
        self.timer.setInterval(2000) # thoi gian doc du lieu 1 lan
        #self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
        #self.show_information(read_information()) #------------------------------------------------FINISH but not test
        
        #------------------------------------------
        # stop code hear: 14/01/2021
        #self.show_issue_(_data)
        #------------------------------------------#
        #self.show_table()
    def start_request(self):
        print("function read data")   
        #self.threadpool.start(Worker(keywords=1))
    def stop_request(self):
        print("function stop read data") 
    def main_layout(self):
        self.ui_import.stackedWidget_content.setCurrentIndex(0)
        print("main Layout")
        
    def setting_layout(self):
        self.ui_import.stackedWidget_content.setCurrentIndex(1)
        print("setting Layout")
        #print(time.gmtime())
        #print(time.localtime().tm_min)
        
    def history_layout(self):
        self.ui_import.stackedWidget_content.setCurrentIndex(2)
        print("history Layout")
        
    def infor_layout(self):
        self.ui_import.stackedWidget_content.setCurrentIndex(3)
        print("history Layout")

    def setting_table(self):
        print("click")
        f = open("fileWr.txt", "w")
        _data=""
        for a in range(16):
            _data=_data+keyIVT_config[a]+" "
            for b in range(15):
                _var=self.ui_import.tableWidget_setting.item(b,a).text()
                _data=_data+_var+" "
        f.write(_data)
        f.close() 
    '''
    def cancel_setting_table(self):
        self.show_table()
    '''
    def show_issue_(self,key,data):
        #key=1 : table buffer
        #key=2 : table issue
        if len(data)>0:
            _count_issue=len(data)
        else:
            _count_issue=0
        if key==1:
            self.ui_import.tableWidget_show.clear()
            for l in range(self.ui_import.tableWidget_show.rowCount()):
                #print(self.ui_import.tableWidget_show.rowCount())
                self.ui_import.tableWidget_show.removeRow(l)
            #print(_count_issue)
            if (_count_issue>0):
                for p in range(len(data)):
                    self.ui_import.tableWidget_show.insertRow(p)
                    for o in range(2):
                        self.ui_import.tableWidget_show.setItem(p,o,QTableWidgetItem(data[p][o]))
                    
        if key==2:
            self.ui_import.tableWidget_record.clear()
            for l in range(self.ui_import.tableWidget_record.rowCount()):
                self.ui_import.tableWidget_record.removeRow(l)
            #print(_count_issue)
            if (_count_issue>0):
                for p in range(len(data)):
                    self.ui_import.tableWidget_record.insertRow(p)
                    for o in range(3):
                        self.ui_import.tableWidget_record.setItem(p,o,QTableWidgetItem(data[p][o]))        


    def recurring_timer(self):# Các Thread được gọi trong này
        global _key_thread1
        global _key_thread2
        #print("call")
        self.show_issue_(1,request_sql_table1())# out of time
        self.show_issue_(2,request_sql_table2())# out of time-----------------------------------need move to if funtion bellow
        _str_test=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.show_information(_str_test)
        if time.localtime().tm_hour>9 :
            if time.localtime().tm_hour<15 :
                #if(condition_request==True):# TEST condition chua duoc thuc hien
                if(True):#--------------------- chay chuong trinh trong luc test
                    if(_key_thread1==0):
                        _key_thread1=1
                        self.threadpool.start(Worker(keywords=1))
                '''
                if (time.localtime().tm_min%interval)==0:
                    if self.buf_1_time==0:
                        print("time to read data")
                        #self.connect_mysql()
                        #self.buf_1_time=1
             
                else:
                    self.buf_1_time=0
                '''
                    
    #def connect_database():
    def connect_mysql(self):
        self.export_annouce(1)
        try:
            mydb = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="solar_database"
            )
            mycursor = mydb.cursor()
            self.export_annouce(2)
            _key_sql=1
            
        except:
            print("Can't connect Database")
            self.export_annouce(3)
            _key_sql=0
    '''       
    def show_table(self):
        #f = open("set_cob.txt", "r")
        f = open("fileWr.txt", "r")
        x = re.split("\s", f.read())
        for a in range(len(keyIVT_config)):
            for i in range(len(x)):
                if x[i]==keyIVT_config[a]:
                    for y in range(15):
                        #print(x[y+i+1])
                        self.ui_import.tableWidget_setting.setItem(y,a,QTableWidgetItem(x[y+i+1]))
    '''
    def export_annouce(self,_key_annouce):
        if(_key_annouce==1):
            self.ui_import.label_annouce.setText("SQL Connecting....")
        if(_key_annouce==2):
            self.ui_import.label_annouce.setText("SQL Connected")
        if(_key_annouce==3):
            self.ui_import.label_annouce.setText("SQL Disconnect")
        if(_key_annouce==4):
            self.ui_import.label_annouce.setText("Inveter Connecting....")
        if(_key_annouce==5):
            self.ui_import.label_annouce.setText("Inveter Connected")

    def show_information(self,data): # 17/01/2022 đọc dữ liệu và show
        key_label=data
        if len(key_label)>0:
            self.ui_import.label_st1.setText(str(key_label[0]+key_label[1]))
            self.ui_import.label_st2.setText(str(key_label[2]+key_label[3]))
            self.ui_import.label_st3.setText(str(key_label[4]+key_label[5]))
            self.ui_import.label_st4.setText(str(key_label[6]+key_label[7]))
            self.ui_import.label_st5.setText(str(key_label[8]+key_label[9]))
            self.ui_import.label_st6.setText(str(key_label[10]+key_label[11]))
            self.ui_import.label_st7.setText(str(key_label[12]+key_label[12]))
            self.ui_import.label_st8.setText(str(key_label[14]+key_label[15]))
            self.ui_import.lcdNumber_radiation.display(str(key_label[16]))
            self.ui_import.lcdNumber_wind.display(str(key_label[17]))
        
class Worker(QRunnable): 
    global _key_thread
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
    @pyqtSlot()
    def run(self):
        global _key_thread1
        global _key_thread2
        print(self.args, self.kwargs)
        
        if self.kwargs["keywords"]==1:#read data and up to database
            print("Thead 1 start")
            _key_thread1=1
                #--------------------------------------------#
                #                                            #
                #        import code thread 1                #
                #                                            #
                #--------------------------------------------#
            _return_thread1=read_data()
            if _return_thread1=="finish":
                _key_thread1=0
                print("Thead 1 stop")
        
        if self.kwargs["keywords"]==2:
            print("Thead 2 start")
            _key_thread2=1
                #--------------------------------------------#
                #                                            #
                #        import code thread 2                #
                #                                            #
                #--------------------------------------------#
            _key_thread2=0
            print("Thead 2 stop")
                

# end::Worker[]
# tag::init[]            

if __name__ == "__main__":
    #global _key_control
    while True:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec_()
    

