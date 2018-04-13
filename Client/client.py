import sys, Ice


Ice.loadSlice('../meta-server.ice')

import MetaServer

with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("MetaServer:default -p 10000")
    metaServer = MetaServer.IMetaServerPrx.checkedCast(base)
    if not metaServer:
        raise RuntimeError("Invalid proxy")

    musics = metaServer.startStreaming("aze","aze","aze")
    print(musics)