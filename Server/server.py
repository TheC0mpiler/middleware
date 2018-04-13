import Ice,sys,signal,os, shutil

Ice.loadSlice('../server.ice')
Ice.loadSlice('../meta-server.ice')

import Server
import MetaServer

class IServer(Server.IServer):

	musics = list()

	def searchMusic(self,name,author,album,current):
		print(self.musics)
		return self.musics
	
	def addMusic(self,fileName,current):
		f = open("../Client-Admin/"+fileName)
		lines =  f.readlines()
		f.close()
		for line in lines:
			line = line.rstrip()
			line = line.split("|")
			shutil.copy2('../Client-Admin/'+line[3], 'music')
			tmp = Server.Song(line[0],line[1],line[2],line[3],line[4],int(line[5]))
			self.musics.append(tmp)
		print("music added !")

def signal_handler(signal, frame):
	print('You pressed Ctrl+C!')
	metaServer.deconnectMe(str(port))
	sys.exit(0)

with Ice.initialize(sys.argv) as communicator:
	err = True
	port = 10000
	name = "Server"
	while err :
	    try :
	        err = False
	        adapter = communicator.createObjectAdapterWithEndpoints("ServerAdapter", "default -p "+str(port))
	    except :
	        err = True
	        port += 1
	object = IServer()
	adapter.add(object, communicator.stringToIdentity("Server"))
	adapter.activate()


	print(name+":"+"default -p "+str(port))


	base = communicator.stringToProxy("MetaServer:default -p 10000")
	metaServer = MetaServer.IMetaServerPrx.checkedCast(base)
	if not metaServer:
	    raise RuntimeError("Invalid proxy")

	metaServer.connectToMe(str(port))
	signal.signal(signal.SIGINT, signal_handler)
	communicator.waitForShutdown()