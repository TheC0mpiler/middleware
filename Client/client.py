# -*- coding: utf-8 -*-
import sys, Ice ,time


Ice.loadSlice('../meta-server.ice')

import MetaServer

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("MetaServer:default -p 10000")
    metaServer = MetaServer.IMetaServerPrx.checkedCast(base)
    if not metaServer:
        raise RuntimeError("Invalid proxy")

    metaServer.startStreaming("Basique","Orelsan","La fête est finie");

    