class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел



class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        val = self.end.data
        self.end = self.end.pref
        return val

    def push(self, val):
        #print(val)
        new_node = Node(val)
        if self.end != None:
            new_node.pref = self.end
            self.end = new_node
        else:
            self.end = new_node

    def print(self):
        tmp_node = self.end
        values = []
        strg = ""
        while tmp_node != None:
            values.append(tmp_node.data)
            tmp_node = tmp_node.pref
        print(values[::-1])

        pass


