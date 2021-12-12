import time

from brownie import network  # type: ignore
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(180)
    assert advanced_collectible.tokenCounter() == 1
