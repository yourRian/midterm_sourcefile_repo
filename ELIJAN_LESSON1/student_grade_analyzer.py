scores = [85, 72, 91, 64, 78]

print("Student Scores:")
for score in scores:
    print(score)

print()

def get_remark(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 75:
        return "Good"
    else:
        return "Failed"

def get_status(score):
    return "Passed" if score >= 75 else "Failed"

passed_count = 0
failed_count = 0

for i, score in enumerate(scores, start=1):
    remark = get_remark(score)
    status = get_status(score)
    if status == "Passed":
        passed_count += 1
        print("Student " + str(i) + ": " + str(score) + " - " + remark + " - " + status)
    else:
        failed_count += 1
        print("Student " + str(i) + ": " + str(score) + " - " + status)

total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)

print()
print("Total Score: " + str(total))
print("Average Score: " + str(round(average)))
print("Highest Score: " + str(highest))
print("Lowest Score: " + str(lowest))
print("Passed: " + str(passed_count))
print("Failed: " + str(failed_count))