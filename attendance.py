students = ['alisaeed','Shaheer Mukhtiar', 'Ali Waris']
students = ['alisaeed', 'Wahaaj Nasir']
students = [
    'zara sahar',
    'eshmal rumman',
    'yashfa sikandar',
]

def show_attendance():
    print("Class Attendance List:")
    for student in students:
        print("-", student)

if __name__ == "__main__":
    show_attendance()