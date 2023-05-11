BMI_in_Python

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
