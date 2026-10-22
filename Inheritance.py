class A :
     def m1(self):
         print("this is a parent class method")

class B (A):
    def m2(self):
        print("this is a child class method")
class C(B):
    def m3(self):
        print("this is a super child class method")

a1=A()
a1.m1()
b1=B()
b1.m1()
b1.m2()
c1=C()
c1.m3()
c1.m1()
c1.m2()

print("=========================================")
class BasePage:
    def open_page(self):
        print("Opening page")

    def login(self):
        print("Login successful")


class HomePage(BasePage):
    def search(self):
        print("Searching product")


class LoginPage(BasePage):
    def enter_username(self):
        print("Entering username")


home = HomePage()

home.open_page()       # inherited from BasePage
home.login()           # inherited from BasePage
home.search()          # HomePage method

login = LoginPage()

login.open_page()      # inherited from BasePage
login.login()          # inherited from BasePage
login.enter_username() # LoginPage methods


