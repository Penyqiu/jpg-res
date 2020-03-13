def jpeg_res(filename):
   # otwiera plik w trybie do odczytu
   with open(filename,'rb') as img_file:

       # podglada rozdzielczosc znajdujac ja na 164 bajcie
       img_file.seek(163)

       # odczyt
       a = img_file.read(2)

       # oblicz wysokosc
       height = (a[0] << 8) + a[1]

       # nastepne 2 bajty to szerokosc
       a = img_file.read(2)


       width = (a[0] << 8) + a[1]

   print("Rozdzielczosc zdjecia to:",width,"x",height)

jpeg_res("zdjecie.jpg")