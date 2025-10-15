#!/usr/bin/python
"""A module reads the report of students scores"""

def generate_report(names, grades):
    try:
        combined = zip(names, grades)
        valid_grades = []
        
        for name, grade in combined:
            grade_int = int(grade)
            if grade_int < 0:
                raise ValueError(f"Invalid grade for {name}: {grade}")
            valid_grades.append(grade_int)
        
        if all(g >= 50 for g in valid_grades):
            return "All students passed"
        else:
            return "Some students failed"
    except ValueError as e:
        return ValueError(e)
    finally:
        print("Report generation completed")

if __name__=="__main__":
    names = ["Alice", "Bob", "Charlie"]
    grades = ["85", "42", "78"]
    print(generate_report(names, grades))
                
