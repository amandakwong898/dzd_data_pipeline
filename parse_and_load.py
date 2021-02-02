import sqlite3
from collections import Counter

def mer(mystring):
  mystring_len = len(mystring)
  possible_matches = []
  matches = []
  for start_index in range(0, mystring_len-2):
    for end_index in range(start_index+1, mystring_len+1):
      current_string = mystring[start_index:end_index]
      if len(current_string) == 21:
        possible_matches.append(mystring[start_index:end_index])
  for possible_match, count in Counter(possible_matches).most_common():
    if count < 1: break
    matches.append((possible_match, count))
  for match, count in matches:
    print(f'{match}: {count}')
  return len(matches)

filename = 'SP1.fastq'
with open(filename) as file_object:
  lines = file_object.readlines()
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute("CREATE TABLE kmer(k_mer TEXT NOT NULL,count INTEGER)")
print ("Table created!!!")
con.commit()
con.close()

for line in lines:
  upper = [ch for ch in line if ch.isupper() or ch.isspace()]
  if len(upper) == len(line):
    print(line.rstrip())
    k_mer = line.rstrip()
    count = mer(line.rstrip())
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO kmer(k_mer,count) VALUES(?,?)", (k_mer,count))
    print ("Data Inserted!!!")
    con.commit()
    con.close()