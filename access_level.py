import tkinter
from tkinter import messagebox
from tkinter import *

CLASS_TYPE = 8
LEVEL = 4

def butten_action(level,class_type):
    if level_button[level][class_type]["text"] == '0':
        for i in range(level,LEVEL):
            level_button[i][class_type]["text"] = '1'
    else:
        for i in range(0,level+1):
            level_button[i][class_type]["text"] = '0'
    # generate access level
    access_level = 0
    for i in range(LEVEL):
        for j in range(CLASS_TYPE):
            access_level <<= 1
            if level_button[i][j]["text"] == '1':
                access_level |= 0x1 
    str_b = "二进制表示："+format(access_level,'b').zfill(32)
    str_x = "十六进制表示："+format(access_level,'x').zfill(8)
    level_show["text"] = "权限值：" + "\n" + str_b + "\n" + str_x

def reset():
    for i in range(LEVEL):
        for j in range(CLASS_TYPE):
            level_button[i][j]["text"] = '0'
    access_level = 0
    str_b = "二进制表示："+format(access_level,'b').zfill(32)
    str_x = "十六进制表示："+format(access_level,'x').zfill(8)
    level_show["text"] = "权限值：" + "\n" + str_b + "\n" + str_x

if __name__ == '__main__':
    top = tkinter.Tk()
    top.title("权限设置")

    access_level_frame = Frame(top)
    access_level_frame.pack(anchor='center')
    level_show = Label(top,bg='white',cursor='circle',justify=LEFT,text="权限值：")
    level_show.pack(anchor='center',pady=10)
    str_note = "判断说明：\n用户权限值: user\n物品权限值: item\n判断条件:\nif item == user & item : \n     permission \nelse :\n     forbidden"
    note = Label(top,bg='white',cursor='circle',justify=LEFT,text=str_note)
    note.pack(anchor='center',pady=10)

    sheet_class_type = Label(access_level_frame,bg='white',cursor='circle',justify=LEFT,text="级别\类别 |   办公    设计      机械     电子     文档   危险品    贵重品   其他  ")
    sheet_class_type.pack(anchor='w')
    sheet_level_type = Label(access_level_frame,bg='white',cursor='circle',justify=LEFT,text="  P0        \n\n  P1        \n\n  P2        \n\n  P3        ")
    sheet_level_type.pack(side = 'left',anchor='nw')

    level_button = [ [0] * 8 for i in range(4)]
    p0_frame = Frame(access_level_frame)
    p0_frame.pack(side = 'top',anchor='nw')

    level_button[0][0] = Button(p0_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(0,0))
    level_button[0][1] = Button(p0_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(0,1))
    level_button[0][2] = Button(p0_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(0,2))
    level_button[0][3] = Button(p0_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(0,3))
    level_button[0][4] = Button(p0_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(0,4))
    level_button[0][5] = Button(p0_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(0,5))
    level_button[0][6] = Button(p0_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(0,6))
    level_button[0][7] = Button(p0_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(0,7))
    for i in range(0,CLASS_TYPE):
        level_button[0][i].pack(side = 'left',anchor='nw',fill='none')

    p1_frame = Frame(access_level_frame)
    p1_frame.pack(side = 'top',anchor='nw')
    level_button[1][0] = Button(p1_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(1,0))
    level_button[1][1] = Button(p1_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(1,1))
    level_button[1][2] = Button(p1_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(1,2))
    level_button[1][3] = Button(p1_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(1,3))
    level_button[1][4] = Button(p1_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(1,4))
    level_button[1][5] = Button(p1_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(1,5))
    level_button[1][6] = Button(p1_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(1,6))
    level_button[1][7] = Button(p1_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(1,7))
    for i in range(0,CLASS_TYPE):
        level_button[1][i].pack(side = 'left',anchor='nw',fill='none')

    p2_frame = Frame(access_level_frame)
    p2_frame.pack(side = 'top',anchor='nw')
    level_button[2][0] = Button(p2_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(2,0))
    level_button[2][1] = Button(p2_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(2,1))
    level_button[2][2] = Button(p2_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(2,2))
    level_button[2][3] = Button(p2_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(2,3))
    level_button[2][4] = Button(p2_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(2,4))
    level_button[2][5] = Button(p2_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(2,5))
    level_button[2][6] = Button(p2_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(2,6))
    level_button[2][7] = Button(p2_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(2,7))
    for i in range(0,CLASS_TYPE):
        level_button[2][i].pack(side = 'left',anchor='nw',fill='none')

    p3_frame = Frame(access_level_frame)
    p3_frame.pack(side = 'top',anchor='nw')
    level_button[3][0] = Button(p3_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(3,0))
    level_button[3][1] = Button(p3_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(3,1))
    level_button[3][2] = Button(p3_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(3,2))
    level_button[3][3] = Button(p3_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(3,3))
    level_button[3][4] = Button(p3_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(3,4))
    level_button[3][5] = Button(p3_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(3,5))
    level_button[3][6] = Button(p3_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(3,6))
    level_button[3][7] = Button(p3_frame,bg='#FFEBCD',width=5,text="0",command=lambda:butten_action(3,7))
    for i in range(0,CLASS_TYPE):
        level_button[3][i].pack(side = 'left',anchor='nw',fill='none')

    reset_button = Button(access_level_frame,bg="#FFF0F5",text="reset",command=reset)
    reset_button.pack(side = 'top',anchor='center')
    # img_yes = PhotoImage(file='./yes.png')
    # b = Button(top,bg='#FFEBCD',image=img_yes)
    # b.pack()
    
    top.mainloop()