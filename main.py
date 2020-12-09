import pyautogui
from time import sleep
import pandas as pd
from datetime import datetime
pyautogui.FAILSAFE = False
def sign_in(meeting_id, pswd):
	def keypress(pyautogui, code):
		pyautogui.keyDown(code)
		pyautogui.keyUp(code)


		#Open Zoom:
	print("Opening Zoom")
	pyautogui.keyDown("winleft")
	pyautogui.keyUp("winleft")
	sleep(3)
	pyautogui.write("zoom")
	pyautogui.keyDown("\n")
	pyautogui.keyUp("\n")
	sleep(15)
	print("Done")

	print("clicking join")
	sleep(2)
	while pyautogui.locateOnScreen('D:\zoom\joinbutton.png'):
		sleep(3)
		w = pyautogui.locateOnScreen('D:\zoom\joinbutton.png')
		pyautogui.moveTo(w)
		pyautogui.click()
		break
	else: print(".")
	print("done")

	sleep(5)

	print("entering meeting id")
	sleep(2)
	while pyautogui.locateOnScreen('D:\zoom\meetingid.png'):
		sleep(2)
		q = pyautogui.locateOnScreen('D:\zoom\meetingid.png')
		pyautogui.moveTo(q)
		pyautogui.click()
		break
	else: print("")
	pyautogui.write(meeting_id)
	sleep(3)
	print("joining")
	sleep(2)
	while pyautogui.locateOnScreen('D:\zoom\joinbtn.png'):
		sleep(2)
		q = pyautogui.locateOnScreen('D:\zoom\joinbtn.png')
		pyautogui.moveTo(q)
		pyautogui.click()
		break
	else: print(".")
	
	sleep(3)
#checking if invalid id pops up
	while pyautogui.locateOnScreen('D:\zoom\inv.png'):
		import rr
		break
	else: print(".")

	print("entering password")
	sleep(4)
	pyautogui.write(pswd)


	print("clicking joinmeeting")
	sleep(3)

	r = pyautogui.locateOnScreen('D:\zoom\joinmeeting1.png')
	print(r)
	pyautogui.click(r)

	sleep(5)
	print("meeting_joined")
print("I'm Looking for the timetable")

df = pd.read_csv('D:\zoom\enter.csv')

while True:
	#checking timetable
	now = datetime.now().strftime('%d/%m/%Y %H:%M')
	if now in str(df['timings']):
		row = df.loc[df['timings'] == now]
		m_id = str(row.iloc[0,1])
		m_pswd = str(row.iloc[0,2])

		sign_in(m_id, m_pswd)
		sleep(5)
		print("signed in")
	elif pyautogui.locateOnScreen('D:\zoom\sign.png'):
		pyautogui.hotkey('altleft', 'f4')
