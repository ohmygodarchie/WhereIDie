import getinfo
import AccountClass
import Constants
def main():
    print("This is the main function")
    apiObject = getinfo.apihandler(Constants.API_KEY)
    accountDto = apiObject.getvalpuuid("ohmygodarchie","001")
    account = AccountClass.Account(accountDto,apiObject)
    print(account.puuid)
if __name__ == "__main__":
    main()