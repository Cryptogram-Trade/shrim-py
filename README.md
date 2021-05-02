# Shrim.py, the Better Shrimpy Python API

This API connect to [Shrimpy Developers API](https://developers.shrimpy.io/) in a more flexible way than [the official API](https://github.com/shrimpy-dev/shrimpy-python).

It also covers a [Shrimpy Users API](https://www.shrimpy.io/docs/) that wasn't available until now.

Signature headers and hashing are fully covered, no hassle.


## Benefits Over the Official Shrimpy Python Lib

This Shrimpy library has the following features:
- Connect to the User API in order to drive your Shrimpy account and portfolios
- Tested (yes, Shrimpy official is totally untested ¯\_(ツ)_/¯)
- Access all endpoints explicitely as documented. eg: `client.get("/list_exchanges")` instead of searching for corresponding method when they exist
- Access latest endpoints with the current lib version, not need to upgrade and get the corresponding method


## Installation

You probably [want a virtualenv](https://docs.python.org/3/library/venv.html) first, then:

```
pip install shrim-py
```

## Usage

This API allows you to connect to the [Shrimpy Developers API](https://developers.shrimpy.io/docs/) or the [Shrimpy User API](https://www.shrimpy.io/docs).

```python
from shrimpy import ShrimpyDevClient

client = ShrimpyDevClient("myapikey", "myapisecret")
client.get("/list_exchanges")
```

if you want to connect to the Shrimpy User API instead just import and use `ShrimpyUserClient` instead:

```python
from shrimpy import ShrimpyUserClient

client = ShrimpyUserClient("myapikey", "myapisecret")
client.get("/binance/ticker")
```

## Shrimpy Client Methods

when creating a `client` you can then call the following methods: `get`, `post` and `delete`.

#### Retrieve a Resource

```
client.get(endpoint)
```

#### Create a Resource
```
client.post(endpoint)
```

#### Delete a Resource

```
client.delete(endpoint)
```

There's no other method used in Shrimpy. However if you needed to manually call an endpoint with a different method you could shortcut using `client.call(method, endpoint)`.


## List of Endpoints

The full list of endpoints **for the User API** for accessing public resources, account, portfolios and data types is available on the official doc: https://www.shrimpy.io/docs

With the **Developers API** endpoint you can manage public, trading, historical, user info, management and analytics data: https://developers.shrimpy.io/docs
