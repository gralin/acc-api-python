# Avigilon Control Center API for Python

[![PyPI version](https://img.shields.io/pypi/v/accapi.svg)](https://pypi.org/project/accapi)

## About

This package alows you to communicate with Avigilon Control Center (ACC) API. Please join [Avigilon Technology Partner Program](https://www.avigilon.com/partners/technology-partner-program#become-a-partner) prior to using it in your project. When you become Avigilon partner, in addition to support, you will be receive your unique set of `user_nonce` and `user_key` to be used by your integration. Only with this data will you be able to communicate with the ACC server instance.

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
