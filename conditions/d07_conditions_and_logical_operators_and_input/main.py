# Check exam result
# Ask if student passed the test (yes/no)
# Ask if student arrived on time (yes/no)
# If both answers are "yes" → print "Exam passed"
# Otherwise → print "Exam failed"

print("Let's check your results!")
test = input("Did you pass your test (yes/no): ")
on_time = input("Did you arrive on time (yes/no): ")

if test.lower() == "yes" and on_time.lower() == "yes":
    print("Exam passed")
else:
    print("Exam failed")
    
    
