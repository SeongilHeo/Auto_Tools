from smtplib import SMTP
import winsound as ws
import pyautogui
import time
import pyperclip
import mouse
import os
import smtplib
 
from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendd(name):
    from_addr = formataddr(('허성일', 'tjddlf101@google.com'))
    to_addr = formataddr(('정동현', 'gjtjddlf101@naver.com'))

    session = None

    try:
        # SMTP 세션 생성
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.set_debuglevel(True)

        # SMTP 계정 인증 설정
        session.ehlo()
        session.starttls()
        session.login('tjddlf101@gmail.com', 'jhkirkivgucihfbh')

        # 메일 콘텐츠 설정
        message = MIMEMultipart("alternative")

        # 메일 송/수신 옵션 설정
        message.set_charset('utf-8')
        message['From'] = from_addr
        message['To'] = to_addr
        message['Subject'] = name

        # 메일 콘텐츠 - 내용
        body = '<h2>%s</h1>'%(name)
        bodyPart = MIMEText(body, 'html', 'utf-8')
        message.attach( bodyPart )

        # 메일 발송
        session.sendmail(from_addr, to_addr, message.as_string())            

        print( 'Successfully sent the mail!!!' )
    except Exception as e:
        print( e )
    finally:
        if session is not None:
            session.quit()
            
def beepsound():
    freq = 2000    # range : 37 ~ 32767
    dur = 1000     # ms
    ws.Beep(freq, dur) # winsound.Beep(frequency, duration)

def check_result(rgb_sc,name):
    for x in range(rgb_sc.height):
        for y in range(rgb_sc.width):
            if (255,150,50) == rgb_sc.getpixel((y,x)):
                sendd(name)
                return True
def main(status):
    while status:
        if mouse.is_pressed():
            break    
    pyautogui.hotkey('f5')
    time.sleep(3)
    for name in var_list:
        pyautogui.hotkey('ctrl', 'f')
        pyperclip.copy(name)
        pyautogui.hotkey('ctrl','v')
        prt_sc=pyautogui.screenshot() 
        rgb_sc=prt_sc.convert('RGB')
        if check_result(rgb_sc,name):
            var_list.remove(name)
            status = True
            print(var_list)
            return 
    return False
     
            
var_list = input("student names with space").split()
status=True
while True:
    if len(var_list)==0:
        break
    status=main(status)
