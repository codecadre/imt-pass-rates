## What's this

IMT pass rates from 2015-2020 parsed and ready to use in a jupyter notebook. **Check the [demo](/demo.ipynb)**.

This was originally done for [passaprimeira.xyz](https://www.passaprimeira.xyz).

## Background

[passaprimeira.xyz](https://www.passaprimeira.xyz) is the second iteration of a project that aims at bringing transparency to the driving school business in Portugal, by crossing public data and presenting it in an accessible format. Originally it was only a web app, but we decided to release some of the data and code, in a usable way, so that others could benefit form it.

TODO: reframe
If you want to read more about how a freedom of information act might have helped release this data or not, check [my blog](https://www.flaviosousa.co/pedido-accesso-dados-publicos/) for some background story.

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

## Licence

TODO

GPL2 maybe
MIT Maybe
