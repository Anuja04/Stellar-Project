# Stellar Coding Challenge
Descriription:

Write an API web server that accepts a snippet of text and makes that snippet
available at a URL. Each snippet should be available as text at a URL until it
expires. A snippet's expiry should be extended by 30 seconds each time it is accessed.

The request to store the snippet should accept this information:

| Name       | Description                                      |
|------------|--------------------------------------------------|
| name       | Name of the snippet                              |
| expires_in | Seconds from now until the snippet should expire |
| snippet    | Contents of the snippet                          |

The request to store the snippet should be replied to with a response that
includes the URL where the snippet can be read.

Snippets can be stored in memory, and do not need to be editable after storing.
The solution needs only to be an API, not a graphical or website user
interface.

Snippets should be retrievable by name.This project generates a cumulative vesting schedule from a series of individual vesting events​from a given data file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The project is implemented in python3.8 environment. Working python 3 environment is required to run the code successfully.

## How to run the project

Example:
python3 test_server.py


## For the time being only only part 1 of the project are implemented.

1. At a time server serves only 1 request.
2. Data is stored in memory and single instance of data is stored.
3. Datetime format is default datetime.now()
4. Error handling is not added for now.


## further improvements can be done:
1. Display correct timezone information.
2. Add multiple instances of data.
3. Sever should serve multiple requests.
4. Store data in disk.
5. Add error handling.









