import Ice,sys

Ice.loadSlice('../server.ice')
Ice.loadSlice('../meta-server.ice')

import Server
import MetaServer


class IMetaServer(MetaServer.IMetaServer):
	servers = list()
	streamServer = None
	def searchMusic(self,name,author,album,current):
		print("Search Music")
		with Ice.initialize(sys.argv) as communicator:
		    
			responses = list()
				
			musics = list()

			for server in self.servers:

				base = communicator.stringToProxy("Server:default -p "+server)
				connection = Server.IServerPrx.checkedCast(base)
				if not server:
				    raise RuntimeError("Invalid proxy")
		
				request = connection.begin_searchMusic(name,author,album)
				responses.append(connection.end_searchMusic(request))

			for response in responses:
				for music in response:
					musics.append(MetaServer.Song(music.name,music.author,music.album,music.path,music.cover,music.duration))

		return musics	
	def startStreaming(self,name,author,album,time,current):
		if self.streamServer != None:
			self.pause(current)	
		with Ice.initialize(sys.argv) as communicator:
			for server in self.servers:
				base = communicator.stringToProxy("Server:default -p "+server)
				connection = Server.IServerPrx.checkedCast(base)
				if not connection:
				    raise RuntimeError("Invalid proxy")

				async = connection.begin_findSongPath(name,author,album)
				ok = connection.end_findSongPath(async)
				print(name+" "+author+" "+album)
				print(ok)
				if ok != None:
					self.streamServer = server
					print("Start streaming on server "+self.streamServer)
					connection.startStreaming(name,author,album,time)
					break

	def play(self,time,current):
		if self.streamServer != None :
			with Ice.initialize(sys.argv) as communicator:
				base = communicator.stringToProxy("Server:default -p "+self.streamServer)
				connection = Server.IServerPrx.checkedCast(base)
				if not connection:
				    raise RuntimeError("Invalid proxy")
				print("Play server "+self.streamServer)
				connection.play(time)
	
	def pause(self,current):
		if self.streamServer != None :
			with Ice.initialize(sys.argv) as communicator:
				base = communicator.stringToProxy("Server:default -p "+self.streamServer)
				connection = Server.IServerPrx.checkedCast(base)
				if not connection:
				    raise RuntimeError("Invalid proxy")
				print("Pause server "+self.streamServer)
				connection.pause()
		self.streamServer = None
			

	def connectToMe(self,port,current):
		self.servers.append(port)
		print(self.servers)
	
	def deconnectMe(self,port,current):
		for server in self.servers:
			if port in str(server):
				self.servers.remove(server)

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("MetaServerAdapter", "default -p 10000")
    object = IMetaServer()
    adapter.add(object, communicator.stringToIdentity("MetaServer"))
    adapter.activate()
    communicator.waitForShutdown()