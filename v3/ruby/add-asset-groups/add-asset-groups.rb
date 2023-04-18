#!/usr/bin/env ruby
#
#                  Description : Create asset groups from a list.
#                                Filter is hard coded, but this code 
#                                can be used as a template to build asset groups with various filters.
#                                based on individual needs..
require 'httparty'
require 'csv'
require 'json'
require 'highline/import'

# Defaults: Change to suit your environment.
default_name = 'username'
default_con = '<console_ip_address>'
#
nxconsole = ask('Enter your console IP:  ') { |q| q.default = default_con }
user = ask('Enter your username:  ') { |q| q.default = default_name }
pass = ask('Enter your password:  ') { |q| q.echo = '*' }
#


#Timeout setting below is for submitting commands that run a long time , load content for example
#command will still run but throws a ruby error if the timout is exceeded.

def create_ag(name,type,nxconsole,user,pass)
   cmd = "{
		    \"description\": \"asset group called #{name}\",
		        \"name\": \"#{name}\",
			\"searchCriteria\" : {
 		          \"match\" : \"all\",
		          \"filters\" : [ {
		            \"field\" : \"operating-system\",
		            \"operator\" : \"contains\",
			    \"value\" : \"mac\"
	 } ]
	},
			    \"type\": \"#{type}\"
	
}"
#url = "https://#{nxconsole}:3780/api/3/asset_groups"
auth = {:username => user, :password => pass,:verify => false}
options = { :basic_auth => auth,
	    :headers => { 'Content-Type' => 'application/json'},
	    :verify => false,
	    :timeout => 900,
	    :body =>  cmd
	  }

results = HTTParty.post("https://#{nxconsole}:3780/api/3/asset_groups", options)
parsed = JSON.parse(results.read_body)
return parsed
end
csv_text = File.read("aglist.txt")
csv = CSV.parse(csv_text, :headers => true)
csv.each do |row|
    n = "#{row['AG Name']}"
    t = "#{row['Type']}"
    puts "Creating asset group #{n} of type #{t}"
  res = create_ag(n,t,nxconsole,user,pass)
  pp res
end
