#Definindo lista de empresas
lista = \
[
    {
        "Empresa": "Empresa1",
        "Data": "2022/02/04",
        "DadosComprometidos": ["Senha", "Ajuda da senha"]
    },
    {
        "Empresa": "Empresa2",
        "Data": "2022/03/04",
        "DadosComprometidos": ["Ajuda da senha", "Telefone", "Email"]
    },
    {
        "Empresa": "Empresa3",
        "Data": "2021/12/04",
        "DadosComprometidos": ["Senha", "Email"]
    },
    {
        "Empresa": "Empresa4",
        "Data": "2021/03/12",
        "DadosComprometidos": ["Email", "Senha", "Ajuda da senha", "Nomes"]
    },
    {
        "Empresa": "Empresa5",
        "Data": "2022/01/05",
        "DadosComprometidos": ["Ajuda da senha", "Telefone", "Email"]
    }
]

"""
Definindo o peso por dado comprometido, sendo senha o mais crítico:
    * Senha = 10000
    * Ajuda da senha = 1000
    * Telefone = 100
    * Nomes = 10
    * Email = 1
"""

pesos = {
    "Senha": 10000,
    "Ajuda da senha": 1000,
    "Telefone": 100,
    "Nomes": 10,
    "Email": 1
}

#Função de pré-processamento que determina o valor da somatória dos pesos e acrescenta no objeto
def pre_processing(obj):
    peso = 0
    for key in obj["DadosComprometidos"]:
        peso+= pesos[key]

    obj["Peso"] = peso


#Chamando função de pré-processamento em todos os objetos
for obj in lista:
    pre_processing(obj)


#Ordenando os objetos: os que tem mais peso primeiro, se houver empate é desempatado pela data (mais recente vem primeiro)
lista.sort(key=lambda x: (x["Peso"], x["Data"]), reverse=True)

print("Criticidade ordenada:")
for element in lista:
    print(element)