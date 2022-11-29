import random
from modules.table import group, mvp, paisCopa


def get_response(message: str) -> str:
    p_message = message.lower()

    hello = ["oi", "bom dia", "oie", "hello", "hi"]
    grupos = ["!grupo a", "!grupo b", "!grupo c", "!grupo d", "!grupo e", "!grupo f" ,"!grupo g", "!grupo h", "!g a", "!g b", "!g c", "!g d", "!g e", "!g f" ,"!g g", "!g h"]
    
    if p_message in hello:
        return 'Oi, tudo bem ? \n```Grupos: !grupo <letra_do_grupo> ou !g <letra_do_grupo>\nSobre o país que vai ser a copa: !paiscopa```'
    
    if p_message in grupos:
        grupo = p_message.split()
        return group(grupo[1])
    
    if p_message == '!mvp':
        return mvp()    
    
    if p_message == '!paiscopa':
        return paisCopa()    

    if p_message == '!help':
        return '```Grupos: !grupo <letra_do_grupo> ou !g <letra_do_grupo>\nMVP: !mvp\nSobre o país que vai ser a copa: !paiscopa```'

    return 'Não faço ideia do que está falando, para ver meus comandos digite: !help.'