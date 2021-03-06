# -*- coding:utf-8 -*-

from future.utils import with_metaclass

from ..common import SingletonMeta


class DocumentTraceQueue(with_metaclass(SingletonMeta, object)):
    """
    Queue of modification, inserted, deleted document.
    """

    trace_queue = []

    def is_empty(self):
        """
        Is empty trace_queue?

        :return: True or False
        """

        if len(self.trace_queue) > 0:
            return False
        else:
            return True

    def count(self):
        """
        Count of trace_queue

        :return: count
        """
        return len(self.trace_queue)

    def enqueue(self, event, is_index_file):
        """
        Enqueue event to trace_queue

        :param event: insert/update/del event
        :param is_index_file: True or False
        """
        if isinstance(is_index_file, bool):
            self.trace_queue.append((event, is_index_file))
        else:
            raise Exception("is_index_file parameter is bool type.")

    def dequeue(self):
        """
        Dequeue event
        Return the copy of top event in trace_queue

        :return: event
        """
        if self.is_empty():
            return None
        else:
            import copy
            event = copy.deepcopy(self.trace_queue[0])
            self.trace_queue.remove(event)
            return event

    def clear(self):
        """
        Remove all trace_queue
        """
        self.trace_queue = []
