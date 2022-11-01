def cnpj(xml):
    import xml.etree.ElementTree as ET
    tree = ET.parse(xml)
    root = tree.getroot()
    link = '{http://www.portalfiscal.inf.br/nfe}'
   
    for cnpj in root.findall(f"./{link}NFe/{link}infNFe/{link}emit/{link}CNPJ"):
       return cnpj.text

def nomeCSV(cnpj):
    if cnpj == '62461140002834':
        nome = 'Panco'
        nomeCSV ='arquivos/Panco BD.csv'
        
    elif cnpj =='61186888014305':
        nome ='Coca-Cola'
        nomeCSV = 'arquivos/CC BD.csv'

    elif cnpj =='24782106000152':
        nome ='Tirol'
        nomeCSV = 'arquivos/Tirol BD.csv'

    elif cnpj == '77887412000543':
        nome = 'DEYCON'
        nomeCSV = 'arquivos/Deycon BD.csv'

    elif cnpj == '12133164000176':
        nome = 'RD'
        nomeCSV = 'arquivos/RD BD.csv'

    elif cnpj == '93209765047342':
        nome = 'WMS'
        nomeCSV = 'arquivos/WMS BD.csv'

    elif cnpj == '03303285000128':
        nome = 'Arrojito'
        nomeCSV = 'arquivos/Arrojito BD.csv'

    elif cnpj == '73778144000147':
        nome = 'Triunfante'
        nomeCSV = 'arquivos/Triunfante BD.csv'

    elif cnpj == '01333984000438':
        nome = 'Segalas'
        nomeCSV = 'arquivos/Segalas BD.csv'

    elif cnpj == '13495487000253':
        nome = 'Destro'
        nomeCSV = 'arquivos/Destro BD.csv'

    elif cnpj == '16624530000140':
        nome = 'BOCCHI'
        nomeCSV = 'arquivos/Bocchi BD.csv'

    elif cnpj == '07757548000120':
        nome = 'CBN'
        nomeCSV = 'arquivos/CBN BD.csv'

    elif cnpj == '11330623000149':
        nome = 'STAMPA'
        nomeCSV = 'arquivos/Stampa BD.csv'

    elif cnpj == '56228356005958':
        nome = 'Ambev'
        nomeCSV = 'arquivos/Ambev BD.csv'

    elif cnpj == '21381251000133':
        nome = 'Vigor'
        nomeCSV = 'arquivos/Vigor BD.csv'

    elif cnpj == '76492305000200':
        nome = 'Ouro fino'
        nomeCSV = 'arquivos/Ouro fino BD.csv'

    elif cnpj == '60409075019767':
        nome = 'Nestle'
        nomeCSV = 'arquivos/Nestle BD.csv'

    elif cnpj == '28842819000115':
        nome = 'BDL'
        nomeCSV = 'arquivos/BDL BD.csv'

    elif cnpj == '09241957000102':
        nome = 'Amabile'
        nomeCSV = 'arquivos/Amabile BD.csv'

    elif cnpj == '25769266002844':
        nome = 'Arcom'
        nomeCSV = 'arquivos/Arcom BD.csv'

    elif cnpj == '15814440000150':
        nome = 'IBD'
        nomeCSV = 'arquivos/IBD BD.csv'

    elif cnpj == '81611931000209':
        nome = 'OESA'
        nomeCSV = 'arquivos/OESA BD.csv'

    elif cnpj == '01838723012567':
        nome = 'BRF'
        nomeCSV = 'arquivos/BRF BD.csv'

    elif cnpj == '09095640000105':
        nome = 'Sueko'
        nomeCSV = 'arquivos/Sueko BD.csv'

    elif cnpj == '17790307000640':
        nome = 'E-UB'
        nomeCSV = 'arquivos/E-UB BD.csv'

    elif cnpj == '90724261000902':
        nome = 'Oniz'
        nomeCSV = 'arquivos/Oniz BD.csv'

    elif cnpj == '00249906000144':
        nome = 'Lemes e Oliveiras'
        nomeCSV = 'arquivos/Lemes e Oliveiras BD.csv'

    elif cnpj == '19195971000162':
        nome = 'DP4'
        nomeCSV = 'arquivos/DP4 BD.csv'

    elif cnpj == '01554188000182':
        nome = 'Grupo Lobo'
        nomeCSV = 'arquivos/Grupo Lobo BD.csv'

    elif cnpj == '10842044000384':
        nome = 'Copini'
        nomeCSV = 'arquivos/Copini BD.csv'

    elif cnpj == '24509214000156':
        nome = 'Oliveira'
        nomeCSV = 'arquivos/Oliveira BD.csv'

    elif cnpj == '77595395000490':
        nome = 'Frimesa'
        nomeCSV = 'arquivos/Frimesa BD.csv'
    
    elif cnpj == '29635803000102':
        nome = 'Hawaii Distribuição de materiais'
        nomeCSV = 'arquivos/Hawaii BD.csv'

    elif cnpj == '76430438010134':
        nome = 'Max Atacadista'
        nomeCSV = 'arquivos/Max BD.csv'

    elif cnpj == '36486464000105':
        nome = 'Chef Distribuidora'
        nomeCSV = 'arquivos/Chef BD.csv'

    elif cnpj == '17467515002738':
        nome = 'Cafe Tres Coracoes S.A'
        nomeCSV = 'arquivos/Três corações BD.csv'

    elif cnpj == '02914460045170':
        nome = 'Seara'
        nomeCSV = 'arquivos/Seara BD.csv'
    
    else:
        print('Empresa não cadastrada')

    print('')
    print(f'Essa nota é da empresa: {nome}')
    print(30*'-')

    return nomeCSV

from funcoes.produtosNaoCadastrados import produtosNaoCadastrados as pnc

xml = str(input('nome do arquivo: ')) + '.xml'
cnpj = cnpj(xml)
nomeCSV = nomeCSV(cnpj)

pnc(nomeCSV=nomeCSV, xml=xml)
