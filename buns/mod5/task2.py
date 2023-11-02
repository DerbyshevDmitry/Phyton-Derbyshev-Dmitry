class Node:
    """
    Вспомогательный класс для узлов списка
    """

    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    count = 0
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди
        self.__counter = 0
    def pop(self):
        """
        возвращаем элемент val из начала списка с удалением из списка
        """
        val = self.start.data
        self.start = self.start.nref
        return val

    def push(self, val):
        new_node = Node(val)
        if self.start == None:
            self.end = new_node
            self.start = new_node
            self.__counter += 1
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node
            self.__counter += 1



    def insert(self, n, val):
        """
        вставить элемент val между элементами с номерами n-1 и n
        """
        tmp_node = self.start

        # TODO : проверить n = 0, проверить n = размер массив
        if n == 0:
            new_node = Node(val)
            new_node.nref = tmp_node
            tmp_node.pref = new_node
            self.__counter += 1
            self.start = new_node
        elif n == self.__counter + 1:
            new_node = Node(val)
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node
            self.__counter += 1

        else:
            for i in range(n - 2):
                tmp_node = tmp_node.nref
            tmp_next = tmp_node.nref
            new_node = Node(val)
            new_node.pref = tmp_node
            new_node.nref = tmp_next
            tmp_node.nref = new_node
            tmp_next.pref = new_node
            self.__counter += 1

    def print(self):
        tmp_node = self.start
        while tmp_node != None:
            print(tmp_node.data, end=" ")
            tmp_node = tmp_node.nref
        print()

