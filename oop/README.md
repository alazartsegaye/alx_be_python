This project demonstrates the implementation of key Python concepts such as object-oriented programming, polymorphism, and the use of static and class methods. It is divided into four different scripts:

## Files in the Project

### 1. `book_class.py`
Defines the `Book` class with attributes and methods that demonstrate object initialization, deletion, and string representations.

#### Features:
- **Attributes**: `title`, `author`, `year`.
- **Methods**:
  - `__init__`: Initializes the book with a title, author, and year.
  - `__del__`: Outputs a message when the book object is deleted.
  - `__str__`: Provides a user-friendly string representation of the book.
  - `__repr__`: Returns a detailed string representation suitable for debugging.

### 2. `library_system.py`
Implements a `Library` class to manage a collection of books and includes polymorphic behavior through inheritance from a base `Book` class.

#### Features:
- **Base Class**: `Book`.
- **Derived Classes**:
  - `EBook` with an additional `file_size` attribute.
  - `PrintBook` with an additional `page_count` attribute.
- **Library Class**:
  - Manages a collection of books.
  - Includes methods to add books and list them.

### 3. `polymorphism_demo.py`
Demonstrates polymorphism by creating a base `Shape` class and derived classes like `Circle`, `Square`, and `Rectangle`.

#### Features:
- **Polymorphic Behavior**:
  - Each derived class overrides a `calculate_area` method to provide specific implementations.
  - A `describe` method provides descriptions unique to each shape.

### 4. `class_static_methods_demo.py`
Illustrates the usage of `@staticmethod` and `@classmethod` in Python using a `Calculator` class.

#### Features:
- **Static Method**:
  - `add(a, b)`: Adds two numbers and returns the sum.
- **Class Method**:
  - `multiply(cls, a, b)`: Multiplies two numbers and prints a class attribute before returning the product.
- **Class Attribute**: `calculation_type` with a value of "Arithmetic Operations".
