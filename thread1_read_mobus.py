from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
init_read= False
from config import *
import time
key=0
key_check=0
list_Buffer1=[]
list_countCOB=[]
list_result=[]
list_issue=[]
list_issue_export=[]
_count=0
_count_issue=0
_key_condition=False
_list_issue_final=[]
import mysql.connector
from datetime import datetime
#from time import time,ctime
from playsound import playsound
def connect_database():
    try:
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="solar_database"
        )
    except NameError:
        print("CANT CONNECT DATA")
class FloatModbusClient(ModbusClient):
    def read_float(self , address, number=1):
        reg_l = self.read_holding_registers(address,number * 2)
        if reg_l:
            return [utils.decode_ieee(f) for f  in utils.word_list_to_long(reg_l)]
        else:
            reg_l = [16000,16000]
            return [utils.decode_ieee(f) for f  in utils.word_list_to_long(reg_l)]    
c = FloatModbusClient()
def Connect_MbTCP(ip,func,reg_addr,reg_nb): #data=Connect_MbTCP("192.168.1.151",3,1,15)
    init_read= False
    SERVER_HOST = ip
    SERVER_PORT = 502
    c.host(SERVER_HOST)
    c.port(SERVER_PORT)
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))
    if c.is_open():
        if func==3:
            regs_data = c.read_float(reg_addr,reg_nb)
            return regs_data
            c.close() #đóng tab để kết nối tab mới
        if func==4:
            regs_data=c.read_input_registers(reg_addr,reg_nb)
            return regs_data
            c.close()
        else:
            print("PLS! choose FunctionCod")
    print("CAN'T CONNECT")

def read_modbus():
    print("read func 1")
    global _list_issue_final
    _count=0
    _count_issue=0
    list_issue=[]
    list_issue_export=[]
    # nhận dữ liệu thô và xử lý
    while _count<10:
        _time=datetime.now().time()
        for i in range(len(keyIVT_config)):# get name inveter
            list_Buffer1=[]
            list_countCOB=list(IVT[keyIVT_config[i]].values())#count COB in IVT
        
            list_Buffer1=Connect_MbTCP(ip_config[keyIVT_config[i]],3,1,15) #connect data IVT
            list_result=[]# reset before append data
            for z in range(len(list_Buffer1)):
                _var=list_Buffer1[z]/list_countCOB[z]
                list_result.append(_var)
            _max=max(list_result)
            _var_compare=(_max/100)*5 #--------------------------------- giá trị cài đặt 
            
            for x in range(len(list_result)):
                if ((list_result[x]+_var_compare)<_max):
                    list_issue.append(list(IVT[keyIVT_config[i]].keys())[x])
        _count=_count+1
        time.sleep(2) #--------------------------------------------------- time =30
    # bóc tách dữ liệu 80%
    
    for y in range(len(list_issue)):
        _count_issue=0
        _var_compare=0
        for w in range(len(list_issue)):
            if list_issue[y]==list_issue[w]:
                _count_issue=_count_issue+1
        if _count_issue>8: # xuất hiện hơn 70% trong mảng
            if len(list_issue_export)==0:
                list_issue_export.append(list_issue[y])#add data first time
            else:
                for a in range(len(list_issue_export)):
                    if list_issue[y]==list_issue_export[a]:
                        _var_compare=_var_compare+1
                if _var_compare<1:
                        list_issue_export.append(list_issue[y])
                else:
                    _var_compare=0
    _count=0
    find_min_of_min(list_issue_export)  #code finish
    list_issue=[]
    list_result=[]
    
def find_min_of_min(data):
    print("read func 2")
    list_min=[]
    _key_list_min=0
    i=0
    j=0
    z=0
    w=0
    if len(data)>0:
        for i in range(len(data)):
            for j in range(len(keyIVT_config)): 
                for z in range(len(IVT[keyIVT_config[j]].keys())):
                    if data[i]==list(IVT[keyIVT_config[j]].keys())[z]:   
                        if len(list_min)==0:#list INVERTER
                            list_min.append(keyIVT_config[j])# TÊN CÁC INVERTER CO SỰ CỐ  
                        else:
                            for w in range(len(list_min)):
                                if list_min[w]==keyIVT_config[j]:
                                    _key_list_min=_key_list_min+1
                                else:
                                    _key_list_min=_key_list_min
                            if _key_list_min>0:
                                #print("-")
                                _key_list_min=0
                            else:
                                list_min.append(keyIVT_config[j])
    #print(list_min)
    read_list_min(list_min,data)# ĐÃ TÌM ĐƯỢC CÁC INVERTER CÓ SỐ COB TÍN HIỆU YẾU.
    print(list_min)
    
    
def read_list_min(data,data_lisCOBmin):
    print("read func 3")
    _list_value_min=[]
    _list_key_min=[]
    _list_min_export=[]
    _var=0
    i=0
    z=0
    list_Buffer1=[]
    if len(data)>0:# bắt đầu đọc lại
        for i in range(len(data)):
            list_countCOB=list(IVT[data[i]].values())
            list_Buffer1=Connect_MbTCP(ip_config[data[i]],3,1,15)
            list_result=[]# reset before append data
            for z in range(len(list_Buffer1)):
                _var=list_Buffer1[z]/list_countCOB[z]
                list_result.append(_var)
            _max=max(list_result)
            
            _var_compare=(_max/100)*5#----------------------------------------------------
            for y in range(len(list_result)):
                if list_result[y]<(_max-_var_compare):
                    _list_value_min.append(list_result[y])
                    _list_key_min.append(list(IVT[data[i]].keys())[y])
            #------------------------------ THÊM CODE 11/01/2021 ------------------------------
            # code tăng thêm tính ổn định cho chương trình
           
            _var=0
            for p in range(len(_list_key_min)):
                for q in range(len(data_lisCOBmin)):# dữ liệu đọc từ đầu chương trình
                    if _list_key_min[p]== data_lisCOBmin[q]:
                        _var=_var+1
                if _var==len(_list_key_min): #  đầu ra dữ liệu chuẩn so với 10 lần đọc trước
                    if _var<3:
                        # thực hiện xuất dữ liệu ngay lập tức
                        w=0
                        for w in range(len(_list_value_min)):
                            print("issue type 1 a")
                            print(_list_key_min[w])
                            _list_min_export.append(_list_key_min[w])
                    else:
                        _var_max=max(_list_value_min)
                        _var_compare=(_var_max/100)*4#-----------------------------------------------------------------
                        for e in range(len(_list_value_min)):
                            if _list_value_min[e]<_var_max-_var_compare:
                                #add data to list and move to other function
                                _list_min_export.append(str(_list_key_min[e])) # sửa 17:21 ngày 13/01

            #----------------------------------------------------------------------------------
            # sửa 17:21 ngày 13/01
            '''
            if len(_list_key_min)<2:
                w=0
                for w in range(len(_list_value_min)):
                    print("issue type 1 a")
                    print(_list_key_min[w])
                    _list_min_export.append(_list_key_min[w])
                    
            else:
                w=0
                _var_compare=(max(_list_value_min)/100)*6
                for w in range(len(_list_value_min)):
                    if _list_value_min[w]< (max(_list_value_min)-_var_compare):
                        #print("issue type 2")
                        #print(_list_key_min[w]) #----------------------------------------------------finish
                        _list_min_export.append(_list_key_min[w])
            
            #them doan code xuat du lieu tung IVT
            if len(_list_min_export)>0 and len(_list_min_export)<3:
                print("issue type 1")
                print(_list_min_export)
            '''
            
            load_data(_list_min_export)
            print(_list_min_export)
            _list_min_export=[]
            _list_value_min=[]
            _list_key_min=[]
            
            # load data lên cơ sở dữ liệu
def load_data(data):  #FINISH TEST
    print("read func 4")
    _result=[]
    #step1: check data in table_buffer
    #step2: compare data
    #step3:write or move data to final_table
    _count_sql=0
    try:
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="solar_database"
                )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name FROM buffer_table")
        myresult = mycursor.fetchall()
        #boc tach [('name 2',), ('name 3',)]
        for t in range(len(myresult)):
            _result_buff=myresult[t]
            _result.append(_result_buff[0])
        print(_result) # 
        
    except NameError:
        print("CANT CONNECT DATA")
    _myresult=_result
    
    
    if len(_myresult)>0:#old
        print(_myresult)
        for r in range(len(data)):
            for t in range(len(_myresult)):
                if data[r]==_myresult[t]:
                    _count_sql=_count_sql+1
            if _count_sql==0:
                #add data to buffer
                handle_database(1,data[r])
                print("add data")
            else:
                _count_sql=0   
        _count_sql=0 
              
        for r in range(len(_myresult)):
            for t in range(len(data)):
                if _myresult[r]==data[t]:
                    _count_sql=_count_sql+1
            if _count_sql==0:# old and new different: dele old
                #delete data from buffer
                handle_database(2,_myresult[r])
                print("delete data")
            else:
                _count_sql=0
    else:
        for y in range(len(data)):
            handle_database(1,data[y])
               
    print("step 2")
                
def handle_database(_key_handle,_data): #FINISH TEST
    print("read func 5")
    #1 add data
    #2 clear data and move to new database
    #3 
    _time_stop=datetime.now().time()
    #_time_stop=ctime() #------------------------------------------------------------ CHUA DOC DUOC DU LIEU
    if(1<<2):# điều kiện thời gian đọc------------------------------------------------
        print("step 3")
        
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="solar_database"
        
        )
        if(_key_handle==1): #add data
            mycursor = mydb.cursor()
            sql = "INSERT INTO buffer_table (name, address) VALUES (%s, %s)"
            val = (str(_data),str(_time_stop))
            mycursor.execute(sql, val)
            mydb.commit()
            func_sound()
            print(mycursor.rowcount, "record inserted to buffer_table.")
            
        if(_key_handle==2):#dele data
            
            mycursor = mydb.cursor()
            sql = "SELECT * FROM buffer_table WHERE name = %s "
            add=(str(_data), )
            mycursor.execute(sql,add)
            myresult = mycursor.fetchall()
            _tuple=myresult[0]
           
            sql = "INSERT INTO issue_table (ID, TIME_START, TIME_STOP) VALUES (%s, %s,%s)"
            val = ( _tuple[1], _tuple[2],_time_stop)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted to issue_table.")
            
            
            sql = "DELETE FROM buffer_table WHERE name = %s "
            add=(str(_data), )
            mycursor.execute(sql,add)
            mydb.commit()
            print(mycursor.rowcount, "record(s) deleted")
            
def insert_datasql(name,time):
    print("read func 6")
    try:
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="solar_database"
        )
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO buffer_table (name, address) VALUES (%s, %s)"
        val = (name, time)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except NameError:
        print("CAN NOT INSERT DATA")
        
        
def condition_request():
    print("read func 7")
    _var_weather01=Connect_MbTCP(ip_weather_config[0],4,1,1)
    
    _var_weather02=Connect_MbTCP(ip_weather_config[1],4,1,1)
    if (_var_weather01[0]>5000)and(_var_weather02[0]>5000):
        _key_condition=True
    else:
        _key_condition=False
    print("IRADIAN NOW: "+str(_var_weather01)+" AND "+ str(_var_weather02))
    return _key_condition
    #time.sleep(1)       


#function write 17/01/2021 NOT TEST-------------------------------------------------------
def read_information():
    print("read func 8")
    # power of 8 IVT
    # radiation
    # wind
    # status: run or off
    value_information=[]
    key_information=["INVERTER01","INVERTER02","INVERTER03","INVERTER04","INVERTER05","INVERTER06","INVERTER07","INVERTER08",
                     "INVERTER09","INVERTER10","INVERTER11","INVERTER12","INVERTER13","INVERTER14","INVERTER15","INVERTER16"
                     ,"WEATHER1-1"]
    _key_weather=(1,4)
    for i in range(len(key_information)):
        if key_information[i]!="WEATHER1-1":
            try:
                _var=Connect_MbTCP(ip_config[key_information[i]],4,31,1)
                if _var>0:
                    value_information.append(_var)
                else:
                    value_information.append(1)
            except:
                value_information.append(1)
        else:
            for j in (1,4):
                try:
                    _var=Connect_MbTCP(ip_config[key_information[i]],4,j,1)
                    if _var>0:
                        value_information.append(_var)
                    else:
                        value_information.append(1)
                except:
                    value_information.append(1)
    return value_information    
    print(value_information  )
def func_sound():
    playsound("short_sound_effect.mp3",True)            

def read_data():
    read_modbus()
    time.sleep(1)
    return "finish"     
#boctach=['5-CM-2-11', '5-CM-2-10','5-CM-2-09']   
#boctach=['5-CM-2-11','5-CM-2-09','5-CM-2-04']   
#load_data(boctach)                   
#read_information()
#read_modbus()
#handle_database(1,"5-CM-2-11")
#read_information()
#data=Connect_MbTCP("192.168.1.1",4,31,1)
#print(data)