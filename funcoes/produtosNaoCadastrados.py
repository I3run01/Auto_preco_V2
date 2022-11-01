def produtosNaoCadastrados(xml, nomeCSV):
    import xml.etree.ElementTree as ET
    import pandas as pd

    tree = ET.parse(xml)
    root = tree.getroot()

    link = '{http://www.portalfiscal.inf.br/nfe}'

    #planilha que será aberta
    df = pd.read_csv(nomeCSV)
    df = df.drop(df.columns[[0]], axis = 1)

    #conferência se o produto tem cadastro
    for cProd in root.findall(f"./{link}NFe/{link}infNFe/{link}det/{link}prod/{link}cProd"):
        codigoProd = str(f'f{cProd.text}')
        print(codigoProd)

        