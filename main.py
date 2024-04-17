import tkinter

# window
window = tkinter.Tk()
window.minsize(width=200, height=200)
window.config(pady=20)


# conclusion method
def conclusion():
    weight = weight_entry.get()
    height = height_entry.get()
    if weight == "" or height == "":
        result_label.config(text="Enter both oh them!")
    else:
        try:
            bmi = int(weight) / (int(height) / 100) ** 2
            result_label.config(text=result(bmi))
        except:
            result_label.config(text="Enter a valid number")


# weight label
weight_label = tkinter.Label(text="Type Your Weight(kg)")
weight_label.pack()

# weight entry
weight_entry = tkinter.Entry()
weight_entry.config(width=15)
weight_entry.pack()

# height label
height_label = tkinter.Label(text="Type Your Height(cm)")
height_label.pack()

# height entry
height_entry = tkinter.Entry()
height_entry.config(width=15)
height_entry.pack()

# calculation button
calculate_button = tkinter.Button()
calculate_button.config(text="calculate", width=10, command=conclusion)
calculate_button.pack(pady=5)

# result label
result_label = tkinter.Label()
result_label.pack()


def result(bmi):
    result_string = f"Your BMI is : {round(bmi, 2)}, you are "
    if bmi <= 16:
        result_string += "severely thin"
    elif 16 < bmi <= 17:
        result_string += "moderately thin"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin"
    elif 18.5 < bmi <= 25:
        result_string += "normal"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class1"
    elif 35 < bmi <= 40:
        result_string += "obese class2"
    else:
        result_string += "obese class2"
    return result_string


window.mainloop()
