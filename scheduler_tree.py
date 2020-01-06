from tree_nodes import SubjectNode, EventNode
from constants import Constants

import datetime
import json


class SchedulerTree:
    """
    Holds the tree that contains all the various events and subjects of Scheduler.
    """
    def __init__(self):
        self._total_objs = 1
        self._root = SubjectNode('Root', 1)  # the root node cannot be destroyed

    def delete_node(self, node):
        """
        Delete the given node and return if successful. Will return false
        if the given node is root as root cannot be destroyed.
        """
        parent = node.get_parent()
        if parent:
            self._total_objs -= 1
            parent.remove(node)
            return True
        return False

    def add_node(self, parent, node):
        """
        Add node to the tree given a parent and a node.
        """
        parent.add_child(node)

    def get_root(self):
        return self._root

    def create_node(self, node_type, name, date_due=None, priority=0):
        """
        Creates a node given the type of node, the name of the node,
        the date it is due, and the priority. A node type of 0 is a
        SubjectNode and 1 is an EventNode.
        """
        self._total_objs += 1
        if node_type == 1:
            # add error handling for when date_due isn't included for an eventnode
            node = EventNode(name=name, id=self._total_objs, date_due=date_due, priority=0)
        else:
            node = SubjectNode(name=name, id=self._total_objs, priority=priority)
        return node

    def create_datetime(self, year, month, day):
        return datetime.date(year, month, day)

    def print_tree(self, node='root', level=0):
        """
        A debugging method that prints out a given subtree to the console.
        """
        if node is 'root':
            node = self._root
        if isinstance(node, EventNode):
            print('\t' * level + str(node))
            return
        print('\t' * level + str(node))
        for child in node.get_children():
            self.print_tree(child, level + 1)

    def _del_parents(self, node='root'):
        """
        Deletes the parent instance variable to prevent circular
        hold when converting the tree to json.
        """
        if node is 'root':
            node = self._root
        if isinstance(node, EventNode):
            del node.__dict__['_parent']
            return
        del node.__dict__['_parent']
        for child in node.get_children():
            self._del_parents(child)

    def to_json(self):
        """
        Write the contents of the scheduler tree to a json file.
        """
        self._del_parents()
        with open(Constants.SCHEDULER_TREE_JSON_FILE_PATH, 'w') as w_fp:
            json.dump(self._root, w_fp, indent=4)

    def from_json(self):
        """
        Read the contents of the scheduler tree from a json file.
        """
        with open(Constants.SCHEDULER_TREE_JSON_FILE_PATH, 'r') as r_fp:
            self._root = self._from_dict(json.load(r_fp))

    def _from_dict(self, _dict, parent=None):
        """
        Recursively reconstruct from json file to tree structure.
        SubjectNodes have node_type of 0 while EventNodes have node_type of 1
        """
        if _dict['_node_type'] == 0:
            root = SubjectNode(_dict['_name'], _dict['_id'], _dict['_priority'], parent, _dict['_children'])
        else:
            root = EventNode(_dict['_name'], _dict['_id'], _dict['_date_due'], _dict['_priority'], parent, _dict['_date_made'])
        if parent:
            root.set_parent(parent)
        if isinstance(root, SubjectNode):
            root.set_children([self._from_dict(child, root) for child in root.get_children()])
        return root


if __name__ == '__main__':
    tree = SchedulerTree()

    # create nodes
    chem = tree.create_node(0, 'chem')
    bio = tree.create_node(0, 'bio')
    hw = tree.create_node(1, 'bio hw', tree.create_datetime(2020, 7, 1))

    # ad the nodes to the tree under their respective parents
    tree.add_node(tree.get_root(), chem)
    tree.add_node(tree.get_root(), bio)
    tree.add_node(bio, hw)

    # print the tree
    tree.print_tree()

    # convert the tree to json
    tree.to_json()

    # get the tree back from json
    tree.from_json()

    # print the tree
    tree.print_tree()

