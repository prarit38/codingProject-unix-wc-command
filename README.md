# How to use ccwc command in windows system

1. After cloning the project, activate the virtual environment located in "unixwc/Scripts/activate.bat"
2. Run pip install -e {path to the folder in which ccwc.py is located}
3. Following commands are available as part of the ccwc package:
   * ccwc -c {filapath} -> gives number of bytes in the file
   * ccwc -l {filapath} -> gives number of lines in the file
   * ccwc -w {filapath} -> gives number of words in the file
   * ccwc {filapath} -> gives combination result of -l -w -c in the file
