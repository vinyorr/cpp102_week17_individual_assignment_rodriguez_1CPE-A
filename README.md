# Simulated Device Monitoring and Alert System

**Student Name:** Kevin Roy S. Rodriguez  
**Student Number:** 2601268  
**Section:** 1CPE-A  

## Project Description
Make this statement humanize
This program is a simulated device monitoring system that keeps track of room temperature readings. It allows users to view and add readings, check if the temperature is NORMAL, WARNING, or CRITICAL, and generate a summary report. It also uses basic Python concepts such as lists, loops, functions, conditional statements, and numerical calculations to process the data.

## Features
- View all stored temperature readings
- Add a new temperature reading
- Classify temperature readings as NORMAL, WARNING, or CRITICAL
- Generate a summary report
- Display the total, average, highest, and lowest temperature
- Display the number and percentage of each classification
- Display the overall monitoring status
- Return to the main menu or exit the program

## Requirements
- Python 3
- Visual Studio Code
- No external packages are required

## How to Run
1. Open the Week17 folder in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

## Sample Output
```
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 1

CURRENT ROOM TEMPERATURE READINGS
----------------------------------
Reading 1: 20 °C
Reading 2: 25 °C
Reading 3: 32 °C
Reading 4: 34 °C
Reading 5: 17 °C
Reading 6: 27 °C

Enter "1" to return to the main menu or "2" to exit: 1

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 2
Enter new reading (°C): 34
Reading added successfully: 34 °C


Enter "1" to return to the main menu or "2" to exit: 1

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 3

READING CLASSIFICATION
----------------------
Reading 1: 20 °C -> HIGH
Reading 2: 25 °C -> HIGH
Reading 3: 32 °C -> CRITICALLY HIGH
Reading 4: 34 °C -> CRITICALLY HIGH
Reading 5: 17 °C -> LOW
Reading 6: 27 °C -> HIGH
Reading 7: 34 °C -> CRITICALLY HIGH

Enter "1" to return to the main menu or "2" to exit: 1

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 4

SUMMARY REPORT:
----------------
Total readings: 7
Average room temperature: 27.00 °C
Highest room temperature: 34 °C
Lowest room temperature: 17 °C

NORMAL   : 3 (42.86%)
WARNING  : 3 (42.86%)
CRITICAL : 1 (14.29%)

Overall Status: ATTENTION REQUIRED

Enter "1" to return to the main menu or "2" to exit: 1

SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 5
Thank you for using the Device Monitoring System.
```

## Test Cases
I performed 10 tests. __ passed and __ failed.
Full details are in test_cases.md.

## Known Limitations
One bug found during testing was that entering an invalid input instead of "1" to return to the main menu or "2" to quit would automatically bring the user back to the main menu. The program should validate the input and display an error message when an invalid option is entered.

## Reflection
Making this project made me realize how complex coding in Python can be. I discovered new variables, functions, and other concepts that can help make my code shorter and more organized. The hardest part of creating this program was figuring out how to return the user to the main menu after entering a number. It took me a while to understand how to make it work properly.

One of the bugs I encountered was in the last part of the code:

```python
if __name__ == "__main__":
    while True:
        main_menu()
```

It kept showing an error saying that `"__main__"` was not defined, even though the code was already written correctly. After checking the code, I realized that the problem was caused by incorrect indentation.

Lastly, I will continue improving my Python coding skills to make my programs more organized, shorter, and easier to understand.

```text
python device_monitor.py