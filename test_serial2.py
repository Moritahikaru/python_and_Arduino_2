import time
import serial
import csv
import tkinter as tk
import tkinter.filedialog as tkFileDialog
import tkinter.font as tkFont

class Ser:
    def __init__(self):
        self.ser=None
    def start_connect(self):
        comport='COM3' # arduino ideで調べてから。
        tushinsokudo=57600 # arduinoのプログラムと一致させる。
        timeout=5 # エラーになったときのために。とりあえず１０秒で戻ってくる。
        self.ser = serial.Serial(comport,tushinsokudo,timeout=timeout)
        time.sleep(2) # 1にするとダメ！短いほうがよい。各自試す。
    def send_com(self):
        ser=self.ser
        ser.write('a'.encode('ascii')) # arduinoへ開始の合図を送る。
        data=v.get() # vの文字列は、v.get()で取り出す。
        ser.write(data.encode('ascii'))
        ser.flush() # バッファ内の待ちデータを送りきる。
        print("sent: "+data)
        time.sleep(1) # send直後にreceiveしようとすると、timeoutになるので。
    def receive_com(self):
        ser=self.ser
        ser.write('b'.encode('ascii')) # arduinoへ開始の合図を送る。
        ser.flush() # バッファ内の待ちデータを送りきる。
        line = ser.readline().decode('ascii').rstrip()
        print("received: "+line)
        time.sleep(1) # 安全のため
    def connect(self):
        self.start_connect()
        send_button.configure(state=tk.NORMAL)
        receive_button.configure(state=tk.NORMAL)
        send_entry.configure(state=tk.NORMAL)
root=tk.Tk()
font=tkFont.Font(size=24)
ser=Ser()
v=tk.StringVar() # tk.TK()の後に書く。
connect_button=tk.Button(root,text='connect',font=font,height=2,padx=20,command=ser.connect)
connect_button.grid(row=0,column=0)
send_button=tk.Button(root,text='send',font=font,height=2,padx=20,command=ser.send_com)
send_button.grid(row=0,column=1)
send_button.configure(state=tk.DISABLED)
receive_button=tk.Button(root,text='receive',font=font,height=2,padx=20,command=ser.receive_com)
receive_button.grid(row=0,column=2)
receive_button.configure(state=tk.DISABLED)
send_entry=tk.Entry(root,font=font,textvariable=v)
send_entry.grid(row=1,column=0,columnspan=3)
send_entry.configure(state=tk.DISABLED)

root.mainloop()