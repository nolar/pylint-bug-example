from ..aspects.sizes import MixinA, MixinB


class Base(object):
    pass


class ClassA(MixinA, Base):
    pass


class ClassB(MixinB, ClassA):
    pass
