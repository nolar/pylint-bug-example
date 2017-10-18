from pkg.objects import ClassB


class FinalClass(ClassB):

    def __init__(self):
        pass
        self.name = 'x'  # NB: remove/comment it, and the problem disappears.
