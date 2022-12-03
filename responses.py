from modules.table import group, tableKeys, mvp, countryCup, win


def get_response(message: str) -> str:
    p_message = message.lower()

    hello = ["oi", "bom dia", "oie", "hello", "hi"]
    grupos = ["!grupo a", "!grupo b", "!grupo c", "!grupo d", "!grupo e", "!grupo f" ,"!grupo g", "!grupo h", "!g a", "!g b", "!g c", "!g d", "!g e", "!g f" ,"!g g", "!g h"]
    table = ["!tabela oitavas", "!tabela quartas", "!tabela semifinal", "!tabela terceiro", "!tabela final","!t oitavas", "!t quartas", "!t semifinal", "!t terceiro", "!t final"]
    
    if p_message in hello:
        return 'Oi, tudo bem ? \n```Grupos: !grupo <letra_do_grupo> ou !g <letra_do_grupo>\nTabela: !t <oitavas>/<quartas>/<terceira>/<semifinal>/<final>\nVencedor: !vencedor\nQuem fez mais gol: !mvp\nSobre o país que vai ser a copa: !paiscopa```'
    
    if p_message in grupos:
        grupo = p_message.split()
        return group(grupo[1])
    
    if p_message in table:
        table = p_message.split()
        return tableKeys(table[1])
    
    if p_message == '!mvp':
        return mvp()    
    
    if p_message == '!paiscopa':
        return countryCup()    
    
    if p_message == '!v':
        winCup = p_message.split()
        return win(winCup[0])    

    if p_message == '!help':
        return '```Grupos: !grupo <letra_do_grupo> ou !g <letra_do_grupo>\nTabela: !t <oitavas>/<quartas>/<terceira>/<semifinal>/<final>\nVencedor: !vencedor\nQuem fez mais gol: !mvp\nSobre o país que vai ser a copa: !paiscopa```'

    return 'Não faço ideia do que está falando, para ver meus comandos digite: !help.'
