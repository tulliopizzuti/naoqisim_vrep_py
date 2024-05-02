# naoqisim_vrep_py
This project aims to be able to control a virtual NAO robot within a virtual environment of the CoppeliaSim simulator, taking advantage of the Choregraphe environment.
The project was developed and tested on a Windows operating system (10 and 11), but the steps for macOS and Linux should be similar.
Specific versions of Choregraphe and the SDK were chosen because they do not create too many problems. More updated versions may not work properly and require extra steps concerning the compilation of libraries for x64 systems.

## Requirements
- Choregraphe 2.5.10: https://www.aldebaran.com/en/support/pepper-naoqi-2-9/choregraphe-setup-2510-windows
- CoppeliaSim V4.6.0 rev18: https://www.coppeliarobotics.com/
- NAOqi SDK 2.1.4: https://community-static.aldebaran.com/resources/2.1.4.13/sdk-c%2B%2B/naoqi-sdk-2.1.4.13-win32-vs2010.zip
- Anaconda Environment: https://www.anaconda.com/download

## Installation Step

1. Install Choregraphe, Coppelia and Anaconda
2. Extract NAOqi SDK 2.1.4 in a folder and set the env variable NAOQISDK to main folder
3. Set the env var CHOREGRAPHE_DIR to ..program files..\Choregraphe Suite 2.5
4. Set the env var PYTHONPATH to %NAOQISDK%\lib
5. Create a conda env
```
conda create -n nao
conda activate nao
conda config --env --set subdir win-32
conda install python=2.7
conda install pillow
pip install argparse
```

## Execute Project
After downloading this repo, follow this step to start the simulated env.

1. Go to the main folder
2. Execute "run_nao.bat"
3. Execute "run_choregraphe.bat"
4. Run CoppeliaSim and open the scene in scene\NAO.ttt
5. Run the simulation on CoppeliaSim
6. Open a prompt in script folder and run
```
conda activate nao
python nao.py
```
7. Port number is 9559 by default (if you want change the port can run on a prompt the command %CHOREGRAPHE_DIR%\bin\naoqi-bin.exe -p CUSTOM_PORT)

After the connection on Choregraphe, you can see in video monitor the simulated environment loaded in CoppeliaSim.
In this version movement and vision utility works.

## Future work
1. Proximity Sensors integration
2. Fix 2.8.8 movement library error. Proximity Sensors (probably) don't make the robot walk decently in the simulator with this version of SDK.

## Thanks
This project is an extension of the repo: https://github.com/PierreJac/Project-NAO-Control/tree/master
