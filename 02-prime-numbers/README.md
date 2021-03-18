
02 – Prímszám tesztelés
---

### A feladat leírása

A feladat, hogy a kapott számokról eldöntsük, hogy prímszámok-e vagy sem.

Az _input_ egy szöveges fájl (pl. `basic-inputs.txt`). A számok
külön sorban szerepelnek, és egy sorban csak egy szám szerepel. Figyeljünk oda,
hogy a számok lehetnek _negatív_ vagy _tizedes tört_ számok is; amolyan
csapdaként.

Példa egy inputra:

```
1
2
3
4
11
-1
3.1415
```

Az _output_ pedig kiírás az _stdout_ra (`print(...)`) úgy,
hogy, ha az adott szám:
* **prímszám**, akkor írjuk ki magát a számot (pl. `2`) majd egy szünetjel
  (` `) után, hogy `1`; például ha az input a `2` volt, akkor az output
  legyen: `2 1`;
* **nem prímszám, de egész pozitív**, akkor írjnuk a szám és egy szünetjel után
  egy `0`-t; például ha az input az `1` volt, akkor az output legyen: `1 0`;
* **különben** írjnuk a szám és egy szünetjel után
  egy _kötőjelet_ (`-`); például ha az input az `1.45` volt, akkor az output
  legyen: `1.45 -`;

Példa outputra, az előző inputra nézve:

```
1 0
2 1
3 1
4 0
11 1
-1 -
3.1415 -
```
