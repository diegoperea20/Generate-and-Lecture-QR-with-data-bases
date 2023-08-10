# Generate and Lecture QR with data bases 


<p align="justify">
 Generates QR codes based on user data obtained from a specified API endpoint. It utilizes the requests library to retrieve user names from the API, and the qrcode library to create QR codes for each user. The generated QR code images are saved with the user names as file names ; And capture real-time video from a camera, decode QR codes, and log the scanned data into an Excel file. Each QR code's content, along with the timestamp, is saved in an Excel worksheet.
</p>

<p align="justify">
First users are registered in the database
</p>

<p align="center">
  <img src="README-images\register.PNG" alt="StepLast">
</p>

<p align="justify">
When executing generate_qr.py it does a "Get" to 'http://127.0.0.1:5000/qr' where it goes through the names of 'user' in which each user converts it into qr code.
</p>

<p align="center">
  <img src="README-images\get_qr.PNG" alt="StepLast">
</p>

<p align="center">
  <img src="README-images\users.PNG" alt="StepLast">
</p>

<p align="justify">
In the code "control_gate.py"capture real-time video from a camera, decode QR codes, and log the scanned data into an Excel file. Each QR code's content, along with the timestamp, is saved in an Excel worksheet with columns of 'Name', 'Hour' ,'Minute' and 'Date' . The script also handles the creation of a new Excel file at the beginning of each day to organize the scanned data.
</p>

<p align="center">
  <img src="README-images\detection_qr_gate.PNG" alt="StepLast">
</p>

<p align="center">
  <img src="README-images\excel-save.PNG" alt="StepLast">
</p>
<p align="center">
  <img src="README-images\excel_show.PNG" alt="StepLast">
</p>

---
<p align="justify">
There is also a file called "activate.py" where it activates "control_gate.py" at a specified time and also closes at a specified time (Note that you must have the same dependencies or libraries installed when executing "activate.py").
</p>

## Optional steps to implement

1. Use Dockerfile 
2. Use virtual enviroments and apply  requirements.txt 
```python
#virtual enviroment with conda 
conda create -n my_enviroment python=3.11.4

pip install -r requirements.txt
```