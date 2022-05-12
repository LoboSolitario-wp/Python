import openpyxl

#arq = openpyxl.load_workbook(r"C:\Users\peo_wipereira\Downloads\teste.xlsx")
#plan = arq["Planilha1"]
#plan['C1'] = 'Teste'
#arq.save(r"C:\Users\peo_wipereira\Downloads\teste.xlsx")

arq = openpyxl.load_workbook(r"C:\Users\peo_wipereira\Downloads\Majoração Fase 3 - Varejo - Total (1).xlsx")

plan = arq["Base"]

plan['AJ630332'] = 0
plan['AJ630333'] = 0
plan['AJ630334'] = 0
plan['AJ630335'] = 0


arq.save(r"C:\Users\peo_wipereira\Downloads\Majoração Fase 3 - Varejo - Total (1).xlsx")
