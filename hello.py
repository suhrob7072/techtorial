print("First Exam Score:")
ex1 = float(input())
print("Second Exam Score:")
ex2 = float(input())
print("Third Exam Score:")
ex3 = float(input())
print("Attrndance in %:")
at = float(input())

average = (ex1 * 0.2) + (ex2 * 0.3) + (ex3 * 0.5)
bool = average >= 65 and at >= 80
print(bool)