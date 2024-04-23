import vrep
import sys
from naoqi import ALProxy  
import argparse
from controllers.movements_controller import MovementsController
from controllers.video_controller import VideoController
from controllers.sonar_controller import SonarController
from threading import Thread


parser = argparse.ArgumentParser()
parser.add_argument("--nao", help="Nao connection NAO_IP:NAO_PORT", default="127.0.0.1:9559")
parser.add_argument("--coppelia", help="CoppeliaSim connection COPPELIA_IP:COPPELIA_PORT",default="127.0.0.2:19999")
parser.add_argument("--removecontrollers", help="Remove controller from the exectution [Movements, Video, Sonar]",default="", type=str)
args = parser.parse_args()

removecontroller=args.removecontrollers.replace(", ",",")
removecontroller=removecontroller.split(",")
nao_ip, nao_port = args.nao.split(":")
nao_port=int(nao_port)
coppelia_ip, coppelia_port = args.coppelia.split(":")
coppelia_port=int(coppelia_port)
print ("CoppeliaSim connection.....")
vrep.simxFinish(-1)
clientID=vrep.simxStart(coppelia_ip,coppelia_port,True,True,5000,5)
if clientID!=-1:
	print('Connected to CoppeliaSim')
else:
	print('Connection to CoppeliaSim non successful')
	exit()

try:
    print ("Nao connection.....")
    motionProxy = ALProxy("ALMotion",nao_ip, nao_port)
    postureProxy = ALProxy("ALRobotPosture", nao_ip, nao_port)
    videoProxy = ALProxy("ALVideoDevice", nao_ip, nao_port)
    memoryProxy = ALProxy("ALMemory", nao_ip, nao_port)
    sonarProxy = ALProxy("ALSonar",nao_ip,nao_port)
    navigationProxy = ALProxy("ALNavigation",nao_ip,nao_port)
    print('Connected to Nao')
	
except:
	print('Connection to Nao non successful')
	exit()

controllers=[]
controllers.append({"name": "Movements", "controller":  MovementsController(vrep, motionProxy, postureProxy, clientID)})
controllers.append({"name": "Video", "controller":  VideoController(vrep, videoProxy, clientID)})
controllers.append({"name": "Sonar", "controller":  SonarController(vrep, sonarProxy, memoryProxy, motionProxy, clientID)})

controllers=list(filter(lambda x: x["name"] not in removecontroller, controllers))


threads=[]
for c in controllers:
    
    print ("Init "+ c["name"] +" controller.....")
    c["controller"].init()
    print ("Start "+ c["name"] +" controller.....")
    controller_thread = Thread(target=c["controller"].run)
    controller_thread.daemon=True
    controller_thread.start()
    print (c["name"]+" controller started successfully")
    threads.append(controller_thread)


print ("Connection ready.....")

while True:
    exit=True
    for i in threads:
        exit = exit and i.is_alive()
    if not exit:
        break

