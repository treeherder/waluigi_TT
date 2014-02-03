import sqlite3
import bot
from multiprocessing import Process

def strm():
  stream.filter(track=['year luigi'])

def prnt():
  c = sqlite3.connect('waluigi_tt.db')
  cur = c.cursor()
  cur.execute("select * from tweets where rowid = (select max(rowid) from tweets)")
  r = cur.fetchone()
  print "content {0}".format(r)

strm()
