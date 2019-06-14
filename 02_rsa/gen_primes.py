#!/usr/bin/env python2.7

def write_file(path_to_file, mode, data) :
  try :
    with open(path_to_file, mode) as written_file :
      written_file.write(data)
  except IOError :
    return(False)
  print(" writting:\t%s" % (path_to_file))
  return(True)

prime_mask = "00:I1A:40:dc:44:ba:03:d1:53:42:f7:59:08:e0:f9:30:05:96:64:4a:de:94:68:5e:08:e2:8c:9a:b1:64:0c:2f:62:c2:9a:b9:a2:39:82:4b:9e:be:eb:76:ae:6d:87:21:a3:5e:9e:d9:8d:7e:I7:38:3e:59:09:34:a5:78:I10:f7:2e:89:5d:5c:37:52:ea:fd:f6:31:cc:ba:d2:d9:60:e4:45:1d:67:76:d2:1f:I5:9c:9d:c9:b1:90:45:51:ed:d2:I2:dd:b6:74:b4:99:I3:b1:0a:d9:b7:c2:be:8b:I8:07:22:0a:8e:3a:36:ff:6d:c1:1d:63:93:af:cb:4e:c0:47:9f:65:bf:df:e3:f0:5f:1e:98:61:45:74:ec:36:a7:a5:b1:f1:8d:3d:97:6b:5a:82:49:09:00:08:0d:9d:c2:74:I9:4e:30:a1:39:68:2f:22:34:71:13:aa:3b:f2:20:4f:8e:10:eb:d4:d0:9b:I11:8c:c2:53:5f:9d:71:13:0c:0f:21:b6:6e:13:39:40:d3:a6:b1:eb:74:ad:dd:0a:29:14:81:b1:90:ad:e0:53:f0:89:c8:00:fe:dc:ad:56:59:fc:28:1d:c0:cf:5e:08:c0:I6:33:24:a3:52:bb:f3:25:10:43:c3:73:b8:40:4f:fc:6b:6b:77:bd:5f:22:24:eb:I4:15"

candidate = ""
for a in range(2) :
  key = ["7f", "fb"]
  p = prime_mask.replace("I1A", key[a])
  candidate = candidate + p + '\n'
write_file("candidates1.txt", 'w+', candidate)

candidate = ""
with open("candidates1.txt") as f :
  for line in f :
    for k in ["7f", "fb"] :
      p = line.replace("I2", k)
      candidate = candidate + p + '\n'
write_file("candidates2.txt", 'w+', candidate)

candidate = ""
with open("candidates2.txt") as f :
  for line in f :
    for k in ["7f", "fb"] :
      p = line.replace("I3", k)
      candidate = candidate + p + '\n'
write_file("candidates3.txt", 'w+', candidate)

candidate = ""
with open("candidates3.txt") as f :
  for line in f :
    for k in ["7f", "fb"] :
      p = line.replace("I4", k)
      candidate = candidate + p + '\n'
write_file("candidates4.txt", 'w+', candidate)

candidate = ""
with open("candidates4.txt") as f :
  for line in f :
    for k in ["f4", "12"] :
      p = line.replace("I5", k)
      candidate = candidate + p + '\n'
write_file("candidates5.txt", 'w+', candidate)

candidate = ""
with open("candidates5.txt") as f :
  for line in f :
    for k in ["16", "54"] :
      p = line.replace("I6", k)
      candidate = candidate + p + '\n'
write_file("candidates6.txt", 'w+', candidate)

candidate = ""
with open("candidates6.txt") as f :
  for line in f :
    for k in ["a4", "57"] :
      p = line.replace("I7", k)
      candidate = candidate + p + '\n'
write_file("candidates7.txt", 'w+', candidate)

candidate = ""
with open("candidates7.txt") as f :
  for line in f :
    for k in ["a4", "57"] :
      p = line.replace("I8", k)
      candidate = candidate + p + '\n'
write_file("candidates8.txt", 'w+', candidate)

candidate = ""
with open("candidates8.txt") as f :
  for line in f :
    for k in ["a4", "57"] :
      p = line.replace("I9", k)
      candidate = candidate + p + '\n'
write_file("candidates9.txt", 'w+', candidate)

candidate = ""
with open("candidates9.txt") as f :
  for line in f :
    for k in ["b5", "cd"] :
      p = line.replace("I10", k)
      candidate = candidate + p + '\n'
write_file("candidates10.txt", 'w+', candidate)

candidate = ""
with open("candidates10.txt") as f :
  for line in f :
    for k in ["b5", "cd"] :
      p = line.replace("I11", k)
      candidate = candidate + p + '\n'
write_file("candidates11.txt", 'w+', candidate)
