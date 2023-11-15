Division = {
    'barisal': {'Districts': 6, 'upazila': 41, 'union': 352},
    'chittagong': {'Districts': 11, 'upazila': 103, 'union': 949},
    'dhaka': {'Districts': 13, 'upazila': 89, 'union': 885},
    'khulna': {'Districts': 10, 'upazila': 59, 'union': 571},
    'mymensingh': {'Districts': 4, 'upazila': 35, 'union': 351},
    'rajshahi': {'Districts': 8, 'upazila': 67, 'union': 565},
    'rangpur': {'Districts': 8, 'upazila': 58, 'union': 535},
    'sylhet': {'Districts': 4, 'upazila': 41, 'union': 338},

}
userInput = str(input("Enter your Bebag :"))
Input = userInput.lower()


print(Division.get(Input,"invalid"))
