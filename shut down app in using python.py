from tkinter import *
import os 

st = Tk()
st.title("shutdown App")
st.geometry("500x500")
st.config(bg="red")

r_button = Button(st, Text="Restart", font=("Time New Roman",20,"bold"),
   relief=RAISED,cursor="plus",command= restart)               
r_button.place(x=150,y=60,hight=50,width=200)

rt_button =Button(st,Text="Restart Time",font=("Time New Roman",20,"bold"),
    relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,hight=50,width=200)

st.mainloop()