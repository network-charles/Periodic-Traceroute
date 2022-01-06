# Subprocess makes it possible to run other languages inside a Python script.
import subprocess

# A mini python program is defined, so that it runs only when you call it.
def pinger():
    # The batch script file is called from the folder it was saved in my PC.
    subprocess.call([r'C:\Users\Admin\Documents\Project\Traceroutes\tracer.bat'])

# Here I try to run the code three times using a "for loop" concept.
for number_of_runs in range(3):
    # Here I specify that when the batchh script runs the first time, it shows an 
    # an output specifying the first one has ran successfully, etc.
    if number_of_runs == 0:
        pinger()
        print('First Traceroute has been completed')
    if number_of_runs == 1:
        pinger()
        print('Second Traceroute has been completed')
    if number_of_runs == 2:
        pinger()
        print('Third Traceroute has been completed')
