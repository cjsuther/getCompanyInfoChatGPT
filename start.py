from base.base import Base
from excel import readAllData
from os import listdir
from os.path import isfile, join
from llm import processCompany

bm = Base()

dataSheets = readAllData("data.xlsx")

excelPath = dataSheets[2][0][1]
pdfPath = dataSheets[2][1][1]

onlyExcelfiles = [f for f in listdir(excelPath) if isfile(join(excelPath, f)) and f.endswith(".xlsx")]
onlyPDFfiles = [f for f in listdir(pdfPath) if isfile(join(pdfPath, f)) and f.endswith(".pdf")]
companies = [[f.split('_')[0], f.split('_')[1].replace('.pdf', '')]  for f in onlyPDFfiles]
print(companies)
for company in companies:
    pdfFile = pdfPath + '/' + company[0] + '_' + company[1] + '.pdf'
    excelModel = excelPath + '/' + next(f for f in onlyExcelfiles if f.startswith(company[0] + '_'))
    processCompany(company[0], company[1], pdfFile, excelModel)

#print(onlyExcelfiles)
