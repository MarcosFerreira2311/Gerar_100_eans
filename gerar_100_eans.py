import random
import barcode
from barcode.writer import ImageWriter

# Configuração
TOTAL_CODIGOS = 100
PREFIXO_BRASILEIRO = "789"
SALVAR_IMAGENS = False  # Altere para True se quiser salvar as imagens

# Função para calcular o dígito verificador do EAN-13
def calcular_digito_verificador(codigo):
    pesos = [1, 3] * 6  # alternância de pesos 1 e 3 para os 12 dígitos
    soma = sum(int(codigo[i]) * pesos[i] for i in range(12))
    return str((10 - (soma % 10)) % 10)

# Função para gerar um único código EAN-13
def gerar_ean13():
    corpo = PREFIXO_BRASILEIRO + ''.join(str(random.randint(0, 9)) for _ in range(9))
    digito = calcular_digito_verificador(corpo)
    return corpo + digito

# Lista para armazenar os códigos
codigos_gerados = []

# Gerar e armazenar os códigos
for i in range(TOTAL_CODIGOS):
    ean = gerar_ean13()
    codigos_gerados.append(ean)

    if SALVAR_IMAGENS:
        classe_ean = barcode.get_barcode_class('ean13')
        ean_barcode = classe_ean(ean, writer=ImageWriter())
        ean_barcode.save(f"ean_{i+1:03}")  # Salva como ean_001.png, ean_002.png etc.

# Salvar os códigos em um arquivo TXT
with open("codigos_ean.txt", "w") as arquivo:
    for codigo in codigos_gerados:
        arquivo.write(codigo + "\n")

print(f"{TOTAL_CODIGOS} códigos EAN-13 gerados com sucesso e salvos em 'codigos_ean.txt'")
if SALVAR_IMAGENS:
    print("As imagens também foram salvas no mesmo diretório.")
