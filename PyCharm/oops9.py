#-------------------------multi level inheritance--------------------------------#

# class Dad:
#     basketball = 1
#
# class Son(Dad):
#     dance = 1
#     def isDance(self):
#         return f"yes I dance {self.dance} no of times"
#
# class Grandson(Son):
#     dance = 6
#     # def isDance(self):
#     #     return f"Jackson yeah!!" \
#     #            f"  yes I dance incredibly {self.dance} no of times"
#
# jai = Dad()
# sahil = Son()
# nil = Grandson()
#
# print(nil.isDance())
# print("\n", nil.basketball)

#------------------------Exercise ----------------------------------------#
#3 classes = electonic device, pocket gadget , phone , multi level inheritrance

class Electronic_Device:
    screen = '8 inch'
    battery =100

class PocketGadget(Electronic_Device):
    screen = '6 inch'
    def light(self):
        return f"bright screen light"

class Phone(PocketGadget):
    screen = '5 inch'

    def ring(self):
        print("rings for call")
    def light(self):
        print(f"too much bright screen light")

a = Electronic_Device()
b = PocketGadget()
c = Phone()

print(c.light())