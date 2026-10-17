# Test Cases – Simulated Device Monitoring and Alert System
 
Tested by: Kevin Roy S. Rodriguez        Date: October 17, 2026
 
| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Five readings were displayed correctly: 28, 31, 35, 37, 29 | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | Reading 33 °C was added successfully | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | Invalid input was rejected and the list remained unchanged | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | Invalid negative reading was rejected and the list remained unchanged | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | Invalid high reading was rejected and the list remained unchanged | Pass |
| TC06 | Add 30, then choose 3 | 30 °C is classified as WARNING | 30 °C was classified as WARNING | Pass |
| TC07 | Add 35, then choose 3 | 35 °C is classified as WARNING | 35 °C was classified as WARNING | Pass |
| TC08 | Choose 4 | Summary displays total, average, highest, lowest, category counts, percentages, and overall status | Summary report displayed all required information correctly | Pass |
| TC09 | Enter 9 in the main menu | Invalid choice message displayed; menu appears again | Invalid choice message was displayed and the main menu appeared again | Pass |
| TC10 | Choose 5 | Exit message displayed and program ends | Exit message was displayed and the program ended | Pass |
 
## Bugs Found and Fixed

One bug I found was that the program could not handle invalid inputs like abc. It would show an error because the input was directly converted into an integer. I fixed it by adding input validation so invalid entries are rejected.