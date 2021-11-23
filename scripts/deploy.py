from brownie import accounts, config, SimpleStorage, network


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)


def main():
    deploy_simple_storage()
