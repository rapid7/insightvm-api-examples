# Example python code for apiV3 InsightVM

## Overview
This directory contains example python scripts that use apiV3 of Insightvm.  The intent of these scripts are to provide a starting point of code to illustrate how to code to the api.
These are working scripts, however most would need modifications to fit a specific need.
A template script is also provided that can be used as a starting point for writing any python api script to interact with InsightVm.  The template is one way to complete authentication into the console.

In order to use the template, the following variables will need to be set to match your insightvm environment:  
&emsp;&emsp;CONSOLE_URL : hostname or ip address of your InsightVM console.  
&emsp;&emsp;CONSOLE_USER : user name that is used by the script to log into the console.   
&emsp;&emsp;CONSOLE_PASS : password of the console user you are trying to authenticate with.

The template simply performs a get request to the console using the host and credentials provided, and retrieves the information from the api/3/sites endpoint and prints the results to the screen.


Additional sub directories contain script examples and documentation.
