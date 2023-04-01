# BitCoin CLI

When running Bitcoin core you can run on three different networks:

**Mainnet**: This is THE Bitcoin network. Transactions on this network have real value. Testing any applications here is highly risky. 

**Testnet**: This is a separate, much smaller network, designed specifically for testing. Transactions on this network exchange testnet coins. You can acquire testnet bitcoins at a testnet faucet such as https://testnet-faucet.mempool.co/. Testnet coins, by design, have no monetary value. They are simply exchanged between developers who are testing Bitcoin applications. 

**Regtest**: This is an entirely local network. You could create a regtest network in your home for you and your roommates. Or set one up at the office, etc. It does not link to mainnet or testnet in any way. It is your own private Bitcoin network.

## Links

* [RPC CALL CLI CMDS : https://www.blockmeadow.com/complete-bitcoin-rpc-calls-list-with-examples/](https://www.blockmeadow.com/complete-bitcoin-rpc-calls-list-with-examples/)

* [BITCOIN CLI QUERIES : https://chainquery.com/bitcoin-cli](https://chainquery.com/bitcoin-cli)

* [BITCOIN CLI SANDBOX : https://bitcoindev.network/bitcoin-cli-sandbox/](https://bitcoindev.network/bitcoin-cli-sandbox/)

## Commands

1. `bitcoind --daemon`

```sh
Bitcoin Core starting
```

2. `bitcoin-cli -getinfo`

```sh
Chain: main
Blocks: 0
Headers: 0
Verification progress: ▒░░░░░░░░░░░░░░░░░░░░ 0.0000%
Difficulty: 1

Network: in 0, out 7, total 7
Version: 240001
Time offset (s): 0
Proxies: n/a
Min tx relay fee rate (BTC/kvB): 0.00001000

Warnings: (none)
```

3. `bitcoin-cli createwallet "test_wallet_cs120"`

```sh
{
  "name": "test_wallet_cs120",
  "warning": ""
}
```

4. `bitcoin-cli getnewaddress`

```sh
bc1qs3a6hmpkhc73neskepmrjwtvgpurd7hrfr7e2x
```

5. `bitcoin-cli getblockcount`

```sh
0
```

6. `bitcoin-cli getrpcinfo`

```sh
{
  "active_commands": [
    {
      "method": "getrpcinfo",
      "duration": 64
    }
  ],
  "logpath": "/Users/family/Library/Application Support/Bitcoin/debug.log"
}
```

7. `bitcoin-cli -regtest generatetoaddress 10 "bc1qs3a6hmpkhc73neskepmrjwtvgpurd7hrfr7e2x"`


```sh
# To add some data to our blockchain we'll need to mine some blocks, which gives us a mining reward. Run the below command to generate 10 new blocks.
```

8. `bitcoin-cli -generate 101`


```sh
{
  "address": "bc1qnf0vzxy6jd40wsesmsmf3dkd8hs4luln99w4u9",
  "blocks": null
}
```

9. `bitcoin-cli getblock [block hash]<string>`

Get the info for particular hash

10. `bitcoin-cli gettransaction [transaction ID]<string>`