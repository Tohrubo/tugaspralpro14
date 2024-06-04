import re
import datetime as dati

sentence = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawanasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)"

dt = re.findall("\d{4}-\d{2}-\d{2}", sentence)

dtnow = dati.datetime.now()

for dates in dt:
    ymd = dates.split("-")
    dtthen = dati.datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]))
    print(f"{dtthen} selisih {(dtnow-dtthen).days} hari")