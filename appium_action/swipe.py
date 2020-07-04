import time
from time import sleep
from find_element.capability import driver

#获取屏幕尺寸
def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x,y

#显示屏幕尺寸
l = get_size()
print(l)

#向左滑动
def swipeLeft():
    l = get_size()
    x1 = int(l[0]*0.9)
    y1 = int(l[0]*0.5)
    x2 = int(l[0] * 0.1)
    driver.swipe(x1,y1,x2,y1,1000)

#向右滑动
def swipeRight():
    l = get_size()
    x1 = int(l[0]*0.1)
    y1 = int(l[0]*0.5)
    x2 = int(l[0] * 0.9)
    driver.swipe(x1,y1,x2,y1,1000)

#向上滑动
def swipeUp():
    l = get_size()
    y1 = int(l[0]*0.9)
    x1 = int(l[0]*0.5)
    y2 = int(l[0] * 0.1)
    driver.swipe(x1,y1,x1,y2,1000)

#向下滑动
def swipeDown():
    l = get_size()
    y1 = int(l[0]*0.1)
    x1 = int(l[0]*0.5)
    y2 = int(l[0] * 0.9)
    driver.swipe(x1,y1,x1,y2,1000)



#向左滑动两次
for i in range(2):
    swipeLeft()
    sleep(0.5)
time.sleep(0.9)

for i in range(2):
    swipeRight()
    sleep(0.5)

# driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()