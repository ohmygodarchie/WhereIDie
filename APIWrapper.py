import getinfo
import AccountClass

def main():
    print("This is the main function")
    apiObject = getinfo.apihandler("")
    accountDto = apiObject.getvalpuuid("ohmygodarchie","001")
    account = AccountClass.Account(accountDto,apiObject)
    print(account.puuid)
if __name__ == "__main__":
    main()