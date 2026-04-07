# Running a Single Test with Pytest

This guide shows how to execute:

* A single test file
* A single test function
* A specific test inside a class

---

## 1. Run a Single Test File

```bash
pytest path/to/test_file.py
```

### Example

```bash
pytest tests/test_math.py
```

---

## 2. Run a Single Test Function

Use `::` to target a specific test function:

```bash
pytest path/to/test_file.py::test_function_name
```

### Example

```bash
pytest tests/test_math.py::test_addition
```

---

## 3. Run a Test Inside a Class

```bash
pytest path/to/test_file.py::TestClassName::test_method_name
```

### Example

```bash
pytest tests/test_math.py::TestCalculator::test_addition
```

---

## 4. Run Tests Matching a Pattern

```bash
pytest -k "pattern"
```

### Example

```bash
pytest -k "addition"
```

---

## 5. Stop on First Failure

```bash
pytest -x
```

---

## 6. Show Print Statements

```bash
pytest -s
```

---

## 7. Verbose Output

```bash
pytest -v
```

---

## 8. Combine Options

```bash
pytest tests/test_math.py::test_addition -v -s
```

---

## 9. Common Project Structure

```
project/
├── src/
├── tests/
│   ├── test_math.py
│   └── test_api.py
└── pyproject.toml
```

---

## 10. Tips

* Test files must start with `test_`
* Test functions must start with `test_`
* Classes should be prefixed with `Test`
* Avoid `__init__` in test classes

---

## 11. Quick Reference

```bash
# File
pytest tests/test_file.py

# Function
pytest tests/test_file.py::test_function

# Class method
pytest tests/test_file.py::TestClass::test_method
```
