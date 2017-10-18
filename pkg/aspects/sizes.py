from .._containers import MixinFactory


class MixinA(MixinFactory(int)):
    pass


class MixinB(MixinFactory(str)):
    pass
