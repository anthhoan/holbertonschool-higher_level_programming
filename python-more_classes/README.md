### 📦 Class Definition: `Rectangle`

```python
class Rectangle:
```

Defines a new class `Rectangle`.

---

### 🧮 Class Attributes

```python
number_of_instances = 0
print_symbol = "#"
```

* `number_of_instances`: Tracks how many `Rectangle` objects currently exist.
* `print_symbol`: Used for string representation (defaults to `#`).

---

### 🔧 Constructor: `__init__`

```python
def __init__(self, width=0, height=0):
```

Initializes a new rectangle with:

* `width` and `height` (default to 0).
* Calls property setters to validate input.
* Increments `number_of_instances`.

---

### 📐 Properties: `width` and `height`

#### Getter and Setter for `width`

```python
@property
def width(self): ...
@width.setter
def width(self, value): ...
```

* Ensures `width` is an integer and ≥ 0.
* Stores it privately as `self.__width`.

#### Getter and Setter for `height`

```python
@property
def height(self): ...
@height.setter
def height(self, value): ...
```

* Same validation and storage logic as `width`.

---

### 📏 Area Calculation

```python
def area(self):
    return (self.__width * self.__height)
```

Returns the area of the rectangle.

---

### 📏 Perimeter Calculation

```python
def perimeter(self):
    if self.__width == 0 or self.__height == 0:
        return 0
    return (2 * (self.__width + self.__height))
```

Returns the perimeter, but `0` if width or height is `0`.

---

### 📄 String Representation: `__str__`

```python
def __str__(self): ...
```

* Returns a visual representation using `print_symbol`.
* Returns an empty string if width or height is `0`.

Example (for 2x3 rectangle):

```
##
##
##
```

---

### 🧠 Official Representation: `__repr__`

```python
def __repr__(self):
    return ("Rectangle({}, {})".format(self.__width, self.__height))
```

* Returns a string that can recreate the rectangle using `eval()`.

---

### 🗑️ Destructor: `__del__`

```python
def __del__(self):
    Rectangle.number_of_instances -= 1
    print("Bye rectangle...")
```

* Called when a rectangle is deleted.
* Decrements `number_of_instances`.
* Prints a goodbye message.

---

### 📏 Static Method: `bigger_or_equal`

```python
@staticmethod
def bigger_or_equal(rect_1, rect_2): ...
```

* Compares two rectangles by area.
* Raises `TypeError` if arguments aren’t `Rectangle` instances.
* Returns the bigger one (or `rect_1` if equal).

---

### 🔁 Class Method: `square`

```python
@classmethod
def square(cls, size=0):
    return cls(size, size)
```

* Creates a **square** (a rectangle with equal sides).
* Returns a new `Rectangle` object where `width == height == size`.

---

### ✅ Summary

This `Rectangle` class:

* Validates input.
* Tracks instances.
* Supports printing and comparison.
* Provides methods for area, perimeter, and square creation.
* Is well-structured and object-oriented.

Let me know if you want examples or test cases to see how it works in action!
