from brownie import BonusToken, LiquidityMigrator
from scripts.helpful_scripts import get_account


def deploy():
    router_add = ""
    pair_add = ""
    router_fork_add = ""
    pair_fork_add = ""
    bonus_token_add = ""
    account = get_account()
    bonus_token = BonusToken.deploy({"from": account})
    liquidity_migrator = LiquidityMigrator.deploy(
        router_add,
        pair_add,
        router_fork_add,
        pair_fork_add,
        bonus_token_add,
        {"from": account},
    )
    return liquidity_migrator, bonus_token


def main():
    deploy()
