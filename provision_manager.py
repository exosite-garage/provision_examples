#==============================================================================
# provision_manager.py
# Python script that has routines to verify vendor manager-speicific provision
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
class ProvisionManager():
#===============================================================================
#-------------------------------------------------------------------------------
  def __init__(self, host, port, vendortoken, devicemodel, clonerid, contentid):
    self.host = host
    self.port = port
    self.vendorToken = vendortoken
    self.deviceModel = devicemodel
    self.deviceCloneRID = clonerid
    self.contentID = contentid
    
#-------------------------------------------------------------------------------
  def provisionManageModelPOST(self): # /provision/manage/model/ POST
    print '\r\n\r\n*************************************'
    print __name__,'(create model)'
    
    body = 'model=' + self.deviceModel + '&rid=' + self.deviceCloneRID + '&options[]=noaliases'
    length = len(body)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('POST /provision/manage/model/ HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n')
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
      
#-------------------------------------------------------------------------------
  def provisionManageModelGET(self): # /provision/manage/model/ GET
    print '\r\n\r\n*************************************'
    print __name__,'(list models)'
    print 'vendor token is '+self.vendorToken+'.'  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('GET /provision/manage/model/ HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n'

    return self.getbody(data)
    
#-------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------
  def provisionManageModelModelGET(self): # /provision/manage/model/<model> GET
    print '\r\n\r\n*************************************'
    print __name__,'(show model info)'
      
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('GET /provision/manage/model/' + self.deviceModel + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n' 

    return self.getbody(data)
    
#-------------------------------------------------------------------------------    
  def provisionManageModelModelPUT(self, param = ''): # /provision/manage/model/<model> PUT
    print '\r\n\r\n*************************************'
    print __name__,'(update model)'

    body = 'rid=' + self.deviceCloneRID + param
    length = len(body)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('PUT /provision/manage/model/' + self.deviceModel + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n')
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
      
#-------------------------------------------------------------------------------    
  def provisionManageModelModelDELETE(self): # /provision/manage/model/<model> DELETE
    print '\r\n\r\n*************************************'
    print __name__,'(delete model)'
      
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('DELETE /provision/manage/model/' + self.deviceModel + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n' 
    
    code = self.getbody(data)
    
    if (-1 != code.find('HTTP/1.1 4')):
      print 'FAILED', code
      sys.exit()

#-------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------
  def provisionManageContentModelPOST(self): # /provision/manage/content/<model>/ POST
    print '\r\n\r\n*************************************'
    print __name__,'(create content entity)'
    
    body = 'id=' + self.contentID + '&description=New_Firmware'
    length = len(body)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('POST /provision/manage/content/' + self.deviceModel + '/ HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n')
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
      
#-------------------------------------------------------------------------------
  def provisionManageContentModelGET(self): # /provision/manage/content/<model>/ GET
    print '\r\n\r\n*************************************'
    print __name__,'(list model content files)'
      
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('GET /provision/manage/content/' + self.deviceModel + '/ HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n' 

    return self.getbody(data)
    
#-------------------------------------------------------------------------------  
#-------------------------------------------------------------------------------
  def provisionManageContentModelIDPOST(self): # /provision/manage/content/<model>/<id> POST
    print '\r\n\r\n*************************************'
    print __name__,'(upload content)'
    
    body = 'THISISMYFIRMWAREFILE'
    length = len(body)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('POST /provision/manage/content/' + self.deviceModel + '/' + self.contentID + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n')
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
      
#-------------------------------------------------------------------------------
  def provisionManageContentModelIDGET(self, param = ''): # /provision/manage/content/<model>/<id> GET
    print '\r\n\r\n*************************************'
    print __name__,'(download content or content info)'
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('GET /provision/manage/content/' + self.deviceModel + '/' + self.contentID + '?' + param + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n' 

    return self.getbody(data)
    
#-------------------------------------------------------------------------------
  def provisionManageContentModelIDDELETE(self): # /provision/manage/content/<model>/<id> DELETE
    print '\r\n\r\n*************************************'
    print __name__,'(delete content)'
      
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('DELETE /provision/manage/content/' + self.deviceModel + '/' + self.contentID + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n' 

    code = self.getbody(data)
    
    if (-1 != code.find('HTTP/1.1 4')):
      print 'FAILED', code
      sys.exit()
      
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
  def provisionManageModelModelInfoPOST(self, param = ''): # /provision/manage/model/<model>/ POST
    print '\r\n\r\n*************************************'
    print __name__,'(add serial numbers)'
    
    body = param
    length = len(body)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('POST /provision/manage/model/' + self.deviceModel + '/ HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n')
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
      
#-------------------------------------------------------------------------------
  def provisionManageModelModelInfoGET(self, param = ''): # /provision/manage/model/<model>/ GET
    print '\r\n\r\n*************************************'
    print __name__,'(list serial numbers)'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('GET /provision/manage/model/' + self.deviceModel + '/?' + param + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n'

    return self.getbody(data)
    
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
  def provisionManageModelModelSNPOST(self, serialnumber, param = ''): # /provision/manage/model/<model>/<sn> POST
    print '\r\n\r\n*************************************'
    print __name__,'(instantiate/move/enable/disable a client)'
    
    body = param
    length = len(body)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('POST /provision/manage/model/' + self.deviceModel + '/' + serialnumber + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n')
    s.send('Content-Type: application/x-www-form-urlencoded; charset=utf-8\r\n')
    s.send('Content-Length: ' + str(length) + '\r\n\r\n')
    s.send(body)

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n'

    code = self.getbody(data)
    
    if (-1 != code.find('HTTP/1.1 4')):
      print 'FAILED', code
      self.provisionManageModelModelInfoPOST('remove=true&sn=' + serialnumber);
      sys.exit()
     
    print 'Response was ' + code
      
#-------------------------------------------------------------------------------
  def provisionManageModelModelSNGET(self, serialnumber, param = ''): # /provision/manage/model/<model>/<sn> GET
    print '\r\n\r\n*************************************'
    print __name__,'(show serial number status and most recent activity log)'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('GET /provision/manage/model/' + self.deviceModel + '/' + serialnumber + '?' + param + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n'

    return self.getbody(data)
    
#-------------------------------------------------------------------------------
  def provisionManageModelModelSNDELETE(self, serialnumber): # /provision/manage/model/<model>/<sn> DELETE
    print '\r\n\r\n*************************************'
    print __name__,'(delete serial numbers)'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    s.send('DELETE /provision/manage/model/' + self.deviceModel + '/' + serialnumber + ' HTTP/1.1\r\n')
    s.send('Host: m2.exosite.com\r\n')
    s.send('X-Exosite-Token: ' + self.vendorToken + '\r\n\r\n')

    data = s.recv(1024)
    s.close()
    print '\r\nReceived: \r\n', repr(data),'\r\n\r\n'    

    code = self.getbody(data)
    
    if (-1 != code.find('HTTP/1.1 4')):
      print 'FAILED', code
      sys.exit()
      
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




