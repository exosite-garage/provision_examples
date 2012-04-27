#==============================================================================
# provision_device.py
# Python script that has routines to verify device/client-speicific provision
# API calls for Exosite's One Platform API  
#==============================================================================
## Tested with python 2.7
##
## Copyright (c) 2012, Exosite LLC
## All rights reserved.
##
## For License see LICENSE file
##
## NOTE: We use primitive socket interaction (raw headers and body) so that
## embedded developers can more-easily use this code for their software 
##
import sys
import socket

#===============================================================================
class ProvisionDevice():
#===============================================================================
#-------------------------------------------------------------------------------
  def __init__(self, host, port, vendorname, devicemodel, contentid):
    self.host = host
    self.port = port
    self.vendorName = vendorname
    self.deviceModel = devicemodel
    self.contentID = contentid
    self.deviceCIK = ''
    
#-------------------------------------------------------------------------------
  def provisionActivatePOST(self, serialnum): # /provision/activate POST
    print '\r\n\r\n*************************************'
    print __name__,'(activate device)'
    
    body = 'vendor=' + self.vendorName + '&model=' + self.deviceModel + '&sn=' + serialnum
    length = len(body)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('POST /provision/activate HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('Content-Type: application/x-www-form-urlencoded; charset=utf-8\r\n')
    s.send('Content-Length: ' + str(length) + '\r\n\r\n')
    s.send(body)
    
    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n'

    code = self.getbody(data)
    
    if (-1 != code.find('HTTP/1.1 4')):
      print 'FAILED', code
      sys.exit()
      return
    
    self.deviceCIK = code
    
#-------------------------------------------------------------------------------
  def provisionDownloadGET(self, param = ''): # /provision/download GET
    print '\r\n\r\n*************************************'
    print __name__,'(download or info on content)'
    
    params = 'vendor=' + self.vendorName + '&model=' + self.deviceModel + '&id=' + self.contentID + param
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('GET /provision/download?' + params +' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-CIK: ' + self.deviceCIK + '\r\n\r\n')
    
    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n'

    return self.getbody(data)

#-------------------------------------------------------------------------------
  def ip(self): # /ip GET
    print '\r\n\r\n*************************************'
    print __name__,'(get server ip)'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('GET /ip HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n\r\n')
    
    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n'

    return self.getbody(data)

#-------------------------------------------------------------------------------
  def getbody(self, rxdata):
    line = rxdata.find('\r\n') #end of HTTP line
    if (-1 != line):
      line = rxdata[line:].find('\r\n') #end of Date line
      if (-1 != line):
        line = rxdata[line:].find('\r\n') #end of Server line
        if (-1 != line):
          line = rxdata[line:].find('\r\n') #end of Connection line
          if (-1 != line):
            line = rxdata[line:].find('\r\n\r\n') #end of Content line (beginning of body)
            if (-1 != line):
              return rxdata[line+4:]
    return -1     
    


