import random
from ctypes import *
#構造体の作り方https://qiita.com/pashango2/items/5075cb2d9248c7d3b5d4
END_TIME = 1000.0
P1 = 10.0 #平均到着間隔
P2 = 5.0

'''
typedef enum{
    E_ARRIVAL = 100,
    E_DEPARTURE
}event_type;
'''

class event_type(Structure):
    _field_ = (
    ('E_ARRIVAL', 100),
    (E_DEPARTURE),
    )

class struct_event(Structure):
    (event_type(type)),
    (time),
    (struct,_event,*next)
