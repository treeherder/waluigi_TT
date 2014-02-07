import sqlite3

def write_file(lines):
  f = open("data.txt", "a+")
  f.writelines("{0}\n".format(lines))
c = sqlite3.connect('waluigi_tt.db')
with c:
  cu = c.cursor()
  cu.execute("SELECT status FROM tweets")
while 1:
  r = cu.fetchone()
  if r == None:
    break
  print r
  write_file(r)
