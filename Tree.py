class Tree:
    def __init__(self):
        self.children = []

    def add(self):
        pass

    def to_string(self):
        pass

class BasicNode:
    def  __init__(self):
        self.title = "hi"
        self.color = ""
        self.parent = ""

    def remove(self):
        pass

    def add(self):
        pass

class SubtreeNode(BasicNode):
    def __init__(self):
        super().__init__()
        self.children = []


class EventNode(BasicNode):
    def __init__(self):
        super().__init__()
        self.due_date = ""
        self.created_date = ""
        self.priority = 0

