# Lotta NC ohjelmia

## tool-length.nc

OHJE: korvaa rivillä 4 oleva Rxxxxxxx seuraavalla arvolla:
Coordinate set NO.00 - mittapuikon/piipparin ym paksuus ja muunna tulos mikrometreiksi.
Esim 328.183 - 5.00 = 323.183 -> 323183
(2.4.2021 piipparin korkeus 53,748mm)


rivi 4: `G65 H02 P#101 Q#5023 R323183`

### 5mm mittapuikolla:
328.183 - 5.00 = 323.183 -> 323183  
`R323183`

### Piipparilla
Korkeudeksi 2.4.2021 mitattu 53,748
328.183 - 53.748 = 274.435 -> 274435
`R274435`


