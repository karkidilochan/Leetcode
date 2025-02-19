class StringBuilder:

    def __init__(self):
        self.fragments = []

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError("Only strings can be appended")

        self.fragments.append(string)

    def __str__(self):
        return " ".join(self.fragments)

    def clear(self):
        self.fragments = []

    def insert(self, string, index):
        if not isinstance(string, str):
            raise TypeError("Only strings can be appended")

        self.fragments.insert(index, string)

    def delete(self, index):
        self.fragments.pop(index)
