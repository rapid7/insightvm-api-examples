**Script name** : add-asset-groups.rb

**Description**: Example ruby script that reads a csv file containing a list of asset group names and types in two column format.  Script will read through the file (called aglist.txt) and create asset groups of the specified type.  No error checking is done - if the asset group name already exists, this script will error and continue through the rest of the list.  Note that in this repository, the example aglist.txt file contains 2 columns.  The name of the asset group in column 1 and they type of asset group in column 2.  File can be modified to fit the needs of the user.

Script also hard codes the search criteria filters, creating an asset group with any assets having mac in the operating system name.  This was intentional due the the potential complexity of the filters.  It would be difficult to create a column that contained all of the information required for a complex search filter.  However, this script could be improved upon to add additional functionality in the future.

**Instructions**
Place the script and aglist.txt file in a directory on a system with ruby installed.  The following gems are used and will need to be added to the system if not already installed :

 'httparty'
 'csv'
 'json'
 'highline/import'

Set execute permissions on the ruby script.
chmod 700 add-asset-groups.rb
Run the script 

> ./add-asset-groups.rb
> Enter your console IP:  |<console_IP_address>|
> Enter your username:  |username|
>
> Enter your password:  *********
>

 For each line in the txt file, script will print out the following message:

Creating asset group one of type static
{"links"=>
  [{"href"=>"https://<console_IP_address>:3780/api/3/asset_groups", "rel"=>"self"},
   {"href"=>"https://<console_IP_address>:3780/api/3/asset_groups/29",
    "rel"=>"AssetGroup"}],
 "id"=>29}

In words, it created an asset group named one with type static and the asset group id number is 29.
