import Ice,sys,signal,os, shutil

Ice.loadSlice('../server.ice')
Ice.loadSlice('../meta-server.ice')

import Server
import MetaServer

import vlc
import time

class IServer(Server.IServer):

	musics = list()

	def findSongPath(name,author,album):
		for music in musics:
			if music.name == name and music.author == author and music.album == album:
				return music.path
		return None	
	def searchMusic(self,name,author,album,current):
		print(self.musics)
		return self.musics
	
	def startStreaming(self,name,author,album,current):
		for music in self.musics:
			if music.name == name and music.author == author and music.album == album:
				path = music.path

		instance = vlc.Instance()

		#Create a MediaPlayer with the default instance
		player = instance.media_player_new()

		#Load the media file
		media = instance.media_new('music/basique.mp3')

		#Add the media to the player
		player.set_media(media)

		#Play for 10 seconds then exit
		player.play()
		time.sleep(10)
	
	def addMusic(self,fileName,current):
		f = open("../Client-Admin/"+fileName)
		lines =  f.readlines()
		f.close()
		for line in lines:
			line = line.rstrip()
			line = line.split("|")
			shutil.copy2('../Client-Admin/'+line[3], "music/"+line[3])
			tmp = Server.Song(line[0],line[1],line[2],"music/"+line[3],line[4],int(line[5]))
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
