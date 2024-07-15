import psutil
import time
from plyer import notification

disconnect=False
while not disconnect:

    battery=psutil.sensors_battery()
    if battery.percent >96:
              notification.notify(
            title = "Battry full",
            message=" Unplug charger" ,
           
            # displaying time
            timeout=2)
    elif battery.percent <18:
              notification.notify(
            title = "Battry empty",
            message=" Plug charger" ,
           
            # displaying time
            timeout=2)
    else:
              notification.notify(
            title = "Battry normal",
            message=" keep using laptop" ,
           
            # displaying time
            timeout=2)
    time.sleep(20)
    inp=input("disconnect ,y for yes ,n for no? \n")
    if(inp=="y"):
       disconnect=True