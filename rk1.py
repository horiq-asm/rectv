import os
import datetime
import subprocess, shlex
os.system('curl -o /home/pi/rr.txt https://www.asmtek.co.jp/rq/rr.txt')
f = open("rr.txt", "r")
for line in f:
   mylist = line.split(' ')
   res = filter(lambda w:w != '' and w != '\n', mylist)
#                        2024 02 12 21 45 15 31 番組名 00
   dt_now = datetime.datetime.now()
   year = dt_now.year
   month=dt_now.month
   day=dt_now.day
   hour=dt_now.hour
   minute=dt_now.minute
   if minute  >= 55:
      hour = hour+1
      if hour >=24:
         hour =0
         day = datetime.datetime.now() + datetime.timedelta(days = 1).day
         month = datetime.datetime.now() + datetime.timedelta(days = 1).month
         year  = datetime.datetime.now() + datetime.timedelta(days = 1).year
   if dt_now.year == (int(mylist[0]))  and dt_now.month == (int(mylist[1]))  and dt_now.day == (int(mylist[2])):
       if hour == (int(mylist[3])):
          if (minute  < 55  and  ( int(mylist[4]) - minute) <=5  and  int(mylist[4]) > minute)  or  ( minute  >= 55 and int(mylist[4]) <5):
               cmd = f"/usr/local/bin/recpt1  --b25 --strip " + mylist[6] + " " + str(int(mylist[5])*60+60) + " /media/tvrec/" + mylist[7] + mylist[1] + mylist[2] + mylist[3] + mylist[4] + ".ts &"
               print(cmd)
               args = shlex.split(cmd)
               ret = subprocess.call(args)
               f.close()
               break
f.close()
