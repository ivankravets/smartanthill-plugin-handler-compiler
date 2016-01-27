# Copyright (C) 2016 OLogN Technologies AG
#
# This source file is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License version 2
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


class Child(object):
    '''
    Intermediate instance to hold a child reference
    '''

    def __init__(self, parent, allowed_type, optional=False, list_item=False):
        '''
        Constructor
        '''
        super(Child, self).__init__()
        self._child_node = None
        self._parent = parent
        self._allowed_type = allowed_type
        self._optional = optional

        if not list_item:
            parent.add_child(self)

    def set(self, child):
        '''
        Sets the child
        There must not be any previous child
        '''
        assert isinstance(child, self._allowed_type)
        assert self._child_node is None
        child.set_parent(self._parent)
        self._child_node = child

    def is_none(self):
        '''
        Returns where there is a child here
        '''
        assert self._optional
        return self._child_node is None

    def is_kind(self, some_kind):
        '''
        Returns where there is a child here
        '''
        return self._allowed_type == some_kind

    def get(self):
        '''
        Returns the current child
        '''
        assert self._optional or self._child_node is not None
        return self._child_node

    def reset(self, child):
        '''
        Replaces existing child
        '''
        temp = self._child_node
        self._child_node = None
        self.set(child)
        return temp

    def clear(self):
        '''
        Replaces existing child
        '''
        temp = self._child_node
        self._child_node = None
        return temp

    def call(self, functor):
        '''
        Walks this child
        '''
        if self._child_node is not None:
            return functor(self)


class ChildList(object):
    '''
    Intermediate instance to hold a child list

    '''

    def __init__(self, parent, allowed_type):
        '''
        Constructor
        '''
        super(ChildList, self).__init__()
        self._child_list = []
        self._parent = parent
        self._allowed_type = allowed_type

        parent.add_child(self)

    def __iter__(self):
        '''
        Easy iteration
        '''
        return self._child_list.__iter__()

    def _make(self, child):
        '''
        Helper method
        '''
        box = Child(self._parent, self._allowed_type, False, True)
        box.set(child)
        return box

    def get_size(self):
        '''
        Returns the child count
        '''
        return len(self._child_list)

    def add(self, child):
        '''
        Adds a child
        '''
        self._child_list.append(self._make(child))

    def add_all(self, childs):
        '''
        Adds all childs in iterable
        '''
        for each in childs:
            self.add(each)

    def at(self, index):
        '''
        Returns a child
        '''
        return self._child_list[index]

    def insert_at(self, index, child):
        '''
        Inserts a child
        '''
        self._child_list.insert(index, self._make(child))

    def remove_at(self, index):
        '''
        Removes a child
        '''
        return self._child_list.pop(index).get()

    def replace_at(self, index, child):
        '''
        Replaces a child
        '''
        assert isinstance(child, self._allowed_type)

        temp = self.remove_at(index)
        self.insert_at(index, child)
        return temp

    def split_at(self, index):
        '''
        Splits this list at index, all items from index on, are returned
        '''
        assert index <= len(self._child_list)
        assert index >= 0

        other = []
        for i in range(index, len(self._child_list)):
            other.append(self._child_list[i].get())
            self._child_list[i] = None

        self._child_list = self._child_list[0:index]
        return other

    def call(self, functor):
        '''
        Walks all childs
        '''
        for each in self._child_list:
            each.call(functor)
