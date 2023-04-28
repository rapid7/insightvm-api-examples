# Rapid7 InsightVM API Function Examples

This code is meant to be used as a function reference to be imported into your own code and used to reduce the amount of code within your own script. Each of the three functions take in the arguments of `console_url`, `creds`, and `resource`. The `PUT` and `POST` calls additonally call far a `in_payload` variable which would be defined wihtin your script and passed in.



## Getting Started

### Console URL

The console URL is looking for either the console IP or the FQDN of the console server. This is including the port being used. For example if you're using the default port of :3780 then the full value of the console_url variable would be `1.2.3.4:3780` or `example.domain.com:3780`. If you're using a hosted console or have changed the web server port from 3780 to 443 then you would leave off the port and simply use `example.domain.com`.

### Credentials

The InsightVM API (v3) uses basic auth so this script is just looking for the base64 of your `username:password`. This can be changed or handled separately if you intend to pass the whole Basic Auth through from your script. Simply remove the Basic text from the Authorization line within each call.

### Resource

This field refers to the final endpoint you're trying to reach within the call. Examples would be `sites`, `shared_credentials`, `assets`, etcnope