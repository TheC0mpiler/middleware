import Ice,sys

Ice.loadSlice('../server.ice')
Ice.loadSlice('../meta-server.ice')

import Server
import MetaServer


class IMetaServer(MetaServer.IMetaServer):
	servers = list()
	def searchMusic(self,name,author,album,current):
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