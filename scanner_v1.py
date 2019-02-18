from socket import *
print("\n\t==Port Scanner By Mohamed Ali Ayedi==")
ip=raw_input("\t\tTARGET IP >>> ")
port= input("\t\tPORT To SCAN >>> ")
s=socket(AF_INET,SOCK_STREAM)
try:
  s.connect((ip,port))
  print " Port "+str(port)+" is Open !"
except:
  print "Port is Close "
