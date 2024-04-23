import time

class SonarController:
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
    def __init__(self, vrep, sonarProxy, memoryProxy, motionProxy, clientID):
        self.vrep=vrep
        self.sonarProxy=sonarProxy
        self.memoryProxy=memoryProxy
        self.motionProxy=motionProxy
        self.clientID=clientID
        
    def init(self):
        self.reset_all_sensors()
        self.reset_all_event()
        #self.remove_events()
        for e in self.sonarProxy.getSubscribersInfo():
            self.sonarProxy.unsubscribe(e[0])
        errorCode,self.sonar_middle_handle=self.vrep.simxGetObjectHandle(self.clientID,'sonar_middle',self.vrep.simx_opmode_oneshot_wait)
        errorCode,self.sonar_front_left_handle=self.vrep.simxGetObjectHandle(self.clientID,'sonar_front_left',self.vrep.simx_opmode_oneshot_wait)
        errorCode,self.sonar_front_right_handle=self.vrep.simxGetObjectHandle(self.clientID,'sonar_front_right',self.vrep.simx_opmode_oneshot_wait)
        errorCode,self.sonar_lateral_left_handle=self.vrep.simxGetObjectHandle(self.clientID,'sonar_lateral_left',self.vrep.simx_opmode_oneshot_wait)
        errorCode,self.sonar_lateral_right_handle=self.vrep.simxGetObjectHandle(self.clientID,'sonar_lateral_right',self.vrep.simx_opmode_oneshot_wait)

    def run(self):
        
        while(self.vrep.simxGetConnectionId(self.clientID)!=-1):
            errorCode,self.sonar_middle_detection_state,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=self.vrep.simxReadProximitySensor(self.clientID,self.sonar_middle_handle,self.vrep.simx_opmode_streaming)   
            errorCode,self.sonar_front_left_detection_state,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=self.vrep.simxReadProximitySensor(self.clientID,self.sonar_front_left_handle,self.vrep.simx_opmode_streaming)   
            errorCode,self.sonar_front_right_detection_state,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=self.vrep.simxReadProximitySensor(self.clientID,self.sonar_front_right_handle,self.vrep.simx_opmode_streaming)   
            errorCode,self.sonar_lateral_left_detection_state,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=self.vrep.simxReadProximitySensor(self.clientID,self.sonar_lateral_left_handle,self.vrep.simx_opmode_streaming)   
            errorCode,self.sonar_lateral_right_detection_state,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=self.vrep.simxReadProximitySensor(self.clientID,self.sonar_lateral_right_handle,self.vrep.simx_opmode_streaming)   
            nothing_detected=True
            
            if self.sonar_middle_detection_state:
                nothing_detected=False
                self.memoryProxy.raiseEvent("SonarMiddleDetected", 0.1)

            if self.sonar_front_left_detection_state:
                nothing_detected=False
                self.memoryProxy.raiseEvent("SonarLeftDetected", 0.1)
            else:
                self.memoryProxy.raiseEvent("SonarLeftNothingDetected", 5.0)
            
            if self.sonar_front_right_detection_state:
                nothing_detected=False
                self.memoryProxy.raiseEvent("SonarRightDetected", 0.1)
            else:
                self.memoryProxy.raiseEvent("SonarRightNothingDetected", 5.0)
                
            if self.sonar_lateral_left_detection_state:
                #nothing_detected=False
                self.memoryProxy.raiseEvent("SonarLateralLeftDetected", 0.1)
                
            if self.sonar_lateral_right_detection_state:
                #nothing_detected=False
                self.memoryProxy.raiseEvent("SonarLateralRightDetected", 0.1)
                
            if nothing_detected:
                self.memoryProxy.raiseEvent("SonarNothingDetected", 5.0)
                self.memoryProxy.raiseEvent("Navigation/AvoidanceNavigator/ObstacleDetected",[])
            else:
                self.memoryProxy.raiseEvent("Navigation/AvoidanceNavigator/ObstacleDetected",[1,1])
                if self.motionProxy.moveIsActive():                  
                    #TODO: Check the direction and block only when walk toward the obstacle
                    self.motionProxy.stopMove()

                
            time.sleep(2)

        print("End sonar controller")

    def reset_all_sensors(self):
        for e in self.leftsensorvalue:
                self.memoryProxy.insertData(e, 5.0)
        for e in self.rightsensorvalue:
                self.memoryProxy.insertData(e, 5.0)  

    def reset_all_event(self):
            for e in self.event:
                self.memoryProxy.raiseEvent(e, 5.0)

    def remove_events(self):
        for e in self.event:
                self.memoryProxy.removeEvent(e)