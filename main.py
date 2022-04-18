import pytesseract

import pyautogui

import time

from PIL import Image as ImagePil

import cv2

import pyscreeze

import threading

import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import re

from tkinter import *
from tkinter import Frame as Frametk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox 
from tkinter import Button as ButtonTK 
from tkinter.filedialog import askopenfilename
import glob, os, os.path
from tkinter.ttk import Progressbar
from collections import OrderedDict

from pynput.mouse import Button, Controller
from pynput import keyboard
from pynput.keyboard import  Controller as ControllerKey
from pynput.keyboard import Key as Keyboard
from pynput.keyboard import Listener

import pydirectinput

import ctypes

class Frame:
    def __init__(self) -> None:
       self.khongthaotac = 0
       self.threads = []
       self.kiemtradis = 0
    def GUI(self):
        window = Tk()

        window.title("AUTO Frame")

        window.geometry('700x500')

        window.grid_rowconfigure(0, minsize=20, weight=1)

        lbl = Label(window, text="DESIGN BY DEVELOPER TÀI NGUYỄN", font=("Arial Bold", 20), width=55, pady=10, bg="black" , fg="white",borderwidth=2, relief="raised")

        lh = Label(window, text="NHẬN CODE TOOL & THIẾT KẾ WEBSITE THEO YÊU CẦU - ZALO/SDT 0387865006", font=("Arial Bold", 12), width=93,pady=1 , fg="red",borderwidth=2, relief="raised")

        lbl.pack(fill=X)

        lh.pack(fill=X)

        fame1 = Frametk(window)

        fame1.pack(side=TOP,fill=X,pady=20,padx=20)

        lbl1 = Label(fame1, text= 'Số ô auto :', font=("Time New Roman", 14))

        lbl1.grid(column=0,row=0,padx=5,pady=5,sticky='w')

        lbl2 = Spinbox(fame1,from_=6, to=8,width=10)

        lbl2.grid(column=0,row=1,padx=5,pady=5,sticky='w')

        lbl3 = Label(fame1, text= 'Hạt giống cần trồng :', font=("Time New Roman", 14))

        lbl3.grid(column=0,row=2,padx=5,pady=5,sticky='w')

        lb = Listbox(fame1,activestyle="none",height=10,width=30)
        
        lb.grid(column=0,row=3,padx=5,pady=5,sticky='w')
        lb.insert(0, ' Khoai tây')
        lb.insert(1, ' Cà rốt')
        lb.insert(2, ' Hành')
        lb.insert(3, ' Lúa mì')
        lb.insert(4, ' Hoa hồng')
        lb.insert(5, ' Lavender')  
        lb.insert(6, ' Hướng dương')  
        lb.insert(7, ' Tulip')            

        def START():
            soluong = lbl2.get()
            
            threadmain = threading.Thread(target=self.main,args=(soluong))
            threadmain.start()
            threading.Thread(target=stop, args=()).start()
            self.threads.append(threadmain)
        def stop():
            def on_press(key):
                if str(key) == "Key.esc":
                    thread_id = self.threads[0].native_id
                    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                        ctypes.py_object(SystemExit))
                    if res > 1:
                        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
                    return False
            with keyboard.Listener(on_press=on_press) as listend:
                listend.join()
       
        ButtonTK(fame1,cursor='hand2',text='Bắt đầu',command=START).grid(column=0,row=4,padx=5,pady=5,sticky='w')

        window.mainloop()


    def main(self,soluong):
        def suaanh(img):
            im = ImagePil.open(img + ".png")
            im = im.convert("P")
            im2 = ImagePil.new("P",im.size,0)

            im = im.convert("P")

            temp = {}

            for x in range(im.size[1]):
                for y in range(im.size[0]):
                    pix = im.getpixel((y,x))
                    temp[pix] = pix
                    if pix > 180: # Đây là các màu được lấy_
                        im2.putpixel((y,x),255)

            im2.save(img + ".gif")
        def replace_chars(text):
            """
            Replaces all characters instead of numbers from 'text'.
            
            :param text: Text string to be filtered
            :return: Resulting number
            """
            list_of_numbers = re.findall(r'\d+', text)
            result_number = ''.join(list_of_numbers)
            return result_number
        def main_test():
            pyautogui.screenshot('screen.png')
            
            timeout = 0
            error = 0

            self.khongthaotac = 0
            
            for a in range(0,int(soluong)): 
                error = 0
                timeout = 0
                while error == 0:
                    IMG_PATH = "screen.png"
                    img = cv2.imread(IMG_PATH)
                    lm_crop2 = img[listtoadoy[a]:listtoadoy[a] + 70,listtoadox[a]:listtoadox[a] + 67 :]
                    crop_lm2 = "tien" + str(a + 1) + ".png"
                    cv2.imwrite(crop_lm2, lm_crop2) 
                    kiemtralogin = pyscreeze.locate(r'nuoc.png',"tien" + str(a + 1) + ".png", confidence=.65)
                    kiemtralogin2 = pyscreeze.locate(r'thuhoach.png',"tien" + str(a + 1) + ".png", confidence=.65)
                    if kiemtralogin == None and kiemtralogin2 == None:
                        lm_crop2 = img[listtoadoy2[a]:listtoadoy2[a] + 55,listtoadox2[a]:listtoadox2[a] + 105 :]
                        crop_lm2 = "dh" + str(a + 1) + ".png"
                        cv2.imwrite(crop_lm2, lm_crop2) 
                        kiemtradh = pyscreeze.locate(r'dongho.png',"dh" + str(a + 1) + ".png", confidence=.8)       
                        if kiemtradh == None:                
                            pyautogui.screenshot('screen.png')
                        else:
                            khongthaotac = 1
                            error = 1
                            
                    else:
                        error = 1
                    timeout += 1
                    time.sleep(1)
                    if timeout == 6:
                        error = 1
        def getsoluong():
            IMG_PATH = "Untitled.png"
            img = cv2.imread(IMG_PATH)
            lm_crop2 = img[348:375,790:815 :]
            crop_lm2 = "soluong.png"
            cv2.imwrite(crop_lm2, lm_crop2)  
        listtoadox = [1040,1040,1040,1130,1130,1130,1245,1245,1245]
        listtoadoy = [445,358,280,280,358,445,445,359,280]
        listtoadox2 = [1017,1017,1017,1115,1115,1115,1228,1228,1228]
        listtoadoy2 = [455,370,290,290,370,455,455,370,290]
        listhanhdong = []
        listdichuyen = ['d','w','w','d','s','s','d','w','w']
        listitemx = [1206,1510,1201,1519,1201,1519,1202,1510]
        listitemy = [405,410,533,533,662,662,786,786]
        listhatgiong = [' Khoai tây',' Cà rốt',' Hành',' Lúa mì',' Hoa hồng',' Lavender',' Hướng dương',' Tulip'] 
        
        def xulyanh():
            for a in range(0,int(soluong)):
                kiemtranc = pyscreeze.locate(r'nuoc.png','tien' + str(a + 1) + '.png', confidence=.65)
                if kiemtranc != None:
                    listhanhdong.append('tưới nước')
                kiemtrathu = pyscreeze.locate(r'thuhoach.png','tien' + str(a + 1) + '.png', confidence=.65)
                if kiemtrathu != None:
                    listhanhdong.append('Thu hoạch')
                if kiemtranc == None and kiemtrathu == None:
                    kiemtradh = pyscreeze.locate(r'dongho.png','dh' + str(a + 1) + '.png', confidence=.65)
                    if kiemtradh != None:
                        listhanhdong.append('Không có thao tác')
                    else:
                        listhanhdong.append('Trồng cây')
            if listhanhdong.count('Không có thao tác') == int(soluong):
                self.khongthaotac = 1
        time.sleep(5)

        with open('data/listacc.txt') as file:
            data = file.read()
        data = data.splitlines()

        mouse = Controller()

        Key = ControllerKey()
        def dichuyen(huong):
            for a in range(2):
                Key.press(huong)
                time.sleep(0.5)
                Key.release(huong)
            time.sleep(1)
        def disconnect():
                pyautogui.screenshot('disconnect.png')
                kiemtradh = pyscreeze.locate(r'disconnect2.png','disconnect.png', confidence=.65)
                if kiemtradh != None:
                    pyautogui.click(x=kiemtradh[0],y=kiemtradh[1])
        def saipass():
            Pass = "dung"
            pyautogui.screenshot('saipass.png')
            ktpass = pyscreeze.locate('erroruser.png','saipass.png',confidence=.65)
            if ktpass != None:
                pyautogui.click(x=1333,y=363)
                Pass = "sai"
            return Pass
        while True:
            for a in data:
                user = a.split('|')[0]
                passw = a.split('|')[1]
                thuhoachitem = 0
                # bắt đầu đăng nhập
                self.kiemtradis = 0
                time.sleep(3)
                disconnect()
                pydirectinput.click(1271,464)
                mouse.press(Button.left)
                mouse.release(Button.left)
                time.sleep(1)
                for i in range(0,30):
                    Key.press(Keyboard.backspace)
                time.sleep(1)
                Key.type(user)
                pydirectinput.click(1260,604)
                time.sleep(1)
                mouse.press(Button.left)
                mouse.release(Button.left)
                time.sleep(1)
                for i in range(0,30):
                    Key.press(Keyboard.backspace)
                time.sleep(1)
                Key.type(passw)
                pydirectinput.click(1740,1010)
                mouse.press(Button.left)
                mouse.release(Button.left)
                time.sleep(3)
                pydirectinput.click(1740,1010)
                mouse.press(Button.left)
                mouse.release(Button.left)
                self.kiemtradis = 1
                time.sleep(3)
                ktp = saipass()
                if ktp == 'dung':
                    time.sleep(8)
                    # vào đăng nhập
                    main_test()   
                    xulyanh()
                    if self.khongthaotac == 0:
                        dichuyen('w')
                        time.sleep(1)
                        mouse.press(Button.right)
                        mouse.release(Button.right)
                        time.sleep(3)
                        pydirectinput.click(863,331)
                        mouse.press(Button.left)
                        mouse.release(Button.left)     
                        time.sleep(2)      
                        pyautogui.screenshot('Untitled.png')
                        ktban =  pyscreeze.locate('maxitem.png','Untitled.png',confidence=.65)
                        if ktban != None:
                            pydirectinput.click(967,710)
                            mouse.press(Button.left)
                            mouse.release(Button.left)  
                            time.sleep(1)  
                            pydirectinput.click(1212,732)
                            mouse.press(Button.left)
                            mouse.release(Button.left)   
                            time.sleep(2) 
                        pydirectinput.click(356,431)
                        mouse.press(Button.left)
                        mouse.release(Button.left)     
                        time.sleep(2)      
                        pyautogui.screenshot('Untitled.png')
                        ktban =  pyscreeze.locate('maxitem.png','Untitled.png',confidence=.65)
                        if ktban != None:
                            pydirectinput.click(967,710)
                            mouse.press(Button.left)
                            mouse.release(Button.left)  
                            time.sleep(1)  
                            pydirectinput.click(1212,732)
                            mouse.press(Button.left)
                            mouse.release(Button.left)   
                            time.sleep(2) 
                        pyautogui.screenshot('Untitled.png')
                        getsoluong()
                        suaanh('soluong')
                        pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract'
                        text1 = pytesseract.image_to_string(r"soluong.gif",config='--psm 10 --oem 0 -c tessedit_char_whitelist=0123456789',lang='vie')
                        hatgiong = listhatgiong.index(' Hành')
                        if replace_chars(text1) == '':
                            text1 = '0'
                        if int(replace_chars(text1)) <= int(soluong):
                            for a in range(int(soluong) - int(replace_chars(text1)) + 1):
                                pydirectinput.click(listitemx[hatgiong],listitemy[hatgiong])
                                mouse.press(Button.left)
                                mouse.release(Button.left)     
                                time.sleep(2) 
                                pydirectinput.click(1213,731)
                                mouse.press(Button.left)
                                mouse.release(Button.left)  
                                time.sleep(2)
                        pydirectinput.click(1683,148)
                        mouse.press(Button.left)
                        mouse.release(Button.left)     
                        time.sleep(1)
                        dichuyen('s')
                        for a in range(int(soluong)):
                            print(listdichuyen[a])
                            if listhanhdong[a] == 'tưới nước':
                                dichuyen(listdichuyen[a])
                                Key.type('4')
                                time.sleep(1)
                                mouse.press(Button.left)
                                mouse.release(Button.left)
                                time.sleep(3)
                            elif listhanhdong[a] == 'Thu hoạch':
                                dichuyen(listdichuyen[a])
                                Key.type('4')
                                time.sleep(1)
                                mouse.press(Button.left)
                                mouse.release(Button.left)
                                thuhoachitem = 1
                                time.sleep(3)
                                Key.type('5')
                                time.sleep(1)
                                mouse.press(Button.left)
                                mouse.release(Button.left)
                                time.sleep(3)
                                Key.type('4')
                                time.sleep(1)
                                mouse.press(Button.left)
                                mouse.release(Button.left)
                                time.sleep(3)
                            elif listhanhdong[a] == 'Trồng cây':
                                dichuyen(listdichuyen[a])
                                Key.type('2')
                                time.sleep(1)
                                mouse.press(Button.left)
                                mouse.release(Button.left)
                                time.sleep(3)
                                Key.type('5')
                                time.sleep(1)
                                mouse.press(Button.left)
                                mouse.release(Button.left)
                                time.sleep(3)
                                Key.type('4')
                                time.sleep(1)
                                mouse.press(Button.left)
                                mouse.release(Button.left)
                                time.sleep(3)
                            else:
                                dichuyen(listdichuyen[a])
                        if thuhoachitem == 1:
                            Key.type('p')
                            time.sleep(3)
                            pydirectinput.click(1352,739)
                            mouse.press(Button.left)
                            mouse.release(Button.left)
                            time.sleep(2)
                            pydirectinput.click(752,756)
                            mouse.press(Button.left)
                            mouse.release(Button.left)
                            time.sleep(8)                 
                            pydirectinput.click(1740,1010)
                            mouse.press(Button.left)
                            mouse.release(Button.left)
                            time.sleep(3)
                            pydirectinput.click(1740,1010)
                            mouse.press(Button.left)
                            mouse.release(Button.left)
                            time.sleep(8)
                            dichuyen('w')
                            time.sleep(1)
                            mouse.press(Button.right)
                            mouse.release(Button.right)
                            time.sleep(4)
                            pydirectinput.click(866,337)
                            mouse.press(Button.left)
                            mouse.release(Button.left) 
                            time.sleep(2)   
                            pydirectinput.click(967,710)
                            mouse.press(Button.left)
                            mouse.release(Button.left)  
                            time.sleep(1)  
                            pydirectinput.click(1212,732)
                            mouse.press(Button.left)
                            mouse.release(Button.left)   
                            time.sleep(2)  
                            pydirectinput.click(1683,148)
                            mouse.press(Button.left)
                            mouse.release(Button.left)     
                            time.sleep(1) 
                    else:
                        pass
                    # logout
                    Key.type('p')
                    time.sleep(3)
                    pydirectinput.click(1352,739)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    time.sleep(2)
                    pydirectinput.click(752,756)
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    time.sleep(8)   
                    listhanhdong = []     
                else:
                    pass                                    
Frame().GUI()