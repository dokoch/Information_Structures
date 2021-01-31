# Getting Setup to Learn Python and SAS/Python


## Introduction
These instructions are for Lipscomb University students who are enrolled in *MSDS5023 Information Structures* and our *SAS/Python Bootcamp*. The goal is to get your Python environment configured and ready for use and to test that you can connect to your SAS cloud instance using Python.

## Python Setup
There are several ways to install Python on your PC.  If you have a Python environment installed that you are happy with, you can use that in this course.  

We will be teaching the Python portions of this course with JupyterLab installed with Anaconda. This is the easiest way to get a very robust Python/R data science environment up and running quickly on your PC.

1. [Download Anaconda](https://www.anaconda.com/products/individual#Downloads) for your OS (Windows 10, macOS or Linux).
1. Run the installer to complete the installation of Anaconda. At the time of this writing, Anaconda installs Python 3.8.
1. Launch Anaconda and click the JupyterLab tile to launch JupyterLab in your browser.
     
## SAS Setup

1. You should have already received instructions to register for a **SAS OnDemand for Analytics (ODA)** cloud account. As a reminder, the instructions can be found [at this link]( https://support.sas.com/ondemand/steps.html). Verify that you can log into **ODA** and launch **SAS® Studio**.

1. Install the SAS Python library, [SASPy](https://pypi.org/project/saspy/).

    From the JupyterLab select "File"->"New Launcher" and select the "Terminal" tile to launch a new shell.  Execute the following commands from the shell command line. 
    
    ```conda install saspy```
        Alternatively, if you are not using Anaconda for your Python environment, you can execute
           
    ```pip install saspy```
        
1. Configure your Python environment to access **ODA**.

   Once you have authenticated to **ODA**, follow the instructions at [SASPy access to SAS® hosted servers](https://support.sas.com/ondemand/saspy.html) to configure your Python environment to access the ODA SAS server.
   
1. Test access to **ODA** from JupyterLab or your Python environment:

    1. Download the Jupyter notebook **Testing_SAS_Python_Connection.ipynb** from this GitHub project or using [this Google Drive share](https://drive.google.com/file/d/1pNoSsM7ieinjvWTjNkzWRbyZMkIZ8Tpt/view?usp=sharing). 
    1. Open the notebook with JupyterLab and follow the instructions for completing the test.
    
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

[PDF Download](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.pdf)

![Cheat Sheet](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3.png)

---



