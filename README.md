SI 507 Project 1 by Amanda Jung

In this project, our goal was to create a simple banking app using code from the files lab3_code.py, si507_project1, and requirements.txt.

In lab3_code.py, there are 5 classes (Currency, Dollar, Yuan, Pound, and Bank) where Dollar, Yuan, and Pound are child classes of Currency.
  - The Currency class contains a constructor with the instance variable "value" and the function conversion which converts the value of the current currency to the value of the desired currency.
  - It's child classes (Dollar, Yuan, and Pound) each include a constructor and str method.
  - The Bank class contains a constructor with instance variables of name, unit, and value; a str method, and a deposit method that checks to see and allow deposits of currency.

In si507_project1.py, we incorporate Flask and have different routes with specific set of inputs based on the url. Underneath each route is a function definition that incorporates the input and class definitions from lab3_code.py and produces the desired output.

The file requirements.txt contains the packages (e.g. Flask) that are necessary to run the files of code listed above.
