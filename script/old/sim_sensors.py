# -*- coding: utf-8 -*-
"""
@author: Pierre Jacquot
"""
#For more informations please check : http://www.coppeliarobotics.com/helpFiles/en/apiFunctions.htm
import vrep,sys



print '================ Program Sarted ================'

vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.2',19999,True,True,5000,5)
if clientID!=-1:
	print 'Connected to remote API server'

else:
	print 'Connection non successful'
	sys.exit('Could not connect')



errorCode,sonar_middle_handle=vrep.simxGetObjectHandle(clientID,'sonar_middle',vrep.simx_opmode_oneshot_wait)
while(vrep.simxGetConnectionId(clientID)!=-1):
	errorCode,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=vrep.simxReadProximitySensor(clientID,sonar_middle_handle,vrep.simx_opmode_streaming)   
	print(detectionState)             


