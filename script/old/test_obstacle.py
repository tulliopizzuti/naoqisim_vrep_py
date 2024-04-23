from naoqi import ALProxy  
from pynput import keyboard
from pynput.keyboard import Key
from pynput.keyboard import KeyCode
import time
def reset_all_sensors():
        for e in leftsensorvalue:
                memProxy.insertData(e, 5.0)
        for e in rightsensorvalue:
                memProxy.insertData(e, 5.0)  
def reset_all_event():
        for e in event:
                memProxy.raiseEvent(e, 5.0)
def remove_events():
        for e in event:
                memProxy.removeEvent(e)

'''
def on_key_release(key):
        if key == Key.right:
                memProxy.insertData(rightsensorvalue[0], 0.40)
                print("Right key clicked")
        elif key == Key.left:
                memProxy.insertData(leftsensorvalue[0], 0.40)
                print("Left key clicked")
        elif key == Key.up:
                memProxy.insertData(rightsensorvalue[0], 0.40)
                memProxy.insertData(leftsensorvalue[0], 0.40)
                print("Up key clicked")
        elif key == Key.down:
                memProxy.insertData(rightsensorvalue[1], 1.40)
                memProxy.insertData(leftsensorvalue[1], 1.40)
                print("Down key clicked")     
        elif key == KeyCode.from_char('0'):
                memProxy.insertData(actuator, 0.0)  
                print("0 key clicked")             
        elif key == KeyCode.from_char('1'):
                memProxy.insertData(actuator, 1.0)  
                print("1 key clicked")             
        elif key == KeyCode.from_char('2'):
                memProxy.insertData(actuator, 2.0)
                print("2 key clicked")             
        elif key == KeyCode.from_char('3'):
                memProxy.insertData(actuator, 3.0) 
                print("3 key clicked")             
        elif key == KeyCode.from_char('4'):
                memProxy.insertData(actuator, 4.0)
                print("4 key clicked")             
        elif key == KeyCode.from_char('5'):
                memProxy.insertData(actuator, 12.0) 
                print("5 key clicked")             
        elif key == KeyCode.from_char('6'):
                memProxy.insertData(actuator, 68.0) 
                print("6 key clicked")             
        elif key == KeyCode.from_char('e'):
                reset_all_event()
                print("e key clicked")  
        elif key == KeyCode.from_char('w'):
                reset_all_sensors()
                print("w key clicked")  
        elif key == KeyCode.from_char('q'):
                remove_events()
                print("q key clicked") 
        elif key == KeyCode.from_char('r'):
                for e in sonarProxy.getSubscribersInfo():
                        sonarProxy.unsubscribe(e[0])
                print("r key clicked") 
        elif key == KeyCode.from_char('p'):
                print(sonarProxy.getSubscribersInfo())
                print("p key clicked") 
        elif key == Key.esc:
                #sonarProxy.unsubscribe("myApplication")
                exit()
'''

def on_key_release(key):
        if key == Key.up:
                memProxy.raiseEvent(event[3], 0.10)
                memProxy.raiseEvent(event[4], 0.10)
                memProxy.raiseEvent(event[5], 0.10)
                print("up key clicked")
        if key == Key.left:
                memProxy.raiseEvent(event[5], 0.10)
                print("left key clicked")
        if key == Key.right:
                memProxy.raiseEvent(event[4], 0.10)
                print("right key clicked")
                
                
        elif key == KeyCode.from_char('t'):
                motionProxy.stopWalk()
                memProxy.raiseEvent("Navigation/AvoidanceNavigator/ObstacleDetected", [0.1,0.1,0])
                memProxy.raiseEvent("Navigation/SafeNavigator/BlockingObstacle", [0.1,0.1,0])
                memProxy.raiseEvent("Navigation/SafeNavigator/DangerousObstacleDetected", [0.1,0.1,0])
                print("t key clicked")    
        elif key == KeyCode.from_char('a'):

                print("a key clicked")       
                
                
                
                
                
                
                
          
        elif key == KeyCode.from_char('e'):
                reset_all_event()
                print("e key clicked")  
        elif key == KeyCode.from_char('w'):
                reset_all_sensors()
                print("w key clicked")  
        elif key == KeyCode.from_char('q'):
                #remove_events()
                print("q key clicked") 
        elif key == KeyCode.from_char('r'):
                for e in sonarProxy.getSubscribersInfo():
                        sonarProxy.unsubscribe(e[0])
                print("r key clicked") 
        elif key == KeyCode.from_char('p'):
                print(sonarProxy.getSubscribersInfo())
                print("p key clicked") 
        elif key == Key.esc:
                #sonarProxy.unsubscribe("myApplication")
                exit()





print "================ Choregraphe's Initialization ================"
print 'Enter your NAO IP'
naoIP = "127.0.0.1"#raw_input()
print 'Enter your NAO port'
naoPort = 9559 #raw_input()
naoPort=int(naoPort)
memProxy = ALProxy("ALMemory",naoIP,naoPort)
sonarProxy = ALProxy("ALSonar",naoIP,naoPort)
motionProxy = ALProxy("ALMotion",naoIP,naoPort)
#sonarProxy.subscribe("myApplication")
actuator = "Device/SubDeviceList/US/Actuator/Value"
sensor = "Device/SubDeviceList/US/Sensor/Value"
leftsensorvalue=[
"Device/SubDeviceList/US/Left/Sensor/Value",
"Device/SubDeviceList/US/Left/Sensor/Value1",
"Device/SubDeviceList/US/Left/Sensor/Value2",
"Device/SubDeviceList/US/Left/Sensor/Value3",
"Device/SubDeviceList/US/Left/Sensor/Value4",
"Device/SubDeviceList/US/Left/Sensor/Value5",
"Device/SubDeviceList/US/Left/Sensor/Value6",
"Device/SubDeviceList/US/Left/Sensor/Value7",
"Device/SubDeviceList/US/Left/Sensor/Value8",
"Device/SubDeviceList/US/Left/Sensor/Value9",
]
rightsensorvalue=[
"Device/SubDeviceList/US/Right/Sensor/Value",
"Device/SubDeviceList/US/Right/Sensor/Value1",
"Device/SubDeviceList/US/Right/Sensor/Value2",
"Device/SubDeviceList/US/Right/Sensor/Value3",
"Device/SubDeviceList/US/Right/Sensor/Value4",
"Device/SubDeviceList/US/Right/Sensor/Value5",
"Device/SubDeviceList/US/Right/Sensor/Value6",
"Device/SubDeviceList/US/Right/Sensor/Value7",
"Device/SubDeviceList/US/Right/Sensor/Value8",
"Device/SubDeviceList/US/Right/Sensor/Value9",
]

event = [
"SonarRightNothingDetected", #0
"SonarLeftNothingDetected", #1
"SonarNothingDetected", #2
"SonarMiddleDetected", #3
"SonarRightDetected", #4
"SonarLeftDetected", #5
"SonarLateralRightDetected", #6
"SonarLateralLeftDetected", #7
]
reset_all_sensors()
reset_all_event()

#print(memProxy.getEventList())
#print(memProxy.getMicroEventList())

print "================ Ready - Press ESC for exit ================"
with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()
