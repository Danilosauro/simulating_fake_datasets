from faker import Faker 
import pandas as pd 
import random 
from datetime import date
from dateutil.relativedelta import relativedelta
from municipalities import codigos_municipios

def gerar_dados_falsos(num_linhas):
    fake = Faker(['pt_BR']) 
    Faker.seed(4321) 
    random.seed(4321)
    dados_falsos = []
    for _ in range(num_linhas):
        numerodn = fake.random_number(digits=8)  
        codinst = random.choice(['M', 'R', 'E']) 
        numerodv = fake.random_number(digits=2)
        origem = random.choice(['0','1','2','3','88','99'])
        prefixodn = fake.random_number(digits=8)
        codcart = fake.random_number(digits=5) 
        codmuncart = random.choice(codigos_municipios) 
        numregcart = fake.random_number(digits=5) 
        dtregcart = fake.date_of_birth(minimum_age=4, maximum_age=11)
        codestab = fake.random_number(digits = 5)
        codmunnasc = codmuncart
        locnasc = random.choice(['0','1','2','3','4','5','88','99']) 
        endnasc = fake.address() 
        bainasc = fake.neighborhood() 
        codbainasc = fake.random_number(digits=5)
        codendnasc = codbainasc
        complnasc = fake.neighborhood()
        numendnasc = codbainasc 
        cepnasc = fake.random_number(digits = 8) 
        nomemae = fake.first_name_female() 
        numsusmae = fake.random_number(digits = 15) 
        nomernasc = fake.first_name() 
        idademae = random.choice([15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45])
        estcivmae = random.choice(['0','1','2','3','4','5','88','99']) 
        escmae = random.choice(['0','1','2','3','4','5','88','99'])
        codocupmae = fake.random_number(digits=5) 

        qtdfilvivo = 1
        if idademae == 15: 
            qtdfilvivo = 1 
        elif idademae > 15 and idademae <=20: 
            qtdfilvivo = random.randint(1,2) 
        elif idademae > 20 and idademae <=25 : 
            qtdfilvo = random.randint(1,3) 
        elif idademae > 25 and idademae <= 45: 
            qtdfilvivo = random.randint(1,5) 

        qtdfilmort = fake.random_number(digits=1)
        codmunres = codmunnasc
        baires = bainasc 
        codbaires = codbainasc
        endres = endnasc 
        codendres = fake.random_number(digits = 5)
        complres = endnasc
        numres = numendnasc 
        cepres = cepnasc
        codpaisres = 55 
        gestacao = random.choice(['0','1','2','3','4','5','6','88','99'])
        gravidez  = random.choice(['0','1','2','3','88','99'])
        parto = random.choice(['0','1','2','3','4','88','99'])
        consultas = random.choice(['0','1','2','3','4','88','99']) 
        dtnasc = dtregcart 
        horanasc = fake.time()
        sexo = random.choice(['0','1','2','88','99'])
        apgar1 = random.choice(['0','1','2']) 
        apgar5 = random.choice(['0','1','2'])
        racacor = random.choice(['0','1','2','3','4','5','88','99'])
        racacorn = racacor 
        racacormae = racacor
        peso = round(random.uniform(0,8),3) 
        idanomal = random.choice(['0','1','2','88','99']) 

        if idanomal == '1': 
            codanomal = random.choice(["Q00", "Q05", "Q07", "Q10", "Q15", "Q16", "Q18", "Q20", "Q21", "Q25", "Q28", "Q30", "Q31", "Q32", 
                                         "Q34", "Q35", "Q38", "Q39", "Q45"])
        else: 
            codanomal = ''

        codmunnatu = codmunres
        seriescmae = random.randint(1,8) 
        escmaeagr1 = random.choice(['0','1','2','3','4','5','6','7','8','9','10','11','12','88','99'])
        dtnascmae = dtnasc - relativedelta(years= idademae)
        
        qtdgestant = qtdfilvivo
        qtdparnor = 0 
        qtdpartces = 0 

        if parto == '1':
            qtdpartnor = 1 
            qtdpartces = qtdfilvivo - qtdpartnor
        elif parto == '2': 
            qtdpartnor = qtdfilvivo - qtdpartces
            qtdpartces = 1
        else:
            qtdpartnor = qtdfilvivo

         
        idadepai = idademae
        dtultmenst = dtnasc - relativedelta(weeks= 41) 
        semagestac = 41
        tpmetestim = random.choice(['0','1','2','3','88','99'])
        consprenat = random.randint(8,12)
        mesprenat = dtnasc.month - (dtnasc.month -1 ) + random.randint(0,2)
        tpapresent = random.choice(['0','1','2','3','88','99']) 
        sttrabpart = random.choice(['0','1','2','77','88','99'])
        stcespart = random.choice(['0','1','2','77','88','99']) 
        
        paridade =  0 
        if qtdgestant == 1: 
            paridade = 1 
        elif qtdgestant > 1: 
            paridade = 2
        else: 
            paridade = random.choice(['88','99']) 

        tprobson = 0 
        if paridade == 1 and semagestac >= 37: 
            tprobson = 1 
        elif paridade == 1 and semagestac >=37 and sttrabpart ==1: 
            tprobson = 2 
        elif paridade == 2 and parto ==1 and semagestac >=37:
            tprobson = 3
        elif paridade ==2 and parto ==1 and semagestac >= 37 and sttrabpart ==1:
            tprobson = 4 
        elif paridade ==2 and qtdpartces >= 1 and semagestac >=37 : 
            tprobson = 5
        elif paridade == 1 and tpapresent ==1 : 
            tprobson = 6 
        elif paridade == 2 and tpapresent ==1: 
            tprobson = 7 
        elif int(gravidez) > 1: 
            tprobson = 8 
        elif tpapresent == 3: 
            tprobson = 9 
        elif semagestac <=36: 
            tprobson = 10 
        
        kotelchuck = random.choice(['CPNA','CPNA+']) 
        oport_dn = ''
        codufnatu = str(codmunnasc)[:2]
        difdata = ''
        naturalmae = codufnatu
        versaosist = 'v.5'
        stdnnova = random.choice(['0','1','2','88','99'])
        tpnascassi = random.choice(['0','1','2','3','4','88','99'])
        numerolote = ''
        dtcadastro = dtnasc
        dtrecebim = dtnasc + relativedelta(weeks = 1)
        stdnepidem = random.choice(['0','1','2','88','99']) 
        dtrecoriga = dtrecebim 
        dtrecorig_original = dtrecoriga 
        escmaeagr2 = escmaeagr1
        recuperados = '' 
        
        regiao = 0 

        if int(codufnatu) >=11 and int(codufnatu) <=17: 
            regiao = 1 
        elif int(codufnatu) >=21 and int(codufnatu) <=29: 
            regiao = 2 
        elif int(codufnatu) >=31 and int(codufnatu) <=35: 
            regiao = 3 
        elif int(codufnatu) >=41 and int(codufnatu) <=43: 
            regiao = 4
        elif int(codufnatu) >=50 and int(codufnatu) <=53: 
            regiao = 5

        ano_base = dtnasc.year 
        codestocor = codufnatu
        id_cidacs_sinasc_v5 = random.randint(1,10000)
 

        
        # adicionar as variáveis a lista abaixo
        dados_falsos.append([numerodn, codinst, numerodv, origem, prefixodn, codcart, codmuncart, numregcart, dtregcart, codestab, codmunnasc, locnasc, endnasc,
         bainasc, codbainasc, codendnasc, complnasc, numendnasc, cepnasc, nomemae,numsusmae, nomernasc, idademae, estcivmae, escmae, codocupmae,
         qtdfilvivo, qtdfilmort, codmunres, baires, codbaires, endres, codendres, complres, numres, cepres, codpaisres, gestacao, gravidez, parto,
         consultas, dtnasc, horanasc, sexo, apgar1, apgar5, racacor, racacorn, racacormae, peso, idanomal, codanomal, seriescmae, escmaeagr1, dtnascmae, qtdgestant, 
         qtdpartnor, qtdpartces, idadepai, dtultmenst, semagestac, consprenat, mesprenat, tpapresent, sttrabpart, stcespart, paridade, tprobson, kotelchuck,
         oport_dn, codufnatu, difdata, naturalmae, versaosist, tpnascassi, dtcadastro, dtrecebim, stdnepidem, dtrecoriga, dtrecorig_original, escmaeagr2, recuperados, 
         regiao, ano_base, codestocor])
    
    return dados_falsos


num_linhas = 10000

dados = gerar_dados_falsos(num_linhas)

# adicionar as variáveis a lista abaixo
colunas = ['numerodn', 'codinst', 'numerodv', 'origem', 'prefixodn', 'codcart', 'codmuncart', 'numregcart', 'dtregcart', 'codestab', 'codmunnasc', 'locnasc', 'endnasc', 
'bainasc', 'codbainasc', 'codendnasc','complnasc', 'numendnasc', 'cepnasc', 'nomemae','numsusmae','nomernasc','idademae', 'estcivmae', 'escmae', 'codocupmae','qtdfilvivo',
'qtdfilmort', 'codmunres', 'baires', 'codbaires', 'endres', 'codendres', 'complres', 'numres', 'cepres', 'codpaisres', 'gestacao', 'gravidez', 'parto',
'consultas', 'dtnasc', 'horanasc', 'sexo', 'apgar1', 'apgar5', 'racacor', 'racacorn', 'racacormae', 'peso','idanomal', 'codanomal','seriescmae', 'esmaeagr1','dtnascmae',
'qtdgestant','qtdpartnor', 'qtdpartces', 'idadepai', 'dtultmenst', 'semagestac', 'consprenat','mesprenat','tpapresent', 'sttrabpart','stcespart', 'paridade','tprobson',
'kotelchuck','oport_dn','codufnatu', 'difdata', 'naturalmae','versaosist', 'tpnascassi', 'dtcadastro','dtrecebim', 'stdnepidem', 'dtrecoriga', 'dtrecoriga_original',
'escmaeagr2','recuperados','regiao', 'ano_base', 'codestocor']

dados_falsos = pd.DataFrame(dados, columns=colunas)

dados_falsos.to_csv('../output/dados_falsos_sinasc_v5.csv', index=False)

print("Dados falsos gerados e salvos no arquivo 'dados_falsos_sinasc_v5.csv'.") 
