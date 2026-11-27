

def greetUser():
    fullName = input("Enter your first name and last name separated by a space: ")

    # find the space between the names
    spaceIndex = fullName.find(" ")

    # string slicing to extract the first and last names
    firstName = fullName[:spaceIndex]
    lastName = fullName[spaceIndex + 1:]

    # capitalize each name
    firstNameCap = firstName.capitalize()
    lastNameCap = lastName.capitalize()

    output = f"""
    {'=' * 55}
    'Hi, {firstNameCap} {lastNameCap}!,You Performed following actions':^55
    {'=' * 55}
    Input Given             : {fullName}
    You have space at       : {spaceIndex} index
    Your First Name         : {firstName}
    Your Last Name          : {lastName}
    Capitalized First Name  : {firstNameCap}
    Capitalized Last Name   : {lastNameCap}
    {'=' * 55}
    """

    print(output)

greetUser()