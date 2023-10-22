from PySide2.QtWidgets import *
import sys

from GUI_FactorySettings import *
from main import *

class FactorySettingsWindow(QDialog, Ui_FactorySettingsForm):

    def __init__(self, settingsDict, parent=None): # settingsDict is the dictionary having all factory settings
        super(FactorySettingsWindow, self).__init__(parent)

        self.factSett = Ui_FactorySettingsForm()
        self.factSett.setupUi(self)

        self.factSett.groupBox.setVisible(False)

        self.factSett.buttonFactoryPW.clicked.connect(self.testPW)

        self.factSett.spinExtendedResolution.setValue(settingsDict[0])
        self.factSett.spinReducedResolution.setValue(settingsDict[1])
        self.factSett.spinDefaultRotation.setValue(settingsDict[2])
        self.factSett.spinDisplayFlip.setValue(settingsDict[3])
        self.factSett.spinSaveFlip.setValue(settingsDict[4])

        self.factSett.buttonFactOK.clicked.connect(self.accept)
        self.factSett.buttonFactCancel.clicked.connect(self.reject)

    def testPW(self):
        # if self.factSett.lineFactory.text() == "b10zen@":
        if self.factSett.lineFactory.text() == "zzzz":
            self.factSett.groupBox.setVisible(True)
        else:
            self.factSett.groupBox.setVisible(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = FactorySettingsWindow()
    form.show()
    app.exec_()