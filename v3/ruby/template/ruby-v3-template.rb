#!/usr/bin/env ruby
#
require 'httparty'
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

url = "https://#{nxconsole}:3780/api/3/sites"
auth = {:username => user, :password => pass}
response = HTTParty.get(url,:basic_auth => auth,:verify => false)
#parsed = JSON.parse(response.read_body)

# Put your code here
