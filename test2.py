# g = []
# print(dir(g))

class A:
    def speak(self):
        print("A speaks")


class B(A):
    def speak(self):
        print("B speaks")


class C(A):
    def speak(self):
        print("C speaks")


class D(B, C):
    pass


d = D()
print(d.speak())
