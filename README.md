<h1>File Integrity Monitor</h1>

<h2>Description</h2>
This project consists of a simple python script that acts as a file integrity monitor (FIM). First, the user will use the utility to create a baseline hash of the file they want to monitor. Next, the script allows the user to check the integrity of files they've previously made a baseline hash for. Based on the output of the script, the user will be able to determine if a file has been modified or tampered with. 
<br>


<h2>Languages and Environments Used</h2>

- <b>Languages: Python</b> 
- <b>Libraries: Hashlib, os</b>
- <b>Environment: Linux, Bash</b>

<h2>Project Walk-Through:</h2>

<p align="center">

<h3>How It Works:</h3>
<br />

- <b>Baseline Creation:</b> The script takes a file, runs it through the SHA-256 algorithm, and saves a unique fingerprint (hash) of the file at the time of creation. <br />
- <b>Integrity Check:</b> Later, the script recalculates the hash and compares it to the saved baseline to find changes.<br/>  
<br />

1. I wrote the script using Python3 and VSCode:<br />
[Python Script](https://github.com/cai-spice/Python-Based-FIM/blob/d77886c845f395334806c3a093249c6eabf9e629/fim.py)

2. I created a new file to use with the script: <br/>
<img src="https://i.imgur.com/pwATeg8.png" height="80%" width="80%" alt="FIM"/>
<img src="https://i.imgur.com/eiUovgl.png" height="80%" width="80%" alt="FIM"/>
<br />
<br />
3. I used the script to easily create a baseline hash and the script automatically made the baseline hash file:  <br />
<img src="https://i.imgur.com/VMzwNgd.png" height="80%" width="80%" alt="FIM"/>
<img src="https://i.imgur.com/KaijIUm.png" height="80%" width="80%" alt="FIM"/>
<br />
<br />
4. Then, I verified the integrity of the file (before making edits) to test the scripts functionality: <br />
<img src="https://i.imgur.com/VMzwNgd.png" height="80%" width="80%" alt="FIM"/>
<br />
<br />
5. Next, I appended a period (".") to the original file to test the script's functionality:  <br />
<img src="https://i.imgur.com/JYbyvjs.png" height="80%" width="80%" alt="FIM"/>
<img src="https://i.imgur.com/K9zz1pc.png" height="80%" width="80%" alt="FIM"/>
<br />

</p>
