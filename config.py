
isus_dict = {
    "issue_1":[],
    "issue_2":[],
    "issue_3":[],
    "issue_4":[],
    "issue_5":[]
}
#keyIVT_config=('WEATHER1-1', 'WEATHER1-2', 'WEATHER1-3', 'WEATHER2-1', 'WEATHER2-2',
#              'WEATHER2-3','IVT01_1', 'IVT01_2', 'IVT02_1', 'IVT02_2', 'IVT03_1', 'IVT03_2',
#              'IVT04_1', 'IVT04_2', 'IVT05_1', 'IVT05_2', 'IVT06_1', 'IVT06_2', 'IVT07_1', 'IVT07_2', 'IVT08_1', 'IVT08_2'
#           )
keyIVT_config=['IVT01_1', 'IVT01_2', 'IVT02_1', 'IVT02_2', 'IVT03_1', 'IVT03_2',
              'IVT04_1', 'IVT04_2', 'IVT05_1', 'IVT05_2', 'IVT06_1', 'IVT06_2', 'IVT07_1', 'IVT07_2', 'IVT08_1', 'IVT08_2'
                ]
keyIVT_ip=['IVT01_1', 'IVT02_1', 'IVT03_1','IVT04_1', 'IVT05_1', 'IVT06_1', 'IVT07_1',  'IVT08_1',
                ]
keyWEATHER_config=["WEATHER1-1","WEATHER1-2","WEATHER1-3","WEATHER2-1","WEATHER2-2","WEATHER2-3"]
buff_test=[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
buff_value=[0,0]
ip_weather_config=("192.168.1.111","192.168.1.114")
ip_config = {
    # import config data 17/01/2022
    "INVERTER01": "192.168.1.1",
    "INVERTER02": "192.168.1.2",
    "INVERTER03": "192.168.1.3",
    "INVERTER04": "192.168.1.4",
    "INVERTER05": "192.168.1.5",
    "INVERTER06": "192.168.1.6",
    "INVERTER07": "192.168.1.7",
    "INVERTER08": "192.168.1.8",
    "INVERTER09": "192.168.1.9",
    "INVERTER10": "192.168.1.10",
    "INVERTER11": "192.168.1.11",
    "INVERTER12": "192.168.1.12",
    "INVERTER13": "192.168.1.13",
    "INVERTER14": "192.168.1.14",
    "INVERTER15": "192.168.1.15",
    "INVERTER16": "192.168.1.16",
    
    "WEATHER1-1": "192.169.1.111",
    "WEATHER1-2": "192.169.1.112",
    "WEATHER1-3": "192.169.1.113",
    "WEATHER2-1": "192.169.1.114",
    "WEATHER2-2": "192.169.1.115",
    "WEATHER2-3": "192.169.1.116",
    
    "IVT01_1": "192.168.1.151",
    "IVT01_2": "192.168.1.152",
    "IVT02_1": "192.168.1.153",
    "IVT02_2": "192.168.1.154",
    "IVT03_1": "192.168.1.155",
    "IVT03_2": "192.168.1.156",
    "IVT04_1": "192.168.1.157",
    "IVT04_2": "192.168.1.158",
    "IVT05_1": "192.168.1.159",
    "IVT05_2": "192.168.1.160",
    "IVT06_1": "192.168.1.161",
    "IVT06_2": "192.168.1.162",
    "IVT07_1": "192.168.1.163",
    "IVT07_2": "192.168.1.164",
    "IVT08_1": "192.168.1.165",
    "IVT08_2": "192.168.1.166",
}
var_config={
    "max":1
}
name_ip=("WEATHER1-1","WEATHER1-2","WEATHER1-3",
         "WEATHER2-1","WEATHER2-2","WEATHER2-3",
         "SCB1-1","SCB1-2",
         "SCB2-1","SCB2-2",
         "SCB3-1","SCB3-2",
         "SCB4-1","SCB4-2",
         "SCB5-1","SCB5-2",
         "SCB6-1","SCB6-2",
         "SCB7-1","SCB7-2",
         "SCB8-1","SCB8-2"
         )
IVT={
    "IVT01_1":{
        "1-CM-1-1":19,
        "1-CM-1-2":22,
        "1-CM-1-3":22,
        "1-CM-1-4":19,
        "1-CM-1-5":18,
        "1-CM-1-6":22,
        "1-CM-1-7":22,
        "1-CM-1-8":20,
        "1-CM-1-9":20,
        "1-CM-1-10":19,
        "1-CM-1-11":22,
        "1-CM-1-12":19,
        "1-CM-1-13":22,
        "1-CM-1-14":22,
        "1-CM-1-15":22,
            },
    "IVT01_2":{
        "1-CM-2-1":18,
        "1-CM-2-2":21,
        "1-CM-2-3":21,
        "1-CM-2-4":21,
        "1-CM-2-5":21,
        "1-CM-2-6":22,
        "1-CM-2-7":22,
        "1-CM-2-8":22,
        "1-CM-2-9":22,
        "1-CM-2-10":18,
        "1-CM-2-11":22,
        "1-CM-2-12":22,
        "1-CM-2-13":22,
        "1-CM-2-14":20,
        "1-CM-2-15":16,
            },

    "IVT02_1":{
        "2-CM-1-1":18,
        "2-CM-1-2":18,
        "2-CM-1-3":20,
        "2-CM-1-4":21,
        "2-CM-1-5":18,
        "2-CM-1-6":18,
        "2-CM-1-7":22,
        "2-CM-1-8":22,
        "2-CM-1-9":22,
        "2-CM-1-10":22,
        "2-CM-1-11":22,
        "2-CM-1-12":22,
        "2-CM-1-13":22,
        "2-CM-1-14":22,
        "2-CM-1-15":22,
            },
    "IVT02_2":{
        "2-CM-2-1":21,
        "2-CM-2-2":21,
        "2-CM-2-3":21,
        "2-CM-2-4":21,
        "2-CM-2-5":20,
        "2-CM-2-6":22,
        "2-CM-2-7":20,
        "2-CM-2-8":22,
        "2-CM-2-9":20,
        "2-CM-2-10":16,
        "2-CM-2-11":22,
        "2-CM-2-12":22,
        "2-CM-2-13":22,
        "2-CM-2-14":22,
        "2-CM-2-15":16,
            },
    "IVT03_1":{
        "3-CM-1-1":18,
        "3-CM-1-2":19,
        "3-CM-1-3":20,
        "3-CM-1-4":20,
        "3-CM-1-5":19,
        "3-CM-1-6":22,
        "3-CM-1-7":22,
        "3-CM-1-8":20,
        "3-CM-1-9":21,
        "3-CM-1-10":22,
        "3-CM-1-11":22,
        "3-CM-1-12":22,
        "3-CM-1-13":22,
        "3-CM-1-14":22,
        "3-CM-1-15":22,
            },
    "IVT03_2":{
        "3-CM-2-1":21,
        "3-CM-2-2":21,
        "3-CM-2-3":21,
        "3-CM-2-4":21,
        "3-CM-2-5":20,
        "3-CM-2-6":22,
        "3-CM-2-7":22,
        "3-CM-2-8":22,
        "3-CM-2-9":20,
        "3-CM-2-10":16,
        "3-CM-2-11":20,
        "3-CM-2-12":22,
        "3-CM-2-13":20,
        "3-CM-2-14":20,
        "3-CM-2-15":16,
            },
    "IVT04_1":{
        "4-CM-1-1":18,
        "4-CM-1-2":20,
        "4-CM-1-3":20,
        "4-CM-1-3":20,
        "4-CM-1-4":20,
        "4-CM-1-5":20,
        "4-CM-1-6":18,
        "4-CM-1-7":22,
        "4-CM-1-8":22,
        "4-CM-1-9":22,
        "4-CM-1-10":22,
        "4-CM-1-11":22,
        "4-CM-1-12":21,
        "4-CM-1-13":21,
        "4-CM-1-14":21,
        "4-CM-1-15":18
    },
    "IVT04_2":{
        "4-CM-2-1":21,
        "4-CM-2-2":22,
        "4-CM-2-3":22,
        "4-CM-2-4":22,
        "4-CM-2-5":22,
        "4-CM-2-6":22,
        "4-CM-2-7":22,
        "4-CM-2-8":22,
        "4-CM-2-9":22,
        "4-CM-2-10":17,
        "4-CM-2-11":18,
        "4-CM-2-12":22,
        "4-CM-2-13":22,
        "4-CM-2-14":20,
        "4-CM-2-15":18
    },
    "IVT05_1":{

        "5-CM-1-1":16,
        "5-CM-1-2":20,
        "5-CM-1-3":22,
        "5-CM-1-4":22,
        "5-CM-1-5":20,
        "5-CM-1-6":16,
        "5-CM-1-7":22,
        "5-CM-1-8":22,
        "5-CM-1-9":20,
        "5-CM-1-10":20,
        "5-CM-1-11":22,
        "5-CM-1-12":21,
        "5-CM-1-13":21,
        "5-CM-1-14":22,
        "5-CM-1-15":21,
    },
    "IVT05_2":{
        "5-CM-2-1":21,
        "5-CM-2-2":21,
        "5-CM-2-3":21,
        "5-CM-2-4":21,
        "5-CM-2-5":20,
        "5-CM-2-6":22,
        "5-CM-2-7":20,
        "5-CM-2-8":22,
        "5-CM-2-9":20,
        "5-CM-2-10":16,
        "5-CM-2-11":22,
        "5-CM-2-12":22,
        "5-CM-2-13":22,
        "5-CM-2-14":22,
        "5-CM-2-15":16,
        
    },
    "IVT06_1":{
        "6-CM-1-1":18,
        "6-CM-1-2":20,
        "6-CM-1-3":22,
        "6-CM-1-4":22,
        "6-CM-1-5":22,
        "6-CM-1-6":20,
        "6-CM-1-7":18,
        "6-CM-1-8":22,
        "6-CM-1-9":22,
        "6-CM-1-10":22,
        "6-CM-1-11":22,
        "6-CM-1-12":21,
        "6-CM-1-13":18,
        "6-CM-1-14":18,
        "6-CM-1-15":21,
    },
    "IVT06_2":{
        "6-CM-2-1":21,
        "6-CM-2-2":21,
        "6-CM-2-3":21,
        "6-CM-2-4":21,
        "6-CM-2-5":22,
        "6-CM-2-6":22,
        "6-CM-2-7":22,
        "6-CM-2-8":22,
        "6-CM-2-9":22,
        "6-CM-2-10":16,
        "6-CM-2-11":20,
        "6-CM-2-12":18,
        "6-CM-2-13":16,
        "6-CM-2-14":22,
        "6-CM-2-15":22,
    },
    "IVT07_1":{
        "7-CM-1-1":18,
        "7-CM-1-2":20,
        "7-CM-1-3":22,
        "7-CM-1-4":22,
        "7-CM-1-5":20,
        "7-CM-1-6":18,
        "7-CM-1-7":20,
        "7-CM-1-8":18,
        "7-CM-1-9":22,
        "7-CM-1-10":22,
        "7-CM-1-11":22,
        "7-CM-1-12":22,
        "7-CM-1-13":19,
        "7-CM-1-14":21,
        "7-CM-1-15":22,
    },
    "IVT07_2":{
        "7-CM-2-1":20,
        "7-CM-2-2":20,
        "7-CM-2-3":20,
        "7-CM-2-4":22,
        "7-CM-2-5":20,
        "7-CM-2-6":22,
        "7-CM-2-7":22,
        "7-CM-2-8":18,
        "7-CM-2-9":22,
        "7-CM-2-10":22,
        "7-CM-2-11":22,
        "7-CM-2-12":22,
        "7-CM-2-13":22,
        "7-CM-2-14":22,
        "7-CM-2-15":16,
    },
    "IVT08_1":{
        "8-CM-1-1":18,
        "8-CM-1-2":18,
        "8-CM-1-3":22,
        "8-CM-1-4":22,
        "8-CM-1-5":22,
        "8-CM-1-6":22,
        "8-CM-1-7":20,
        "8-CM-1-8":18,
        "8-CM-1-9":16,
        "8-CM-1-10":22,
        "8-CM-1-11":22,
        "8-CM-1-12":22,
        "8-CM-1-13":22,
        "8-CM-1-14":22,
        "8-CM-1-15":22,
    },
    "IVT08_2":{
        "8-CM-2-1":20,
        "8-CM-2-2":18,
        "8-CM-2-3":18,
        "8-CM-2-4":20,
        "8-CM-2-5":22,
        "8-CM-2-6":22,
        "8-CM-2-7":20,
        "8-CM-2-8":22,
        "8-CM-2-9":22,
        "8-CM-2-10":20,
        "8-CM-2-11":22,
        "8-CM-2-12":22,
        "8-CM-2-13":22,
        "8-CM-2-14":22,
        "8-CM-2-15":20,
    }
}







