# Example Ruby code for API v3 InsightVM

## Overview
This directory contains example Ruby scripts that use apiV3 of InsightVM.  The intent of these scripts are to provide a starting point of code to illustrate how to code to the api.
These are working scripts, however most would need modifications to fit a specific need.
A template script is also provided that can be used as a starting point for writing any ruby api script to interact with InsightVm.  The template is one way to complete authentication into the console.
The template uses the following gems
httparty - used to make post/get/push calls within the api
json - used to manage/parse the data in json format.
highline - used to take user input, as the template script asks for console, user and password information.  This gem allows the ability to mask the password and not print it to the screen.

In order to use the template, the following variables will need to be set to match your insightvm environment:  
&emsp;&emsp;default_name : user name that is used by the script to log into the console.  
&emsp;&emsp;default_con  : hostname or ip address of your InsightVM console.  

The template simply logs into the console, and retrieves the information from the api/3/sites endpoint and stores it in a variable called parsed.  If you want to see the results, just add a print statement
to the bottom of the script ( puts parsed )


Additional sub directories contain script examples and documentation.
