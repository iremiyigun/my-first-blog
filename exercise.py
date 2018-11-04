C:\Users\User>cd Dekstop
Sistem belirtilen yolu bulamıyor.

C:\Users\User>cd Desktop

C:\Users\User\Desktop>cd
C:\Users\User\Desktop

C:\Users\User\Desktop>mkdir irem

C:\Users\User\Desktop>mkdir irem2

C:\Users\User\Desktop>cd irem2

C:\Users\User\Desktop\irem2>cd ..

C:\Users\User\Desktop>cd
C:\Users\User\Desktop

C:\Users\User\Desktop>del(irem2)
Could Not Find C:\Users\User\Desktop\(irem2)

C:\Users\User\Desktop>rmdir irem2

C:\Users\User\Desktop>cd irem2
Sistem belirtilen yolu bulamıyor.

C:\Users\User\Desktop>rmdir irem

C:\Users\User\Desktop>cd irem
Sistem belirtilen yolu bulamıyor.

C:\Users\User\Desktop>dir
 Volume in drive C is OS
 Volume Serial Number is C6D5-9CE3

 Directory of C:\Users\User\Desktop

04.11.2018  10:26    <DIR>          .
04.11.2018  10:26    <DIR>          ..
19.01.2018  10:26            52.721 2. grup M kitapçığı.docx
08.08.2018  13:29            18.470 ahmet bayram.docx
18.04.2018  13:29    <DIR>          asistan karnesi
04.11.2018  09:06    <DIR>          aöf
11.07.2018  12:01    <DIR>          boston
13.09.2018  01:00            44.649 bronkopulmoner displazi.docx
15.05.2018  04:32    <DIR>          DCIM
25.04.2018  22:04           524.288 denver el kitabı.doc
03.05.2018  12:00        28.057.559 endokrinoloji toplantısı, tpit sunumu.pptx
13.04.2018  14:10            13.673 espe abstract.docx
13.04.2018  17:51            14.230 espe abstractRevAo.docx
17.09.2018  22:55           134.684 ESPEposter dicle son.pptx
21.09.2018  00:40           107.762 ESPEposter.pptx
20.03.2018  01:26            75.928 grafikler.xlsx
18.04.2018  11:35           288.981 header-t.jpg
18.12.2017  04:05         1.941.427 hr ve cast.docx
16.02.2018  19:31    <DIR>          IBM SPSS Statistics (32bit) 21.0
08.08.2018  14:54    <DIR>          iphone fotolar
23.10.2018  22:24            65.183 izzet-tez.docx
11.07.2018  12:04    <DIR>          makaleler
04.09.2018  17:41            12.759 materyalist teori.docx
19.10.2018  09:22    <DIR>          mortalite kitapçığı 2016-17
17.04.2018  13:11    <DIR>          My EndNote Library.Data
07.09.2018  13:47            14.458 pcd genler.docx
26.06.2018  12:09    <DIR>          pcd makaleleri
11.09.2018  16:47            25.973 pcd.docx
24.02.2018  13:23    <DIR>          pediatri kurs
23.09.2018  12:44            15.725 pituitary-pitx.docx
19.10.2018  09:17    <DIR>          slayt
04.06.2015  14:30        10.395.648 slayt son hali.ppt
08.10.2018  18:30    <DIR>          tez
19.04.2018  15:31         9.137.766 untitled.png
19.03.2018  05:52            22.148 veriler.sav
23.02.2018  15:30        45.844.311 YILMAZ_BERAT.rar
20.09.2018  09:32    <DIR>          çalışmalar
              21 File(s)     96.808.343 bytes
              16 Dir(s)  189.279.227.904 bytes free

C:\Users\User\Desktop>phyton --version
'phyton' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\User\Desktop>python --version
Python 3.7.1

C:\Users\User\Desktop>cd ..

C:\Users\User>python
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD6
4)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+3
5
>>> 2**3
8
>>> "irem"
'irem'
>>> "irem"+" nasılsın"
'irem nasılsın'
>>> "irem "+"nasılsın"
'irem nasılsın'
>>> "irem nasılsın"
'irem nasılsın'
>>> "irem""nasılsın"
'iremnasılsın'
>>> "irem\""
'irem"'
>>> len("çel
  File "<stdin>", line 1
    len("çel
            ^
SyntaxError: EOL while scanning string literal
>>> len("çekoslavakyaklılaştıramadıklarımızdanmısınız")
44
>>> len(5667890ı)
  File "<stdin>", line 1
    len(5667890ı)
               ^
SyntaxError: invalid syntax
>>> len(4356789)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> len(35000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> len(str(35000))
5
>>> int('irem')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'irem'
>>> int('irem')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'irem'
>>> name= "irem"
>>> name
'irem'
>>> a= 4
>>> b= 6
>>> a*b
24
>>> neme
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'neme' is not defined
>>> city = "Tokyo"
>>> ciyt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ciyt' is not defined
>>> print(city)
Tokyo
>>> print(city*city)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
>>> print(Tokyo)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Tokyo' is not defined
>>> print("Tokyo")
Tokyo
>>> lottery= [3, 42, 12, 19, 30, 59]
>>> len(lottery)
6
>>> lottery.sort()
>>> print(lottery)
[3, 12, 19, 30, 42, 59]
>>> lottery.reverse()
>>> print(lottery)
[59, 42, 30, 19, 12, 3]
>>> print(lottery[0]]
  File "<stdin>", line 1
    print(lottery[0]]
                    ^
SyntaxError: invalid syntax
>>> print(lottery[0])
59
>>> print(lottery[5])
3
>>> print(lottery[6])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> lottery.pop(0)
59
>>> print(lottery)
[42, 30, 19, 12, 3]
>>> participants= {'name': 'irem', 'country': 'Türkiye', 'favorite_numbers': [8,
 12]
... participants= {'name': 'irem', 'country': 'Türkiye', 'favorite_numbers': [8,
 12]}
  File "<stdin>", line 2
    participants= {'name': 'irem', 'country': 'Türkiye', 'favorite_numbers': [8,
 12]}
               ^
SyntaxError: invalid syntax
>>> participants= {'name': 'irem', 'country': 'Türkiye', 'favorite_numbers': [8,
 12]}
>>> print(participants['name'])
irem
>>> participants['age']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
>>> participant['favorite_language']='Phyton'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'participant' is not defined
>>> participant['favorite_language']= 'Phyton'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'participant' is not defined
>>> participants['favorite_language']='Phyton'
>>>
>>> len(participants)
4
>>> del participants['favorite numbers']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'favorite numbers'
>>> del participants['favorit_ numbers']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'favorit_ numbers'
>>> del participants['favorite_ numbers']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'favorite_ numbers'
>>> del participants['favorite_ numbers']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'favorite_ numbers'
>>> del participants['favorite_ numbers']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'favorite_ numbers'
>>> print(participants)
{'name': 'irem', 'country': 'Türkiye', 'favorite_numbers': [8, 12], 'favorite_language': 'Phyton'}
>>> del participants['favorite_numbers']
>>> print(participants)
{'name': 'irem', 'country': 'Türkiye', 'favorite_language': 'Phyton'}
>>> 5>2
True
>>> 2>5
False
>>> 3<1
False
>>> 3==3
True
>>> 3==5
False
>>> 3!=5
True
>>> 5!=5
False
>>> x=3
>>> y=5
>>> x>y
False
>>> x=5
>>> x==y
True
>>> 6>=12/2
True
>>> 3<=2
False
>>> 6>2 and 5<9
True
>>> 7>14 or 6<12
True
>>> a = True
>>> a = True
>>> b = False
>>> 7>14
False
>>> a = 2>5
>>> a
False
>>> a = True
>>> b = False
>>> b = False
>>> a
True
>>> b
False
>>> a = 2>5
>>> a
False
>>> a = 2>5 and b = 5>7
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> a
False
>>> b
False
>>>
