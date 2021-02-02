from abc import ABC, abstractmethod



class TextBox():
    def draw(self):
        print("textbox")


class DropDownList():
       def draw(self):
           print("dropdownlist")

def draw(controls):
    for control in controls:
    control.draw()

ddl = DropDownList()
draw(ddl)
ddl2 = TextBox()
draw(ddl2)

draw([ddl, ddl2])