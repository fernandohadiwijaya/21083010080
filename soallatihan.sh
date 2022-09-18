#!/bin/bash
Showroom="Showroom Motor Bekas Berkualitas"

echo "siapa namamu?"

read nama
printf "halo kak $nama!\n"
printf "Selamat Datang di $Showroom ?\n"
printf "motor bekas apa yang ingin anda cari?\n"
printf "Honda PCX ?\n"
printf "Yamaha NMAX ?\n"
printf "Yamaha Aerox ?\n"
printf "Honda ADV ?\n"

read motor

case "$motor" in
  "Honda PCX")
    echo "Untuk motor ini ada beberapa pilihan menarik "
    ;;
  "Yamaha NMAX")
    echo "Untuk motor ini stok hanya tersedia 1 saja"
    ;;
  "Yamaha Aerox")
    echo "Untuk motor ini stock kosong"
    ;;
  "Honda ADV")
    echo "Untuk motor ini tinggal stock apa adanya"
    ;;
  *)
    echo "Mohon maaf motor yang anda cari kami tidak tersedia"
    ;;
esac
