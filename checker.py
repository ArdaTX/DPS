#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
import urllib.request as urllib
request = urllib.build_opener()
request.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]
server = 'https://api.ipify.org'
try:
  url = request.open(server, timeout=20)
  request = url.read()
  url.close()
  try:
      request = request.decode('UTF-8')
  except UnicodeDecodeError:
      request = request.decode('ISO-8859-1')
  print(' Tu IP Externa es:'+request)
except:
 print('Try Later Monkey '+server)

