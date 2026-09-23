def is_pass(mark):
    if mark>= 50:
        return True
    else :
        return False

def calculate_grade(mark):
    if mark> 90:
        return "A grade"
    elif mark> 80:
        return "B grade"
    elif mark> 70 :
        return "C grade"
    elif mark> 60:
        return "D grade"
    else :
        return "Fail"
