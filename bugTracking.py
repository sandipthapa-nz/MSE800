# Collect all required information from the user
project_name= input("Enter the project name: ")
bugID=input("Enter the bug ID: ")
bugDescription=input("Enter the bug description: ")
bugSeverity=int(input("Enter the bug severity score (1-5): "))
estimatedTimeToFix=float(input("Enter the estimated hours to fix the bug: "))
hourlyRate=float(input("Enter the hourly rate for fixing the bug: "))
isReproducible=input("Is the bug reproducible? (yes/no): ")