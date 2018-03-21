# CryptoDonationCheckMuhely
Check incoming cryptocurrency transfers to Donate To addresses, for Blockchain Atelier, Budapest

Blokklánc Műhely   https://blokklancmuhely.club/

# Usage and Configuration
This is written in Python, so a python environment is needed.
There is no support to run in background or on a remote server, that is not the point of the exercise.

## Configuration
The config.json file has to set up with a few parameters:
- btc_address: The BTC address to watch (can be empty).  Pre-populated.
- eth_address: The ETH address to watch (can be empty).  Pre-populated.
- checkPeriodMins: the numberof minutes to wait between checks.
- to_addr: The email address to send mails to
- from_addr:  The sender email address, pre-populated.
- etherscan_apiKeyToken: API token for etherscan service (must register).  Pre-populated.
- smtp_server: SMTP server to use for sending.
- smtp_port: Port used for SMTP sending.
- smtp_user: Optional username for SMTP server.
- smtp_pass: Optional password for SMTP server.

## Running
The checker has to be started like this:
```
python3 DonationCheck.py 
```
It runs indefinitely, it can be stopped by Ctrl-C.


# Approaches
1. Run (full) nodes locally, and interface with them.
1.a. Interface through APIs of the nodes, if available
1.b. Extend the code of the nodes with relevant interfaces
1.c. Extract info from local data files ofthe nodes
1.d. Interface with command-line tools of the nodes

2. Interface with nodes ran by someone else, through some API

3. Use API service of available blockchain explorer sites

I have chosen 3. for simplicity and fast prototyping.

