// SPDX-License6Identifer: MIT

pragma solidity =0.6.6;

import "@openzepplin/contracts/token/ERC20/ERC20.sol";

contract BonusToken is ERC20 {
    address public admin;
    address public liquidator;

    constructor() public ERC20("BonusToken", "BTK") {
        admin = msg.sender;
    }

    function setLiquidator(address _liquidator) external {
        require(msg.sender == admin, "only admin");
        liquidator = _liquidator;
    }

    function mint(address _to, uint256 _amount) external {
        require(msg.sender == liquidator, "only liquidator");
        _mint(_to, _amount);
    }
}
