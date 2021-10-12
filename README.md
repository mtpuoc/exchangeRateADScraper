# Pràctica 1: Web scraping
Aquest treball s'ha realitzat per una pràctica de l'assignatura _Tipologia i cicle de vida de les dades_ del 
Màster en Ciència de dades de la Universitat Oberta de Catalunya. 
El treball es centra en aplicar les tècniques de web scraping per a recuperar la informació del preu de la moneda que es publica mensualment 
al butlleti oficial i poder centralitzar-ho tota aquesta informació en un dataset. També hi ha un python per a poder fer un analisis inicial 
i poder aplicar unes técniques o revisar si esta dintre dels termes legals.


## Primers passos
Per poder utilitzar **el projecte exchangeRateADScraper** es necessita tenir instalat les següents llibreries:
````
pip install python-whois
pip install builtwith
````

## Estructura del projecte
El projecte conte les següents carpetes:
* **docs/**: Aquesta carpeta conté dos fitxers: el PDF amb les preguntes que demana la pràctica i l'altre el fitxer CSV que ha generat el proces python.
* **src/**: Aquesta carpeta conté els procesos de python per a poder generar el fitxer CSV amb la informació que s'ha recuperat de la web. Al punt següent s'entrara en detall dels fitxers python.
* **test/**: Aquesta carpeta conté proves que s'han realitzat per detectar errors i analitzar el funcionament de algunes funcions.

### Fitxers python
Dintre de la carpeta de source(src) hi ha els següents pythons:
1. **main.py** es el proces principal per executar
2. **avaluation.py**
3. **csvfile**
4. **global_vars**
5. **functions**
6. **vars**
## Execució programa
````
python main.py <action:(scraping|analize)>
````
## Persones del equip
El projecte ha sigut realitzat per Marc T.





