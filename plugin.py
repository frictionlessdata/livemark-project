from livemark import Plugin


class CustomPlugin(Plugin):
    identity = "custom"

    # Process

    def process_snippet(self, snippet):
        pass

    def process_markup(self, markup):
        pass
