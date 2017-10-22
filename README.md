# MiniURL

A web service to make short URLs. It is built with flask to handle web requests and redis to store the generated short versions of the URLs. The app includes tests.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install flask, redis and other packages included in the ```requirements.txt``` file.

### Installing

A step by step series of examples that tell you have to get a development env running

First lets build the virtual environment:

```
virtualenv miniurl && cd miniurl
```

Lets activate it:

```
source miniurl/bin/activate
```

Clone the repo:

```
git clone https://github.com/jkklapp/miniurl
```

Now install the dependecies

```
pip install requirements.txt
```

And run the server:

```
python server.py
```

## Running the tests

The tests are written using ```unittest```. To run them:

```
python server_test.py
```

## Deployment

To deploy the app in production a redis cluster will be needed, and appropriate config added, for instance in ```settings/prod.py```.

Once the config file has been properly edited the environment variable ```MINIURL_SETTINGS``` must point to the settings file.

```export MINIURL_SETTINGS=settings/prod.py```
