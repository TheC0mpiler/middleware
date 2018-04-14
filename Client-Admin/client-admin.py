import sys, Ice


Ice.loadSlice('../server.ice')


import Server

with Ice.initialize(sys.argv) as communicator:
	port = input("Port : ")
	fichier = raw_input("Fichier : ")
	base = communicator.stringToProxy("Server:default -p "+str(port))
	printer = Server.IServerPrx.checkedCast(base)
	if not printer:
	    raise RuntimeError("Invalid proxy")

	printer.addMusic(fichier)

