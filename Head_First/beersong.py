
word = "Butelki"

for beer_num in range(7, 0, -1):
    print(beer_num, word, "Piwa na ścianie.")
    print(beer_num, word, "Piwa.")
    print("Jedno weź.")
    print("podaj w koło.")
    if beer_num == 1:
        print("nie ma już butelek piwa na ścianie.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "Butelka."
         print(new_num, word, "Piwa na ścianie.")
    print()
print("Do jutra")
