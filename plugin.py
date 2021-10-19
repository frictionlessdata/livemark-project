from livemark import Plugin


class CustomPlugin(Plugin):
    identity = "custom"

    # Process

    def process_markup(self, markup):
        markup.add_markup("<span>(template)<span>", target="h1")
