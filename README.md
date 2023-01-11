# TooGoodToGo-Notifier

This tool allows you to monitor your favorite TooGoodToGo stores and get notified when they have new products available.

## Summary

1. [Installation](#installation)
2. [What is TooGoodToGo?](#what-is-toogoodtogo)
3. [What is this tool for?](#what-is-this-tool-for)

## Installation

**1.** Clone this repository
```
git clone https://github.com/Log-s/TooGoodToGo-Notifier.git
```

**2.** Install the dependency
```
pip3 install tgtg
```

**3.** Get auth tokens
```python
# Run the following in a python interpreter
from tgtg import TgtgClient
client = TgtgClient(email="<your email>")
client.get_credentials()

# You'll have to open the e-mail you received on your computer
# and not your smartphone
# /!\ This is important
```

**4.** Download the `ntfy` app, and subscribe to a subject. The string you choose for your subject must be unique so strangers can't subscribe to your feed. A random string will to the job.

**5.** Fill the `config.json` file with the data from steps 3 and 4 (leave the `available` field empty).

**6.** Setup the cronjob (`crontab -e`)
```bash
* * * * * python3 /opt/TooGoodToGo-Notifier/tooGoodToGo.py
```
*In the example above you cloned the repo in the `/opt` directory.*

## What is TooGoodToGo?

TooGoodToGo is an app that allows you to buy food that would otherwise be thrown away. It's a great way to save money and help the environment.

## What is this tool for?

In the app, you can select favourite stores, that you can easily check for new items. However, you can't get notified when new items are available. This tool allows you to do that, and avoid refreshing the app all the time.

Other **free** tools exist, but notification where sent through a telegram bot, that has to be setup first. I made myself this tool for simplity.