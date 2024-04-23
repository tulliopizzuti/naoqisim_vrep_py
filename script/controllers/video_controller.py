import vision_definitions
from PIL import Image as I
import array
import time
class VideoController:
    subscriberID = 'vrep_bridge'
    fps = 5
    sample_time = 0.2

    def __init__(self, vrep, videoProxy, clientID, visionSensorName='NAO_vision1'):
        self.vrep=vrep
        self.videoProxy=videoProxy
        self.clientID=clientID
        self.visionSensorName=visionSensorName
        
    def init(self):
        self.camID = self.videoProxy.subscribeCamera(self.subscriberID, vision_definitions.kTopCamera, vision_definitions.kVGA, vision_definitions.kRGBColorSpace, self.fps)

    def run(self):
        res1,visionSensorHandle=self.vrep.simxGetObjectHandle(self.clientID,self.visionSensorName,self.vrep.simx_opmode_oneshot_wait)
        res2,resolution,image=self.vrep.simxGetVisionSensorImage(self.clientID,visionSensorHandle,0,self.vrep.simx_opmode_streaming)
        time.sleep(0.5)
        res2,resolution,image=self.vrep.simxGetVisionSensorImage(self.clientID,visionSensorHandle,0,self.vrep.simx_opmode_buffer)
        img = I.new("RGB", (resolution[0], resolution[1]))
        while(self.vrep.simxGetConnectionId(self.clientID)!=-1):
            res,resolution,image = self.vrep.simxGetVisionSensorImage(self.clientID,visionSensorHandle,0,self.vrep.simx_opmode_buffer)
            image_byte_array = array.array('b',image)
            im = I.frombuffer("RGB", (resolution[0],resolution[1]), image_byte_array, "raw", "RGB", 0, 1)
            self.videoProxy.putImage(vision_definitions.kTopCamera, resolution[0], resolution[1], im.rotate(180).tobytes())
        self.videoProxy.unsubscribeCamera(self.subscriberID)
        print("End video controller")