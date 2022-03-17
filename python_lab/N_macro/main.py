import tkinter.ttk as ttk
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
root.title("NSYS macro")


def start():
    #여기에 시작했을때 진행될 매크로를 넣어야함
    # #각 옵션들 값 확인
    # print("가로넓이 :", cmb_width.get())
    # print("간격 :", cmb_space.get())
    # print("포맷 :", cmb_format.get())

    # # 파일 목록 확인
    # if list_file.size() == 0:
    #     msgbox.showwarning("경고","이미지 파일을 추가하세요")
    #     return
    numbers = numbering()
    names = file_name_make(numbers)
    macro(names)
    
    msgbox.showwarning("완료", "저장이 완료 되었습니다.")

#count값을 받고 배열을 생성하는 함수
def numbering():
    numbers = []
    first_val = float(ent_tail.get())
    count = int(ent_count.get())
    if cmb_sign.get() == "양수":
        numbers.append(str(first_val))
        for i in range(1, count):
            next_val = first_val + 0.25
            numbers.append(str(next_val))
            first_val += 0.25
    else: # 음수 일때
        name_val = "M" + str(first_val)
        numbers.append(name_val)
        for i in range(1, count):
            next_val = first_val - 0.25
            name_val = "M" + str(next_val)
            numbers.append(name_val)
            first_val -= 0.25
    return numbers

#각 값을 받고 파일 이름 배열을 생성하는 함수    
def file_name_make(numbers):
    names = []
    head = ent_head.get()
    mid = ent_mid.get()
    count = int(ent_count.get())
    for i in range(0, count):
        name = head+"_"+mid+"_"+numbers[i]
        names.append(name)
    return names
# 주 매크로 함수
def macro(names):
    count = int(ent_count.get())
    for i in range(0, count):
        if pyg.locateCenterOnScreen(os.path.join(image_path , "solution.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 solution 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "solution.png"), confidence = 0.8))
        pyg.doubleClick()
        time.sleep(30)

        # 잘못된 데이터 입력시 생기는 경고창 처리
        warn = pyg.locateCenterOnScreen(os.path.join(image_path , "warning.png"), confidence = 0.8)
        if warn != None:
            pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "warning.png"), confidence = 0.8))
            pyg.move(150, -100)
            pyg.click()
            time.sleep(0.5)
            pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "info.png"), confidence = 0.8))
            pyg.move(420, -75)
            pyg.click()
            time.sleep(0.5)

        # fluent뭐시기 경고창 처리
        warn2 = pyg.locateCenterOnScreen(os.path.join(image_path , "warning2.png"), confidence = 0.8)
        if warn2 != None:
            pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "warning2.png"), confidence = 0.8))
            pyg.move(150, -50)
            pyg.click()
            time.sleep(0.5)
            #창을 종료하는 절대 좌표 클릭
            pyg.moveTo(3150, 15)
            pyg.click()
            time.sleep(0.5)
            #처리 후 원상 복귀 
            pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "solution.png"), confidence = 0.8))
            pyg.doubleClick()
            time.sleep(30)

            
        if pyg.locateCenterOnScreen(os.path.join(image_path , "file.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 file 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "file.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "export.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 export 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "export.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "solution_data.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 solution_data 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "solution_data.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "file_type.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 filetype 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "file_type.png"), confidence = 0.8))
        pyg.move(0, 10)
        pyg.click()
        time.sleep(0.5)
        pyg.move(0, 20)
        time.sleep(0.5)
        pyg.scroll(-500)
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "tecplot.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 tecplot 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "tecplot.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "static.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 static 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "static.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "pressure.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 pressure 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "pressure.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "velocity.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 velocity 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "velocity.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "write.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 write 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "write.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "computer.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 computer 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "computer.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "d.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 d 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "d.png"), confidence = 0.8))
        pyg.doubleClick()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "airfoil.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 airfoil 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "airfoil.png"), confidence = 0.8))
        pyg.doubleClick()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "tecplot_file.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 tecplot_file 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "tecplot_file.png"), confidence = 0.8))
        pyg.move(100, 0)
        pyg.tripleClick()   
        pyg.press('del')
        pyg.typewrite(names[i], interval=0.1)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "ok.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 ok 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "ok.png"), confidence = 0.8))
        pyg.click()
        time.sleep(10)
        if i +1 == count:
            break

        if pyg.locateCenterOnScreen(os.path.join(image_path , "nsys.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 nsys 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "nsys.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "set.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 set 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "set.png"), confidence = 0.8))
        pyg.doubleClick()
        time.sleep(2)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "current.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 current 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "current.png"), confidence = 0.8))        
        pyg.click()
        pyg.press('down')
        pyg.hotkey('shift', 'f10')
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "set_current.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 set_current 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "set_current.png"), confidence = 0.8))
        pyg.click()
        time.sleep(0.5)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "yes.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 yes 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "yes.png"), confidence = 0.8))
        pyg.click()
        time.sleep(20)

        if pyg.locateCenterOnScreen(os.path.join(image_path , "project.png"), confidence = 0.8) == None:
            msgbox.showwarning("경고", f"{names[i]} 순서에서 project 이미지를 찾을 수 없었습니다..")
            break
        pyg.moveTo(pyg.locateCenterOnScreen(os.path.join(image_path , "project.png"), confidence = 0.8))
        pyg.click()
        time.sleep(1)
       
       
       
       




frame_ex = LabelFrame(root, text="예제")
frame_ex.pack(padx=5, pady=5, ipady=5)

lbl_ex = Label(frame_ex, text="head_mid_tail count는 반복횟수" )
lbl_ex.pack(side="left")

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

#head 레이블
lbl_head = Label(frame_option, text="head", width=8)
lbl_head.pack(side="left")

#head 엔트리
ent_head = Entry(frame_option, width= 8)
ent_head.pack(side="left")

#mid 레이블
lbl_mid = Label(frame_option, text="mid", width=8)
lbl_mid.pack(side="left")
 
#mid 엔트리
ent_mid = Entry(frame_option, width= 8)
ent_mid.pack(side="left")

#tail 옵션 레이블
lbl_tail = Label(frame_option, text="tail", width=8)
lbl_tail.pack(side="left")

#tail 옵션 엔트리
ent_tail = Entry(frame_option, width= 8)
ent_tail.pack(side="left", padx=5)


# 옵션 프레임
frame_option2 = LabelFrame(root, text="세부옵션")
frame_option2.pack(padx=5, pady=5, ipady=5)

#sign 옵션 레이블
lbl_sign = Label(frame_option2, text="sign", width=8)
lbl_sign.pack(side="left")

#sign 콤보
opt_sign = ["양수", "음수"]
cmb_sign = ttk.Combobox(frame_option2, state="readonly", values=opt_sign, width=10)
cmb_sign.current(0)
cmb_sign.pack(side="left")

#count 옵션 레이블
lbl_count = Label(frame_option2, text="count", width=8)
lbl_count.pack(side="left")

#count 옵션 엔트리
ent_count = Entry(frame_option2, width= 12)
ent_count.pack(side="left", padx=5)

frame_run = Frame(root)
frame_run.pack(fill="x")




btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)

root.resizable(False, False)
root.mainloop()

