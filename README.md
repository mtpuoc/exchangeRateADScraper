# Pràctica 1: Web scraping
Aquest treball s'ha realitzat per una pràctica de l'assignatura _Tipologia i cicle de vida de les dades_ del 
Màster en Ciència de dades de la Universitat Oberta de Catalunya. 
El treball es centra en aplicar les tècniques de web scraping per a recuperar la informació del preu de la moneda que es publica mensualment 
al butlleti oficial i poder centralitzar-ho tota aquesta informació en un dataset. També hi ha un python per a poder fer un analisis inicial 
i poder aplicar certes técniques o revisar si esta dintre dels termes legals.


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
* **test/**: Aquesta carpeta conté proves que s'han realitzat per detectar errors i analitzar el funcionament de les funcions.

### Fitxers python
Dintre de la carpeta de source(src) hi ha els següents pythons:
1. **main.py** és el proces principal per executar el projecte
2. **avaluation.py** és el proces inicial per analitzar la informació de la web, com per exemple els robots, whois, ...
3. **csvfile** és el proces on ens crear el CSV amb la informació que s'ha tret de la web
4. **global_vars** és un python on hi ha variables globals que s'utilitzen en el programa
   1. Cal destacar que la variable **is_developing** indica si es **TRUE** que consulta directament a la web, si es **FALSE** no realitza cap petició al servidor sino que unicament consulta el fitxer de html_webs 
5. **functions** és un python on hi ha les funcions que s'utilizen en el programa
6. **html_webs** és un fitxer on hi ha dos variables on hi ha el contigut HTML de cada web que s'utilitza pel web scraping

## Execució programa
````
python main.py <action:(scraping|analize)>
````
## Persones del equip
El projecte ha sigut realitzat per Marc T.





