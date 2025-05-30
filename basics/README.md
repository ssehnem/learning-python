# 🧠 Python Basics

For every language you learn - and everything in general - you always have to start from the most basic things and gradually elevate to an intermediate/advanced level. For the basics, I chose to practice **Variables & Data Types**, **Operators** and **Input & Output**. For me, without these three subtopics, you will experience huge difficulty - or even be unable - to create anything. 

👉 Come with me and let's dissect each one of these subtopics! 
You'll find exercises inside every folder, so you can see more examples of these themes being applied in real life. 🧪

## 📦 Variables

To make even basic things such as mathematical operations, we need to create variables (e.g.: name, age, city, etc). They store any information you want: text, numbers, true/false. 
Create variables and use them to build your code.

### ✨ Example

```python
num1 = 3
num2 = 5
num3 = num1 + num2 

print(num3)
```

➡️ This code will print the sum of the variable num1 with the variable num2, turning them into a third variable called num3, and then outputting the value of num3.

## 🧬 Data Types

Python has some data types built-in by default.
It's important to remember that variables can store different types of data, and each type can do specific things.
So it's important to categorize them with their right type!

Here are the built-in types, by category: 

* Text Type:	str
* Numeric Types:	int, float, complex
* Sequence Types:	list, tuple, range
* Mapping Type:	dict
* Set Types:	set, frozenset
* Boolean Type:	bool
* Binary Types:	bytes, bytearray, memoryview
* None Type:	NoneType

But the ones I use the most (and you'll probably use too) are: **str, int, float and bool**.

### ✨ Example

```python
x = 10

print(type(x))
```

➡️ It will return the type of the variable x.
Output: <class 'int'>