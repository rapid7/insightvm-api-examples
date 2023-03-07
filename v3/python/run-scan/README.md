# Scan Site Script

## Description

Script name : **run-scan.py**

Script that runs a scan against a specified site id.  In this example, the default site engine and all assets are used in the script - but this could be easily modified to accept that information as input.
This is example code, intended to give user a starting point which they can build off of to fit the need of their environment.
Output shows the scan id that was launched as well as current status of the scan, if all was successful, it should show as running.  Confirmation can be seen from the console user interface - you should see a running scan much like the following picture:

![Running Scan](run-scan-script.png)


## Installation

Copy script out to machine that has python installed and that also has network connectivity to the Nexpose console being queried.


Script uses the following modules, make sure these are installed on the system used to run the script using pip if needed.
     requests
     getpass
     json
     urllib3

## Usage

Script will prompt user for the following information :
     console IP:  enter ip address of Nexpose console
     username:  enter user name used to login to Nexpose console
     password:  enter password of user id of Nexpose console
     site ID:  The site id number that you wish to use for the scan.  Be sure that the scan range is applicable to the site.<br>
To run: python3 ./run-scan.py <br>
Enter the server name (host) for InsightVM: |<console_hostname_or_ip_address>| <br>
Enter your username:  |username| <br>
Enter your password: \*\*\*\*\*\*\*\* <br>
Enter the site ID: |5|

The scan id is 79 and its current status is running.
