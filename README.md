Ostolaskuohjeen käyttö
======================

Raakateksti on tiedostossa `6aika-ostolaskuohje.md`.

`md2pdf.py` on yksinkertainen Python-skripti, jolla markdown-muotoisesta
.md-tiedostosta saa PDF-tiedoston käyttäen välimuotona HTML:ää. 
Tyylit on määritelty tiedostossa `6aika.css`.


Mac Os X järjestelmässä PDF:n voi tuottaa asentamalla tarvittavat 
kirjastot alla olevilla komennoilla:

```
brew install wkhtmltopdf
mkvirtualenv -p /usr/local/bin/python2.7 6aika
pip install --upgrade pip
pip install wkhtmltopdf pdfkit markdown
python md2pdf.py
```
