class Label:
    def __init__(self):
        self.__text = None

    def get_text(self):
        return self.__text

    def set_text(self, value):
        self.__text = value

    def del_text(self):
        del self.__text

    text = property(get_text, set_text, del_text)

arial = Label()
arial.text = 10
print(arial.get_text())
print(arial.text)