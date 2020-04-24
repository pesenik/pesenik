from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Song:
    title: str
    author: str
    authorHash: str
    text: str
    songTitleHash: str


@dataclass
class Author:
    name: str
    nameHash: str
    songList: List[Song]

    def getSong(self, songTitleHash: str) -> Optional[Song]:
        pass


class Pesennik:
    authorList = List[Author]
    currentSong: Song = None

    def getAuthor(self, authorHash: str) -> Optional[Author]:
        pass


class PesenikManager:
    def authorsList(self):
        return ["aaa", "aab"]

    def songsList(self, author):
        if author == "aaa":
            return ["aaa000"]
        elif author == "aab":
            return ["aab000"]
        return []

    def getSong(self, author, song):
        if author == "aaa":
            return Song(
                "Group1Song1",
                "Group1",
                author,
                """"Group1Song1Text:
                    А я ёжиков люблю""",
                song,
            )
        elif author == "aab":
            return Song(
                "Group2Song1",
                "Group2",
                author,
                """"Group2Song1Text:
                    В каморке, что за актовым залом...""",
                song,
            )

    def authorToHash(self, author):
        return "aaa" if author == "Group1" else "aab"

    def hashToAutor(self, authorHash):
        return "Group1" if authorHash == "aaa" else "Group2"

    def songTitleToHash(self, songTitle):
        return "aaa000" if songTitle == "Group1Song1" else "aab000"

    def hashToSongTitle(self, songTitleHash):
        return "Group1Song1" if songTitleHash == "aaa" else "Group2Song1"
