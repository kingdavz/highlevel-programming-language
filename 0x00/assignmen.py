#!/usr/bin/python
#!/usr/bin/python

def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

if __name__ == "__main__":
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    except ValueError:
        print("Please enter valid numbers for length and width.")

        # ...existing code...
