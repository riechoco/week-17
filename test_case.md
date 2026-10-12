# Test Cases – Simulated Device Monitoring and Alert System
 
Tested by: Joana Marie T. Caban       Date: October 12, 2026
 
# Test Cases – Simulated Device Monitoring and Alert System

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Displays five initial readings: 28, 31, 35, 37, 29 | Displays all five initial readings correctly | Pass |
| TC02 | Choose 2, enter 33 | Displays "Reading added successfully." | Reading added successfully | Pass |
| TC03 | Choose 2, enter abc | Rejects input; readings remain unchanged | Displays an invalid input message | Pass |
| TC04 | Choose 2, enter 101 | Rejects value outside the 0–100 range | Displays an invalid input message | Pass |
| TC05 | Choose 2, enter -1 | Rejects value outside the 0–100 range | Displays an invalid input message | Pass |
| TC06 | Choose 3 | Classifies readings as NORMAL, WARNING, or CRITICAL | Displays each reading's classification | Pass |
| TC07 | Choose 4 | Displays total, average, minimum, maximum, percentages, and overall status | Displays the monitoring summary | Pass |
| TC08 | Enter menu choice 9 | Displays an invalid choice message | Displays an invalid choice message | Pass |
| TC09 | Enter abc at the menu | Rejects input and displays an invalid input message | Displays an invalid input message | Pass |
| TC10 | Choose 5 | Displays the exit message and terminates the program | Displays the thank-you message and exits | Pass |

## Bugs Found and Fixed
I found an error in the classification summary where the program displayed the wrong category label. I fixed it by checking the print statements and changing the label to match the correct category. I tested the summary again to make sure the program displayed the correct number and percentage for each classification.



