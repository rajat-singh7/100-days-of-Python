# Walrus Operator:
The walrus operator := in Python — officially called an assignment expression — lets you assign a value to a variable as part of an expression instead of as a separate statement.

It was introduced in Python 3.8 via [PEP 572] and is useful when you want to store a value and use it immediately in the same line of code 
1
 
2
 
3
.

**Why Use It?**
Avoids repetition of function calls or expressions.
Makes code shorter and cleaner by combining assignment and evaluation.
Improves performance when the expression is expensive to compute (runs only once).
Keeps related logic together — the assignment and the check happen in one place.