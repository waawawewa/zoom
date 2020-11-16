# zoom

HELLO THERE ! THIS BOT JOINS ZOOM MEETINGS AUTOMATICALLY WHEN YOU ENTER 
THE MEETING ID AND PASSCODE (WORKS FOR WINDOWS ONLY)

INSTALLATION :--

**INTERNET CONNECTION REQUIRED FOR INSTALLATION**

CHECK IF YOUR PC IS 64-BIT OR 32-BIT FIRST BY GOING TO "THIS PC or My Computer" and right click -> properties

you can see it there. ( if your system shows 64-bit processor, 32-bit OS then your pc is 32-bit)

**STEP 1**

INSTALL GIT BASH (download the setup file and just keep clicking yes till the installation finishes)

https://git-scm.com/download/win (DOWNLOAD 32bit or 64 bit depending upon your pc)

now clone my repository by opening git bash FROM START MENU and type

YOU CAN OPEN GIT BASH BY GOING TO START MENU AND TYPING GIT BASH, CLICK ON IT, THEN TYPE 

cd Desktop

THEN TYPE

git clone https://github.com/thedopepirate/zoom.git

PRESS ENTER

THE FOLDER NAMED zoom MUST BE DOWNLOADED IN YOUR DESKTOP NOW 

COPY THIS FOLDER INTO YOUR D DRIVE (VERY IMPORTANT)

IF YOU DO NOT HAVE A D DRIVE IN YOUR COMPUTER, YOU WILL HAVE TO COPY IT TO C DRIVE AND FOLLOW THIS TUTORIAL
https://youtu.be/Lv6NGSczZwE


**STEP 2**

INSTALL PYTHON ON YOUR PC 

**WATCH THE VIDEO ATTACHED BELOW FOR INSTALLATION AFTER DOWNLOAD (important)**

DOWNLOAD LINKS:------

FOR WINDOWS 10 OR 8

https://www.python.org/ftp/python/3.9.0/python-3.9.0.exe (FOR 32-BIT OS)

https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe(64-BIT)


IF YOU ARE USING WINDOWS 7, THEN install

https://www.python.org/ftp/python/3.8.6/python-3.8.6.exe (32 bit)

https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe (64 BIT)


**WATCH THIS VIDEO ON HOW TO INSTALL PYTHON AFTER DOWNLOADINF THE ABOVE SETUP**
https://youtu.be/DKXMUGuGMp4


**STEP 3**

WE NEED PIP INSTALLED(follow this tutorial)

https://youtu.be/7Qxn4gcrGwg

GO TO THIS LINK, RIGHT CLICK AND SAVE IT ON DESKTOP. 

https://bootstrap.pypa.io/get-pip.py

ONCE THAT IS DONE, CLICK IT OPEN ( YOU NEED TO INSTALL PYTHON BEFORE DOING THIS)

AND THAT WILL INSTALL PIP

AFTER YOU INSTALL PIP, OPEN GIT BASH FROM START MENU AND TYPE 

pip -V

CLICK ENTER

THE OUTPUT SHOULD LOOK SOMETHING LIKE THIS

pip 20.2.4 from c:\users\home\appdata\local\programs\python\python39-32\lib\site-packages\pip (python 3.9)


IF THERE IS AN ERROR, LIKE **bash: pip: command not found** THEN DO THIS. (skip if the above output is seen)

GO TO THE FOLDER WHERE PYTHON IS INSTALLED (IF YOU FOLLOWED THE VIDEO, THIS WOULD BE THE LOCATION)

C:\Program Files\Scripts


NOW CLICK ON START AND TYPE

sysdm.cpl 

OPEN the application
 
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

LASTLY, TYPE

pip install Pillow

**STEP 5**
 
 GO TO THE ZOOM FOLDER IN D DRIVE  ( IF YOU DO NOT HAVE A D DRIVE, THEN GO TO C DRIVE WHERE WE PASTED ZOOM FOLDER IN THE ABOVE VIDEO)

OPEN THE FILE enter.csv IN NOTEPAD 

YOU NEED TO ENTER THE MEETING DETAILS LIKE I HAVE SHOWN YOU (date:month:year hour:minute) 24 hrs format 

SEPERATE THE TIME, MEETING ID AND PASSWORD WITH A COMMA "," as shown in the 3 examples.
DO NOT LEAVE SPACES

SAVE IT

**MAIN STEP**
IF YOU HAVE MADE IT TILL HERE, YOU ARE JUST 2 STEPS AWAY.

OPEN ZOOM AND GO TO SETTINGS, IN AUDIO ENABLE "AUTOMATICALLY JOIN AUDIO WHEN JOINING" AND IN VIDEO ENABLE "TURN OFF VIDEO WHEN JOINING MEETING"

NOW OPEN THE FOLDER ZOOM IN D DRIVE WHICH YOU COPIED IN THE BEGINNING

DOUBLE CLICK ON THE FILE main.py

JUST WAIT AND RELAX, MY BOT WILL AUTOMATICALLY JOIN THE MEETING

YOU NEED TO OPEN THE FILE main.py ATLEAST A MINUTE BEFORE THE MEETING STARTS.

once the meeting ends, it will join the next meeting AUTOMATICALLY by reading the time in enter.csv

the commands might take some time, do not move your mouse or type when running the bot.

THANKS FOR DOWNLOADING MY BOT

IF YOU FIND THIS USEFUL, AND WISH TO DONATE, DM ME ON INSTAGRAM @thedarknlucid


P.S: i skipped studying for my internals and wrote this bot instead, so thoda toh donation banta hai xD.
i thought of doing a youtube tutorial, but i don't have a microphone lmao. see you until next time!

wubba lubba dub dub



