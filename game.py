#!/usr/bin/python3


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType


import sys
from os import path
import random ,  os  ,  time  , sqlite3


MAIN, _ = loadUiType(path.join(path.dirname(__file__), "unt.ui"))

# icons
stone = "icons/stone.png"
paper = "icons/paper.png"
scissors = "icons/scissors.png"

# colors icon
green = "icons/green.jpg"
red = "icons/red.jpg"
yellow = "icons/yellow.jpg"

# numbers icons
zero = "icons/0.png"

N1 = "icons/n1.png"
N2 = "icons/n2.png"
N3 = "icons/n3.png"

n1 = "icons/n-1.png"
n2 = "icons/n-2.png"
n3 = "icons/n-3.png"


data = [stone , paper , scissors , paper , stone , scissors ]



class MainApp(QMainWindow , MAIN):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_buttons()
        self.open_data_base()



    def handel_buttons(self):
        self.B_stone.clicked.connect(self.handel_play_stone)
        self.B_paper.clicked.connect(self.handel_play_paper)
        self.B_sciss.clicked.connect(self.handel_play_sciss)
        self.next.clicked.connect(self.hande_next)


    
    def robot_play(self):
        global r_choice
        r_choice = random.choice(data)
        self.r_bot.setPixmap(QPixmap(r_choice))
        self.r_bot.setScaledContents(True)
        



    def handel_play_stone(self):
        self.robot_play()
        self.r_you.setPixmap(QPixmap(stone))
        self.r_you.setScaledContents(True)

        self.hande_judge( stone , r_choice)
        self.stackedWidget.setCurrentIndex(1)


    def handel_play_paper(self):
        self.robot_play()
        self.r_you.setPixmap(QPixmap(paper))
        self.r_you.setScaledContents(True)

        self.hande_judge( paper , r_choice)
        self.stackedWidget.setCurrentIndex(1)


    def handel_play_sciss(self):
        self.robot_play()
        self.r_you.setPixmap(QPixmap(scissors))
        self.r_you.setScaledContents(True)

        self.hande_judge( scissors , r_choice)
        self.stackedWidget.setCurrentIndex(1)



    def hande_judge(self , you_choice , bot_choice ):
        global result
        result = 0

        if you_choice == stone and bot_choice == stone:
            self.result_y.setPixmap(QPixmap(yellow))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(yellow))
            self.result_b.setScaledContents(True)
            result = result+0
            self.save_result(0 , 0)
            

        elif you_choice == stone and bot_choice == paper :
            self.result_y.setPixmap(QPixmap(red))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(green))
            self.result_b.setScaledContents(True)
            result = result-1
            self.save_result(0 , -1)


        elif you_choice == stone and bot_choice == scissors :
            self.result_y.setPixmap(QPixmap(green))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(red))
            self.result_b.setScaledContents(True)
            result = result+1
            self.save_result(0 , 1)


        ###########################
        elif you_choice == paper and bot_choice == stone:
            self.result_y.setPixmap(QPixmap(green))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(red))
            self.result_b.setScaledContents(True)
            result = result+1
            self.save_result(0 , 1)

        elif you_choice == paper and bot_choice == paper:
            self.result_y.setPixmap(QPixmap(yellow))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(yellow))
            self.result_b.setScaledContents(True)
            result = result+0
            self.save_result(0 , 0)


        elif you_choice == paper and bot_choice == scissors:
            self.result_y.setPixmap(QPixmap(red))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(green))
            self.result_b.setScaledContents(True)
            result = result-1
            self.save_result(0 , -1)



        ##############################
        elif you_choice == scissors and bot_choice == stone:
            self.result_y.setPixmap(QPixmap(red))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(green))
            self.result_b.setScaledContents(True)
            result = result-1
            self.save_result(0 , -1)
            

        elif you_choice == scissors and bot_choice == paper:
            self.result_y.setPixmap(QPixmap(green))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(red))
            self.result_b.setScaledContents(True)
            result = result+1
            self.save_result(0 , 1)


        elif you_choice == scissors and bot_choice == scissors:
            self.result_y.setPixmap(QPixmap(yellow))
            self.result_y.setScaledContents(True)

            self.result_b.setPixmap(QPixmap(yellow))
            self.result_b.setScaledContents(True)            
    
            self.save_result(0 , 0)

        
    def open_data_base(self):
        db = sqlite3.connect("db/RESULT.db")
        cr = db.cursor()
        cr.execute("create table if not exists results (id int, result int)")
        cr.execute("delete from results where id=0")
        cr.execute("insert into results (id , result ) values(?,?)" , (0 , 0)) 
        db.commit()
        db.close()



    def save_result(self , id , result):
        db = sqlite3.connect("db/RESULT.db")
        cr = db.cursor()
        show = cr.execute("select * from results")  
        for raw in show:
            result = result + raw[1]

        print(result)
        
        cr.execute('''UPDATE results SET result = ? WHERE id = ?''', (result , id))
        db.commit()
        db.close()

        if result == 0:
            self.f_res_y.setPixmap(QPixmap(zero))
            self.f_res_y.setScaledContents(True)

            self.f_res_b.setPixmap(QPixmap(zero))
            self.f_res_b.setScaledContents(True)  


        elif result == -1:
            self.f_res_y.setPixmap(QPixmap(n1))
            self.f_res_y.setScaledContents(True)

            self.f_res_b.setPixmap(QPixmap(N1))
            self.f_res_b.setScaledContents(True) 


        elif result == -2:
            self.f_res_y.setPixmap(QPixmap(n2))
            self.f_res_y.setScaledContents(True)

            self.f_res_b.setPixmap(QPixmap(N2))
            self.f_res_b.setScaledContents(True) 


        elif result == -3:
            self.f_res_y.setPixmap(QPixmap(n3))
            self.f_res_y.setScaledContents(True)

            self.f_res_b.setPixmap(QPixmap(N3))
            self.f_res_b.setScaledContents(True) 


        elif result == 1:
            self.f_res_y.setPixmap(QPixmap(N1))
            self.f_res_y.setScaledContents(True)

            self.f_res_b.setPixmap(QPixmap(n1))
            self.f_res_b.setScaledContents(True) 


        elif result == 2:
            self.f_res_y.setPixmap(QPixmap(N2))
            self.f_res_y.setScaledContents(True)

            self.f_res_b.setPixmap(QPixmap(n2))
            self.f_res_b.setScaledContents(True) 



        elif result == 3:
            self.f_res_y.setPixmap(QPixmap(N3))
            self.f_res_y.setScaledContents(True)

            self.f_res_b.setPixmap(QPixmap(n3))
            self.f_res_b.setScaledContents(True) 







    def hande_next(self):
        self.stackedWidget.setCurrentIndex(0)





def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__== "__main__":
    main()
