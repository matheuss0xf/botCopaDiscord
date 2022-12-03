import json


alinhamento = x = 12 / 2 - 12 / 2

with open("/modules/table.json", encoding='utf8') as file:
    data = json.load(file)

def group(group: str) -> str:
    group_rt = f"""
`Nome                           P    V     E    D  `
`1 - {data["teams"+group.upper()][0]["name"]:<14}`{data["teams"+group.upper()][0]["flag"]}`{data["teams"+group.upper()][0]["p"]:>10}    {data["teams"+group.upper()][0]["w"]:^4} {data["teams"+group.upper()][0]["e"]:^4} {data["teams"+group.upper()][0]["d"]:^4}`
`2 - {data["teams"+group.upper()][1]["name"]:<14}`{data["teams"+group.upper()][1]["flag"]}`{data["teams"+group.upper()][1]["p"]:>10}    {data["teams"+group.upper()][1]["w"]:^4} {data["teams"+group.upper()][1]["e"]:^4} {data["teams"+group.upper()][1]["d"]:^4}`
`3 - {data["teams"+group.upper()][2]["name"]:<14}`{data["teams"+group.upper()][2]["flag"]}`{data["teams"+group.upper()][2]["p"]:>10}    {data["teams"+group.upper()][2]["w"]:^4} {data["teams"+group.upper()][2]["e"]:^4} {data["teams"+group.upper()][2]["d"]:^4}`
`4 - {data["teams"+group.upper()][3]["name"]:<14}`{data["teams"+group.upper()][3]["flag"]}`{data["teams"+group.upper()][3]["p"]:>10}    {data["teams"+group.upper()][3]["w"]:^4} {data["teams"+group.upper()][3]["e"]:^4} {data["teams"+group.upper()][3]["d"]:^4}`
"""
    roundOne = f"""
**1ª RODADA**
`{data["dateRound"]["roundOne"]["group"+group.upper()][0]["teamA"]:<16} {data["dateRound"]["roundOne"]["group"+group.upper()][0]["goalA"]:<5} ❌ {data["dateRound"]["roundOne"]["group"+group.upper()][0]["goalB"]:>5} {data["dateRound"]["roundOne"]["group"+group.upper()][0]["teamB"]:>16}`
`Data: {data["dateRound"]["roundOne"]["group"+group.upper()][0]["date"]:<42}`
`{data["dateRound"]["roundOne"]["group"+group.upper()][1]["teamA"]:<16} {data["dateRound"]["roundOne"]["group"+group.upper()][1]["goalA"]:<5} ❌ {data["dateRound"]["roundOne"]["group"+group.upper()][1]["goalB"]:>5} {data["dateRound"]["roundOne"]["group"+group.upper()][1]["teamB"]:>16}`
`Data: {data["dateRound"]["roundOne"]["group"+group.upper()][1]["date"]:<42}`
"""
    roundTwo = f"""
**2ª RODADA**
`{data["dateRound"]["roundTwo"]["group"+group.upper()][0]["teamA"]:<16} {data["dateRound"]["roundTwo"]["group"+group.upper()][0]["goalA"]:<5} ❌ {data["dateRound"]["roundTwo"]["group"+group.upper()][0]["goalB"]:>5} {data["dateRound"]["roundTwo"]["group"+group.upper()][0]["teamB"]:>16}`
`Data: {data["dateRound"]["roundTwo"]["group"+group.upper()][0]["date"]:<42}`
`{data["dateRound"]["roundTwo"]["group"+group.upper()][1]["teamA"]:<16} {data["dateRound"]["roundTwo"]["group"+group.upper()][1]["goalA"]:<5} ❌ {data["dateRound"]["roundTwo"]["group"+group.upper()][1]["goalB"]:>5} {data["dateRound"]["roundTwo"]["group"+group.upper()][1]["teamB"]:>16}`
`Data: {data["dateRound"]["roundTwo"]["group"+group.upper()][1]["date"]:<42}`
"""
    roundThree = f"""
**3ª RODADA**
`{data["dateRound"]["roundThree"]["group"+group.upper()][0]["teamA"]:<16} {data["dateRound"]["roundThree"]["group"+group.upper()][0]["goalA"]:<5} ❌ {data["dateRound"]["roundThree"]["group"+group.upper()][0]["goalB"]:>5} {data["dateRound"]["roundThree"]["group"+group.upper()][0]["teamB"]:>16}`
`Data: {data["dateRound"]["roundThree"]["group"+group.upper()][0]["date"]:<42}`
`{data["dateRound"]["roundThree"]["group"+group.upper()][1]["teamA"]:<16} {data["dateRound"]["roundThree"]["group"+group.upper()][1]["goalA"]:<5} ❌ {data["dateRound"]["roundThree"]["group"+group.upper()][1]["goalB"]:>5} {data["dateRound"]["roundThree"]["group"+group.upper()][1]["teamB"]:>16}`
`Data: {data["dateRound"]["roundThree"]["group"+group.upper()][1]["date"]:<42}`
"""

    return group_rt + roundOne + roundTwo + roundThree

def tableKeys(table: str) -> str:
    list_table = ""
    list_number = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    name_table = "eight"
    
    if table == 'quartas':
        name_table = 'four'
        list_number = ["one", "two", "three", "four"]

    if table == 'semifinal':
        name_table = 'two'
        list_number = ["one", "two"]
    
    if table == 'terceiro':
        name_table = 'dispute'
        list_number = ["one"]
    
    if table == 'final':
        name_table = 'final'
        list_number = ["one"]
    
    title = f"**`{table.upper()} DE FINAL`**"
    for number in list_number:
        list_table += f"""
`{data["groupStage"][name_table][number]["teamA"]:<16} {data["groupStage"][name_table][number]["goalA"]:<5} ❌ {data["groupStage"][name_table][number]["goalB"]:>5} {data["groupStage"][name_table][number]["teamB"]:>16} `
`Data: {data["groupStage"][name_table][number]["date"]:^42}`
"""
    
    return title + list_table

def mvp() -> str:
    mvp_rt = f'`Jogador: {data["mvp"]["jogador"]}\nGol\'s: {data["mvp"]["gols"]}`'
    return mvp_rt


def paisCopa() -> str:
    worldCup_rt = f'```País: {data["worldCup"]["name"]}\nSobre: {data["worldCup"]["about"]}\nIdioma: {data["worldCup"]["idiom"]}```'
    return worldCup_rt



if __name__ == '__main__':
    paisCopa()
