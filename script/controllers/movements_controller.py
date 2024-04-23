
class MovementsController:
    Head_Yaw=[];Head_Pitch=[];
    L_Hip_Yaw_Pitch=[];L_Hip_Roll=[];L_Hip_Pitch=[];L_Knee_Pitch=[];L_Ankle_Pitch=[];L_Ankle_Roll=[];
    R_Hip_Yaw_Pitch=[];R_Hip_Roll=[];R_Hip_Pitch=[];R_Knee_Pitch=[];R_Ankle_Pitch=[];R_Ankle_Roll=[];
    L_Shoulder_Pitch=[];L_Shoulder_Roll=[];L_Elbow_Yaw=[];L_Elbow_Roll=[];L_Wrist_Yaw=[]
    R_Shoulder_Pitch=[];R_Shoulder_Roll=[];R_Elbow_Yaw=[];R_Elbow_Roll=[];R_Wrist_Yaw=[]
    R_H=[];L_H=[];R_Hand=[];L_Hand=[];
    Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]

    def __init__(self, vrep, motionProxy, postureProxy, clientID, init_posture="StandZero"):
        self.vrep=vrep
        self.motionProxy=motionProxy
        self.postureProxy=postureProxy
        self.init_posture=init_posture
        self.clientID=clientID
        
    def init(self):
        self.motionProxy.stiffnessInterpolation('Body', 1.0, 1.0)
        self.postureProxy.goToPosture(self.init_posture,1.0)
        self.get_first_handles()


    def run(self):
        i=0
        commandAngles = self.motionProxy.getAngles('Body', False)
        
        while(self.vrep.simxGetConnectionId(self.clientID)!=-1):
            commandAngles = self.motionProxy.getAngles('Body', False)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[0][i],commandAngles[0],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[1][i],commandAngles[1],self.vrep.simx_opmode_streaming)
            #Left Leg
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[2][i],commandAngles[8],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[3][i],commandAngles[9],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[4][i],commandAngles[10],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[5][i],commandAngles[11],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[6][i],commandAngles[12],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[7][i],commandAngles[13],self.vrep.simx_opmode_streaming)
            #Right Leg
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[8][i],commandAngles[14],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[9][i],commandAngles[15],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[10][i],commandAngles[16],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[11][i],commandAngles[17],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[12][i],commandAngles[18],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[13][i],commandAngles[19],self.vrep.simx_opmode_streaming)
            #Left Arm
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[14][i],commandAngles[2],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[15][i],commandAngles[3],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[16][i],commandAngles[4],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[17][i],commandAngles[5],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[18][i],commandAngles[6],self.vrep.simx_opmode_streaming)
            #Right Arm
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[19][i],commandAngles[20],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[20][i],commandAngles[21],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[21][i],commandAngles[22],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[22][i],commandAngles[23],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[23][i],commandAngles[24],self.vrep.simx_opmode_streaming)
            #Left Fingers
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[25][i][0],1.0-commandAngles[7],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[25][i][1],1.0-commandAngles[7],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[25][i][2],1.0-commandAngles[7],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[25][i][3],1.0-commandAngles[7],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[25][i][4],1.0-commandAngles[7],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[25][i][5],1.0-commandAngles[7],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[25][i][6],1.0-commandAngles[7],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[25][i][7],1.0-commandAngles[7],self.vrep.simx_opmode_streaming)
            #Right Fingers
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[27][i][0],1.0-commandAngles[25],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[27][i][1],1.0-commandAngles[25],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[27][i][2],1.0-commandAngles[25],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[27][i][3],1.0-commandAngles[25],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[27][i][4],1.0-commandAngles[25],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[27][i][5],1.0-commandAngles[25],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[27][i][6],1.0-commandAngles[25],self.vrep.simx_opmode_streaming)
            self.vrep.simxSetJointTargetPosition(self.clientID, self.Body[27][i][7],1.0-commandAngles[25],self.vrep.simx_opmode_streaming)
        print("End movement controller")

    def get_first_handles(self):    
        print('-> Head for NAO : '+ str(1))
        self.Body[0].append(self.vrep.simxGetObjectHandle(self.clientID,'HeadYaw#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[1].append(self.vrep.simxGetObjectHandle(self.clientID,'HeadPitch#',self.vrep.simx_opmode_oneshot_wait)[1])
        #Left Leg
        print('-> Left Leg for NAO : ' + str(1))
        self.Body[2].append(self.vrep.simxGetObjectHandle(self.clientID,'LHipYawPitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[3].append(self.vrep.simxGetObjectHandle(self.clientID,'LHipRoll3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[4].append(self.vrep.simxGetObjectHandle(self.clientID,'LHipPitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[5].append(self.vrep.simxGetObjectHandle(self.clientID,'LKneePitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[6].append(self.vrep.simxGetObjectHandle(self.clientID,'LAnklePitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[7].append(self.vrep.simxGetObjectHandle(self.clientID,'LAnkleRoll3#',self.vrep.simx_opmode_oneshot_wait)[1])
        #Right Leg
        print('-> Right Leg for NAO : ' + str(1))
        self.Body[8].append(self.vrep.simxGetObjectHandle(self.clientID,'RHipYawPitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[9].append(self.vrep.simxGetObjectHandle(self.clientID,'RHipRoll3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[10].append(self.vrep.simxGetObjectHandle(self.clientID,'RHipPitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[11].append(self.vrep.simxGetObjectHandle(self.clientID,'RKneePitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[12].append(self.vrep.simxGetObjectHandle(self.clientID,'RAnklePitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[13].append(self.vrep.simxGetObjectHandle(self.clientID,'RAnkleRoll3#',self.vrep.simx_opmode_oneshot_wait)[1])
        #Left Arm
        print('-> Left Arm for NAO : ' + str(1))
        self.Body[14].append(self.vrep.simxGetObjectHandle(self.clientID,'LShoulderPitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[15].append(self.vrep.simxGetObjectHandle(self.clientID,'LShoulderRoll3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[16].append(self.vrep.simxGetObjectHandle(self.clientID,'LElbowYaw3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[17].append(self.vrep.simxGetObjectHandle(self.clientID,'LElbowRoll3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[18].append(self.vrep.simxGetObjectHandle(self.clientID,'LWristYaw3#',self.vrep.simx_opmode_oneshot_wait)[1])
        #Right Arm
        print('-> Right Arm for NAO : ' + str(1))
        self.Body[19].append(self.vrep.simxGetObjectHandle(self.clientID,'RShoulderPitch3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[20].append(self.vrep.simxGetObjectHandle(self.clientID,'RShoulderRoll3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[21].append(self.vrep.simxGetObjectHandle(self.clientID,'RElbowYaw3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[22].append(self.vrep.simxGetObjectHandle(self.clientID,'RElbowRoll3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[23].append(self.vrep.simxGetObjectHandle(self.clientID,'RWristYaw3#',self.vrep.simx_opmode_oneshot_wait)[1])
        #Left fingers
        print('-> Left Fingers for NAO : ' + str(1))
        self.Body[24].append(self.vrep.simxGetObjectHandle(self.clientID,'NAO_LThumbBase#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[24].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint8#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[24].append(self.vrep.simxGetObjectHandle(self.clientID,'NAO_LLFingerBase#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[24].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint12#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[24].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint14#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[24].append(self.vrep.simxGetObjectHandle(self.clientID,'NAO_LRFinger_Base#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[24].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint11#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[24].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint13#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[25].append(self.Body[24][0:8])
        #Right Fingers
        print('-> Right Fingers for NAO : ' + str(1))
        self.Body[26].append(self.vrep.simxGetObjectHandle(self.clientID,'NAO_RThumbBase#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[26].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint0#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[26].append(self.vrep.simxGetObjectHandle(self.clientID,'NAO_RLFingerBase#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[26].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint5#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[26].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint6#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[26].append(self.vrep.simxGetObjectHandle(self.clientID,'NAO_RRFinger_Base#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[26].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint2#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[26].append(self.vrep.simxGetObjectHandle(self.clientID,'Revolute_joint3#',self.vrep.simx_opmode_oneshot_wait)[1])
        self.Body[27].append(self.Body[26][0:8]) 

