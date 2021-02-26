# Homework_19

# Multi-Blockchain Wallet in Python

![newtons-coin-cradle](https://user-images.githubusercontent.com/70610967/109235741-1a43bc80-7783-11eb-9ea3-46a40e21c4a7.jpg)

## Background and Wallet Description 

The command line tool, `hd-wallet-derive`, is a Pythin tool for managing multiple type of currencies in one wallet that supports not only BIP32, BIP39 and BIP44, but alis "universal" wallet and can manage billions of addresses across 300+ coins. 

For this homework exercise, I focused on getting 2 coins working: Ethereum and Bitcoin Testnet.


## Wallet.py Code

Created the Wallet.py file to hold the Python code to enable the program to act as my universal wallet script.

First step was to import the Libraries:

![Libraries](https://user-images.githubusercontent.com/70610967/109235894-70186480-7783-11eb-8b33-801660eea5c8.PNG)

Next, the function below calls out the dictionary of coins with addresses and privkeys.

![Derive Wallets](https://user-images.githubusercontent.com/70610967/109236462-8541c300-7784-11eb-9e26-a91efd665793.PNG)

To transfer money from one account to another first you will need to run the 'create_tx" and `send_tx` functions.

![create_tx](https://user-images.githubusercontent.com/70610967/109237352-3ac14600-7786-11eb-8d8f-cd5b046fd2b7.PNG)

![send_tx](https://user-images.githubusercontent.com/70610967/109237439-62181300-7786-11eb-8582-237af4c6e49f.PNG)


Given the difficulties we had in getting our Ethereum PoA mining to work, I only ran the following function sending BTCTEST from one account to another:

![Create BTC](https://user-images.githubusercontent.com/70610967/109237681-ed91a400-7786-11eb-8837-abd845f300f6.PNG)

The results of sending 0.00001 BTCTEST to mmUQuAvBYqVpKzayhaYvnJe9VuwkRdSWPu were as follows:

![Capture2](https://user-images.githubusercontent.com/70610967/109238269-11a1b500-7788-11eb-9f16-9693b6b352b9.PNG)
