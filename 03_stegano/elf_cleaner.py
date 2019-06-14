#!/usr/bin/env python2.7

def write_file(path_to_file, mode, data) :
  try :
    with open(path_to_file, mode) as written_file :
      written_file.write(data)
  except IOError :
    return(False)
  print(" writting:\t%s" % (path_to_file))
  return(True)

data = ""
with open("elf_payload.bin") as f :
  for line in f :
    data = data + line[10:-19].replace(' ', '')

write_file("elf_cleaned.bin", "w", data)