# Emocheck-ReportChecker
This Tool scans the Reports of the EmoChecker.exe and copy/sorts them into an "infected" and a "clear" folder.

This Tool helps you to automatically scan the reports of the EmoChecker.exe by the JPCERT Team (https://github.com/JPCERTCC/EmoCheck)
This Tool creates two folders under the given output path "infected" and "clear" which should say everything, and sorts/copies the reports into.

to use this tool you have the following options:

config.ini:

[Default]
outpath = .\                <-- sets the path to copy the results to.
destpath = C:\Temp\         <-- sets the path to the report files.

Commandline-Parameters:

-d                          <-- sets the path to the report files.
-o                          <-- sets the path to copy the results to.
-dl                         <-- iterates over a list of destinations.
-h                          <-- Displays the help function.

Usage examples:

"python Emocheck_ReportChecker.py -dl C:\Temp\destlist.txt -o C:\Temp\EmocheckResults\"
"python Emocheck_ReportChecker.py -d C:\Temp\ -o C:\Temp\EmocheckResults\"
"python Emocheck_ReportChecker.py" (which will read all from the config.ini)
