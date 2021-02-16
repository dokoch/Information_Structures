# Getting Setup to use SAS/Python


## Introduction
These instructions are for Lipscomb University students who are enrolled in **Information Structures (MSDS5023/DS3223)** and our **SAS/Python Bootcamp**. The goal is to get your Python environment configured and ready for use with your **SAS OnDemand for Academics** cloud instance.

---

## Optional - Install Sublime Text
You will need to edit text files to complete these steps.  If you are using Windows 10, Notepad works just fine.  However, if you are using macOS the default TextEdit app causes some difficulties. 

[Sublime Text](https://www.sublimetext.com/) is a popular and easy to use editor that does a good job working with Python code as well as plain text. It's free, easy to install and to use.

---

## Python Setup
We strongly recommend Anaconda to manage your Python environment.  It is based on Jupyter Notebooks and the Conda package manager which have become standards for Data Science.  If you have a Python setup that you are happy with, you are welcome to complete the course using your setup.

1. [Download Anaconda](https://www.anaconda.com/products/individual#Downloads) for your OS (Windows 10, macOS or Linux).
1. Run the installer to complete the installation of Anaconda.
1. Launch Anaconda and click the JupyterLab tile to launch JupyterLab in your browser.

---

## Java Setup
The SAS Python library, SASPy, requires Java JRE to be installed on your machine.

1. [Download Java Installer](https://java.com/) for your OS (Windows 10, macOS or Linux).
1. Run the installer to complete the installation. 
1. You will need the path to the java executable for creating your **sascfg_personal.py** in a later step.\
Typical locations are:
    * **On macOS:** ```/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/bin/java```
    * **On Windows 10:** ```C:\Program Files (x86)\Common Files\Oracle\Java\javapath\java.exe```
    * **On Linux:** ```/usr/bin/java```
1. Open a terminal or Command window and copy/paste the above full path at the command prompt and hit enter.  If you get the usage output from java, then your java is working correctly.

---

## SASpy Installation

1. You should have already received instructions to register for a **SAS OnDemand for Analytics (ODA)** cloud account.
    * As a reminder, the instructions can be found [at this link]( https://support.sas.com/ondemand/steps.html).
    * Verify that you can log into [ODA](https://welcome.oda.sas.com/login) and launch **SAS® Studio**
    * You will use your SAS userid and password for subsequent steps.
1. Install the SAS Python library (aka [SASPy](https://pypi.org/project/saspy/)).
    * From within JupyterLab select "File"->"New"->"Terminal" to launch a new shell
    * Execute the following commands from the shell command line:\
    ```conda install saspy```

---
## SASpy Configuration

1. Configure SASpy to connect to your **ODA** cloud account.

   * Closely follow the instructions at [SASPy access to SAS® hosted servers](https://support.sas.com/ondemand/saspy.html) to configure your Python environment to access the **ODA** server.
   
   * You will be creating two files on your PC. These files allow you to connect to **ODA** and to authenticate to the server.
     * *sascfg_personal.py*
     * *_authinfo* on Windows
     * *.authinfo* on macOS
   
1. Test access to **ODA** from JupyterLab.
    1. Download the Jupyter notebook **Testing_SAS_Python_Connection.ipynb** from this GitHub project or using [this Google Drive share](https://drive.google.com/file/d/1pNoSsM7ieinjvWTjNkzWRbyZMkIZ8Tpt/view?usp=sharing). 
    1. Open the notebook with JupyterLab and follow the instructions for completing the test.

---

## If You Have Problems
1. Double check that you have accurately followed the instructions provided.
1. **Please don't hesitate** to send me an email or call my cell if you get stuck and I will be happy to assist.

*I love feedback!*  All comments toward improving this document are welcome.  

**Don Koch** - <dokoch@lipscomb.edu> - 919-649-0447

---
## Recommended Reading
---

### [Python for Data Analysis](https://www.oreilly.com/library/view/python-for-data/9781491957653/)
I highly recommend this book for getting started with data science using Python and as a general reference.  Wes McKinney is one of the original developers of the Python Pandas library.

![Book Cover](https://learning.oreilly.com/library/cover/9781491957653/250w/)

---

## [Python 3 Cheat Sheet](https://perso.limsi.fr/pointal/doku.php?id=python:memento&rev=1596204960) 

This is one of my favorites cheat sheets. It's crammed full of Python syntax and basic usage. 

[PDF Download](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)

![Cheat Sheet](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.png)

---




