import datetime

# TODO: Methods to add to the nodes:
#  - .toJson
#  - a nice __str__ method (with indentation for subtrees)


class BasicTreeNode(dict):
    def __init__(self, name, id, priority, parent):
        super().__init__()
        self.__dict__ = self
        self._name = name
        self._priority = priority
        self._id = id
        self._parent = parent

    def get_priority(self):
        return self._priority, 0

    def set_priority(self, priority):
        self._priority = priority

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id


class SubjectNode(BasicTreeNode):
    def __init__(self, name, id, priority=0, parent=None, children=None):
        # Add a color property to this class when we make the UI
        super().__init__(name, id, priority, parent)
        self._node_type = 0
        self._children = [] if not children else children     # THIS LIST SHOULD ALWAYS BE SORTED

    def add_child(self, child):
        self._children.append(child)
        child._parent = self
        p = child.get_priority()
        i = len(self._children) - 1
        # Swap down the new element until self.children is sorted again
        while i > 0 and self._children[i-1].get_priority() > p:
            self._children[i], self._children[i - 1] = self._children[i - 1], self._children[i]
            i -= 1

    def sort_children(self):
        def sort_fcn(x):
            if isinstance(x, SubjectNode):
                # return the highest priority assignment due in any subtree
                if len(x._children) == 0:
                    return -1, -1
                else:
                    return x._children[0].get_priority()
            else:
                # This returns time relative to Jan 1 1582 but we don't care as long as it's comparable to int
                return x.get_priority()

        self._children.sort(key=sort_fcn)

    def remove(self, child):
        # maybe have this implement a binary search for finding what to delete?
        self._children.remove(child)

    def get_children(self):
        return self._children

    def set_children(self, children):
        self._children = children

    def __repr__(self):
        return 'node type: SubjectNode' + \
               ', node_name: ' + self._name + \
               ', id: ' + str(self._id)


class EventNode(BasicTreeNode):
    def __init__(self, name, id, date_due, priority=0, parent=None, date_made=str(datetime.date.today())):
        super().__init__(name, id, priority, parent)
        self._node_type = 1
        self._date_due = str(date_due)
        # if date_made is given as a string in isoformat, it is converted to datatime.date object
        self._date_made = str(date_made)
        # when saving date to file, use date.isoformat()

    def get_priority(self):
        return self._priority, -1 * datetime.date.fromisoformat(self._date_due).toordinal()

    def change_due_date(self, new_date):
        self._date_due = str(new_date)
        self._parent.sort_children()

    def get_date_due_obj(self):
        return datetime.date.fromisoformat(self._date_due)

    def __repr__(self):
        return 'node type: EventNode' + \
               ', node_name: ' + self._name + \
               ', id: ' + str(self._id) + \
               ', date_due: ' + str(self._date_due) + \
               ', date_made: ' + str(self._date_made)
