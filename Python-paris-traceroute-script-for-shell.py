# Subprocess makes it possible to run other languages inside a Python script.
import subprocess

# A mini python program is defined, so that it runs only when you call it.
def pinger():
    # The batch script file is called from the folder it was saved in my PC.
    subprocess.call([r'sh', './shell.sh'])

# Here I try to run the code three times using a "for loop" concept.
for number_of_runs in range(3):
    # Here I specify that when the batchh script runs the first time, it shows an 
    # an output specifying the first one has ran successfully, etc.
    if number_of_runs == 0:
        pinger()
        print('First Paris Traceroute has been completed')
    elif number_of_runs == 1:
        pinger()
        print('Second Paris Traceroute has been completed')
    elif number_of_runs == 2:
        pinger()
        print('Third Paris Traceroute has been completed')
    elif number_of_runs == 3:
        pinger()
        print('Fourth Paris Traceroute has been completed')
    elif number_of_runs == 4:
        pinger()
        print('Fifth Paris Traceroute has been completed')
    elif number_of_runs == 5:
        pinger()
        print('Sixth Paris Traceroute has been completed')
    elif number_of_runs == 6:
        pinger()
        print('Seventh Paris Traceroute has been completed')
    elif number_of_runs == 7:
        pinger()
        print('Eight Paris Traceroute has been completed')
    elif number_of_runs == 8:
        pinger()
        print('Nineth Paris Traceroute has been completed')
    