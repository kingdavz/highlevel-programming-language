#!/usr/bin/python

#!/usr/bin/python

def logical_operations(a, b):
    print(f"{a} AND {b}: {a and b}")
    print(f"{a} OR {b}: {a or b}")
    print(f"NOT {a}: {not a}")
    print(f"NOT {b}: {not b}")

if __name__ == "__main__":
    try:
        a = bool(int(input("Enter first value (0 or 1): ")))
        b = bool(int(input("Enter second value (0 or 1): ")))
        logical_operations(a, b)
    except ValueError:
        print("Please enter 0 or 1 only.")
        