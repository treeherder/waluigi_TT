import sqlite3
import bot
from multiprocessing import Process

def strm():
  stream.filter(track=['year luigi'])

def prnt():
  c = sqlite3.connect('waluigi_tt.db')
  cur = c.cursor()
  cur.execute("SELECT user,status from tweets order by user, limit 1") 
  r = cur.fetchone()
  print "content {0}".format(r)

while True:
  proc_1 =  Process(target=strm)
  proc_2 = Process(target=prnt)
  proc_1.start()
  proc_2.start()
  proc_1.join()  #block the proc1 until terminates
  proc_2.join()  #block the proc2 until terminates
