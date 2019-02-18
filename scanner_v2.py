from socket import *
print("\n\n\t*******Port Scanner By Mohamed Ali Ayedi v2 *******")
i=0 # compteur to compte nombre of port open
ip=raw_input("TARGET IP >> ") # varibale str (ip)
for port in range(0,10000): # loop for 0 > 10000 (port)
 s=socket(AF_INET,SOCK_STREAM) # varibale to libary socket 
 s.settimeout(5) # time out
 if(s.connect_ex((ip,port))==0): # if reverse connection not null the port open ;)
   print "\t\tPort",port, "  is Open" # print
   i+=1 # compteur +1 if port open 
 s.close() #close connection
print(" *******************************************************************")
print " * Scannig Host | "+ip+" | completed Found  > "+str(i)+" <  Port is Open *"
print(" *******************************************************************\n\n")


