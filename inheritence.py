
class parent:
    def __init__(self, value):
        self.value = value

    def apple(self):
        print('parent.apple', 'self.value')




c = parent(1)
print(c.value)
c.value = 10
print(c.value)






































