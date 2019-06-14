#!/usr/bin/env python2.7

def read_file_to_buffer(path_to_file, mode) :
  from os.path import isfile

  if(not(isfile(path_to_file))) : return(False)
  try :
    with open(path_to_file, mode) as file_stream :
      file_content = file_stream.read()
  except Exception as Exception_Error :
    print("%s", (Exception_Error))
    return(False)
  return(file_content)

def write_file(path_to_file, mode, data) :
  try :
    with open(path_to_file, mode) as written_file :
      written_file.write(data)
  except IOError :
    return(False)
  print(" writting:\t%s" % (path_to_file))
  return(True)

data = read_file_to_buffer("Richelieu.b64.txt", 'r').replace("\r\n", '')
from base64 import b64decode

write_file("Richelieu.bin", 'w', b64decode(data))