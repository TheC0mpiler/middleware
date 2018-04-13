#pragma once
module MetaServer
{
    struct Song
    {
        string name;
        string author;
        string album;
        string path;
        string cover;
        int duration;
    };  
    sequence<Song> SongSeq;
    interface IMetaServer
    {
        SongSeq searchMusic(string name, string author, string album);
        void connectToMe(string port);
        void deconnectMe(string port);
    };
};
