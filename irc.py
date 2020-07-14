import socket
import sys

server = "chat.freenode.net"       #settings
channel = "#colbydray"
botnick = "ColbyCoMBBot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ channel +"\n")        #join the chan

while 1:    #puts it in a loop
   text=irc.recv(2040)  #receive the text
   print text   #print text to console

   if text.find('PING') != -1:                          #check if 'PING' is found
		irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)
   if text.find(':[request]') !=-1: #you can change !hi to whatever you want
    t = text.split(':[request]') #you can change t and to :)
    to = t[1].strip() #this code is for getting the first word after !hi
    f=open(str(to),"w+")
    f.close()
    irc.send('PRIVMSG '+channel+' :Your request "'+str(to)+'" was sent to colbydray. \r\n')
