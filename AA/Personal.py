# Dane osobowe Alkoholika
import datetime

alkoholik = []

def enter():
    print("Wprowadź swoje dane")
    imie = input("Podaj imię : ")
    nazwisko = input("Podaj nazwisko : ")
    print("Podaj datę urodzenia")
    rok_u = int(input("Podaj rok urodzenia : "))
    miesiac_u = int(input("Podaj miesiąc urodzenia : "))
    dzien_u = int(input("Podaj dzień urodzenia : "))
    data_u = datetime.date(rok_u, miesiac_u, dzien_u)
    print("Podaj przypuszczalną datę kiedy zacząłeś pić")
    rok_p = int(input("Podaj początkowy rok : "))
    miesiac_p = int(input("Podaj początkowy miesiąc : "))
    dzien_p = int(input("Podaj początkowy dzień : "))
    data_p = datetime.date(rok_p, miesiac_p, dzien_p)
    print("Podaj kiedy przestałeś pić")
    rok_k = int(input("Podaj końcowy rok : "))
    miesiac_k = int(input("Podaj końcowy miesiąc : "))
    dzien_k = int(input("Podaj końcowy dzień : "))
    data_k = datetime.date(rok_k, miesiac_k, dzien_k)
    osoba=(imie, nazwisko, data_u, data_p, data_u)
    alkoholik.append(osoba)
enter()
print(f"Twoje dane : {alkoholik} ")
