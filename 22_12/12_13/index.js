const Web3 = require('web3');
const Contract = require('web3-eth-contract');


Contract.setProvider('https://goerli.infura.io/v3/');

// const provider = 'ADD_YOUR_ETHEREUM_NODE_URL';
const provider = 'https://goerli.infura.io/v3/';
const web3Provider = new Web3.providers.HttpProvider(provider);


const web3 = new Web3(web3Provider);

// const contract = web3.eth.contract([
//     {
//         "inputs": [],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "constructor",
//     },
//     {
//         "anonymous": false,
//         "inputs": [
//             {
//                 "indexed": true,
//                 "internalType": "address",
//                 "name": "owner",
//                 "type": "address",
//             },
//             {
//                 "indexed": true,
//                 "internalType": "address",
//                 "name": "spender",
//                 "type": "address",
//             },
//             {
//                 "indexed": false,
//                 "internalType": "uint256",
//                 "name": "value",
//                 "type": "uint256",
//             },
//         ],
//         "name": "Approval",
//         "type": "event",
//     },
//     {
//         "constant": false,
//         "inputs": [
//             {"internalType": "address", "name": "spender", "type": "address"},
//             {"internalType": "uint256", "name": "amount", "type": "uint256"},
//         ],
//         "name": "approve",
//         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "function",
//     },
//     {
//         "constant": false,
//         "inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}],
//         "name": "burn",
//         "outputs": [],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "function",
//     },
//     {
//         "constant": false,
//         "inputs": [
//             {"internalType": "address", "name": "spender", "type": "address"},
//             {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"},
//         ],
//         "name": "decreaseAllowance",
//         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "function",
//     },
//     {
//         "constant": false,
//         "inputs": [
//             {"internalType": "address", "name": "spender", "type": "address"},
//             {"internalType": "uint256", "name": "addedValue", "type": "uint256"},
//         ],
//         "name": "increaseAllowance",
//         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "function",
//     },
//     {
//         "anonymous": false,
//         "inputs": [
//             {
//                 "indexed": true,
//                 "internalType": "address",
//                 "name": "previousOwner",
//                 "type": "address",
//             },
//             {
//                 "indexed": true,
//                 "internalType": "address",
//                 "name": "newOwner",
//                 "type": "address",
//             },
//         ],
//         "name": "OwnershipTransferred",
//         "type": "event",
//     },
//     {
//         "constant": false,
//         "inputs": [],
//         "name": "renounceOwnership",
//         "outputs": [],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "function",
//     },
//     {
//         "constant": false,
//         "inputs": [
//             {"internalType": "address", "name": "recipient", "type": "address"},
//             {"internalType": "uint256", "name": "amount", "type": "uint256"},
//         ],
//         "name": "transfer",
//         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "function",
//     },
//     {
//         "anonymous": false,
//         "inputs": [
//             {
//                 "indexed": true,
//                 "internalType": "address",
//                 "name": "from",
//                 "type": "address",
//             },
//             {
//                 "indexed": true,
//                 "internalType": "address",
//                 "name": "to",
//                 "type": "address",
//             },
//             {
//                 "indexed": false,
//                 "internalType": "uint256",
//                 "name": "value",
//                 "type": "uint256",
//             },
//         ],
//         "name": "Transfer",
//         "type": "event",
//     },
//     {
//         "constant": false,
//         "inputs": [
//             {"internalType": "address", "name": "sender", "type": "address"},
//             {"internalType": "address", "name": "recipient", "type": "address"},
//             {"internalType": "uint256", "name": "amount", "type": "uint256"},
//         ],
//         "name": "transferFrom",
//         "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "function",
//     },
//     {
//         "constant": false,
//         "inputs": [{"internalType": "address", "name": "newOwner", "type": "address"}],
//         "name": "transferOwnership",
//         "outputs": [],
//         "payable": false,
//         "stateMutability": "nonpayable",
//         "type": "function",
//     },
//     {
//         "constant": true,
//         "inputs": [
//             {"internalType": "address", "name": "owner", "type": "address"},
//             {"internalType": "address", "name": "spender", "type": "address"},
//         ],
//         "name": "allowance",
//         "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
//         "payable": false,
//         "stateMutability": "view",
//         "type": "function",
//     },
//     {
//         "constant": true,
//         "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
//         "name": "balanceOf",
//         "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
//         "payable": false,
//         "stateMutability": "view",
//         "type": "function",
//     },
//     {
//         "constant": true,
//         "inputs": [],
//         "name": "decimals",
//         "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}],
//         "payable": false,
//         "stateMutability": "view",
//         "type": "function",
//     },
//     {
//         "constant": true,
//         "inputs": [],
//         "name": "getOwner",
//         "outputs": [{"internalType": "address", "name": "", "type": "address"}],
//         "payable": false,
//         "stateMutability": "view",
//         "type": "function",
//     },
//     {
//         "constant": true,
//         "inputs": [],
//         "name": "name",
//         "outputs": [{"internalType": "string", "name": "", "type": "string"}],
//         "payable": false,
//         "stateMutability": "view",
//         "type": "function",
//     },
//     {
//         "constant": true,
//         "inputs": [],
//         "name": "owner",
//         "outputs": [{"internalType": "address", "name": "", "type": "address"}],
//         "payable": false,
//         "stateMutability": "view",
//         "type": "function",
//     },
//     {
//         "constant": true,
//         "inputs": [],
//         "name": "symbol",
//         "outputs": [{"internalType": "string", "name": "", "type": "string"}],
//         "payable": false,
//         "stateMutability": "view",
//         "type": "function",
//     },
//     {
//         "constant": true,
//         "inputs": [],
//         "name": "totalSupply",
//         "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
//         "payable": false,
//         "stateMutability": "view",
//         "type": "function",
//     },
// ]).at("0x128baDDE80A48186C5b30c9707DdEF173b1436c3");


const contract = new Contract(abi, "ca address");

contract.methods.balanceOf("").call().then((result) => {
    console.log(result);
})


// 블록넘버 조회
web3.eth.getBlockNumber().then((result) => {
  console.log("Latest Ethereum Block is ",result);
});
