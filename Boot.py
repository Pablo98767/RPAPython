
# ROBÔ QUE ACESSA A BASE DE DADOS DA MINARAÇÃO E FAZ O DOWNLOAD DE SUA BASE DE DADOS.
# Links importantes para realizar o processo: 
# Link de como baixar uma base de dados : https://www.delftstack.com/pt/howto/python/download-a-file-in-python/
# Link de como pegar arquivos em uma pasta e move-las para um outro diretório : https://www.vivaolinux.com.br/topico/Python/Criar-um-arquivo-e-mover-para-uma-pasta-em-PYTHON.

#IMPORTANDO BIBLIOTECAS NECESSÁRIAS PARA O ROBÔ.
import py
import selenium # O selenium fica responsável pela automoção na web
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyautogui # Fica responsável pela parte da automoção desktop
import shutil
from sqlalchemy import PrimaryKeyConstraint # Ficará responsável por mover a pasta com a base para o diretório que precisamos.

# USAREMOS A BIBLIOTECA DO SELENIUM PARA CONSTRUIR NOSSO SISTEMA DE TESTE AUTOMATIZADO E BAIXAR A BASE DE DADOS.
# LINK DA DOCUMENTAÇÃO DO SELENIUM : https://www.selenium.dev/documentation/webdriver/getting_started/

# USAREMOS A BIBLIOTECA DO PYAUTOGUI PARA A PARTE DE AUTOMOÇÃO DESKTOP
# LINK DA DOCUMENTAÇÃO DO PYAUTOGUI : https://pyautogui.readthedocs.io/en/latest/quickstart.html

# USAREMOS A BIBLIOTECA SHUTIL, ELA VAI MOVER NOSSA PASTA COM A BASE DE DADOS PARA O DIRETÓRIO QUE QUEREMOS.
# LINK DA DOCUMENTAÇÃO DO SHUTIL : https://docs.python.org/3/library/shutil.html


#Antes de iniciarmos vamos analisar se tem arquivos dentro de nossos diretórios... se tiver arquivos lá, com certeza
#o selenium vai dar ruim, então vamos fazer esta verificação, se caso tover arquivos lá o robô vai apagar.

#Não ouve necessidade de usar if ou else, mas caso queira usar fique a vontade para alterar este codigo fonte...
print("Verificando se há arquivos nos diretórios...")
pyautogui.PAUSE = 5.0
pyautogui.press('win')
pyautogui.PAUSE = 5.0
pyautogui.write('Download')
pyautogui.PAUSE = 5.0
pyautogui.press('enter')
pyautogui.PAUSE = 5.0
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Observatorio')
pyautogui.PAUSE = 3.0
pyautogui.press('enter')
pyautogui.PAUSE = 2.0
pyautogui.press('tab')
pyautogui.PAUSE = 2.0
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.PAUSE = 10.0
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('down')
pyautogui.press('up')
pyautogui.press('enter')

#ENTROU NO DIRETÓRIO QUE QUEREMOS... AGORA ELE VAI ENTRAR DE PASTA EM PASTA E VAI VARRER TODOS OS ARQUIVOS, 
#PARA QUE UMA BASE DE DADOS ATUALZIADA POSSA SER COLOCADA NO LUGAR DOS ARQUIVOS DESATUALIZADOS!

#Apagando os dados da primeira pasta
pyautogui.press('down')
pyautogui.press('up')
pyautogui.PAUSE = 2.0
pyautogui.press('enter')
pyautogui.PAUSE = 2.0
pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('delete')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.PAUSE = 2.0

#Apagando os dados da segunda pasta
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('delete')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

#Apagando os dados da terceira pasta!
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.press('down')
pyautogui.press('up')
pyautogui.press('enter')
'''pyautogui.press('down')
pyautogui.press('enter')'''
#Apagando a base de dados dessa pasta!
pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('delete')
pyautogui.press('left')
pyautogui.press('enter')
pyautogui.PAUSE = 10
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('delete')
pyautogui.PAUSE  = 10  
pyautogui.press('left')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

#Apagando dados da quinta pasta
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('delete')
pyautogui.press('left')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

#Entrando na proxima pasta
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('delete')
pyautogui.press('left')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
#Entrondo na proxima pasta
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('delete')
pyautogui.press('left')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('enter')

print("Verificação Realizada!")
print("Iniciando teste automatizado...")
# O único objetivo de usar o selenium é só para pegar os arquivos do site e baixa-los.
# Pegando o webdriver
driver = webdriver.Chrome(executable_path="G:/IEL/OBSERVATORIO/ETL/panorama economico/chromedriver_win32/chromedriver.exe")
#Acessando o link com a base de dados
driver.get("https://app.anm.gov.br/DadosAbertos/SCM/")
time.sleep(5)

# proximo comando é acessar  os diretórios do site e baixar a base de dados e joga-las no seguinte diretório abaixo:
# G:\IEL\OBSERVATORIO\BASES DE DADOS OBSERVATÓRIO\Agência Nacional de Mineração

#Baixando os dados do primeiro link disponivel no sistema.
driver.find_element(By.XPATH,'/html/body/pre/a[2]').click() # este comando é o que usaremos para clicar e navegar no site e achar a base de dados que precisamos
time.sleep(5)

#Baixando os dados do segundo link
driver.find_element(By.XPATH,'/html/body/pre/a[3]').click()
time.sleep(5)

#Este comando abaixo é um pdf, e pdfs o selenium não baixa!
#Baixando os dados do terceiro link

'''
driver.find_element(By.XPATH,'/html/body/pre/a[4]').click()
time.sleep(20)
'''

#Baixando os dados do quarto link
driver.find_element(By.XPATH,'/html/body/pre/a[5]').click()
time.sleep(5)

#Baixando os dados do quinto link
driver.find_element(By.XPATH,'/html/body/pre/a[6]').click()
time.sleep(5)

print("Iniciando o processo de download do microdados!")
#Baixando os dados do sexto link
driver.find_element(By.XPATH,'/html/body/pre/a[7]').click() # Clica do diretório "microdados"
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/pre/a[4]').click() #Clicando no arquivo excel
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/pre/a[5]').click() #Clicando no arquivo zip
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/pre/a[1]').click() # Voltando para pasta anterior
time.sleep(5)
print("Dados da pasta microdados baixados com sucesso!")

#Baixando os dados do setimo link
driver.find_element(By.XPATH,'/html/body/pre/a[8]').click()
time.sleep(5)
#Baixando os dados do oitavo link
driver.find_element(By.XPATH,'/html/body/pre/a[9]').click()
time.sleep(5)

#Baixando os dados do decimo link
driver.find_element(By.XPATH,'/html/body/pre/a[10]').click()
time.sleep(5)

#Baixando os dados do decimo primeiro link
driver.find_element(By.XPATH,'/html/body/pre/a[11]').click()
time.sleep(5)

#Baixando os dados do decimo segundo link
driver.find_element(By.XPATH,'/html/body/pre/a[13]').click()
time.sleep(5)

#Baixando os dados do decimo terceiro link
driver.find_element(By.XPATH,'/html/body/pre/a[14]').click()
time.sleep(5)

#Baixando os dados do decimo quarto link
driver.find_element(By.XPATH,'/html/body/pre/a[15]').click()
time.sleep(5)

#Baixando os dados do decimo quinto link
driver.find_element(By.XPATH,'/html/body/pre/a[16]').click()
time.sleep(5)

print("Automoção web concluída!")
print("Base de dados baixados com sucesso!")

#INICIANDO O PROCESSEDIMENTO DA AUTOMOÇÃO DESKTOP
print("Começando o processo de automoção desktop...")

#Verificar se a pasta download está limpa, ou seja o que tem que está na pasta download na hora que executar o robô são somente as bases de dados.
# se não qualquer arquivo que estiver lá vai ser movido junto com a base!!!!
pyautogui.PAUSE = 3.0
pyautogui.press('win') # Digitar a tecla windows
pyautogui.PAUSE = 2.0 # Esperar para executar o programa abaixo
pyautogui.write('Download') # Digitar o texto na lupinha do windows
pyautogui.PAUSE = 2.0 # Esperar por 2 segundos
pyautogui.press('enter')
pyautogui.PAUSE = 2.0

#Agora selecionar todos os arquivos dessa pasta e recorta-los
pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('ctrl','x')
pyautogui.PAUSE = 2.0

#Agora Criar uma pasta nova
pyautogui.hotkey('ctrl','shift','n')
pyautogui.write('base de dados')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.PAUSE = 2.0
pyautogui.hotkey('ctrl','v')
pyautogui.PAUSE = 2.0

#PROCEDIMENTO CONCLUÍDO
print("Salvando a pasta com os arquivos no diretório que necessitamos!")

source = r'C:\Users\pablofelix.iel\Downloads\base de dados'
destination = r'G:\IEL\OBSERVATORIO\BASES DE DADOS OBSERVATÓRIO\Agência Nacional de Mineração\Processos Mineirais por empresa\Dados'
shutil.move(source,destination)
print("Base salva com sucesso!")
print("Aplicação Finalizada!!")


#INICIANDO O PROCEDIMENTO DO SEGUNDO CARD - PRODUÇÃO MINERAL

print("Extraindo os dados da produção mineral...")
time.sleep(5)
print("Extraindo o AMB -Agua Mineral...")
driver.get("http://landpage-h.cgu.gov.br/dadosabertos/index.php?url=https://app.anm.gov.br/dadosabertos/AMB/Agua_Mineral_Producao.csv")
time.sleep(2)
print("Agua mineral extraida com sucesso!")

print("Extraindo Produção Beneficiária...")
driver.get("http://landpage-h.cgu.gov.br/dadosabertos/index.php?url=https://app.anm.gov.br/DadosAbertos/AMB/Producao_Beneficiada.csv")
time.sleep(2)

print("Extraindo Produção Bruta...")
driver.get("http://landpage-h.cgu.gov.br/dadosabertos/index.php?url=https://app.anm.gov.br/DadosAbertos/AMB/Producao_Bruta.csv")
time.sleep(5)

print("Base de dados Mineiração produção baixada!!!")

print("Criando sua pasta...")

pyautogui.PAUSE = 3.0
pyautogui.press('win') # Digitar a tecla windows
pyautogui.PAUSE = 2.0 # Esperar para executar o programa abaixo
pyautogui.write('Download') # Digitar o texto na lupinha do windows
pyautogui.PAUSE = 2.0 # Esperar por 2 segundos
pyautogui.press('enter')

pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('ctrl','x')
pyautogui.PAUSE = 2.0

pyautogui.hotkey('ctrl','shift','n')
pyautogui.write('Producao Mineiral - base de dados')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.PAUSE = 2.0
pyautogui.hotkey('ctrl','v')
pyautogui.PAUSE = 2.0



source_producao_mineral = r'C:\Users\pablofelix.iel\Downloads\Producao Mineiral - base de dados'
destination_producao_mineral = r'G:\IEL\OBSERVATORIO\BASES DE DADOS OBSERVATÓRIO\Agência Nacional de Mineração\Produção Mineiral'
shutil.move(source_producao_mineral,destination_producao_mineral) 
print("Base Produção Mineral salva com sucesso!")


print("Iniciando os Processo da extração da Produção Bruta...")
driver.get("http://landpage-h.cgu.gov.br/dadosabertos/index.php?url=https://app.anm.gov.br/DadosAbertos/AMB/Producao_Bruta.csv")
time.sleep(3)

print("Produção Bruta baixada!")
pyautogui.PAUSE = 3.0
pyautogui.press('win') # Digitar a tecla windows
pyautogui.PAUSE = 2.0 # Esperar para executar o programa abaixo
pyautogui.write('Download') # Digitar o texto na lupinha do windows
pyautogui.PAUSE = 2.0 # Esperar por 2 segundos
pyautogui.press('enter')


pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('ctrl','x')
pyautogui.PAUSE = 2.0



pyautogui.hotkey('ctrl','shift','n')
pyautogui.write('Producao Bruta - base de dados')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.PAUSE = 2.0
pyautogui.hotkey('ctrl','v')
pyautogui.PAUSE = 2.0


source_producao_bruta = r'C:\Users\pablofelix.iel\Downloads\Producao Bruta - base de dados'
distino_producao_bruta = r'G:\IEL\OBSERVATORIO\BASES DE DADOS OBSERVATÓRIO\Agência Nacional de Mineração\Produção Bruta'
shutil.move(source_producao_bruta,distino_producao_bruta)
print("Produção Bruta salva na pasta com sucesso!")

print("Baixando a base da Agua mineral produção...")
driver.get("http://landpage-h.cgu.gov.br/dadosabertos/index.php?url=https://app.anm.gov.br/dadosabertos/AMB/Agua_Mineral_Producao.csv")
time.sleep(5)


print("Dados Agua mineral baixadas com sucesso!")
pyautogui.PAUSE = 3.0
pyautogui.press('win') # Digitar a tecla windows
pyautogui.PAUSE = 2.0 # Esperar para executar o programa abaixo
pyautogui.write('Download') # Digitar o texto na lupinha do windows
pyautogui.PAUSE = 2.0 # Esperar por 2 segundos
pyautogui.press('enter')


pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('ctrl','x')
pyautogui.PAUSE = 2.0


pyautogui.hotkey('ctrl','shift','n')
pyautogui.write('Producao Agua Mineral - base de dados')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.PAUSE = 2.0
pyautogui.hotkey('ctrl','v')
pyautogui.PAUSE = 2.0


sorce_agua_mineral = r'C:\Users\pablofelix.iel\Downloads\Producao Agua Mineral - base de dados'
distino_agua_mineral =r'G:\IEL\OBSERVATORIO\BASES DE DADOS OBSERVATÓRIO\Agência Nacional de Mineração\Produção Àgua Mineral'
shutil.move(sorce_agua_mineral,distino_agua_mineral)
print("Base de dados da Agua mineral salva com sucesso na pasta!")

print("Baixando a Arrecadação CFEM...")

driver.get("http://landpage-h.cgu.gov.br/dadosabertos/index.php?url=https://app.anm.gov.br/DadosAbertos/ARRECADACAO/CFEM_Arrecadacao.csv")
time.sleep(60)

print("Arrecadação CFEM baixadas com sucesso!")

pyautogui.PAUSE = 3.0
pyautogui.press('win') # Digitar a tecla windows
pyautogui.PAUSE = 2.0 # Esperar para executar o programa abaixo
pyautogui.write('Download') # Digitar o texto na lupinha do windows
pyautogui.PAUSE = 2.0 # Esperar por 2 segundos
pyautogui.press('enter')


pyautogui.hotkey('ctrl','a')
pyautogui.PAUSE = 3.0
pyautogui.hotkey('ctrl','x')
pyautogui.PAUSE = 2.0

pyautogui.hotkey('ctrl','shift','n')
pyautogui.write('Arrecadacao CFEM - Base de dados')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.PAUSE = 2.0

pyautogui.hotkey('ctrl','v')
pyautogui.PAUSE = 2.0

source_arrecadacao = r'C:\Users\pablofelix.iel\Downloads\Arrecadacao CFEM - Base de dados'
distino_arrecadacao =r'G:\IEL\OBSERVATORIO\BASES DE DADOS OBSERVATÓRIO\Agência Nacional de Mineração\Arrecadação CFEM'
shutil.move(source_arrecadacao,distino_arrecadacao)

print("Dados CFEM salvos com sucesso na pasta!")
print("Aplicação 100 por cento finalizada!")
print("Fechando o robô...")
print("Teste automatizado finalizado com sucesso!")
time.sleep(20)
driver.quit()




























