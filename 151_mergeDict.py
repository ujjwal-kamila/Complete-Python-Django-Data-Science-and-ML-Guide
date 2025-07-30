# 151. Practice - Merging Two Dictionaries
default_settings = {'theme': 'light', 'font_size': 15}
user_settings = {'font_size': 20, 'show_avatar': True}

merged_settings = {**default_settings, **user_settings,'color':'blue'}
# or using | operator 
# merged_settings = default_settings | user_settings 

print(merged_settings)

# also possivle to unpack more than two dict

# Personal Details
student_personal = {
    'name': 'Ujjwal kamila',
    'dob': '19-11-2004',
    'gender': 'male',
    'email': 'kamila@email.com'
}

# College Enrollment Details
student_enrollment = {
    'roll': 'CSE2026',
    'branch': 'CSE',
    'year': 4,
    'email': 'ujjwalkamila@makautwb' 
}

# Academic Performance
student_marks = {
    'semester': 6,
    'cgpa': 7.5,
    'subjects': {
        'DSA': 92,
        'Electronics': 85,
        'Maths': 89
    }
}

student_home = {
    'contact_number': '123456789',
    'address': 'Jhargrm, West Bengal'
}

# Hobbies and Clubs
student_hobbies = {
    'clubs': ['DSA Zone', 'Hackaut coding club'],
    'hobbies': ['Painting', 'Poetry', 'Cycling']
}


student_profile = {
    **student_personal,
    **student_enrollment,
    **student_marks,
    **student_home,
    **student_hobbies
}
print()
print(student_profile)
