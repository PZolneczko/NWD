def bubbleSort(tablica):
    n = len(tablica)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 

            if tablica[j] > tablica[j+1] :
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
 

tablica = [64, 34, 25, 12, 22, 11, 90]
 
bubbleSort(tablica)
 
print ("Posortowana tablica to:")
for i in range(len(tablica)):
    print ("%d" %tablica[i])
