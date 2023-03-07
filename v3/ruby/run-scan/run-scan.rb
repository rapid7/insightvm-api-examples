#!/usr/bin/env ruby
#
#  Description: Script that uses the Nexpose APIv3 to launch a scan of a specified scan id

require 'time'
require 'highline/import'
require 'httparty'
require 'json'

# Defaults: Change to suit your environment.
default_host = '<console_ip_address>'
default_name = 'username'
default_siteId = '5'
day = Time.now.strftime("%A").downcase

#Prompts to collect nexpose console and login information
host = ask('Enter the server name (host) for Nexpose: ') { |q| q.default = default_host }
user = ask('Enter your username:  ') { |q| q.default = default_name }
pass = ask('Enter your password:  ') { |q| q.echo = '*' }
siteId = ask('Enter the site id:  ') { |q| q.default = default_siteId }

#Methods
def runScan(host,user,pass,scanid)
   cmd = "{
            \"engineId\": \"37\",
            \"hosts\": [ \"IP range\" ],
            \"name\": \"testscan\",
            \"templateId\": \"fastdisco\"
         }"
   url = "https://#{host}:3780/api/3/sites/#{scanid}/scans"
   auth = {:username => user, :password => pass,:verify => false}

   options = { :basic_auth => auth,
            :headers => { 'Content-Type' => 'application/json'},
            :verify => false,
            :timeout => 900
          }
   results = HTTParty.post(url, options)
   parsed = JSON.parse(results.read_body)
   return parsed["id"]

end

def checkRunning(host,user,pass,sid)
   url = "https://#{host}:3780/api/3/scans/#{sid}"
   auth = {:username => user, :password => pass,:verify => false}
   response = HTTParty.get(url,:basic_auth => auth,:verify => false)
   parsed = JSON.parse(response.read_body)
   return parsed["status"]
end

#Main
puts "Day is #{day}"
sid = runScan(host,user,pass,siteId)
status = checkRunning(host,user,pass,sid)
puts "The scan id is #{sid} and its status is #{status}"
