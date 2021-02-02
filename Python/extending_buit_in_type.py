class Text(str):
    def duplicate(self):
        return self + self


text  = Text("Python")
text.lower()