import time_to_sort as T
import print_time as P
import csv


tab = T.time_to_sort ()
print(tab)
P.print_time(tab)

with open('data2.csv','w',newline='') as fichiercsv:
    writer=csv.writer(fichiercsv)
    i = 0
    while i < len(tab):
        writer.writerow([tab[i]])
        i+=1
