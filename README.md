# dk-weather
A Python CLI to fetch values of popular cryptocurrencies in real-time.

This program uses the free and public [Nomics Cryptocurrency and Bitcoin API.](https://p.nomics.com/cryptocurrency-bitcoin-api)

Currently, Nomics only supports returning data in USD. (Sorry!)

# How to run on your machine:
After cloning this repo to your machine, you'll first need to do two things:

1) Get your own free [API key to the Nomics Cryptocurrency and Bitcoin API](https://p.nomics.com/cryptocurrency-bitcoin-api) here, and then,
2) Make a copy of `config.example.py` named `config.py`, and replace the dummy string with your API key. This will allow the program to fetch real-time crypto data straight from your command line!

Then just navigate to the root directory and run `python dk-weather.py`!
