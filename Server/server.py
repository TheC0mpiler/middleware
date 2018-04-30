import Ice,sys,signal,os, shutil

Ice.loadSlice('../server.ice')
Ice.loadSlice('../meta-server.ice')

import Server
import MetaServer

import vlc
import time

class IServer(Server.IServer):

	musics = list()
	vlc_instance = None
	vlc_player = None
	options = None

	def __init__(self):
		self.vlc_instance = vlc.Instance()
		self.vlc_player = self.vlc_instance.media_player_new()
<<<<<<< HEAD
		self.options = 'sout=#transcode{ab=128,channels=2,samplerate=44100}:rtp{sdp=rtsp://:8554/}'
=======
		self.options = 'sout=#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100}:rtp{sdp=rtsp://:8554/}'
>>>>>>> bb4c14bf5be3145d94f84aeb73afbb8d795f2c97
        
	def findSongPath(self,name,author,album,current):
		for music in self.musics:
			if music.name == name and music.author == author and music.album == album:
				print(music)
				return music.path
		return None	
	
	def searchMusic(self,name,author,album,current):
		res = list()
		for music in self.musics:
			if ( ( music.name == name ) or ( name == "" ) )  and ( ( music.author == author ) or ( author == "" ) ) and ( ( music.album == album ) or ( album == "" ) ) :
				res.append(music)
		return res

	def setMusic(self,path):
		#Load the media file
		media = self.vlc_instance.media_new(path,self.options)
		
		#Add the media to the player
		self.vlc_player.set_media(media)

	def startStreaming(self,name,author,album,time,current):
		path = self.findSongPath(name,author,album,current)
		if path != None:
			self.setMusic(path)
			print("I Start Streaming")
			self.play(time,current)
		
	def play(self,time,current):
		self.vlc_player.play()
<<<<<<< HEAD
		#self.vlc_player.set_time(time)
=======
		self.vlc_player.set_time(time)
>>>>>>> bb4c14bf5be3145d94f84aeb73afbb8d795f2c97

	def pause(self,current):
		self.vlc_player.release()



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

<<<<<<< HEAD
communicator = Ice.initialize(sys.argv)
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
=======
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
>>>>>>> bb4c14bf5be3145d94f84aeb73afbb8d795f2c97
