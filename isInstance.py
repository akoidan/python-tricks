class Koko(type):
    def __instancecheck__(self, other):
        print 'hi'
        return True


class EnumInt(int):
    __metaclass__ = Koko

print isinstance('foo', EnumInt) # prints True
