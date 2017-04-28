#import socket for networking
import socket
#import time for displaying timestamp
import time


host = '192.168.236.31'
port = 5000

#list of clients
clients = []

#socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bins the host and the port to the socket object
s.bind((host,port))
#as ive read, all sockets are set to blocking mode. so set it to non blocking state for if the recv() or send() call is empty it will push thru
s.setblocking(0)

quitting = False
print "Server Started."

while not quitting:
    try:
            #receive data from socket, data: the string data received ; addr: address of the socket sending the data
            data, addr = s.recvfrom(1024)
            if "Quit" in str(data):
                    #if the word quit is in the data sent, it will trigger the server to stop.
                    qutting = True
            if addr not in clients:
                    #if the addr is not existing in the clients list, we will add it.
                    clients.append(addr)
            #prints the timestamp , ipaddress and port and the data sent
            print time.ctime(time.time()) + str(addr) + ": :" + str(data)

            for client in clients:
                    #sends the data to all the addresses in the client list
                    s.sendto(data, client)
    except:
            pass
#close the socket
s.close()
