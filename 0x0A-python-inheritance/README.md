# Python Inheritance

This repository provides examples and explanations of Python Inheritance, a powerful object-oriented programming concept.

## Table of Contents

- [Introduction](#introduction)
- [Class Inheritance](#class-inheritance)
- [super() Function](#super-function)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Inheritance is a fundamental concept in object-oriented programming that allows a new class to inherit attributes and methods from an existing class. In Python, you can create a subclass that inherits from a superclass, facilitating code reuse and promoting a modular approach to programming.

## Class Inheritance

The `class Subclass(Superclass):` syntax is used to create a subclass that inherits from a superclass. The subclass can access attributes and methods of the superclass and override or extend them as needed.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an instance of Dog
my_dog = Dog()
my_dog.speak()  # Inherited from Animal
my_dog.bark()   # Specific to Dog

