import socket,cv2, pickle,struct,imutils
from cryptography.fernet import Fernet

#generuje klíč a uloži ho do souboru
key = Fernet.generate_key()#generuje 256-bitový klíč
fernet = Fernet(key) #vytvaři instanci s klíčem jako argument konstruktoru
with open('Key.key','wb') as f:
    f.write(key) #zadava klíč do souboru .key



# Soket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host_name  = socket.gethostname()
host_name = "127.0.0.1"
host_ip = socket.gethostbyname(host_name)
print('HOST IP:',host_ip)
port = 9999
socket_address = (host_ip,port)

# Socket
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:",socket_address)

# Socket Accept
while True:
	client_socket,addr = server_socket.accept()
	print('GOT CONNECTION FROM:',addr)
	if client_socket:
		vid = cv2.VideoCapture("movie.Mjpeg")
		
		while(vid.isOpened()):
			img,frame = vid.read()
			frame = imutils.resize(frame,width=500)
			a = pickle.dumps(frame) #převod obrazových dat do hexadecimální
			a=fernet.encrypt(a) #šifrování hexadecimální text
			message = struct.pack("Q",len(a))+a #balení datového toku do balíčků
			client_socket.sendall(message)#odeslání šifrovaných dat klientovi

			cv2.imshow('TRANSMITTING VIDEO',frame)
			key = cv2.waitKey(1) & 0xFF
			if key ==ord('q'):
				client_socket.close()
