# Day 19: Getters and Setters in Python OOP

### Code Explanation - Line by Line
**LIne 1: Comment**
**Line 2: `class Employee:`**  
Created a blueprint/template called `Employee`. Think of it like an employee record format in a company. All rules for employees will be written inside this class.

**Line 3: `def __init__(self, salary):`**  
This is the constructor. It runs automatically when a new Employee object is created.  
`self` = refers to the current object being created  
`salary` = value passed while creating the object

**Line 4: `self._salary = salary #Single underscore suggest a protected variable`**  
Stored the salary in `_salary`.  
Single underscore `_` means "protected variable" - it's a convention to tell other developers "don't access this directly from outside". Python won't block you, but it's considered bad practice.

**Line 5: `# Getter Method`**  
Comment to indicate the next method will be a Getter.

**Line 6-7: `def get_salary(self): return self._salary`**  
**Getter Method** = Used to read/access the protected data.  
Since `_salary` is protected, we can't do `emp._salary` directly. So we create a function `get_salary()` that safely returns the value from inside the class.

**Line 8: `# Setter Method`**  
Comment to indicate the next method will be a Setter.

**Line 9-13: `def set_salary(self, amount):`**  
**Setter Method** = Used to modify/update the protected data with validation.  
Here we added a check: `if amount > 0:`  
This ensures salary can't be set to a negative value.  
If valid → update `self._salary = amount`  
If invalid → print error message

This is data validation. Without Setter, anyone could do `emp._salary = -5000` and break the logic.

**Line 15: `# Usage`**  
Example of how to use the class.

**Line 16: `emp = Employee(5000)`**  
Created a new Employee object named `emp` with initial salary 5000.  
Constructor `__init__` runs and sets `self._salary = 5000`.

**Line 17: `emp.set_salary(9000) # Must Call as a Function`**  
Updating salary to 9000 using the Setter method.  
We don't directly assign `emp._salary = 9000`. Instead we call `set_salary(9000)` so the validation check runs first.

**Line 18: `print(emp.get_salary()) #9000`**  
Reading salary using the Getter method.  
`get_salary()` fetches the value from inside the class and returns 9000, which gets printed.

### Key Concept: Encapsulation
1. **Data Hiding**: `_salary` is kept protected using single underscore
2. **Controlled Access**: `get_salary()` provides read access  
3. **Validation**: `set_salary()` provides write access with checks

This prevents direct modification of data and ensures data integrity. That's the core idea of Encapsulation in OOP.

**Rule to Remember:**  
`get_` prefix = Getter for reading data  
`set_` prefix = Setter for writing data with validation
