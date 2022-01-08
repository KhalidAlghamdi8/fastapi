# import socket
#
#
# serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.bind(('192.168.8.103', 8000))
# serv.listen(5)
# while True:
#     conn, addr = serv.accept()
#     from_client = ''
#     while True:
#         data = conn.recv(4096)
#         if not data: break
#         from_client += data
#         print (from_client)
#         conn.send("sending data".encode('utf-8'))
#     conn.close()
#     print ('client disconnected')