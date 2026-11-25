# Collect all required information from the user
projectName= input("Enter the project name: ")
bugID=input("Enter the bug ID: ")
bugDescription=input("Enter the bug description: ")
bugSeverity=int(input("Enter the bug severity score (1-5): "))
estimatedTimeToFix=float(input("Enter the estimated hours to fix the bug: "))
hourlyRate=float(input("Enter the hourly rate for fixing the bug: "))
isReproducible=input("Is the bug reproducible? (y/n): ")

# convert the reproducibility input to a boolean value
isReproducible= isReproducible.lower() == "y"

# Calculate the estimated cost to fix the bug
estimatedCFixingCost= estimatedTimeToFix * hourlyRate

# Calculate the testing time
testingTime= estimatedTimeToFix * (25/100)

# calcultae the total development time and cost
totalDevTime= estimatedTimeToFix + testingTime
totalCost= totalDevTime * hourlyRate