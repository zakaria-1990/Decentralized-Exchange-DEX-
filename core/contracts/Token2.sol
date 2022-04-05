// SPDX-License-Identifer: MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Token2 is ERC20 {
    constructor() public ERC20("Token2", "TK2") {}
}
