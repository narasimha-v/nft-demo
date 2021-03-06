from brownie import network  # type: ignore
from scripts.simple_collectible.deploy_and_create import deploy_and_create
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
