import numpy as np


class DataAnalytics:
    """Encapsulates NumPy operations, mathematical computations, and statistical analysis."""

    def __init__(self, data=None):
        """Constructor for initializing the array."""
        if data is None:
            self._data = np.array([])
        else:
            self._data = np.array(data)

    @property
    def data(self):
        """Getter for encapsulated data."""
        return self._data

    @data.setter
    def data(self, new_data):
        """Setter for encapsulated data."""
        self._data = np.array(new_data)

    # --- Private Utility Methods ---
    def _validate_non_empty(self):
        """Private helper to ensure array has elements before operating."""
        if self._data.size == 0:
            raise ValueError("Array is currently empty. Please create or load an array first.")

    def _validate_2d(self, other_array=None):
        """Private helper to ensure arrays are 2D for matrix operations."""
        self._validate_non_empty()
        if self._data.ndim != 2:
            raise ValueError("Operation requires a 2D array.")
        if other_array is not None and other_array.ndim != 2:
            raise ValueError("Secondary input must also be a 2D array.")

    # --- Class Methods & Static Methods ---
    @classmethod
    def create_random_array(cls, shape, low=0, high=100):
        """Class method utility to initialize a DataAnalytics instance with random numbers."""
        random_data = np.random.randint(low, high, size=shape)
        return cls(random_data)

    @staticmethod
    def correlation_coefficient(arr1, arr2):
        """Static utility method to compute correlation matrix between two arrays."""
        a1, a2 = np.array(arr1).flatten(), np.array(arr2).flatten()
        if len(a1) != len(a2):
            raise ValueError("Arrays must be of identical length to compute correlation.")
        return np.corrcoef(a1, a2)

    # --- Array Management Methods ---
    def slice_array(self, slice_tuple):
        """Access specific elements, rows, columns, or slices."""
        self._validate_non_empty()
        return self._data[slice_tuple]

    def concatenate_with(self, secondary_array, axis=0):
        """Combines current array with another along a specified axis."""
        self._validate_non_empty()
        sec_arr = np.array(secondary_array)
        self._data = np.concatenate((self._data, sec_arr), axis=axis)
        return self._data

    def split_array(self, num_sections, axis=0):
        """Splits current array into equal-sized sub-arrays."""
        self._validate_non_empty()
        return np.array_split(self._data, num_sections, axis=axis)

    # --- Mathematical Operations ---
    def elementwise_op(self, other_array, operation='add'):
        """Performs element-wise arithmetic (+, -, *, /)."""
        self._validate_non_empty()
        other = np.array(other_array)
        if operation == 'add':
            return np.add(self._data, other)
        elif operation == 'subtract':
            return np.subtract(self._data, other)
        elif operation == 'multiply':
            return np.multiply(self._data, other)
        elif operation == 'divide':
            return np.divide(self._data, other)
        else:
            raise ValueError("Invalid operation type.")

    def matrix_multiply(self, other_matrix):
        """Calculates dot product / matrix multiplication for 2D arrays."""
        other = np.array(other_matrix)
        self._validate_2d(other)
        return np.matmul(self._data, other)

    # --- Search, Sort & Filter ---
    def search_value(self, target):
        """Searches for indices matching a target value."""
        self._validate_non_empty()
        indices = np.where(self._data == target)
        return indices

    def sort_array(self, ascending=True):
        """Sorts array in ascending or descending order."""
        self._validate_non_empty()
        sorted_arr = np.sort(self._data, axis=None)
        return sorted_arr if ascending else sorted_arr[::-1]

    def filter_by_condition(self, condition_str, threshold):
        """Filters array elements based on user condition (<, >, ==, <=, >=)."""
        self._validate_non_empty()
        ops = {
            '>': self._data > threshold,
            '<': self._data < threshold,
            '==': self._data == threshold,
            '>=': self._data >= threshold,
            '<=': self._data <= threshold
        }
        if condition_str not in ops:
            raise ValueError("Unsupported condition format.")
        return self._data[ops[condition_str]]

    # --- Aggregating & Statistical Functions ---
    def get_summary_stats(self, percentile_val=50):
        """Computes statistical properties, percentiles, and aggregates."""
        self._validate_non_empty()
        return {
            'sum': np.sum(self._data),
            'mean': np.mean(self._data),
            'median': np.median(self._data),
            'std_dev': np.std(self._data),
            'variance': np.var(self._data),
            'min': np.min(self._data),
            'max': np.max(self._data),
            'percentile': np.percentile(self._data, percentile_val)
        }


# --- Interactive Menu Interface ---
def run_cli():
    analyzer = DataAnalytics()

    while True:
        print("\n==============================")
        print("       NUMPY ANALYZER         ")
        print("==============================")
        print("1. Create a numpy array ")
        print("2. display current array properties")
        print("3. Slice / Index Array")
        print("4. Combine / Split Array")
        print("5. Mathematical Operations (Element-wise & Matrix)")
        print("6. Search, Sort & Filter Array")
        print("7. Statistical & Aggregation Summary")
        print("8. Correlation Coefficient (Static Method Utility)")
        print("9. Exit")

        choice = input("\nSelect an option (1-9): ").strip()

        try:
            if choice == '1':
                print("\n[Array Creation Options]")
                print("a. Manual Input")
                print("b. Random Generator (@classmethod)")
                sub = input("Choice (a/b): ").strip().lower()
                
                if sub == 'a':
                    raw = input("Enter numbers (space separated): ")
                    shape_str = input("Enter shape tuple (e.g., '3,3' for 2D or leave empty for 1D): ").strip()
                    arr = np.fromstring(raw, sep=' ')
                    if shape_str:
                        shape = tuple(map(int, shape_str.split(',')))
                        arr = arr.reshape(shape)
                    analyzer.data = arr
                elif sub == 'b':
                    shape = tuple(map(int, input("Enter shape (e.g., 3,3 or 2,3,4): ").split(',')))
                    analyzer = DataAnalytics.create_random_array(shape)
                print(f"[Success] Array updated:\n{analyzer.data}")

            elif choice == '2':
                print(f"\nArray:\n{analyzer.data}")
                print(f"Shape: {analyzer.data.shape} | Dimensions: {analyzer.data.ndim}D | Data Type: {analyzer.data.dtype}")

            elif choice == '3':
                print(f"\nCurrent Array:\n{analyzer.data}")
                idx_str = input("Enter slice index string (Python syntax, e.g., '0' or ':, 1'): ")
                # Using eval safely for tuple indices
                parsed_idx = eval(f"np.s_[{idx_str}]")
                result = analyzer.slice_array(parsed_idx)
                print(f"\nSliced Result:\n{result}")

            elif choice == '4':
                sub = input("Choose (1: Concatenate, 2: Split): ").strip()
                if sub == '1':
                    raw = input("Enter flat array elements to append: ")
                    sec = np.fromstring(raw, sep=' ')
                    print(f"Result:\n{analyzer.concatenate_with(sec)}")
                elif sub == '2':
                    num = int(input("Enter number of splits: "))
                    splits = analyzer.split_array(num)
                    for i, s in enumerate(splits):
                        print(f"Split {i+1}:\n{s}")

            elif choice == '5':
                print("\nOperations: 1: Add, 2: Subtract, 3: Multiply, 4: Divide, 5: Matrix Multiplication")
                op = input("Select operation (1-5): ").strip()
                if op in ['1', '2', '3', '4']:
                    op_map = {'1': 'add', '2': 'subtract', '3': 'multiply', '4': 'divide'}
                    val = float(input("Enter scalar or array value: "))
                    print(f"Result:\n{analyzer.elementwise_op(val, op_map[op])}")
                elif op == '5':
                    raw = input("Enter elements for second matrix (matching dimensions): ")
                    shape = tuple(map(int, input("Enter shape (rows, cols): ").split(',')))
                    other = np.fromstring(raw, sep=' ').reshape(shape)
                    print(f"Matrix Product:\n{analyzer.matrix_multiply(other)}")

            elif choice == '6':
                sub = input("Choose (1: Search, 2: Sort, 3: Filter): ").strip()
                if sub == '1':
                    target = float(input("Enter target value to find indices: "))
                    print(f"Indices found at: {analyzer.search_value(target)}")
                elif sub == '2':
                    order = input("Sort ascending? (y/n): ").strip().lower() == 'y'
                    print(f"Sorted Result:\n{analyzer.sort_array(ascending=order)}")
                elif sub == '3':
                    cond = input("Enter operator (>, <, ==, >=, <=): ").strip()
                    thresh = float(input("Enter threshold value: "))
                    print(f"Filtered Elements:\n{analyzer.filter_by_condition(cond, thresh)}")

            elif choice == '7':
                p = float(input("Enter percentile rank to compute (0-100): "))
                stats = analyzer.get_summary_stats(percentile_val=p)
                print("\n--- STATISTICAL SUMMARY ---")
                for k, v in stats.items():
                    print(f"{k.capitalize():<12}: {v}")

            elif choice == '8':
                arr1 = np.fromstring(input("Enter first array: "), sep=' ')
                arr2 = np.fromstring(input("Enter second array: "), sep=' ')
                corr = DataAnalytics.correlation_coefficient(arr1, arr2)
                print(f"\nCorrelation Matrix:\n{corr}")

            elif choice == '9':
                print("\nExiting NumPy Analyzer. Goodbye!")
                break
            else:
                print("[Error] Invalid selection. Pick between 1 and 9.")

        except Exception as e:
            print(f"[Error] Operation failed: {e}")


if __name__ == "__main__":
    run_cli()