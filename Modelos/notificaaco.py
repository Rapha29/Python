from win10toast import ToastNotifier as tn

while True:
    a = tn()
    b = "Alerta"
    c = "Isso é um alerta!"
    a.show_toast(b, c, duration=10)
    print(b,c)
    