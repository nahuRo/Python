# control de flujo
# if, elif, else

x = 2

if x > 10:
    print(f"{x} es mayor a 10")
elif x < 10:
    print(f"{x} es menor a 10")
else:
    print(f"{x} es igual a 10")


# match es como el switch

serie = "N-02"

match serie:
    case "N-01":
        print("samsung")
    case "N-02":
        print("nokia")
    case "N-03":
        print("lg")
    case "N-04":
        print("motorola")
