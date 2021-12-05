from django.shortcuts import render, HttpResponse

# Create your views here.
from django.views import View
from django.conf import settings
import json
import serial

#TODO
print("init arduino serial here")
serial=serial.Serial()
car_speed=0
def speed_up(request):  # 让车加速
    global car_speed
    if car_speed < 150:
        car_speed = car_speed + 50
    # TODO
    print("place arduino interact here")
    ret = json.dumps({"speed": car_speed})
    # serial.write()
    return HttpResponse(ret)


def speed_down(request):
    global car_speed
    if car_speed > 0:
        car_speed = car_speed - 50
    # TODO
    print("place arduino interact here")
    ret = json.dumps({"speed": car_speed})
    return HttpResponse(ret)


def brake(request):
    global car_speed
    car_speed=0
    #TODO
    print("place arduino interact here")
    return HttpResponse("OK")

def set_direction(request):
    # 此处x和y是表示方向的矢量
    x = request.POST['x']
    y = request.POST['y']
    # TODO
    print(x,y)
    print("place arduino interact here")
    return HttpResponse("OK")


def screen_shot(request):
    # TODO 用时间戳命名这张图片
    print("take a photo here")

    with open("name of the photo",'rb') as f:
        ret_data=f.read()
    return HttpResponse(ret_data,type='image/jpg')

