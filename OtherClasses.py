class Economy:
    loadoutValue = -1
    weapon= ""
    armor=""
    remaining = -1
    spent = -1
    def __init__(self,economyDto):
        self.loadoutValue = economyDto['loadoutValue']
        self.weapon = economyDto['weapon']
        self.armor = economyDto['armor']
        self.remaining = economyDto['remaining']
        self.spent = economyDto['spent']
class Ability:
    grenadeEffects = ""
    ability1Effects = ""
    ability2Effects = ""
    ultimateEffects = ""
    def __init__(self,abilityDto):
        self.grenadeEffects = abilityDto['grenadeEffects']
        self.ability1Effects = abilityDto['ability1Effects']
        self.ability2Effects = abilityDto['ability2Effects']
        self.ultimateEffects = abilityDto['ultimateEffects']
