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
        void startStreaming(string name, string author, string album,int time);
        void connectToMe(string port);
        void deconnectMe(string port);
        void play();
        void pause();
    };
};
