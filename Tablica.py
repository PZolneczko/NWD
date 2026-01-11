def znajdz_max(tablica):
    if len(tablica) == 0:
        return None

    max_wartosc = tablica[0]
    for element in tablica:
        if element > max_wartosc:
            max_wartosc = element

    return max_wartosc


liczby = [3, 1, 4, 1, 5, 9, 2, 6]
print(znajdz_max(liczby))
