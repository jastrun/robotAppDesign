from PyQt5.QtWidgets import QColorDialog

c = QColorDialog.getColor()
print(c.name())