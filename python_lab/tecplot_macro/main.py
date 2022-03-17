import tkinter.messagebox as msgbox
import time
import pyautogui as pyg
import os
import re
from tkinter import *
from tkinter import filedialog

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")


root = Tk()
root.title("Tecplot macro")

# 파일 추가
def add_file():
    i=0
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.",\
        filetypes=(("plt 파일", "*.plt"), ("모든 파일","*.*")),\
            initialdir="E:/")# 최초에 C:/ 경로를 보여줌

    for file in files:
        list_file.insert(END, file)

# 선택 삭제
def del_file():
    #print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


def start():
    #여기에 시작했을때 진행될 매크로를 넣어야함
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고","파일을 추가하세요.")
        return
   
    macro()
    msgbox.showwarning("완료", "저장이 완료 되었습니다.")
    #print(list_file.get(0))

def macro():
    for i in range(0,list_file.size()):
        #open.png 파일 찾고, 마우스 이동후 클릭 후 0.5초 대기   
        # 1
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "open.png")))
        pyg.click()
        time.sleep(0.5)

        #파일 이름 옆의 입력창 클릭 후 파일 이름 적기
        # pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "file_name.png")))
        # pyg.move(70, 0)
        # pyg.click()
        #정규식을 이용해서 전체 파일디렉토리에서 파일명만을 축출
        # 2
        file_select = re.compile("([a-zA-Z0-9_\s]+\.[a-zA-Z0-9\s]+)")
        file_name_find = file_select.findall(list_file.get(i))
        pyg.typewrite(file_name_find[0], interval=0.1)
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path, "open_button.png")))
        pyg.click()
        time.sleep(0.5)

        # 3 frame.png누르고 load_frame.png누르기
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "frame.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "load_frame.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)
        # 4
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "file_open.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        # 5
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "file.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "export.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)
        # 6
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "OK.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        # pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "file_name.png")))
        # pyg.move(70, 0)
        # pyg.click()
        # 7
        pyg.press('del')
        file_select2 = re.compile("([a-zA-Z0-9_\s\.]+(?=\.))")
        file_name_find2 = file_select2.findall(list_file.get(i))
        pyg.typewrite(file_name_find2[0]+".png", interval=0.1)
        pyg.press('enter')
        time.sleep(0.5)

        # 8
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "contour.png"), confidence = 0.8))
        pyg.move(-35 , 0)
        pyg.click()

        # 9 
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "shade.png"), confidence = 0.8))
        pyg.move(-30 , 0)
        pyg.click()

        
        # 10
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "file.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "export.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        # 11
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "OK.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        # 12
        pyg.press('del')
        file_select2 = re.compile("([a-zA-Z0-9_\s\.]+(?=\.))")
        file_name_find2 = file_select2.findall(list_file.get(i))
        pyg.typewrite(file_name_find2[0] + "_pic.png", interval=0.1)
        pyg.press('enter')
        time.sleep(0.5)

        # 13
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "new.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        # 14
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "discard.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)




#파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="선택삭제", command=del_file)
btn_add_file.pack(side="right")

#리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height= 15,width= 90, yscrollcommand=scrollbar.set)
list_file.pack(side="left",fill="both", expand=True)


# 실행 프레임

frame_run = Frame(root)
frame_run.pack(fill="x")


btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()

