# zoom bot (python project by Mithun)

HELLO THERE ! THIS BOT JOINS ZOOM MEETINGS AUTOMATICALLY BY IMAGE RECOGNITION ENTERING
THE MEETING ID AND PASSCODE AT THE SCHEDULED TIME, ONCE THE MEETING ENDS (ENDED BY HOST) IT WILL JOIN THE NEXT MEETING.

THIS IS HOW THE BOT WORKS

https://youtu.be/_ZvAHofiZC0

**(WORKS ON WINDOWS ONLY)**


INSTALLATION :--

**INTERNET CONNECTION REQUIRED FOR INSTALLATION**

CHECK IF YOUR PC IS 64-BIT OR 32-BIT FIRST BY GOING TO "THIS PC or My Computer" and right click -> properties

you can see it there. ( if your system shows 64-bit processor, 32-bit OS then you need to install 32-bit softwares)

**STEP 1**

INSTALL GIT BASH (download the setup file and just keep clicking yes till the installation finishes)

(Download link)

https://git-scm.com/download/win (DOWNLOAD 32bit or 64 bit depending upon your pc)

After the installation is done :---

Clone my repository by opening git bash FROM START MENU (follow the instructions given below)

YOU CAN OPEN GIT BASH BY GOING TO START MENU AND TYPING GIT BASH, CLICK ON IT, THEN TYPE 

```bash
cd Desktop
```
PRESS ENTER

COPY AND PASTE THE CODE BELOW 
```
git clone https://github.com/thedopepirate/zoom.git
```
PRESS ENTER

THE FOLDER NAMED zoom MUST BE DOWNLOADED IN YOUR DESKTOP NOW 

COPY THIS FOLDER INTO YOUR D DRIVE (VERY IMPORTANT)

IF YOU DO NOT HAVE A D DRIVE ON YOUR COMPUTER, YOU WILL HAVE TO COPY IT TO C DRIVE AND FOLLOW THIS TUTORIAL
https://youtu.be/VQXAL68lq9Q


**STEP 2**

INSTALL PYTHON ON YOUR PC 

**WATCH THE VIDEO ATTACHED BELOW FOR INSTALLATION AFTER DOWNLOAD (important)**

DOWNLOAD LINKS:------

FOR WINDOWS 10 OR 8

https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe (FOR 32-BIT OS)

https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe (64-BIT)


IF YOU ARE USING WINDOWS 7, THEN install

https://www.python.org/ftp/python/2.7.18/python-2.7.18.msi (32 bit)

https://www.python.org/ftp/python/2.7.18/python-2.7.18.msi (64 BIT)


**WATCH THIS VIDEO ON HOW TO INSTALL PYTHON AFTER DOWNLOADING THE ABOVE SETUP** (Very IMPORTANT)
https://youtu.be/DKXMUGuGMp4


**STEP 3**

WE NEED PIP INSTALLED(follow this tutorial)

https://youtu.be/7Qxn4gcrGwg

GO TO THIS LINK, RIGHT CLICK AND SAVE IT ON DESKTOP. 

https://bootstrap.pypa.io/get-pip.py

ONCE THAT IS DONE, CLICK IT OPEN ( YOU NEED TO INSTALL PYTHON BEFORE DOING THIS)

AND THAT WILL INSTALL PIP

AFTER YOU INSTALL PIP, OPEN GIT BASH FROM START MENU AND TYPE 
```
pip -V
```
CLICK ENTER

THE OUTPUT SHOULD LOOK SOMETHING LIKE THIS (not exact though)
```
pip 20.2.3 from c:\program files\lib\site-packages\pip (python 3.9)
```
**SKIP TO STEP 4 IF YOU SEE A SIMILAR OUTPUT** 


**ERROR HANDLING** (do not follow this if the above output is already seen on your git bash)

IF THERE IS AN ERROR, LIKE ```bash: pip: command not found``` THEN DO WATCH THIS VIDEO. (skip if the above output is seen)

https://youtu.be/yNJl2t5xPck

GO TO THE FOLDER WHERE PYTHON IS INSTALLED AND OPEN THE FOLDER NAMED SCRIPTS  (IF YOU FOLLOWED THE PYTHON INSTALLATION VIDEO, THIS WOULD BE THE LOCATION)
```
C:\Program Files\Scripts
```

NOW CLICK ON START AND TYPE
```
sysdm.cpl 
```
OPEN the application
 
 Inside the System Properties screen, go to the Advanced tab, then click on Environment Variables
 
 In the Environment Variables screen, go to System variables and click on Path to select it. Then with the Path selected, click the Edit… button.
 
 In the Edit environment variable screen, click on New and add the path where the PiP installation is located (the path you copied) click ok
 
  OPEN GIT BASH AND TYPE 
```
pip -V
```
it should be working now



**STEP 4** (COVERED IN THE VIDEO FROM TIMESTAMP 1:40 https://youtu.be/yNJl2t5xPck)

INSTALL pyautogui , datetime and pandas

GO TO GIT BASH

TYPE AND PRESS ENTER
```
pip install pyautogui
```
AFTER THE INSTALLATION IS DONE TYPE FOLLOWED BY ENTER KEY
```
pip install pandas
```
AFTER THE INSTALLATION IS DONE TYPE FOLLOWED BY ENTER KEY
```
pip install datetime
```
LASTLY, TYPE AND PRESS ENTER
```
pip install Pillow
```

**STEP 5** watch this video (https://youtu.be/_ZvAHofiZC0)
 
 GO TO THE ZOOM FOLDER IN D DRIVE  ( IF YOU DO NOT HAVE A D DRIVE, THEN GO TO C DRIVE WHERE WE PASTED ZOOM FOLDER IN THE VIDEO OF STEP 2)

OPEN THE FILE ```enter.csv``` IN NOTEPAD 

YOU NEED TO ENTER THE MEETING DETAILS LIKE I HAVE SHOWN YOU (date/month/year hour:minute) 24 hrs format 

SEPERATE THE TIME, MEETING ID AND PASSWORD WITH A COMMA "," as shown in the 3 examples.

CHANGE THE DATE , TIME , MEETING ID AND PASSWORD ACCORDING TO YOUR TIMETABLE

SAVE IT

**MAIN STEP**

IF YOU HAVE MADE IT TILL HERE, YOU ARE JUST 2 STEPS AWAY.

OPEN ZOOM AND GO TO SETTINGS, IN AUDIO ENABLE "AUTOMATICALLY JOIN AUDIO WHEN JOINING" AND IN VIDEO ENABLE "TURN OFF VIDEO WHEN JOINING MEETING"

NOW OPEN THE FOLDER ZOOM IN D DRIVE WHICH YOU COPIED IN THE BEGINNING ( C DRIVE FOR THOSE WHO DO NOT HAVE D DRIVE)

DOUBLE CLICK ON THE FILE main.py (watch https://youtu.be/_ZvAHofiZC0)

JUST WAIT AND RELAX, MY BOT WILL AUTOMATICALLY JOIN THE MEETING (enter the timings and meeting id correcrly in enter.csv

SOMETIMES, IF THE TERMINAL WINDOW ABRUPTLY CLOSES YOU WILL HAVE TO FOLLOW THIS VIDEO (https://youtu.be/mrz6Q0-HyKo)

YOU NEED TO OPEN THE FILE ```main.py``` ATLEAST A MINUTE BEFORE THE MEETING STARTS.

once the meeting ends, it will join the next meeting AUTOMATICALLY by reading the time in enter.csv

the commands might take some time, do not move your mouse or type when running the bot.


IF YOU WISH TO YOU CAN FURTHER AUTOMATE THE BOT BY TASK SCHEDULING SO THAT IT RUNS ```main.py``` AUTOMATICALLY (WATCH THIS VIDEO)

https://youtu.be/CBk-PZSvlEY

THANKS FOR DOWNLOADING MY BOT

Follow me on insta @thedarknlucid


wubba lubba dub dub







