
def nome_curto_longo(nomes):
    if not nomes:
        return None, None  
    
    nome_mais_longo = max(nomes, key=len)  
    nome_mais_curto = min(nomes, key=len)  
    
    return nome_mais_longo, nome_mais_curto


nomes = ["Ana", "Fernando", "Cláudia", "Beatriz", "João"]


longo, curto = nome_curto_longo(nomes)


if longo and curto:
    print(f"Nome mais longo: {longo}")
    print(f"Nome mais curto: {curto}")

