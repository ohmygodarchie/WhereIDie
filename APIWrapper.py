import getinfo
import AccountClass

def main():
    print("This is the main function")
    apiObject = getinfo.apihandler("RGAPI-dc863e8b-237b-4a8e-b8a3-525bfc57fd1d")
    accountDto = apiObject.getvalpuuid("ohmygodarchie","001")
    account = AccountClass.Account(accountDto,apiObject)
    print(account.puuid)
if __name__ == "__main__":
    main()