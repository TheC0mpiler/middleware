# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.7.0
#
# <auto-generated>
#
# Generated from file `server.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Server
_M_Server = Ice.openModule('Server')
__name__ = 'Server'

if 'Song' not in _M_Server.__dict__:
    _M_Server.Song = Ice.createTempClass()
    class Song(object):
        def __init__(self, name='', author='', album='', path=''):
            self.name = name
            self.author = author
            self.album = album
            self.path = path

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.name)
            _h = 5 * _h + Ice.getHash(self.author)
            _h = 5 * _h + Ice.getHash(self.album)
            _h = 5 * _h + Ice.getHash(self.path)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_Server.Song):
                return NotImplemented
            else:
                if self.name is None or other.name is None:
                    if self.name != other.name:
                        return (-1 if self.name is None else 1)
                else:
                    if self.name < other.name:
                        return -1
                    elif self.name > other.name:
                        return 1
                if self.author is None or other.author is None:
                    if self.author != other.author:
                        return (-1 if self.author is None else 1)
                else:
                    if self.author < other.author:
                        return -1
                    elif self.author > other.author:
                        return 1
                if self.album is None or other.album is None:
                    if self.album != other.album:
                        return (-1 if self.album is None else 1)
                else:
                    if self.album < other.album:
                        return -1
                    elif self.album > other.album:
                        return 1
                if self.path is None or other.path is None:
                    if self.path != other.path:
                        return (-1 if self.path is None else 1)
                else:
                    if self.path < other.path:
                        return -1
                    elif self.path > other.path:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_Server._t_Song)

        __repr__ = __str__

    _M_Server._t_Song = IcePy.defineStruct('::Server::Song', Song, (), (
        ('name', (), IcePy._t_string),
        ('author', (), IcePy._t_string),
        ('album', (), IcePy._t_string),
        ('path', (), IcePy._t_string)
    ))

    _M_Server.Song = Song
    del Song

if '_t_SongSeq' not in _M_Server.__dict__:
    _M_Server._t_SongSeq = IcePy.defineSequence('::Server::SongSeq', (), _M_Server._t_Song)

_M_Server._t_IServer = IcePy.defineValue('::Server::IServer', Ice.Value, -1, (), False, True, None, ())

if 'IServerPrx' not in _M_Server.__dict__:
    _M_Server.IServerPrx = Ice.createTempClass()
    class IServerPrx(Ice.ObjectPrx):

        def searchMusic(self, name, author, album, context=None):
            return _M_Server.IServer._op_searchMusic.invoke(self, ((name, author, album), context))

        def searchMusicAsync(self, name, author, album, context=None):
            return _M_Server.IServer._op_searchMusic.invokeAsync(self, ((name, author, album), context))

        def begin_searchMusic(self, name, author, album, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.IServer._op_searchMusic.begin(self, ((name, author, album), _response, _ex, _sent, context))

        def end_searchMusic(self, _r):
            return _M_Server.IServer._op_searchMusic.end(self, _r)

        def addMusic(self, fileName, context=None):
            return _M_Server.IServer._op_addMusic.invoke(self, ((fileName, ), context))

        def addMusicAsync(self, fileName, context=None):
            return _M_Server.IServer._op_addMusic.invokeAsync(self, ((fileName, ), context))

        def begin_addMusic(self, fileName, _response=None, _ex=None, _sent=None, context=None):
            return _M_Server.IServer._op_addMusic.begin(self, ((fileName, ), _response, _ex, _sent, context))

        def end_addMusic(self, _r):
            return _M_Server.IServer._op_addMusic.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Server.IServerPrx.ice_checkedCast(proxy, '::Server::IServer', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Server.IServerPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Server::IServer'
    _M_Server._t_IServerPrx = IcePy.defineProxy('::Server::IServer', IServerPrx)

    _M_Server.IServerPrx = IServerPrx
    del IServerPrx

    _M_Server.IServer = Ice.createTempClass()
    class IServer(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Server::IServer')

        def ice_id(self, current=None):
            return '::Server::IServer'

        @staticmethod
        def ice_staticId():
            return '::Server::IServer'

        def searchMusic(self, name, author, album, current=None):
            raise NotImplementedError("servant method 'searchMusic' not implemented")

        def addMusic(self, fileName, current=None):
            raise NotImplementedError("servant method 'addMusic' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Server._t_IServerDisp)

        __repr__ = __str__

    _M_Server._t_IServerDisp = IcePy.defineClass('::Server::IServer', IServer, (), None, ())
    IServer._ice_type = _M_Server._t_IServerDisp

    IServer._op_searchMusic = IcePy.Operation('searchMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_Server._t_SongSeq, False, 0), ())
    IServer._op_addMusic = IcePy.Operation('addMusic', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())

    _M_Server.IServer = IServer
    del IServer

# End of module Server
