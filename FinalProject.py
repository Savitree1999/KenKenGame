from tkinter import *
import random
import numpy as np

window = Tk()
window.title(" \\\(^0^)// KenKen Game \\\(^0^)// ")
window.geometry("800x500")
window.option_add("*Font", "impact 12")#กำหนดรูปแบบตัวอักษร
window.configure(bg = "#000000") #กำหนดสีพื้นหลัง


#---------กำหนดตัวแปร---------------------

x00 = IntVar()
x01 = IntVar()
x02 = IntVar()
x03 = IntVar()

x10 = IntVar()
x11 = IntVar()
x12 = IntVar()
x13 = IntVar()

x20 = IntVar()
x21 = IntVar()
x22 = IntVar()
x23 = IntVar()

x30 = IntVar()
x31 = IntVar()
x32 = IntVar()
x33 = IntVar()

#--------------------ฟังก์ชันสุ่มเลข----------------------------
def randN():
    
    X = [[x00,x01,x02,x03],[x10,x11,x12,x13],[x20,x21,x22,x23],[x30,x31,x32,x33]]
    N = np.array([[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]])
    
    # row 0 
    L = [1,2,3,4]
    for i in range(0,4) :
        X[0][i].set(random.choice(L))
        L.remove(X[0][i].get())
        N[0][i] = X[0][i].get()
        
    # row 1 
    for i in range(0,4) :
        L = [1,2,3,4]
        L.remove(X[0][i].get())
        if i != 0 :
            ii=0
            while ii<i :
                if X[0][i].get() != X[1][ii].get() :
                    L.remove(X[1][ii].get())
                    if L ==[] :
                        return(randN())
                ii+=1   
        X[1][i].set(random.choice(L))
        N[1][i] = X[1][i].get()
   
    # row 2 
    for i in range(0,4) :
        L = [1,2,3,4]
        L.remove(X[0][i].get())
        L.remove(X[1][i].get())
        if i != 0 :
            ii=0
            while ii<i :
                if X[0][i].get() != X[2][ii].get() and X[1][i].get() != X[2][ii].get() :
                    L.remove(X[2][ii].get())
                    if L ==[] :
                        return(randN())
                ii+=1   
        X[2][i].set(random.choice(L))
        N[2][i] = X[2][i].get()
    
    # row 3    
    for i in range(0,4) :
        L = [1,2,3,4]
        L.remove(X[0][i].get())
        L.remove(X[1][i].get())
        L.remove(X[2][i].get())
        if i != 0 :
            ii=0
            while ii<i :
                if X[0][i].get() != X[3][ii].get() and X[1][i].get() != X[3][ii].get() and X[2][i].get() != X[3][ii].get() :
                    L.remove(X[3][ii].get())
                    if L ==[] :
                        return(randN())
                ii+=1   
        X[3][i].set(random.choice(L))
        N[3][i] = X[3][i].get()
        
    return(N) 
#---------------------------randN() end----------------------------
def free():
    ZZ  = 1+1
#--------------------Random : FormA---------------------------------------

# ข้อความแสดงเครื่องหมายที่สุ่มได้
txt1 = ""
txt2 = ""
txt3 = ""
txt5 = ""
txt6 = ""
txt7 = ""
r = IntVar()

def FormA() :
    N = randN()
    #แบ่งช่องตารางเป็น 7 กรุ๊ป a1 -a7
    #a1
    r.set(random.randint(1,2))
    if r.get() == 1 :
        # +
        a1 = N[0][0] + N[0][1] + N[1][1]
        txt1 = '+' 
        
    else :
        a1 = N[0][0] * N[0][1] * N[1][1]  
        txt1 = 'x'
        
    #a2
    r.set(random.randint(1,2))
    if r.get() == 1 :
        # +
        a2 = N[0][2] + N[0][3] + N[1][2]
        txt2 = '+'
        
    else :
        # *
        a2 = N[0][2] * N[0][3] * N[1][2] 
        txt2 = 'x'
        
    #a3
    r.set(random.randint(1,2))
    if r.get() == 1 :
        # +
        a3 = N[2][1] + N[3][0] + N[3][1]
        txt3 = '+'
    else :
        # *
        a3 = N[2][1] * N[3][0] * N[3][1] 
        txt3 = 'x'
        
    #a4 
    a4 = N[1][3]
    
    #a5,6,7
    if (N[1][0]%N[2][0]==0 or N[2][0]%N[1][0]==0) or (N[2][2]%N[2][3]==0 or N[2][3]%N[2][2]==0) or (N[3][2]%N[3][3]==0 or N[3][3]%N[3][2]==0) :
        if N[1][0]%N[2][0]==0 or N[2][0]%N[1][0]==0 :
            if N[1][0]%N[2][0]==0 :
                a5 = int(N[1][0]/N[2][0])
            else :
                a5 = int(N[2][0]/N[1][0])
                
            a6 = abs(N[2][2]-N[2][3])
            a7 = abs(N[3][2]-N[3][3])
            txt5 ='/'
            txt6 ='-'
            txt7 ='-'
        elif N[2][2]%N[2][3]==0 or N[2][3]%N[2][2]==0 :
            a5 = abs(N[1][0]-N[2][0])
            if N[2][2]%N[2][3]==0 :
                a6 = int(N[2][2]/N[2][3])
            else:
                a6 = int(N[2][3]/N[2][2])
            
            a7 = abs(N[3][2]-N[3][3])
            txt5 ='-'
            txt6 ='/'
            txt7 ='-'
            
        elif N[3][2]%N[3][3]==0 or N[3][3]%N[3][2] == 0 :
            a5 = abs(N[1][0]-N[2][0])
            a6 = abs(N[2][2]-N[2][3])
            if N[3][2]%N[3][3]==0 :
                a7 = int(N[3][2]/N[3][3])
            else :
                a7 = int(N[3][3]/N[3][2])
            txt5 ='-'
            txt6 ='-'
            txt7 ='/'
    else :
        a5 = abs(N[1][0]-N[2][0])
        a6 = abs(N[2][2]-N[2][3])
        a7 = abs(N[3][2]-N[3][3])
        txt5 ='-'
        txt6 ='-'
        txt7 ='-'
    # กำหนดสีช่องของแต่ละกรุ๊ป
    TxT[0][0].configure(bg = "red")
    TxT[0][1].configure(bg = "red")
    TxT[1][1].configure(bg = "red")
    
    TxT[0][2].configure(bg = "lime")
    TxT[0][3].configure(bg = "lime")
    TxT[1][2].configure(bg = "lime")
        
    TxT[1][0].configure(bg = "violet")
    TxT[2][0].configure(bg = "violet")
        
    TxT[3][0].configure(bg = "sky blue")
    TxT[2][1].configure(bg = "sky blue")
    TxT[3][1].configure(bg = "sky blue")
        
    TxT[1][3].configure(bg = "gold")
        
    TxT[2][2].configure(bg = "#FF6E05")
    TxT[2][3].configure(bg = "#FF6E05")
        
    TxT[3][2].configure(bg = "pink")
    TxT[3][3].configure(bg = "pink")
    
    #สร้างกล่อง แสดงเครื่องหมายและคำตอบของแต่ละกรุ๊ป
    btn1 = Button(window, text = txt1 +" "+ str(a1) , bg = "red",command = free , width = 5)
    btn1.grid(column = 1, row = 10, padx =2)

    btn2 = Button(window, text = txt2 +" "+ str(a2) , bg = "lime",command = free , width = 5)
    btn2.grid(column = 2, row = 10, padx =2)
        
    btn3 = Button(window, text = txt3 +" "+ str(a3) , bg = "sky blue",command = free , width = 5)
    btn3.grid(column = 3, row = 10, padx =2)
        
    btn4 = Button(window, text = str(a4) , bg = "gold",command = free , width = 5)
    btn4.grid(column = 4, row = 10, padx =2)
        
    btn5 = Button(window, text = txt5 +" "+ str(a5) , bg = "violet",command = free , width = 5)
    btn5.grid(column = 5, row = 10, padx =2)
        
    btn6 = Button(window, text = txt6 +" "+ str(a6) , bg = "#FF6E05",command = free , width = 5)
    btn6.grid(column = 6, row = 10, padx =2)
        
    btn7 = Button(window, text = txt7 +" "+ str(a7) , bg = "pink",command = free , width = 5)
    btn7.grid(column = 7, row = 10, padx =2)
    return(N)
   
#--------------------Random : FormB---------------------------------------
def FormB() :
    N = randN()
    #แบ่งช่องตารางเป็น 7 กรุ๊ป b1 -b7
    #b1
    r.set(random.randint(1,2))
    if r.get() == 1 :
        b1 = N[0][1] + N[1][1] + N[1][2]
        txt1 = "+"
        
    else :
        b1 = N[0][1] * N[1][1] * N[1][2]  
        txt1 = "x"
    #b2
    r.set(random.randint(1,2))
    if r.get() == 1 :
        b2 = N[1][0] + N[2][0] + N[2][1]
        txt2 = "+"
        
    else :
        b2 = N[1][0] * N[2][0] * N[2][1] 
        txt2 = "x"
   
    #b3
    r.set(random.randint(1,2))
    if r.get() == 1 :
        b3 = N[1][3] + N[2][2] + N[2][3]
        txt3 = "+"
        
    else :
        b3 = N[1][3] * N[2][2] * N[2][3] 
        txt3 = "x"
     #b4
    b4 = N[0][0]
    
    #b5,6,7
    if (N[0][2]%N[0][3]==0 or N[0][3]%N[0][2]==0) or (N[3][0]%N[3][1]==0 or N[3][1]%N[3][0]==0) or (N[3][2]%N[3][3]==0 or N[3][3]%N[3][2]==0) :
        if N[0][2]%N[0][3]==0 or N[0][3]%N[0][2]==0 :
            if N[0][2]%N[0][3]==0 :
                b5 = int(N[0][2]/N[0][3])
            else :
                b5 = int(N[0][3]/N[0][2])
                
            b6 = abs(N[3][0]-N[3][1])
            b7 = abs(N[3][2]-N[3][3])
            
            txt5 = "/"
            txt6 = "-"
            txt7 = "-"
            
        elif N[3][0]%N[3][1]==0 or N[3][1]%N[3][0]==0 :
            b5 = abs(N[0][3]-N[0][2])
            if N[3][0]%N[3][1]==0 :
                b6 = int(N[3][0]/N[3][1])
            else:
                b6 = int(N[3][1]/N[3][0])
            
            b7 = abs(N[3][2]-N[3][3])
            
            txt5 = "-"
            txt6 = "/"
            txt7 = "-"
            
        elif N[3][2]%N[3][3]==0 or N[3][3]%N[3][2]==0 :
            b5 = abs(N[0][3]-N[0][2])
            b6 = abs(N[3][0]-N[3][1])
            if N[3][2]%N[3][3]==0 :
                b7 = int(N[3][2]/N[3][3])
            else :
                b7 = int(N[3][3]/N[3][2])
            
            txt5 = "-"
            txt6 = "-"
            txt7 = "-"
    else :
        b5 = abs(N[0][3]-N[0][2])
        b6 = abs(N[3][0]+N[3][1])
        b7 = abs(N[3][2]-N[3][3])
        txt5 = "-"
        txt6 = "-"
        txt7 = "-"
    
    # กำหนดสีช่องของแต่ละกรุ๊ป
    TxT[0][1].configure(bg = "sky blue")
    TxT[1][1].configure(bg = "sky blue")
    TxT[1][2].configure(bg = "sky blue")

    TxT[1][0].configure(bg = "violet")
    TxT[2][0].configure(bg = "violet")
    TxT[2][1].configure(bg = "violet")
        
    TxT[1][3].configure(bg = "pink")
    TxT[2][2].configure(bg = "pink")
    TxT[2][3].configure(bg = "pink")
        
    TxT[0][0].configure(bg = "lime")
        
    TxT[0][2].configure(bg = "#FF6E05")
    TxT[0][3].configure(bg = "#FF6E05")
       
    TxT[3][0].configure(bg = "red")
    TxT[3][1].configure(bg = "red")
        
    TxT[3][2].configure(bg = "gold")
    TxT[3][3].configure(bg = "gold")
    
    #สร้างกล่อง แสดงเครื่องหมายและคำตอบของแต่ละกรุ๊ป    
    btn1 = Button(window, text = txt1 +" "+ str(b1) , bg = "sky blue",command = free , width = 5)
    btn1.grid(column = 1, row = 10, padx =2)

    btn2 = Button(window, text = txt2 +" "+ str(b2) , bg = "violet",command = free , width = 5)
    btn2.grid(column = 2, row = 10, padx =2)
        
    btn3 = Button(window, text = txt3 +" "+ str(b3) , bg = "pink",command = free , width = 5)
    btn3.grid(column = 3, row = 10, padx =2)
        
    btn4 = Button(window, text = str(b4) , bg = "lime",command = free , width = 5)
    btn4.grid(column = 4, row = 10, padx =2)
        
    btn5 = Button(window, text = txt5 +" "+ str(b5) , bg = "#FF6E05",command = free , width = 5)
    btn5.grid(column = 5, row = 10, padx =2)
        
    btn6 = Button(window, text = txt6 +" "+ str(b6) , bg = "red",command = free , width = 5)
    btn6.grid(column = 6, row = 10, padx =2)
        
    btn7 = Button(window, text = txt7 +" "+ str(b7) , bg = "gold",command = free , width = 5)
    btn7.grid(column = 7, row = 10, padx =2)
    return(N)

#--------------------Random : FormC---------------------------------------

    
def FormC() :
    N = randN()
    #แบ่งช่องตารางเป็น 7 กรุ๊ป c1 -c7
    #c1
    r.set(random.randint(1,2))
    if r.get() == 1 :
        c1 = N[0][0] + N[0][1] + N[1][0]
        txt1 = "+"
        
    else :
        c1 = N[0][0] * N[0][1] * N[1][0] 
        txt1 = "x"
    
    #c2
    r.set(random.randint(1,2))
    if r.get() == 1 :
        c2 = N[2][1] + N[2][2] + N[3][1]
        txt2 = "+"
        
    else :
        c2 = N[2][1] * N[2][2] * N[3][1] 
        txt2 = "x"
    
    #c3
    r.set(random.randint(1,2))
    if r.get() == 1 :
        c3 = N[2][3] + N[3][2] + N[3][3]
        txt3 = "+"
        
    else :
        c3 = N[2][3] * N[3][2] * N[3][3] 
        txt3 = "x"
        
    #c4
    c4 = N[1][1]
    
    #c5,6,7
    if (N[0][2]%N[0][3]==0 or N[0][3]%N[0][2]==0) or (N[1][2]%N[1][3]==0 or N[1][3]%N[1][2]==0) or (N[2][0]%N[3][0]==0 or N[3][0]%N[2][0]==0) :
        if N[0][2]%N[0][3]==0 or N[0][3]%N[0][2]==0 :
            if N[0][2]%N[0][3]==0 :
                c5 = int(N[0][2]/N[0][3])
            else :
                c5 = int(N[0][3]/N[0][2])
                
            c6 = abs(N[1][2]-N[1][3])
            c7 = abs(N[2][0]-N[3][0])
            txt5 = "/"
            txt6 = "-"
            txt7 = "-"
            
        elif N[1][2]%N[1][3]==0 or N[1][3]%N[1][2]==0 :
            c5 = abs(N[0][2]-N[0][3])
            if N[1][2]%N[1][3]==0 :
                c6 = int(N[1][2]/N[1][3])
            else:
                c6 = int(N[1][3]/N[1][2])
            
            c7 = abs(N[2][0]-N[3][0])
            txt5 = "-"
            txt6 = "/"
            txt7 = "-"
            
        elif N[2][0]%N[3][0]==0 or N[3][0]%N[2][0]==0 :
            c5 = abs(N[0][2]-N[0][3])
            c6 = abs(N[1][2]-N[1][3])
            if N[2][0]%N[3][0]==0 :
                c7 = int(N[2][0]/N[3][0])
            else :
                c7 = int(N[3][0]/N[2][0])
            txt5 = "-"
            txt6 = "-"
            txt7 = "/"
    else :
        c5 = abs(N[0][2]-N[0][3])
        c6 = abs(N[1][2]+N[1][3])
        c7 = abs(N[2][0]-N[3][0])
        txt5 = "-"
        txt6 = "-"
        txt7 = "-"
    
    # กำหนดสีช่องของแต่ละกรุ๊ป
    TxT[0][0].configure(bg = "sky blue")
    TxT[0][1].configure(bg = "sky blue")
    TxT[1][0].configure(bg = "sky blue")
        
    TxT[2][1].configure(bg = "#FF6E05")
    TxT[2][2].configure(bg = "#FF6E05")
    TxT[3][1].configure(bg = "#FF6E05")
        
    TxT[2][3].configure(bg = "gold")
    TxT[3][2].configure(bg = "gold")
    TxT[3][3].configure(bg = "gold")
        
    TxT[1][1].configure(bg = "red")
        
    TxT[0][2].configure(bg = "lime")
    TxT[0][3].configure(bg = "lime")
        
    TxT[1][2].configure(bg = "violet")
    TxT[1][3].configure(bg = "violet")
    
    TxT[2][0].configure(bg = "pink")
    TxT[3][0].configure(bg = "pink")
    
    #สร้างกล่อง แสดงเครื่องหมายและคำตอบของแต่ละกรุ๊ป
    btn1 = Button(window, text = txt1 +" "+ str(c1) , bg = "sky blue",command = free , width = 5)
    btn1.grid(column = 1, row = 10, padx =2)

    btn2 = Button(window, text = txt2 +" "+ str(c2) , bg = "#FF6E05",command = free , width = 5)
    btn2.grid(column = 2, row = 10, padx =2)
        
    btn3 = Button(window, text = txt3 +" "+ str(c3) , bg = "gold",command = free , width = 5)
    btn3.grid(column = 3, row = 10, padx =2)
        
    btn4 = Button(window, text = str(c4) , bg = "red",command = free , width = 5)
    btn4.grid(column = 4, row = 10, padx =2)
        
    btn5 = Button(window, text = txt5 +" "+ str(c5) , bg = "lime",command = free , width = 5)
    btn5.grid(column = 5, row = 10, padx =2)
        
    btn6 = Button(window, text = txt6 +" "+ str(c6) , bg = "violet",command = free , width = 5)
    btn6.grid(column = 6, row = 10, padx =2)
        
    btn7 = Button(window, text = txt7 +" "+ str(c7) , bg = "pink",command = free , width = 5)
    btn7.grid(column = 7, row = 10, padx =2)
    
    return(N)
#-------------------Form End---------------------------------------      

#------------------------Function New Game----------------
fm = IntVar()
def randF():
    # สุ่มรูปแบบของตาราง A B C
    fm.set(random.randint(1,3))
    if fm.get() == 1 :
        Am = FormA()
        
    elif fm.get() == 2 :
        Am = FormB()
        
    elif fm.get() == 3 :
        Am = FormC()
    #เปลี่ยนข้อความในปุ่ม
    btn.configure(text = "New Game")
    # เช็ทให้ข้อความในฟังก์ชันอื่นเป็นค่าเริ่มต้น
    lbl2.configure(text = "",bg = "#000000")
    lbl3.configure(text = "",bg = "#000000")
    for i in range(len(txt)) :
        txt[i].configure(text = "" ,fg = "#000000")
    
    return(Am)
#-------------End Function Random Number-----------------
    
def check():
    
    X = [x00,x01,x02,x03,x10,x11,x12,x13,x20,x21,x22,x23,x30,x31,x32,x33]
    cont = 0
    # เช็คว่าค่าที่รับเข้ามาจาก Entry เท่ากับเลขที่สุมมามั้ย
    for i in range(len(X)):
        if X[i].get() == int(txt[i].get()):
            txt[i].configure(fg = "blue")
            cont +=1
        else :
            txt[i].configure(fg = "white")
    # ถ้า cont =16 แสดงว่าถูกทั้ง 16 ช่อง หมายถึงชนะเกม
    if cont == 16 :
        lbl2.configure(text = " \\\^0^// !!! CONGRATULATIONS !!! \\\^0^//" ,fg = "orange",font="impact 20")    
    lbl3.configure(text = "",bg = "#000000")

def answer():
    # เฉลยคำตอบ
    lbl3.configure(text = "  " +str(x00.get()) + "   " + str(x01.get()) + "   " + str(x02.get()) + "   " + str(x03.get()) +"  "+ "\n" + str(x10.get()) + "   " + str(x11.get()) + "   " + str(x12.get()) + "   " + str(x13.get()) + "\n" + str(x20.get()) + "   " + str(x21.get()) + "   " + str(x22.get()) + "   " + str(x23.get())+ "\n" + str(x30.get()) + "   " + str(x31.get()) + "   " + str(x32.get()) + "   " + str(x33.get()) ,bg = "red" ,fg = "orange",font="impact 20")
    lbl2.configure(text = "",bg = "#000000")

#------------ปุ่ม , ข้อความ-----------------------------------------------    
btn = Button(window, text = "Start" , command = randF,fg="red",bg = "gold",width = 15)
btn.grid(row =0,pady = 5)

btn0 = Button(window, text = "    Check    " , command = check,fg="gold",bg = "red")
btn0.grid(row =3)

btn1 = Button(window, text = "    Answer   " , command = answer,fg="gold",bg = "red")
btn1.grid(row =4)

lbl = Label(window , text = "Condition",fg = "orange",bg = "#000000")
lbl.grid(column = 0, row = 10, pady= 10)

lbl1 = Label(window , text = "วิธีเล่น\nเติมตัวเลข 1-4 ลงในช่องว่างแต่ละช่อง\nโดยแต่ละแถวและแต่ละหลักเลขจะต้องไม่ซ้ำกัน\nในช่องที่มีสีเดียวกันจะต้องใช้ + - x / และ\nได้คำตอบเท่ากับช่อง Condition ของสีนั้น\nเมื่อเติมตัวเลขครบ 16 ช่อง\nกด Check เพื่อตรวจสอบคำตอบ\nจำนวนในช่องที่ตอบ 'ถูก' จะเป็น 'สีฟ้า'\nและจำนวนในช่องที่ตอบ 'ผิด' จะเป็น 'สีขาว'",fg = "red",bg = "#000000" ,justify = LEFT,font="time 12 bold")
lbl1.grid(column = 5,row = 3, rowspan = 6,columnspan = 4, pady= 5,padx=2)

# สำหรับข้อความเฉลย
lbl3 = Label(window , text = "",bg = "#000000")
lbl3.grid(column = 0, row = 11,columnspan = 7 , pady= 30 )

# สำหรับข้อความเมื่อชนะ
lbl2 = Label(window , text ="",bg = "#000000")
lbl2.grid(column = 0, row = 11,columnspan = 9 , pady= 30 )


'''
#ช่องตารางเติมคำตอบ-------------------------------------------
'''

#free 
txtfree = Label(window,width = 23,bg = "#000000")
txtfree.grid(column = 8 , row =10,pady = 2,ipady = 5)

# สร้างช่องสำหรับเติมคำตอบ
TxT = [[None,None,None,None],[None,None,None,None],[None,None,None,None],[None,None,None,None]]
for i in range(4):
    for j in range(4):
        txtij = Entry(window,width = 5)
        txtij.grid(column = j+1 , row = i+3 ,pady = 2,padx =2,ipady = 6)
        TxT[i][j] = txtij
        
# ทำให้ช่องอยู่ใน list เดียว
txt = []
txt[0:4] =TxT[0] 
txt[4:8] =TxT[1]
txt[8:12] =TxT[2]
txt[12:16] =TxT[3]

window.mainloop() 
