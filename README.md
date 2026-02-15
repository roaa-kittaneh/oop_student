##  Project Overview

The `Student` class includes the following:

Attributes:
- name
- student_id
- grades

Methods:
- add_grade()
- get_average()
- __str__()
- __repr__()

---

##  Core Concepts 

### Class and Object
A Class is a blueprint that defines structure and behavior.  
An Object is an instance of that class containing its own data.

---

### Constructor (`__init__`)
The constructor initializes the object when it is created.  
It is responsible for setting up instance attributes and preparing the object for use.

---

### Instance Variables vs Class Variables

Instance Variables:
- Belong to each individual object.
- Store object-specific data.

Class Variables:
- Shared among all instances of the class.
- Represent data common to all objects.

---

### `self`
The `self` keyword refers to the current instance of the class.  
It allows access to the object’s attributes and methods.

---

### Encapsulation and Validation
The class protects its internal state by validating input inside methods.  
Invalid data raises appropriate exceptions to ensure data integrity.

---

### `__str__` vs `__repr__`

`__str__`:
- Intended for end users.
- Provides a readable and clean string representation.

`__repr__`:
- Intended for developers.
- Provides a detailed and precise representation useful for debugging.

---

##  Testing

Unit tests were written using `pytest` to verify:
- Object initialization
- Grade addition
- Average calculation
- Proper exception handling


