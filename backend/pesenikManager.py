from collections import OrderedDict
from dataclasses import dataclass
from typing import OrderedDict as OrderedDictT
import os


@dataclass
class Song:
    title: str
    titleHash: str

    author: str
    authorHash: str

    text: str


@dataclass
class Author:
    name: str
    nameHash: str
    songs: OrderedDictT[str, Song]


def authorHash(name:str):
    return name[0:3]

def titleHash(name:str):
    return name[0:3]


class Pesenik:
    authors: OrderedDictT[str, Author]
    currentSong: Song = None

    def __init__(self):
        self.authors = OrderedDict()
        for root, dirs, files in os.walk("..", True):
            if "Songs" in root:
                path = root.split(os.sep)
                for dir in dirs:
                    authorObj = Author(name = dir, nameHash = authorHash(dir), songs = OrderedDict())
                    self.authors[authorObj.nameHash] = authorObj
                if "Songs" + os.sep in root:
                    for file in files:
                        songFile = open(root + os.sep + file, "r")
                        self.authors[authorHash(path[-1])].songs[titleHash(file)] = (Song(title = file, titleHash = titleHash(file), author = path[-1],     authorHash= authorHash(path[-1]), text = songFile.read()))
                    self.authors[authorHash(path[-1])].songs = OrderedDict(sorted(self.authors[authorHash(path[-1])].songs.items()))
        self.authors = OrderedDict(sorted(self.authors.items(), key = lambda www: www[1].name))
