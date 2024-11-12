class Project:
    def __init__(self, name, description, dependencies, dev_dependencies,authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _listify_dependencies(self, dependencies):
        return "\n" + "\n".join([f"- {dependency}" for dependency in dependencies]) + "\n"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: {self._listify_dependencies(self.authors)}"
            f"\nDependencies:{self._listify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies: {self._listify_dependencies(self.dev_dependencies)}"
        )
