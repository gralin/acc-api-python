# Avigilon Control Center API for Python

[![PyPI version](https://img.shields.io/pypi/v/accapi.svg)](https://pypi.org/project/accapi)

## About

This package alows you to communicate with Avigilon Control Center (ACC) API. Before you can start using it, you need to send and email to integrations@avigilon.com and ask for your unique pair of user nonce and user key values. Only having those will you be able to communicate with ACC server instance.

## Features

* Login and get session
* Get camera list

Currently limited functionality is available but it's easy to extend (contributions welcome!)

## Usage

```python
from accapi.client import AccClientFactory

factory = AccClientFactory("user_nonce", "user_key")
client = factory.create("http://acc_address", "username", "password")
cameras = client.get_cameras()
```
