# Hotwallet Check

Checks the OKCash and Marketer's Coop hotwallet balances and then
sweeps if over a certain threshold.

In addition the script needs to send an email to hello@vivaco.in if
the hotwallet is depleted beneath minimum allowable.

# Installation

## Requirements

* Python 2.7
* OKCash wallet
* Market's Cooperative wallet (if possible)

## Actions

    shell> pip install -r requirements.txt

## Configuration

Edit config.ini

# Usage

1. Invoke OKCash via:

    shell> OKCash -server -rpcuser=uname -rpcpassword=passwd

2. Run scanbalance

    shell> python scanbalance.py config.ini okcash

## Execution screenshots

* [bringing up OKCash wallet](http://prntscr.com/f58qv8)
* [checking the balance](http://prntscr.com/f58roa) against too low a balance
