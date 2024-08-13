# data=['ram','sits','hari','laxmi','laxmi']
# student = [
#     {'name' : 'ram','gender':'male','status':True},
#     {'name' : 'sita','gender':'female','status':True},
#     {'name' : 'hari','gender':'male','status':False},
#     {'name' : 'laxmi','gender':'female','status':False},
#     {'name' : 'gopal','gender':'male','status':True}
#           ]
# total_users
# total_active users
# total inactive users
# total male
# total female 
# total active male 
# total active female 
# total inactive male
# total inactive female
student = [
    {'name' : 'ram','gender':'male','status':True},
    {'name' : 'sita','gender':'female','status':True},
    {'name' : 'hari','gender':'male','status':False},
    {'name' : 'laxmi','gender':'female','status':False},
    {'name' : 'gopal','gender':'male','status':True}
]

# total_users
total_users = len(student)
print("Total users:", total_users)

# total_active users
total_active_users = sum(1 for s in student if s['status'])
print("Total active users:", total_active_users)

# total inactive users
total_inactive_users = sum(1 for s in student if not s['status'])
print("Total inactive users:", total_inactive_users)

# total male
total_male = sum(1 for s in student if s['gender'] == 'male')
print("Total male:", total_male)

# total female
total_female = sum(1 for s in student if s['gender'] == 'female')
print("Total female:", total_female)

# total active male
total_active_male = sum(1 for s in student if s['gender'] == 'male' and s['status'])
print("Total active male:", total_active_male)

# total active female
total_active_female = sum(1 for s in student if s['gender'] == 'female' and s['status'])
print("Total active female:", total_active_female)

# total inactive male
total_inactive_male = sum(1 for s in student if s['gender'] == 'male' and not s['status'])
print("Total inactive male:", total_inactive_male)

# total inactive female
total_inactive_female = sum(1 for s in student if s['gender'] == 'female' and not s['status'])
print("Total inactive female:", total_inactive_female)