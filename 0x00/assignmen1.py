#!/usr/bin/python

# ...existing code...

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

if __name__ == "__main__":
    try:
        choice = input("Calculate area of (r)ectangle or (t)riangle? ").lower()
        if choice == 'r':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = rectangle_area(length, width)
            print(f"The area of the rectangle is: {area}")
        elif choice == 't':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = triangle_area(base, height)
            print(f"The area of the triangle is: {area}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter valid numbers for dimensions.")
    # ...existing code...