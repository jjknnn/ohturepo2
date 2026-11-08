class Project:
    def __init__(self, name, description, licence, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.licence = licence
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_lists(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.licence}"
            f"\n\nAuthors:\n- {self._stringify_lists(self.authors)}"
            f"\n\nDependencies:\n- {self._stringify_lists(self.dependencies)}"
            f"\n\nDevelopment dependencies:\n- {self._stringify_lists(self.dev_dependencies)}"
        )
