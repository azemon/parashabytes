#!/bin/bash

for book in Genesis Exodus Leviticus Numbers Deuteronomy
do
    wget -nv -O $book-hebrew.json "https://raw.githubusercontent.com/Sefaria/Sefaria-Export/master/json/Tanakh/Torah/$book/Hebrew/Tanach%20with%20Nikkud.json"
done
