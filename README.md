# Rapid7 InsightVM API Examples

This project seeks to demonstrate proper usage of v3 of the InsightVM REST API via examples and scripts that showcase a variety of endpoints. Included is a complete guide to getting started with the InsightVM API, as well as navigation of documentation, API usage, and configuration. These examples and use cases will either be Python or Ruby-based, with potential for additional language support in the future based on interest.

# Table of Contents

1. Getting Started
2. API Basics
3. Advanced

## Getting Started

### Credentials

The InsightVM v3 API uses basic authentication and requires a local user with permission level global administrator to fully utilize all endpoints.

## API Basics

In simple terms, an API is something that allows applications to communicate with one another. In this case, we'll be communicating with InsightVM via its API to perform basic actions. These actions allow us to automate functionality within InsightVM that would normally be considered manual.

There are several basic API concepts that are applicable to the InsightVM API, as well. It can be beneficial to review these concepts before utilizing the API to gain a better understanding of best practices.

### Methods

Methods are different types of actions that can be performed in the context of an API call. In other words, it determines what operation will be performed upon the specified resource. There are four common API methods that are used in the examples throughout this project.

`GET` - Used for retrieving information, and NOT for modifying it. For example, a call to the Get Sites endpoint would return a list of sites and their associated details from InsightVM.

`POST` - Used to create new resources, based on data the user provides. For example, a `POST` call to the Tags endpoint would result in a new tag being created in InsightVM, based on the data provided.

`PUT` - Used to update an existing resource, based on some identifier that the user provides. For example, a `PUT` call to the Asset Group endpoint requires an asset group ID to be specified, and would result in that asset group being modified based on the data provided.

`DELETE` - Used for deleting resources. For example, a `DELETE` call to the Asset endpoint requires an asset ID and would result in the associated asset being deleted. Use with caution, as it can result in the permanent loss of data.

### Headers

Headers are used in API requests to supply additional information about the API call itself. This can include info relating to authorization, caching, and the type of content being supplied in the call. A couple headers commonly used in InsightVM API requests are for authorization and content-type.

```
headers = {"X-Api-Key": api_key, "Content-Type": "application/json"}
```

### Body

A request body is a list of key-value pairs used to send information when making an API call. A body is typically required with `POST` and `PUT` requests to specify info about the resource that is being created or updated.

An example JSON body typically resembles the following:

```
{
  "name": "Name 1",
  "description": "This is a description.",
  "type": "Type 1"
}
```

The fields before the colon are the keys, while the fields afterwards are the values. The result is the creation or updating of a resource with each field being given its specified value.

The type of data required in the body will vary based on the endpoint being utilized, as there will always be fields that differ between different types of resources.

## Advanced

For more information on advanced API topics, see our InsightVM console Python repository here: https://github.com/rapid7/vm-console-client-python
