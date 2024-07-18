def calculate_gpa(grades):
    degree = sum(grades) / len(grades)
    if degree > 95:
        gpa = 'A+'
    elif degree > 90:
        gpa = 'A'
    elif degree > 85:
        gpa = 'B+'
    elif degree > 80:
        gpa = 'B'
    elif degree > 75:
        gpa = 'B-'
    elif degree > 70:
        gpa = 'C+'
    elif degree > 65:
        gpa = 'C'
    elif degree > 60:
        gpa = 'C-'
    elif degree > 55:
        gpa = 'D+'
    elif degree > 50:
        gpa = 'D'
    else:
        gpa = 'F'
    return gpa

def recommend_study_schedule(grades, subjects):
    percentage = []
    grades_sum = sum(grades)
    for grade in grades:
        percentage.append(round((100 - grade) / ((len(grades)*100)-grades_sum) * 7))
    # Combine grades with subjects
    grade_subject_pairs = list(zip(subjects, percentage))

    # Sort subjects by grades (ascending order)
    sorted_pairs = sorted(grade_subject_pairs, key=lambda x: x[1], reverse=1)

    # Generate study schedule (more time for subjects with lower grades)
    study_schedule = []
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Assign study days based on ranking
    for topic in sorted_pairs:
        p = topic[1]
        delete_days = []
        for day in days_of_week:
            if p > 0:
              study_schedule.append((day, topic[0]))
              p -= 1
              delete_days.append(day)
            else:
                for d in delete_days:
                    days_of_week.remove(d)
                break

    return study_schedule

# Main

subjects = ["Math", "Science", "History", "English"]
grades = []

for subject in subjects:
    grade = float(input(f"Enter your grade for {subject} (out of 100): "))
    grades.append(grade)

gpa = calculate_gpa(grades)
print(f"Your GPA is: {gpa}")

study_schedule = recommend_study_schedule(grades, subjects)
print("\nRecommended Study Schedule:")
for day, subject in study_schedule:
    print(f"{day}: {subject}")