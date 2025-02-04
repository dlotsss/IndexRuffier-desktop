from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
      
from instr import *
 
class FinalWin(QWidget):
    def __init__(self, experiment):
        #окно, в котором проводится опрос
        super().__init__()
        self.experiment = experiment
        self.initUI()
        self.set_appear()
        self.show()

    def results(self):
        if self.experiment.age < 7:
            self.index_rufie = 0
            return 'нет данных для этого возраста' 
        self.index_rufie = (4 * (int(self.experiment.test1) + int(self.experiment.test2) + int(self.experiment.test3)) - 200) / 10
        if self.experiment.age == 7 or self.experiment.age == 8:
            if self.index_rufie >= 21:
                return level1
            elif self.index_rufie < 21 and self.index_rufie >= 17:
                return level2
            elif self.index_rufie < 17 and self.index_rufie >= 12:
                return level3
            elif self.index_rufie < 12 and self.index_rufie >= 6.5:
                return level4
            else:
                return level5
        elif self.experiment.age == 9 or self.experiment.age == 10:
            if self.index_rufie >= 19.5:
                return level1
            elif self.index_rufie < 19.5 and self.index_rufie >= 15.5:
                return level2
            elif self.index_rufie < 15.5 and self.index_rufie >= 10.5:
                return level3
            elif self.index_rufie < 10.5 and self.index_rufie >= 5:
                return level4
            else:
                return level5
        elif self.experiment.age == 11 or self.experiment.age == 12:
            if self.index_rufie >= 18:
                return level1
            elif self.index_rufie < 18 and self.index_rufie >= 14:
                return level2
            elif self.index_rufie < 14 and self.index_rufie >= 9:
                return level3
            elif self.index_rufie < 9 and self.index_rufie >= 3.5:
                return level4
            else:
                return level5
        elif self.experiment.age == 13 or self.experiment.age == 14:
            if self.index_rufie >= 16.5:
                return level1
            elif self.index_rufie < 16.5 and self.index_rufie >= 12.5:
                return level2
            elif self.index_rufie < 12.5 and self.index_rufie >= 7.5:
                return level3
            elif self.index_rufie < 7.5 and self.index_rufie >= 2:
                return level4
            else:
                return level5
        else:
            if self.index_rufie >= 15:
                return level1
            elif self.index_rufie < 15 and self.index_rufie >= 11:
                return level2
            elif self.index_rufie < 11 and self.index_rufie >= 6:
                return level3
            elif self.index_rufie < 6 and self.index_rufie >= 0.5:
                return level4
            else:
                return level5

    
    def initUI(self):
        #создаёт графические элементы
        self.appeal = QLabel(appeal_1 + str(self.experiment.name) + appeal_2)
        self.workh_text = QLabel(txt_workheart + self.results())
        self.index_text = QLabel(txt_index + str(self.index_rufie))
    
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.appeal, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)        
        self.setLayout(self.layout_line)
    
    #устанавливает, как будет выглядеть окно (надпись, размер, место)
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
