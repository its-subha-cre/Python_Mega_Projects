# def l(*le):
#     print(le[1])
# l1=[1,2,3]
# l(*l1)
class p:
    def show(self):
        print("disco")
class u(p):
    def show(self):
        print("how",end=" ")
        super().show()
uo=u()
uo.show()