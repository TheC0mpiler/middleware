#pragma once
module Server
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
    interface IServer
    {
        SongSeq searchMusic(string name, string author, string album);
        void startStreaming(string name, string author, string album, int time);
        string findSongPath(string name, string author, string album);
        void addMusic(string fileName);
        void play(int time);
        void pause();
    };
};
