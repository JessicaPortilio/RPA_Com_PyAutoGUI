from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from openpyxl import load_workbook

caminho_Arquivo = 'challenge.xlsx'

abrindo_planilha = load_workbook(caminho_Arquivo)
sheet_selecionada = abrindo_planilha['Sheet1']

abriNavegador = webdriver.Chrome()
abriNavegador.get('https://rpachallenge.com/')

inicializar = abriNavegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
inicializar.click()
sleep(2)

for linha in range(2, len(sheet_selecionada['A']) + 1):
    First_Name = sheet_selecionada[f'A{linha}'].value
    Last_Name = sheet_selecionada[f'B{linha}'].value
    Company_Name = sheet_selecionada[f'C{linha}'].value
    Role_in_Company = sheet_selecionada[f'D{linha}'].value
    Address = sheet_selecionada[f'E{linha}'].value
    Email = sheet_selecionada[f'F{linha}'].value
    Phone_Number = sheet_selecionada[f'G{linha}'].value
    
    if First_Name != None:
        # print(First_Name, Last_Name, Company_Name, Role_in_Company, Address, Email, Phone_Number)

        
        preencher = abriNavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
        preencher.clear()
        preencher.send_keys(First_Name)
        
        preencher = abriNavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']")
        preencher.clear()
        preencher.send_keys(Last_Name)
     
        preencher = abriNavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
        preencher.clear()
        preencher.send_keys(Company_Name)
     
        preencher = abriNavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']")
        preencher.clear()
        preencher.send_keys(Role_in_Company)
      
        preencher = abriNavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']")
        preencher.clear()
        preencher.send_keys(Address)
       
        preencher = abriNavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']")
        preencher.clear()
        preencher.send_keys(Email)
        
        preencher = abriNavegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']")
        preencher.clear()
        preencher.send_keys(Phone_Number)
        
        botao = abriNavegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input')
        botao.click()
    
        sleep(0.1)


sleep(5)

