import tkinter

wn=tkinter.Tk()
wn.minsize(250,200)
wn.title("BMI Calculater")
def carpım():
    a=entry1.get()
    b=entry2.get()
    if (a.isdigit() and b.isdigit()):
        sonuc= int(a)/((int(b)*int(b))/10000)
        if sonuc<=18.5:
            label.config(text="You have under weight  BMI:"+ str(sonuc))
        elif sonuc>18.5 and sonuc<=24.9:
            label.config(text="You are Normal  BMI:" + str(sonuc))
        elif sonuc>25.0 and sonuc<=29.9:
            label.config(text="You have OverWeight  BMI:" + str(sonuc))
        elif sonuc>30 and sonuc<=34.9:
            label.config(text="You are 1. degree Obese  BMI:" + str(sonuc))
        elif sonuc>35.0 and sonuc<=39.9:
            label.config(text="You are 2.degree Obese  BMI:" + str(sonuc))
        elif sonuc > 40 :
            label.config(text="You are 3.degree Obese  BMI:" + str(sonuc))
    else:
        label.config(text="Invalid data")

label1=tkinter.Label(text="Enter Your Weight(kg)")
label1.pack()
entry1=tkinter.Entry()
entry1.pack()
label2=tkinter.Label(text="Enter Your Height(cm)")
label2.pack()
entry2=tkinter.Entry()
entry2.pack()
button=tkinter.Button(text="Calculate",command=carpım)
button.pack()
label = tkinter.Label(text="BMI")
label.pack()










wn.mainloop()