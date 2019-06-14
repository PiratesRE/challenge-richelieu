modulus = "00:cd:5f:8a:24:c7:60:50:08:89:7a:3c:92:2c:0e:81:2e:76:9d:e0:a4:64:42:c3:50:cb:78:c7:86:85:39:f3:d3:8a:ac:80:b3:e6:a5:06:60:59:10:e8:59:98:06:b4:d1:d1:48:f2:f6:b8:1d:a0:47:96:a8:a5:ae:e1:8f:29:e8:3e:16:77:5a:2a:0a:00:87:05:41:f6:57:4e:d1:43:86:36:ae:0a:0c:11:6e:07:10:4f:48:f7:20:94:86:3a:38:69:e1:c8:fc:22:06:27:27:89:62:fb:22:87:3e:31:56:f1:8e:55:de:c9:4e:97:00:64:ec:7f:4e:0e:88:45:40:12:e2:fd:5d:fe:5f:8d:19:bf:17:0f:9c:cb:3f:46:e0:fd:10:19:bc:b0:2d:90:83:a0:70:3c:61:7f:99:63:79:e6:47:83:54:a7:3a:e6:e6:ac:bc:e1:f4:33:3e:cf:af:24:36:6a:3e:97:7d:3c:d3:cb:fe:8d:8a:38:7b:d8:76:bf:da:b8:48:8f:6f:47:bf:1f:be:33:01:0f:d2:d7:e2:2b:4d:b2:e5:67:78:3c:e0:b6:06:db:86:b9:37:59:71:4c:4f:63:96:a7:fb:9f:74:c4:02:10:43:b0:f3:d4:6d:26:33:eb:d4:3a:87:78:63:df:7d:68:0f:50:65:87:c1:19:dd:64:10:0c:a8:31:ce:2a:f3:3d:95:1b:52:4c:5f:06:b4:9f:5b:f2:cb:38:1e:74:18:19:30:d0:6a:80:50:5c:06:ab:d5:bf:48:70:f0:c9:fb:58:1b:d8:0d:ba:88:96:60:63:9f:93:6e:de:a8:fe:5d:0c:9e:ae:58:06:2e:d6:93:25:25:83:c7:1c:c7:82:ba:61:3e:01:43:8e:69:b4:3f:9e:64:ec:a8:4f:9e:a0:4e:81:1a:d7:b3:9e:fd:78:76:d1:b6:b5:01:c4:f4:8a:cc:e6:f2:42:39:f6:c0:40:28:78:81:35:cd:88:c3:d1:5b:e0:f2:eb:b7:de:9e:9c:19:a7:a9:30:37:00:5e:e0:a9:a6:40:ba:da:33:2e:c0:d0:5e:e9:f0:8a:83:23:54:a0:48:7a:92:7d:5e:88:06:6e:25:69:e6:c5:d4:68:8e:42:2b:fa:0b:27:c6:17:1c:6d:7b:f0:29:bf:d9:16:57:52:af:19:aa:71:b3:3a:1e:a7:0b:6c:37:1f:b2:1e:47:f5:27:d8:0b:7d:04:f5:82:ad:9f:99:35:af:72:36:82:dc:01:ca:98:80:62:18:70:de:cb:7a:d1:56:48:cd:f4:ef:15:30:16:f3:e6:d8:79:33:b8:ec:54:cf:a1:fd:f8:7c:46:70:20:a3:e7:53"
modulus = modulus.replace(':', '')
exponant = 65537

with open("primes.lst") as dictionary :
  for candidate in dictionary :
    candidate = long(candidate.strip('\n').replace(':', ''), 16)
    if (long(modulus, 16) % long(candidate) == 0) :
      print('-' * 80)
      prime1 = candidate
      prime2 = long(modulus, 16) / prime1
      # print("rsactftool -n %i -p %i -q %i -e %i --private" % (long(modulus, 16), prime1, prime2, exponant))
      print("rsactftool -n %i -p %i -q %i -e %i --uncipherfile motDePasseGPG.txt.enc" % (long(modulus, 16), prime1, prime2, exponant))
