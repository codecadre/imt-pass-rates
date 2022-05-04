## What's this

IMT pass rates from 2015-2020 parsed and ready to use in a jupyter notebook. Check the [demo](/demo.ipynb).

This was originally done for [passaprimeira.xyz](https://www.passaprimeira.xyz)

## Background

[passaprimeira.xyz](https://www.passaprimeira.xyz) is the second iteration of a project that aims at bringing transparency to the driving school business in Portugal, by crossing public data and presenting it in an accessible format. Originally it was only a web app, but we decided to release some of the data and code, in a usable way, so that others could benefit form it.

If you want to read more about how a freedom of information act might have helped release this data or not, check [my blog](https://www.flaviosousa.co/pedido-accesso-dados-publicos/) for some background story.

## Install
`pip3 install -r requirements.txt`

## Run
`~/.local/bin/jupyter-lab`

## How to use it

The entire data set can be found in

- [`data.json` ](result.json)
- `data.pkl`: Check `demo.ipynb` for a quick tour of the data.

## How to reproduce this:

Check [`parse.ipynb`](parse.ipynb).
