from brownie import UniswapV2Router02, WETH
from scripts.helpful_scripts import get_account


def deploy():
    factory_add = "0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87"
    account = get_account()
    weth = WETH.deploy({"from": account})
    uniswap_v2_router = UniswapV2Router02.deploy(
        factory_add, weth.address, {"from": account}
    )
    return uniswap_v2_router, weth


def main():
    deploy()
