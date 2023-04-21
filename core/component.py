class Component:
    def __init__(self):
        self.parent = None
        self.children = []

    def __str__(self):
        return self.__class__.__name__

    def event_loop(self, events):
        ...  # События и любые действия с клавишами

    def update(self):
        ...

    def draw(self, surface):
        raise Exception(f"{self.__class__.__name__}: All components need to implement draw() function")

    def event_sys(self, events):
        for element in self.children:
            element.event_loop(events)
            element.event_sys(events)

    def update_sys(self):
        for element in self.children:
            element.update()
            element.update_sys()
    def draw_sys(self, surface):  # системная отрисовка добавленного интерфейса
        for element in self.children:
            element.draw(surface)
            element.draw_sys(surface)

    def add_child(self, comp):
        comp.parent = self
        self.children.append(comp)
        return len(self.children) - 1  # айди добавленного элемента

    def remove_child(self, index):
        if index >= len(self.children):
            return
        self.children[index].parent = None
        self.children.pop(index)
