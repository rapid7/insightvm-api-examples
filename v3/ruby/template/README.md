**Script name** : ruby-v3-template.rb

**Description**: This is a template file intended to get users new to writing ruby a starting point.  In words, the template can be used to start building a script to interact with the insightvm api-v3.  The script is broken up into 4 sections
     1 required gems. In ruby, gems are re-usable bits of code that can be used in multiple projects.
		httparty - used to send put/post/put requests to the api
		json - used to manipulate data that is in json format - needed as mainly post or put requests will have data that may require to be in json format.
		highline - useful set of tools to accept user input into your script.  Mainly used here to mask the user password when it prompts the user.


     2 Variables - There are two variables that user is required to modify.  default_name and default_con - default_name is the username of the id that is used to login and access the api.  The default_con is the hostname or ip address of the InsightVM console.

     3  prompts for additional information - this section just echos out questions for the user to respond to - the script collects those responses and assigns them to variable to be used later in the script.

     4 Final section which is performing a get request against api/3/sites. and assigning the results to the variable called response.  This is just a simple example, the actual code for the script being built would go here.  All scripts will need to have console/user/password information so makes sense to have it in a template.

**Usage**
Make a copy of the template - call it testfile.rb
Edit testfile.rb, and set the default_name to the user being used to login to the console and access the api.
Set default_con to the console IP address.
Under the comment that says Put your code here - just print out the response variable, with this line.
     puts response
Set execute permissions to testfile.rb
     chmod 700 testfile.rb
     ./testfile.rb
Script will prompt you for console IP, user id and password... apply appropriately and script will output contents of api/3/sites endpoint.
