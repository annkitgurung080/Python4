student = [
     {'name' : 'ram','gender':'male','status':True},
     {'name' : 'sita','gender':'female','status':True},
     {'name' : 'hari','gender':'male','status':False},
     {'name' : 'laxmi','gender':'female','status':False},
     {'name' : 'gopal','gender':'male','status':True}
           ]
total_users=len(student)
total_active_users=0
total_inactive_users=0
total_male=0
total_female=0 
total_activemale=0 
totalactive_female=0 
total_inactive_male=0
total_inactive_female=0
for student in student:
    if student['status']==True:
         total_active_users+=1
    else:
        total_inactive_users+=1
    if student['gender']=='male':
        total_male+=1
    else:
        total_female+=1
    if student['gender']=='male' and student['status']==True:
        total_activemale+=1
         