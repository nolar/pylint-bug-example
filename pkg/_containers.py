def MixinFactory(cls):
    mixin_name = '{}Mixin'.format(cls.__name__)
    mixin_bases = (object,)
    mixin_attrs = {}
    mixin = type(mixin_name, mixin_bases, mixin_attrs)
    return mixin
