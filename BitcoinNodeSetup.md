# Bitcoin Node Setup

```sh
mkdir .bitcoin
touch .bitcoin/bitcoin.conf
cd .bitcoin
vim bitcoin.conf
```

**`bitcoin.conf`**

```sh
# Run Bitcoin as in daemon mode without an interactive shell
daemon=1
# Tell Bitcoin where to put blockchain data
datadir=/path_to_folder_having_.bitcoin_dir/.bitcoin/data
# Tell Bitcoin to run on a regtest network
regtest=1
# Set the RPC password
rpcauth=mysupersecurepassword
# Turn on the RPC server
server=1
# Turn on ZMQ publishing
zmqpubrawblock=tcp://127.0.0.1:28332
zmqpubrawtx=tcp://127.0.0.1:28333
```

### Starting

```sh
bitcoind
bitcoin-cli -getinfo

----O/P----

{
"version": 210100,
"blocks": 0,
"headers": 0,
"verificationprogress": 1,
"timeoffset": 0,
"connections": {
		"in": 0,
	"out": 0,
	"total": 0
},
"proxy": "",
"difficulty": 4.656542373906925e-10,
"chain": "regtest",
"relayfee": 0.00001000,
"warnings": ""

}
```