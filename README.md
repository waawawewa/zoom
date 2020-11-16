# zoom

HELLO THERE ! THIS BOT JOINS ZOOM MEETINGS AUTOMATICALLY WHEN YOU ENTER 
THE MEETING ID AND PASSCODE (WORKS FOR WINDOWS ONLY)

**INTERNET CONNECTION REQUIRED**

**STEP 1**

INSTALL GIT BASH (download the setup file)

https://git-scm.com/download/win (DOWNLOAD 32bit or 64 bit depending upon your pc)

now clone my repository by opening git bash and type

git clone https://github.com/thedopepirate/zoom.git

THE FOLDER NAMED ZOOM MUST BE IN YOUR DESKTOP or somewhere inside USERS folder in C drive

COPY THIS FOLDER INTO YOUR D DRIVE (VERY IMPORTANT)



**STEP 2**

INSTALL PYTHON ON YOUR PC (download links)

FOR WINDOWS 10 OR 8

https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe (FOR 32-BIT OS)

https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe(64-BIT)
 
BEFORE CLICKING THE INSTALL BUTTON, CHECK WHERE IT IS BEING INSTALLED (the path) COPY THAT PATH AND SAVE IT IN A NOTEPAD
IF YOU ARE USING WINDOWS 7, THEN 

https://www.python.org/ftp/python/3.8.6/python-3.8.6.exe (32 bit)

https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe (64 BIT)


**STEP 3**

WE NEED PIP INSTALLED(follow this tutorial)

https://www.youtube.com/watch?v=AVCcFyYynQY

AFTER YOU INSTALL PIP, OPEN GIT BASH AND TYPE 

pip -V

THE OUTPUT SHOULD LOOK SOMETHING LIKE THIS

pip 20.2.4 from c:\users\home\appdata\local\programs\python\python39-32\lib\site-packages\pip (python 3.9)


IF THERE IS AN ERROR, LIKE **‘pip’ is not recognized as an internal or external command** or *bash: pip: command not found* THEN DO THIS. (skip if the above output is seen)

open windows command prompt

type python -c "import sys; print(sys.executable)"

you will get an output like this (might not be completely same)

C:\Users\HOME\AppData\Local\Programs\Python\Python39-32\python.exe (this is where python is located)

copy the path till by Python39-32 selecting it in mouse and ctrl+c

paste it in file explorer

open the file Scripts, copy this path

now again in windows command prompt

type sysdm.cpl
 
 Inside the System Properties screen, go to the Advanced tab, then click on Environment Variables
 
 In the Environment Variables screen, go to System variables and click on Path to select it. Then with the Path selected, click the Edit… button.
 
 In the Edit environment variable screen, click on New and add the path where the PiP installation is located (the path you copied) click ok
 
  OPEN GIT BASH AND TYPE 

pip -V

it should be working now


**STEP 4**

INSTALL pyautogui , datetime and pandas

GO TO GIT BASH

TYPE 

pip install pyautogui

AFTER THE INSTALLATION IS DONE TYPE 

pip install pandas

AFTER THE INSTALLATION IS DONE TYPE 

pip install datetime

**STEP 5**

OPEN THE FILE enter.csv IN NOTEPAD 

YOU NEED TO ENTER THE MEETING DETAILS LIKE I HAVE SHOWN YOU IN THE FILE 

SEPERATE THE TIME, MEETING ID AND PASSWORD WITH A COMMA ",".
DO NOT LEAVE SPACES

SAVE IT




