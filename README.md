Sundalang an interpreter written in python
===

## Requirements
- sly

## Installation
1. ```pip3 install sly```
2. clone this repo ```git clone https://github.com/reorr/2018-programming-language-series```
3. to run the interpreter use ```python3 main.py``` command.

## Syntax
| Syntax | In english |
| --- | --- |
| UPAMI | IF |
| SATULUNYA | THEN |
| SEDANGKEUN | ELSE |
| KEUR | FOR |
| PUNGSI | FUN |
| KA | TO |
| CETAK | PRINT |

### Examples
```
sundalang » CETAK 4+2
sundalang » 6
sundalang » KEUR c=0 KA 10 SATULUNYA CETAK c
0
1
2
3
4
5
6
7
8
9
sundalang » 
```

You can also feed plain text file to main.py

Create `example.snd`
```
b=2
a=8

CETAK a+2

KEUR c=0 KA a SATULUNYA CETAK c

UPAMI a==8 SATULUNYA CETAK a SEDANGKEUN CETAK a+1

PUNGSI anu() -> UPAMI a==6 SATULUNYA CETAK a SEDANGKEUN CETAK a+1

anu()

CETAK "a"
```
Feed `example.snd` to main.py
```
$ python3 main.py example.snd
10
0
1
2
3
4
5
6
7
8
9
a
$
```