with open("cumle.txt", "w") as f:
    f.write("Birinci cumle ucun olan hisse\nbu da ikinci cümle ucun olan hisse.")


with open("cumle.txt", "r") as f:
    ilk_setir = f.readline()

    boyuk_herfler = ilk_setir.upper()

with open("boyuk_herfler.txt", "w") as f:
    f.write(boyuk_herfler)
