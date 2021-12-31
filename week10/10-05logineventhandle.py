# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:41:26 2021

@author: 엄지희
"""

from tkinter import *

users = dict(python='power', java='beauty')

def checkid():
    uid = et1.get().strip() # 입력된 사용자 이름 문자열받기
    pwd = et2.get().strip() # 입력된 암호 문자열받기
    print(uid, pwd)
    if uid in users.keys(): # 사용자 이름이 있는지 검사
        if users[uid] == pwd: # 사용자 이름과 암호 일치
            print('로그인 성공')
        else:
            print('암호를 확인하세요.')
    else:
        print('사용자 이름을 확인하세요.')

win = Tk()
win.title('사용자 인증')

lb1 = Label(win, text='사용자 이름')
lb2 = Label(win, text='암호')
lb1.grid(row = 0, column = 0, sticky = E) # 현 구역에서 위치를 오른쪽으로 조정
lb2.grid(row = 1, column = 0, sticky = E) # 현 구역에서 위치를 오른쪽으로 조정

et1 = Entry(win)
et2 = Entry(win)
et1.grid(row = 0, column = 1)
et2.grid(row = 1, column = 1)

# 가장 아래에 버튼 2개를 저장할 레이블을 생성해 배치
lb = Label(win)
lb.grid(row=2, column=0, columnspan = 2) # 두 열을 합해서 배치
bt1 = Button(lb, text='OK', command=checkid)
bt2 = Button(lb, text='CANCEL')
bt1.grid(row=0, column=0, padx=10) # 외부 가로 여백을 10을 둠
bt2.grid(row=0, column=1, padx=10) # 외부 가로 여백을 10을 둠

win.mainloop()