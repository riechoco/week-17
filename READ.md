# Simulated Device Monitoring and Alert System
 
**Student Name:** Joana Marie T. Caban
**Student Number:** 2600403
**Section:** 1CpEA
 
## Project Description
This program is used to monitor device temperature readings. It shows the readings, classifies them based on their temperature, and gives a summary of the results. It also helps identify if the device needs attention.
 
## Features
- View all stored temperature readings
- Add a new reading 
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings
 
## Requirements
- Python 3 
 
## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: python device_monitor.py
   (On macOS or Linux, type: python3 device_monitor.py)
 
## Sample Output

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 4

MONITORING SUMMARY
------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 1 (20.00%)
WARNING  : 3 (60.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
This matches the initial readings in your program: 28, 31, 35, 37, 29
 
## Test Cases
I performed 10 tests. 10 passed and 0 failed.
Full details are in test_cases.md.
 
## Known Limitations
- The user must manually enter new readings.
- The user must manually enter new readings.
- The program only accepts whole numbers.
 
## Reflection
The hardest part was classifying the temperature readings correctly. I fixed the input validation to prevent the program from accepting letters and values outside the allowed range. I also learned how to calculate the average and percentages for the summary. Next, I would improve the program by saving the readings so I can access them even after closing it.