# NumPy Analyzer

A Python-based **NumPy Analyzer** project that provides an interactive command-line interface for performing array manipulation, mathematical calculations, searching, filtering, sorting, and statistical analysis using **NumPy**.

The project is implemented using an object-oriented `DataAnalytics` class and demonstrates NumPy operations along with class methods, static methods, properties, private helper methods, and exception handling.

## 📌 Features

* Create NumPy arrays manually
* Generate random NumPy arrays
* Display array properties
* View array shape, dimensions, and data type
* Slice and index arrays
* Concatenate arrays
* Split arrays into sections
* Perform element-wise:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Perform matrix multiplication
* Search for specific values
* Sort arrays in ascending or descending order
* Filter values using conditions
* Calculate statistical summaries
* Calculate:

  * Sum
  * Mean
  * Median
  * Standard deviation
  * Variance
  * Minimum
  * Maximum
  * Percentile
* Calculate correlation coefficient between two arrays
* Interactive menu-driven CLI
* Error handling and input validation

## 🛠️ Technologies Used

* **Python 3**
* **NumPy**

## 📂 Project Structure

```text
numpy-analyzer/
│
├── project 8 rnw.py
└── README.md
```

## 🧩 Main Class

### `DataAnalytics`

The `DataAnalytics` class manages NumPy arrays and provides different analytical operations.

The constructor accepts optional data and converts it into a NumPy array.

```python
analyzer = DataAnalytics([10, 20, 30, 40, 50])
```

## 🔹 Array Management

### Create Random Array

The `create_random_array()` class method creates an array containing random integers.

```python
DataAnalytics.create_random_array(shape, low=0, high=100)
```

The implementation uses `np.random.randint()`.

### Slice Array

```python
analyzer.slice_array(slice_tuple)
```

Used to access particular elements, rows, columns, or slices of an array.

### Concatenate Arrays

```python
analyzer.concatenate_with(second_array)
```

Combines the current array with another array using NumPy's `concatenate()` function.

### Split Array

```python
analyzer.split_array(3)
```

Divides an array into the requested number of sections using `np.array_split()`.

## 🔢 Mathematical Operations

The project supports element-wise arithmetic operations:

```text
Addition
Subtraction
Multiplication
Division
```

Example:

```python
analyzer.elementwise_op([1, 2, 3], "add")
```

The implementation uses NumPy functions such as `np.add()`, `np.subtract()`, `np.multiply()`, and `np.divide()`.

### Matrix Multiplication

```python
analyzer.matrix_multiply(other_matrix)
```

Matrix multiplication is performed using `np.matmul()` and requires 2D arrays.

## 🔎 Search, Sort & Filter

### Search

Search for a specific value:

```python
analyzer.search_value(25)
```

This returns the indices where the target value occurs.

### Sort

```python
analyzer.sort_array(ascending=True)
```

Supports both ascending and descending sorting.

### Filter

Values can be filtered using:

```text
>
<
==
>=
<=
```

Example:

```python
analyzer.filter_by_condition(">", 50)
```

The method creates a Boolean condition and returns matching elements.

## 📊 Statistical Analysis

The `get_summary_stats()` method calculates several statistical measurements:

```python
stats = analyzer.get_summary_stats()
```

It returns:

```text
Sum
Mean
Median
Standard Deviation
Variance
Minimum
Maximum
Percentile
```

These calculations use NumPy statistical functions such as `np.sum()`, `np.mean()`, `np.median()`, `np.std()`, `np.var()`, `np.min()`, `np.max()`, and `np.percentile()`.

## 📈 Correlation Coefficient

The project includes a static method for calculating the correlation matrix between two arrays:

```python
DataAnalytics.correlation_coefficient(arr1, arr2)
```

Both arrays must contain the same number of elements. The method uses `np.corrcoef()`.

## 🖥️ Interactive Menu

When the program runs, it provides the following menu:

```text
==============================
       NUMPY ANALYZER
==============================

1. Create a numpy array
2. Display current array properties
3. Slice / Index Array
4. Combine / Split Array
5. Mathematical Operations
6. Search, Sort & Filter Array
7. Statistical & Aggregation Summary
8. Correlation Coefficient
9. Exit
```

The CLI is implemented through the `run_cli()` function.

## 🚀 Installation

### 1. Install Python

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

### 2. Install NumPy

```bash
pip install numpy
```

### 3. Clone the Repository

```bash
git clone https://github.com/your-username/numpy-analyzer.git
```

### 4. Open the Project

```bash
cd numpy-analyzer
```

## ▶️ Run the Program

Run the Python file:

```bash
python "project 8 rnw.py"
```

The interactive NumPy Analyzer menu will appear.

## 💡 Example Workflow

Example array:

```text
10 20 30 40 50
```

The analyzer can then be used to:

```text
Search → Find 30
Sort → Sort the array
Filter → Find values greater than 25
Statistics → Calculate mean, median, variance, etc.
```

## 🧠 OOP Concepts Demonstrated

This project is also useful for learning Object-Oriented Programming in Python.

### Constructor

```python
__init__()
```

Initializes the analyzer and its NumPy array.

### Property

The `data` property provides controlled access to the internal array.

### Private Methods

The project uses:

```python
_validate_non_empty()
_validate_2d()
```

These methods validate the array before performing operations.

### Class Method

```python
create_random_array()
```

Creates a new `DataAnalytics` object containing random data.

### Static Method

```python
correlation_coefficient()
```

Performs correlation analysis without requiring an instance.

## ⚠️ Error Handling

The program uses validation and exception handling to prevent invalid operations.

Examples include:

* Empty array validation
* 2D array validation for matrix operations
* Invalid mathematical operation
* Unsupported filter condition
* Arrays with different lengths for correlation
* Invalid menu selections

The CLI catches exceptions and displays an error message instead of terminating immediately.

## 🎯 Learning Objectives

This project helps demonstrate:

* NumPy fundamentals
* Array manipulation
* Mathematical operations
* Statistical analysis
* Matrix operations
* Boolean filtering
* Sorting and searching
* Object-Oriented Programming
* Properties and setters
* Class methods
* Static methods
* Private helper methods
* Exception handling
* Menu-driven programming
* Command-line applications

## 🔮 Future Improvements

Possible future enhancements:

* Add CSV file import/export
* Add Pandas integration
* Add Matplotlib data visualization
* Add data cleaning features
* Add histogram and scatter plots
* Add covariance analysis
* Add more statistical functions
* Add unit tests
* Add a graphical user interface
* Add support for saving analysis reports

## 📄 License

This project is intended for educational and learning purposes.

## 👨‍💻 Author

**Your Name**

GitHub: `https://github.com/your-username`

---

⭐ If you found this project useful, consider giving the repository a star!
