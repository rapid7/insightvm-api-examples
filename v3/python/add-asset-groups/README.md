**Script name**: add-asset-groups.py

**Description**: Example python script that creates a Dynamic Asset Group based off the search criteria provided. No error checking is done - if the asset group name already exists, this script will error so ensure the asset group name is unique and not in use. 

The script also hard codes the search criteria filters, creating an asset group with any assets having a risk score greater than 25,000.  This was intentional due the the potential complexity of the filters.  It would be difficult to create a column that contained all of the information required for a complex search filter.  However, this script could be improved upon to add additional functionality in the future using variations of the search criteria located at https://help.rapid7.com/insightvm/en-us/api/index.html#section/Responses/SearchCriteria

**Instructions**:
Place the script in a directory on a system with python3 installed.  The following modules are used and will need to be added to the system if not already installed :

 'json'<br>
 'getpass'<br>
 'requests'<br>
 'urllib3'<br>

Set execute permissions on the python script.<br>
chmod 700 add-asset-groups.py<br>
Run the script<br>

> ./add-asset-groups.py<br>
> Enter the server name (host) for InsightVM:  |<console_hostname_or_IP_address>|<br>
> Enter your username:  |<username>|<br>
> Enter your password:  *********<br>


The script will print out the following message:
Asset Group 79 created and can be found at https://<console_host>:3780/group.jsp?groupid=79
