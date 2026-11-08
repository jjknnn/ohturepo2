from urllib import request
from project import Project
from toml import loads


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_toml = loads(content)
        dep_groups = parsed_toml["dependency-groups"]
        authors = parsed_toml["project"].get("authors")
        authors = [x.get("name") for x in authors]
        return Project(parsed_toml["project"].get("name"),
                       parsed_toml["project"].get("description"),
                       parsed_toml["project"].get("license"),
                       authors,
                       parsed_toml["project"].get("dependencies"),
                       dep_groups["dev"]
                        )


