import getinfo
import AccountClass
import Constants
import MatchClasses

#no clue if this needs to exist
class APIWrapper:
    def __init__(self,api_key):
        self.api_key = api_key
        self.api_handler = getinfo.apihandler(api_key)
        self.accountDto = self.api_handler.getvalpuuid("ohmygodarchie","001")
        self.account = AccountClass.Account(self.accountDto,self.api_handler)
    def get_account(self):
        return self.account
    def get_account_Dto(self):
        return self.accountDto
    def get_api_handler(self):
        return self.api_handler
    def get_api_key(self):
        return self.api_key
    #gets a specific match from match id (does not include matchlist entry information such as gameStartTimeMillis or teamId for a certain player)
    def get_match_info(self,match_id):
        return MatchClasses.Match(self.api_handler.getvalmatch(match_id))
    
    def get_match_list(self):
        return self.account.listofmatches
    def get_comp_matches(self):
        compmatches =[]
        for x in self.account.listofmatches:
            if x.isRanked == True:
                return x
        return compmatches
    
def main():
    print("This is the main function")
    apiObject = getinfo.apihandler(Constants.API_KEY)
    accountDto = apiObject.getvalpuuid("ohmygodarchie","001")
    account = AccountClass.Account(accountDto,apiObject)
    print(account.puuid)
if __name__ == "__main__":
    main()