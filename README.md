# DOTE3

Parsing data (passed tests) from the training site. After parsing the data, it is possible to sort the data (remove duplicates). Also, after removing duplicates, a JS code for DEV TOOLS is generated.

## Launch

1. install all packages
```bash
pip install -r requirements.txt
```
2. launch main.py
3. Input link to page with test.

[![screen](https://i.postimg.cc/MTX2SVp7/Untitled.png)](https://postimg.cc/VryH9SMv)

4. Select TXT file that contains login and passwors (login1[space]Password1). Each new login and password should start on the new row.
5. Press the start to start parsing data.
5. The progress of this processing shows in dialod window. The dialog box displays the number of correct and incorrect questions. And also the result.

[![screen](https://i.postimg.cc/VLZc9ZgP/photo-2023-02-21-14-07-32.jpg)](https://postimg.cc/fJdFDK18)

6. After parsing is completed, the name of the file where the data is saved is displayed. A button will appear, by clicking on which duplicates will be deleted. 

[![screen](https://i.postimg.cc/RFmzMXw3/1.jpg)](https://postimg.cc/WD5y8mWj)

7. The name of the new file will be displayed (FIX +[NAME OF TEST ].TXT).
A button will appear that copies the JS code to the clipboard, which can be pasted into the browser console at the time of passing the test, in order to automatically fill in the correct answers.

[![screen](https://i.postimg.cc/Jn6gWc8J/end.png)](https://postimg.cc/bDnLxnsN)

Good luck on your exam :)
