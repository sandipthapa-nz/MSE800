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

# Comparisons
isCritical= bugSeverity >= 4
over8Hours= estimatedTimeToFix > 8
over1kCost= totalCost > 1000
isUrgent = isCritical and isReproducible

# Output in f-string format
report = f"""
{'=' * 55}
{'BUG TRACKING REPORT':^55}
{'=' * 55}
Project Name      : {projectName}
Bug ID            : {bugID}
Description       : {bugDescription}
Severity Score    : {bugSeverity} / 5
Reproducible      : {isReproducible}
{'-' * 55}
TIME & COST BREAKDOWN
{'-' * 55}
Hourly Rate       : ${hourlyRate:,.2f}/hr
Fixing Time       : {estimatedTimeToFix:.2f} hrs
Testing Time (25%): {testingTime:.2f} hrs
Total Dev Time    : {totalDevTime:.2f} hrs
Fixing Cost       : ${estimatedCFixingCost:,.2f}
Total Est. Cost   : ${totalCost:,.2f}
{'-' * 55}
STATUS & PRIORITY FLAGS
{'-' * 55}
Critical Bug                 : {isCritical}
Requires > 8 Fixing Hours    : {over8Hours}
Total Cost Exceeds $1,000    : {over1kCost}
Urgent Attention Required    : {isUrgent}
{'=' * 55}
"""

print(report)