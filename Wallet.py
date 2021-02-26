import subprocess
import json
import os

from bit import wif_to_key, PrivateKeyTestnet
from web3 import Account, Web3
from bit.network import NetworkAPI
# from eth_account import Account
from constants import BTC, ETH, BTCTEST
from pprint import pprint
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER", "http://127.0.0.1:8545")))

mnemonic = os.getenv('MNEMONIC') #, 'inhale angle inner tiny enlist trial heavy gospel submit any tornado evil')

def derive_wallets(coin, mnemonic):
    command = f'php hd-wallet-derive.php -g --mnemonic={mnemonic} --cols=path,address,privkey,pubkey --coin={coin} --format=json --numderive=3'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)

    return keys

coins = {"ETH":derive_wallets(ETH, mnemonic), "BTCTEST":derive_wallets(BTCTEST, mnemonic)}
pprint(coins)

def priv_key_to_account(coin, priv_key):
    # Account.privateKeyToAccount(priv_key)
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

def create_tx(coin, account, to, amount):
    # This will create the raw, unsigned transaction that contains all metadata needed to transact
    # Parameters are coin -- the coin type (defined in constants.py), account -- the account object from priv_key_to_account, to -- the recipient address and amount -- the amount of the coin to send
    if coin == ETH:
        value = w3.toWei(amount, "ether")
        gas = w3.eth.estimateGas({"to": to, "from": account.address, "amount": value})
        gasPrice = w3.eth.generateGasPrice()
        nonce = w3.eth.getTransactionCount(account.address)
        chainID = w3.net.chainId
        return {"to": to,
                "from": account.address,
                "value": value,
                "gas": gas,
                "gasPrice": gasPrice,
                "nonce": nonce,
                "chainID": chainID}
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address,[(to, amount, BTC)])

# create a function to hold Ethereum
eth_acc = priv_key_to_account(ETH, derive_wallets(ETH, mnemonic)[0]['privkey'])

def send_tx(coin, account, to, amount):
    # This will call create_tx, sign the transaction, then send it to the designated network
    # Parameters are coin -- the coin type (defined in constants.py), account -- the account object from priv_key_to_account, to -- the recipient address and amount -- the amount of the coin to send

    if coin == ETH:
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    if coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed = account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signed)

# ## BTCTEST Transactions

btc_PrivateKey = coins['BTCTEST'][0]['privkey']

btc_acc = priv_key_to_account(BTCTEST, btc_PrivateKey)
print(btc_acc)


# create BTC transaction
create_tx(BTCTEST, btc_acc, "mmUQuAvBYqVpKzayhaYvnJe9VuwkRdSWPu", '0.00001')

# Send BTC transaction
send_tx(BTCTEST, btc_acc, "mmUQuAvBYqVpKzayhaYvnJe9VuwkRdSWPu", '0.00001')

# ## ETH Transactions

# connecting to HTTP with address pk

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545/0x9f7df41ca30f39bbb75e2f660139d605a891dab2a0cc90d1c75b20c8e6ada021"))

# double check if  I am connected to blockchain.
w3.isConnected()

# ## Check the Balance of the account with local mining blockchain

w3.eth.getBalance("0x882FB0E63Ce059787243482eF9107564715Fd7F6")

create_tx(ETH, eth_acc, "0xE49E3220EdD764a3187D6698CBCeE8AFEBfD63Ac", 1000)

send_txn(ETH, eth_acc, "0x55D8A1Dbc5b3a4Ad9eAAD0d49466491d6D234cf2", 1000)

# ## Confirmation of

w3.eth.getBalance("0x55D8A1Dbc5b3a4Ad9eAAD0d49466491d6D234cf2")