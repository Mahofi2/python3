"""
marks = 78, 65, 90, 45, 56
roll = int(input("Enter your class roll :"))
result = marks[roll - 1]
print(result)
"""
"""
marks = [[34, 78, 45, 67], [79, 89, 34, 67], [67, 54, 87, 56], [45, 67, 65, 78]]
roll = int(input("Enter your roll number :"))
result = marks[roll - 1]
print(result)
"""
"""
# dictionary
mark = {
    1: 45,
    2: 78,
    3: 90,
    4: 65,
    }
roll = int(input("Enter your roll :"))
print(mark[roll])
"""
"""
# result dictionary
mark = {
    'sadia': {'Bangla': 90, 'English': 56, 'Math': 78, 'Science': 89},
    'mehedi': {'Bangla': 67, 'English': 90, 'Math': 56, 'Science': 87},
    'mahofi': {'Bangla': 76, 'English': 67, 'Math': 87, 'Science': 97},
    'riyan': {'Bangla': 56, 'English': 67, 'Math': 87, 'Science': 87},
    'rifat': {'Bangla': 76, 'English': 76, 'Math': 65, 'Science': 76},
}
emptyDic = {}
name = input("Enter your name :")
print(mark[name]['Math'])
"""
# dictionary
division = {
    'Dhaka Division': {'District': 13, 'Upazilas': 89, 'Union Councils': 885, 'Area': 2059374},
    'Chittagong Division': {'District': 11, 'Upazilas': 103, 'Union Councils': 949, 'Area': 33202326},
    'Barisal Division': {'District': 6, 'Upazilas': 41, 'Union Councils': 352, 'Area': 1322520},
    'Khulna Division': {'District': 10, 'Upazilas': 59, 'Union Councils': 571, 'Area': 2228422},
    'Rangpur Division': {'District': 8, 'Upazilas': 58, 'Union Councils': 535, 'Area': 1618499},
    'Selhet Division': {'District': 4, 'Upazilas': 41, 'Union Councils': 338, 'Area': 1263522},
    'Rajshahi Division': {'District': 8, 'Upazilas': 67, 'Union Councils': 565, 'Area': 1815308},
    'Mymensingh Division': {'District': 4, 'Upazilas': 35, 'Union Councils': 351, 'Area': 1058406},
}
emptyDic = {}
place = input("Enter your division name :")
print(division[place]['District'])
