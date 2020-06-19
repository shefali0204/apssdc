class one:
    def a(self):
        print("one is executed")
class two(one):
    def a(self):
        print("two is executed")
class three(two):
    def a(self):
        print("three is executed")
class four(three):
    def a(self):
        print("four is executed")
class five(four):
    def a(self):
        #print("five is executed")
        pass
z=five()
z.a()