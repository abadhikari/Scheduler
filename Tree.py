import datetime

# TODO: Methods to add to the nodes:
#  - .toJson
#  - a nice __str__ method (with indentation for subtrees)

class BasicTreeNode:
    def __init__(self, name):
        self.name = name
        self.parent = None # To satisfy pyLint

class SubjectNode(BasicTreeNode):
    def __init__(self, name):
        # Add a color property to this class when we make the UI
        super.__init__(name)
        # THIS LIST SHOULD ALWAYS BE SORTED
        self.children = []

    def addChild(self, child):
        self.children.append(child)
        child.parent = self
        p = child.getPriority()
        i = len(self.children) - 1
        # Swap down the new element until self.children is sorted again
        while i > 0 and self.children[i-1].getPriority() > p:
            self.children[i], self.children[i-1] = self.children[i-1], self.children[i]
            i -= 1

    def sortChildren(self):
        def sortFcn(x):
            if isinstance(x, SubjectNode):
                # return the highest priority assignment due in any subtree
                if len(x.children) == 0:
                    return (-1,-1)
                else:
                    return x.children[0].getPriority()
            else:
                # This returns time relative to Jan 1 1582 but we don't care as long as it's comprable to int
                return x.getPriority()

        self.children.sort(key=sortFcn)

    def remove(self, child):
        # Maybe have this implement a binary search for finding what to delete?
        self.children.remove(child)

class EventNode(BasicTreeNode):
    def __init__(self, name, dateDue, dateMade = datetime.date.today(), priority = 0):
        super(name)
        self.dateDue = dateDue
        self.dateMade = dateMade
        self.priority = 0
        # When saving date to file, use date.isoformat()

    def getPriority(self):
        return (self.priority, -1 * self.dateDue.toordinal())

    def changeDate(self, newDate):
        self.dateDue = newDate
        self.parent.sortChildren()
