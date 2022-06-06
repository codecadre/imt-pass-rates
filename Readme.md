## What's this

IMT pass rates from 2015-2020 parsed and ready to use in a jupyter notebook. **Check the [demo](/demo.ipynb)**.

This was originally done for [passaprimeira.xyz](https://www.passaprimeira.xyz).

## Background

[passaprimeira.xyz](https://www.passaprimeira.xyz) aims at bringing transparency to the driving school business in Portugal, by crossing public data and presenting it in an accessible format. Originally it was only a web app, but we decided to release some of the data and code, in a accessible format, so that others could benefit form it.

Check [this blog post](https://www.flaviosousa.co/pedido-accesso-dados-publicos/) for more background on the difficulties of getting this data set release.



## Data origin

A collection of pdfs on the [Imt Website](https://www.imt-ip.pt/sites/IMTT/Portugues/EnsinoConducao/taxasdeaprovacao/Paginas/TaxasdeAprovacao.aspx).

## Data issues

Some schools show up with slightly different names so we merge them together after the import.

Other schools show up with different names under the same license number, so we'll treat them as different schools

```
| :nec |                                                        :ks |
|------+------------------------------------------------------------|
| 1216 |       caloira-de-estarreja-01216 -- estrela-do-caima-01216 |
|  830 |                      douro-sul-00830 -- reis-armamar-00830 |
| 1075 |                         auto-dao-01075 -- de-repeses-01075 |
|  626 |                         celas-00626 -- siiimpletunas-00626 |
| 1349 |                     nova-de-tomar-01349 -- nova-mira-01349 |
| 1314 |                             malhoa-01314 -- prestige-01314 |
|  587 |        nascente-do-ave-00587 -- auto-dinamica-do-ave-00587 |
|  447 | infante-sagresvila-real-de-santo-antonio-00447 -- vr-00447 |
|  760 |                               ip4-00760 -- auto-stop-00760 |
| 1079 |                        mota-galiza-01079 -- prestige-01079 |
|  339 |                mortaguense-00339 -- nova-de-esgueira-00339 |
|  746 |                    tyrsense-00746 -- dinamica-do-vez-00746 |
|  900 |          armando-machado-da-cruz-00900 -- grand-tour-00900 |
| 1257 |                        inicios-01257 -- siiimpletejo-01257 |
```

## Install

```
pip3 install -r requirements.txt
```

## Run

```
~/.local/bin/jupyter-lab
```

## How to use it

The entire data set can be found in

- [`parsed-data/db.json` ](result.json)
- `parsed-data/db.pkl`: Check [`demo.ipynb`](/demo.ipynb) for a quick tour of the data.

## How to reproduce this:

Check [`parse.ipynb`](parse.ipynb).

## Licence (code and open data)

Code is MIT license - basically you can do what you want with the code, just give this project credit for it. 

The data being reproduced here is assumed to be in the public domain. Aditionally, when I stated the purpose in the [FOI I filled with IMT](https://www.flaviosousa.co/pedido-accesso-dados-publicos/), no objection was made on the grounds of it being made public.

Acording to the [Open Data Directive](https://digital-strategy.ec.europa.eu/en/policies/open-data), countries are encouraged to make public data accessible, regardless of the end use:

> clearly obliged member states to ‘encourage public sector bodies and public undertakings to produce and make available documents [...] in accordance with the principle of “open by design and by default’’. 

[From wikipedia](https://en.wikipedia.org/wiki/Directive_on_the_re-use_of_public_sector_information#Open_data_licensing)

Here, "encouraging" is the key word. Given that no explicit consent or license was given, in principle there's always a chance that this project is using data beyond the scope of it's intended use. We hope to show that initiatives like this bring about positive changes and that they further encourage government bodies to release data with explicit [Open Data licenses](https://en.wikipedia.org/wiki/Directive_on_the_re-use_of_public_sector_information#Open_data_licensing)
