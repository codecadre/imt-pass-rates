import numpy as np
import pandas as pd
from unidecode import unidecode
import re

files = {
    2014: {
        "1-sem": {
            "theory": "imt-data/Taxasdeaprovacao_1_Semestre_2014_Teoricas_Integradas.pdf",
            "driving": "imt-data/Taxasdeaprovacao_1_Semestre_2014_Praticas_Integradas.pdf"
        },
        "2-sem": {
            "theory": "imt-data/Taxasdeaprovacao_2_Semestre_2014_Teoricas_Integradas.pdf",
            "driving": "imt-data/Taxasdeaprovacao_2_Semestre_2014_Praticas_Integradas.pdf"
        }
    },
    2015: "imt-data/TaxasApr_2015_Relatorio_Escolas_de_Condução.pdf",
    2016: "imt-data/TaxasApr_2016_Relatorio_EscolasDeConducao.pdf",
    2017: "imt-data/TaxasApr_2017_Relatorio_EscolasDeConducao.pdf",
    2018: "imt-data/TaxasApr_2018_Relatorio_EscolasDeConducao.pdf",
    2019: "imt-data/EscolasdeCondução-2019.pdf",
    2020: "imt-data/EscolasdeCondução-2020.pdf",
    2021: "imt-data/EscolasdeConducao-2021.pdf"
}


def parse_rate (x):

    if x == '#DIV/0!':
        return np.NAN
    elif pd.isna(x):
        return x
    else:
        return float((x.replace(',', '.').replace('%', 'e-2')))

def parse_int (x):

    if pd.isna(x):
        return
    elif isinstance(x, str):
        return np.int64(x.replace(' ', ''))
    else:
        return np.int64(round(x,0))

def name_to_keyword(x):

    s = unidecode(x)

    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)

    s = s.lower() \
    .replace('escola de conducao da ', '') \
    .replace('escola de conducao de ', '') \
    .replace('escola de conducao ', '') \
    .replace('escola do ', '') \
    .strip() \
    .replace('  ', ' ') \
    .replace(' ', '-')

    return s

def nec_to_string (s):

    if pd.isna(s):
        return "xxxxx"
    else:
        return str(s).zfill(5)


headers = ['nec', 'name_raw', 't_scheduled', 't_done', 't_rate', 'd_scheduled', 'd_done', 'd_rate']
headers_full = ['nec', 'name_raw', 't_scheduled', 't_done', 't_rate', 'd_scheduled', 'd_done', 'd_rate', 'total_scheduled', 'total_done', 'total_rate']
