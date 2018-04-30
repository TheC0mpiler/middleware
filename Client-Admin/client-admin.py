import sys, Ice


Ice.loadSlice('../server.ice')


import Server

<<<<<<< HEAD
communicator = Ice.initialize(sys.argv)
port = input("Port : ")
fichier = raw_input("Fichier : ")
base = communicator.stringToProxy("Server:default -p "+str(port))
printer = Server.IServerPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

printer.addMusic(fichier)
=======
with Ice.initialize(sys.argv) as communicator:
	port = input("Port : ")
	fichier = raw_input("Fichier : ")
	base = communicator.stringToProxy("Server:default -p "+str(port))
	printer = Server.IServerPrx.checkedCast(base)
	if not printer:
	    raise RuntimeError("Invalid proxy")

	printer.addMusic(fichier)
>>>>>>> bb4c14bf5be3145d94f84aeb73afbb8d795f2c97

