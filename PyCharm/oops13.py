# -------Diamond shape problem in multiple inheritance-----------------
# refer to screenshot
# multiple inheritance causes confusion, hence try to go for single inheritance and multilevel inher.
#java does not allow multiple inher. PYTHON & C++ allow multiple inher
class A:
    def met(self):
        print("this is a method from class A")


class B(A):
    def met(self):
        print("this is a method from class B")


class C(A):
    def met(self):
        print("this is a method from class C")


class D(C, B):
    def met(self):
        print("this is a method from class D")

a= A()
b=B()
c= C()
d=D()

d.met()