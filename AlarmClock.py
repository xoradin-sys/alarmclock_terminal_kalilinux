#! /usr/bin/env python3

from datetime import datetime
import os
import time

class clock():
    def __init__(self):   
        self.timeinput = ''
        self.time1 = ''
        print('Hello I m your best Friend The AlarmClock!!')
        print('-------------------------------------------')
        self.show_time()
        print(self.time1)         
    
    def show_time(self):
        #current date and time
        now = datetime.now()
        #date and time format: dd/mm/YYYY H:M:S
        #format = "%d/%m/%Y %H:%M:%S"
        format = "%H:%M"
        #format datetime using strftime() 
        self.time1 = now.strftime(format)
        #print(self.time1)
        #return self.time1    
         
    def alarm_set(self):
        alarm = input('U wanne set the alarm? Y or N : ')
        if alarm.lower() == 'y':
            while 1:
                try:
                    self.timeinput = input('Pls give in the activation time (HH:MM) : ')
                    time.strptime(self.timeinput, '%H:%M')
                    #print(self.timeinput)
                    print('Alarmsetting Accepted!!')
                    #return self.timeinput
                    break
                except:
                    print('Wrong INPUT! Try again!')
                    pass        
        else:
            os._exit(0)
            #pass
        
    def sound(self):
        print('beep-beep-beep')
        file = "/home/xoradin/Desktop/Alarm-ringtone.mp3"
        os.system("mpg123 " + file)     
    
    def run(self):

        while True:
            self.show_time()
            #print(self.timeinput + ' ' + self.time1)
            if self.time1 == self.timeinput:
                self.sound()
                os._exit(0)
                #break
            else:
                pass
            print('Time :'+self.time1, end='\r')
            time.sleep(1)



if __name__ == '__main__':

	al = clock()
	al.show_time()
	al.alarm_set()
	al.run()




