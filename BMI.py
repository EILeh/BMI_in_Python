"""
Body Mass Index

This program has a graphical interface which calculates the user's body mass
index (BMI). The program is intended to work so, that the user can enter their
weight and height and click the button for calculating the BMI. In addition to
just displaying the decimal value of the BMI, we will also reserve a space in
the user interface for displaying a verbal description to the user.

The weight is entered as kilograms and height as centimeters. The weight index
is calculated using the formula weight/(height*height). Thus, the entries must
be changed to a suitable format before calculating the BMI. The result of the
calculation is shown to the specificity of two decimals in the user interface
component.

The error checks that the program performs are:
the entered weight and length must be numbers and if there's an error the
program shall print the message:
Error: height and weight must be numbers.

weight and length cannot be negatives or a zero, and if there's an error the
program shall print the message:
Error: height and weight must be positive.

When the BMI value is between 18.5–25, display the text:
Your weight is normal.

When the value is greater, display:
You are overweight.

and when it's less display:
You are underweight.


Writer of the program

Name: EILeh

"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        self.__bmi = 0.00

        self.__weight_value = Entry()
        self.__weight_value.grid(row=0, columnspan=2)
        self.__weight_value_text = Label(self.__mainwindow, text="kg")
        self.__weight_value_text.grid(row=0, column=3, columnspan=2)

        self.__height_value = Entry()
        self.__height_value.grid(row=1, columnspan=2)
        self.__height_value_text = Label(self.__mainwindow, text="cm")
        self.__height_value_text.grid(row=1, column=3, columnspan=2)

        self.__calculate_button = Button(self.__mainwindow, text="Calculate",
                                         command=self.calculate_BMI)
        self.__calculate_button.grid(row=2, column=0, columnspan=1)

        self.__result_texts = ""
        self.__result_text = Label(self.__mainwindow, text=self.__result_texts)
        self.__result_text.grid(row=3, columnspan=4)

        self.__explanation_texts = ""
        self.__explanation_text_under = "You are underweight."
        self.__explanation_text_over = "You are overweight."
        self.__explanation_text_normal = "Your weight is normal."
        self.__explanation_text_numbers_error = \
            "Error: height and weight must be numbers."
        self.__explanation_text_not_positive = \
            "Error: height and weight must be positive."
        self.__explanation_text = Label(self.__mainwindow,
                                        text=self.__explanation_texts)
        self.__explanation_text.grid(row=4, columnspan=4)

        self.__stop_button = Button(self.__mainwindow, text="Stop",
                                         command=self.stop)
        self.__stop_button.grid(row=2, column=1, columnspan=2)

    def calculate_BMI(self):
        """
        This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        are_weight_and_height_integers = self.reset_fields()

        if are_weight_and_height_integers:

            weight = int(self.__weight_value.get())
            height = int(self.__height_value.get())

            height = height/100

            self.__bmi = weight / (height * height)
            self.__result_text.configure(text=f"{self.__bmi:.2f}")

            if self.__bmi > 25.0:
                self.__explanation_text.configure(
                    text=self.__explanation_text_over)

            elif self.__bmi < 18.5:
                self.__explanation_text.configure(
                    text=self.__explanation_text_under)

            else:
                self.__explanation_text.configure(
                    text=self.__explanation_text_normal)

        else:
            self.__weight_value.delete(0, END)
            self.__height_value.delete(0, END)


    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        weight = self.__weight_value.get()
        height = self.__height_value.get()

        try:
            weight = int(weight)
            height = int(height)

        except ValueError:
            self.__explanation_text.configure(
                text=self.__explanation_text_numbers_error)
            return False

        if weight < 0 or (height < 0):
            self.__explanation_text.configure(
                text=self.__explanation_text_not_positive)
            return False

        return True


    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():

    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
