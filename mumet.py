Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama ='Muhammad Saiful Mujab'
>>> NIM ='L200180139'
>>> x ='1' + NIM[7:]
>>> a = int(x)
>>> b =len(Nama)
>>> type(a)
<type 'int'>
>>> #artinya a memiliki variabel integer atau bilangan bulat
>>> type(b)
<type 'int'>
>>> #artinya b memiliki variabel integer atau bilangan bulat
>>> a/b
54
>>> 10*(a-999)
1400
>>> #variabel a dikurangi 999 dikali 10 = 1400
>>> b**2
441
>>> #variabel b jika dpangkat = 441
>>> a%b
5
>>> #sisa hasil bagi a dibagi b adalah 11
>>> C = 12.5
>>> type(c)

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    type(c)
NameError: name 'c' is not defined
>>> C = 12.5
>>> type(C)
<type 'float'>
>>> a/c

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a/c
NameError: name 'c' is not defined
>>> a/C
91.12
>>> a//C
91.0
>>> a%C
1.5
>>> 
>>> C > b
False
>>> type(C > b)
<type 'bool'>
>>> a > b and b >C
True
>>> a > 1100 or b < 10
True
>>> Nama = 'Muhammad Saiful Mujab'
>>> NIM ='139'
>>> Tinggi ='165'
>>> Berat ='62'
>>> TahunLahir ='2000'
>>> Aku =(TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data =(TahunLahir, Berat, Tinggi, NIM, Nama)
>>> type(Aku)
<type 'tuple'>
>>> Aku(0)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    Aku(0)
TypeError: 'tuple' object is not callable
>>> Aku[0]
'2000'
>>> a = NIM%4 ; Aku[a]

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a = NIM%4 ; Aku[a]
TypeError: not all arguments converted during string formatting
>>> a =NIM % 4 ; Aku[a]

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a =NIM % 4 ; Aku[a]
TypeError: not all arguments converted during string formatting
>>> a =NIM % 4 ; Aku[0]

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a =NIM % 4 ; Aku[0]
TypeError: not all arguments converted during string formatting
>>> Aku[0]
'2000'
>>> a = NIM % 4; Aku[a]

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a = NIM % 4; Aku[a]
TypeError: not all arguments converted during string formatting
>>> a = NIM%4 ; Aku [a]

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a = NIM%4 ; Aku [a]
TypeError: not all arguments converted during string formatting
>>> Nama ='Muhammad Saiful Mujab'
>>> NIM =139
>>> Tinggi =165
>>> Berat =60
>>> TahunLahir =2000
>>> Aku =(TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data =(TahunLahir, berat, Tinggi, NIM, Nama)

Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    Data =(TahunLahir, berat, Tinggi, NIM, Nama)
NameError: name 'berat' is not defined
>>> Data =[TahunLahir, Berat, Tinggi, NIM, Nama)
SyntaxError: invalid syntax
>>> Data =(TahunLahir, Berat, Tinggi, NIM, Nama)
>>> type(Aku)
<type 'tuple'>
>>> Aku[0]
2000
>>> a = NIM % 4; Aku[a]
139
>>> type(Aku[a])
<type 'int'>
>>> Aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #objek dalam tuple tidak bisa diganti
>>> type(data)

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    type(data)
NameError: name 'data' is not defined
>>> type(Data)
<type 'tuple'>
>>> type(Data[4])
<type 'str'>
>>> Data[4][5]
'm'
>>> Data[4][a;6]
SyntaxError: invalid syntax
>>> Data[4]
'Muhammad Saiful Mujab'
>>> Data[5]

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    Data[5]
IndexError: tuple index out of range
>>> NIM%4
3
>>> Data[4][a:6]
'amm'
>>> Data[0] = 'ok' ; Data

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    Data[0] = 'ok' ; Data
TypeError: 'tuple' object does not support item assignment
>>> a
3
>>> Data[0] = 'ok' ; Data

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    Data[0] = 'ok' ; Data
TypeError: 'tuple' object does not support item assignment
>>> Data[0]='ok';Data

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    Data[0]='ok';Data
TypeError: 'tuple' object does not support item assignment
>>> Data = [TahunLahir , Berat, Tinggi, NIM, Nama]
>>> Data[0] = 'ok' ; Data
['ok', 60, 165, 139, 'Muhammad Saiful Mujab']
>>> Data [-a]
165
>>> range(a)
[0, 1, 2]
>>> <type 'tuple'>
SyntaxError: invalid syntax
>>> Nama ='Muhammad Saiful Mujab'
>>> NIM =139
>>> Tinggi =165
>>> Berat =60
>>> TahunLahir =2000
>>> Aku =(TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data =[TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<type 'tuple'>
>>> #artinya aku adalah tuple atau deretan objek
>>> Aku[0]
2000
>>> #artinya data ke-0 dalam tuple Aku adalah TahunLahir
>>> a =NIM%4 ; Aku[a]
139
>>> #sisa hasil bagi NIM dibagi 4=3, jadi data ke 3 pada
>>> type(Aku[a])
<type 'int'>
>>> #data ke 3 dalam tuple adalah integer atau bilangan bulat
>>> Aku(Aku[4])

Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    Aku(Aku[4])
TypeError: 'tuple' object is not callable
>>> Aku [a:4]
(139,)
>>> #data dari a ke 4 adalah 139
>>> type(Aku[4])
<type 'str'>
>>> #data ke 4 dalam aku merupakan string
>>> Aku[0] ='ok'

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    Aku[0] ='ok'
TypeError: 'tuple' object does not support item assignment
>>> #objek didalam type data tuple tidak dapat diganti
>>> type(Data)
<type 'list'>
>>> #data adalah list
>>> type(data[4])

Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    type(data[4])
NameError: name 'data' is not defined
>>> type(Data[4])
<type 'str'>
>>> #data ke 4 adalah string (nama)
>>> Data[4][5]
'm'
>>> Data[4]
'Muhammad Saiful Mujab'
>>> Data[5]

Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    Data[5]
IndexError: list index out of range
>>> #baris index tidak boleh keluar dari urutan
>>> a =NIM%4
>>> Data[4][a:6]
'amm'
>>> #data ke 4 slicing ke a-6 adalah amm
>>> a
3
>>> Data[0]='ok';Data
['ok', 60, 165, 139, 'Muhammad Saiful Mujab']
>>> #data ke 0 diganti string ok
>>> Data[-a]
165
>>> #artinya data ke a kurangi 1=165
>>> range(a)
[0, 1, 2]
>>> #jarak/cukupan sampai ke a adalah 0,1,2
