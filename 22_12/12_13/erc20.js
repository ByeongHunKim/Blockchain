const Web3 = require('web3')

const Web3js = new Web3(new Web3.providers.HttpProvider("https://goerli.infura.io/v3/"))

const privateKey = "" // Your address's private key


let tokenAddress = '' //  Token contract address

let toAddress = ''// where to send it

let fromAddress = ''// Your address

let contractABI = 

let contract = new Web3js.eth.Contract(contractABI, tokenAddress, { from: fromAddress })

let amount = Web3js.utils.toHex(Web3js.utils.toWei("10")); // 10 DEMO Token

let data = contract.methods.transfer(toAddress, amount).encodeABI()

console.log(data);

sendErcToken()

function sendErcToken() {

   let txObj = {

       gas: Web3js.utils.toHex(100000), // gas fee 계산하는 거 advanced

       "to": tokenAddress,

       "value": "0x00",

       "data": data,

       "from": fromAddress

   }

   Web3js.eth.accounts.signTransaction(txObj, privateKey, (err, signedTx) => {

       if (err) {

           return callback(err)

       } else {

           console.log("signedTx :", signedTx)

           return Web3js.eth.sendSignedTransaction(signedTx.rawTransaction, (err, res) => {

               if (err) {

                   console.log(err)

               } else {

                   console.log("res: ", res)
                   return Web3js.eth.getTransactionReceipt(res)
               }

           })

       }

   })

}