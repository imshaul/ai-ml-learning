# Python OOP Practice Questions (Beginner → Advanced)

A set of 30 practice questions covering Python Object-Oriented Programming, from basics to advanced concepts. Try solving each one yourself before checking any reference material.

---

## 🟢 Beginner (1–10)

1. Create a class `Person` with attributes `name` and `age`. Create an object and print both attributes.
2. What is the difference between a class and an object? Give a simple example.
3. Create a class `Car` with a method `start()` that prints `"Car started"`. Call it using an object.
4. What is `self` in Python classes? Why is it needed in methods?
5. Create a class `Student` with a class variable `school_name` shared by all objects. Create two student objects and print the school name from both.
6. Write a class `Rectangle` with attributes `length` and `width`, and a method `area()` that returns the area.
7. What is the purpose of the `__init__` method? Write a class that uses it to set two attributes.
8. Create a class `Animal` with a method `sound()`. Create three different objects and call the method on each.
9. Explain the difference between instance variables and class variables with a code example.
10. Create a class `BankAccount` with a `balance` attribute and methods `deposit()` and `withdraw()`.

---

## 🟡 Intermediate (11–20)

11. Create a parent class `Vehicle` and a child class `Car` that inherits from it. Add one extra method in `Car`.
12. What is multiple inheritance? Write a class that inherits from two parent classes.
13. Use `super()` to call a parent class's `__init__` method from a child class.
14. What is method overriding? Demonstrate it with a parent and child class.
15. Create an abstract class `Shape` with an abstract method `area()`. Implement it in two subclasses: `Circle` and `Square`.
16. What is polymorphism? Write an example using two classes with the same method name but different behavior.
17. What is duck typing in Python? Write a small example demonstrating it.
18. Create a class with a private attribute (using `__` prefix) and a getter method to access it.
19. What is aggregation in OOP? Write a small example with two classes showing an aggregation relationship.
20. Create a class `Employee` and a class `Department` where a `Department` object contains a list of `Employee` objects (composition).

----

## 🔴 Advanced (21–30)

21. What is the Method Resolution Order (MRO) in Python? Use `ClassName.__mro__` to check it for a multiple inheritance example.
22. Explain the diamond problem in multiple inheritance and how Python resolves it.
23. Create a class using `@staticmethod` and explain when you'd use a static method instead of a regular method.
24. Create a class using `@classmethod` and explain the difference between `@classmethod` and `@staticmethod`.
25. What are dunder (magic) methods? Implement `__str__` and `__repr__` in a class and explain the difference.
26. Implement operator overloading by defining `__add__` in a class so two objects of that class can be added using `+`.
27. What is encapsulation? Write a class that fully encapsulates its data using private attributes and public methods.
28. Create a custom exception class that inherits from `Exception`, and use it inside a `try/except` block.
29. Explain composition vs inheritance — when would you prefer one over the other? Support with a short example of each.
30. Create a class hierarchy with at least 3 levels (grandparent → parent → child) and demonstrate how `super()` chains across all three.

---

*Solving these in order will take you from OOP basics to a solid intermediate/advanced understanding.*
