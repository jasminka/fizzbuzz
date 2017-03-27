import Tkinter
import tkMessageBox

window = Tkinter.Tk()
greeting = Tkinter.Label( window, text="Vnesi stevilo med 1 in 100!")
greeting.pack()

guess = Tkinter.Entry( window )
guess.pack()

def fizzbuzz():
    if int(guess.get()) <= 100:
        result = []

        for i in range(1, int(guess.get()) + 1):
            if i % 15 == 0:
                result.append("fizzbuzz")
            elif i % 3 == 0:
                result.append("fizz")
            elif i % 5 == 0:
                result.append("buzz")
            else:
                result.append(str(i))

        tkMessageBox.showinfo("Result", '\n'.join(result))
    else:
        tkMessageBox.showinfo("Result", "Your number is too high. Try again.")


submit = Tkinter.Button( window, text='Submit', command=fizzbuzz )
submit.pack()
window.mainloop()
