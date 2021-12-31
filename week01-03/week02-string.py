Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'python'[0]
'p'
>>> //첨자를 이용한 문자열의 문자 참조
SyntaxError: invalid syntax
>>> _첨자
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    _첨자
NameError: name '_첨자' is not defined
>>> #첨자를 이용한 문자열의 문자 참조
>>> /*첨자*/
SyntaxError: invalid syntax
>>> 
====================================== RESTART: Shell ======================================
>>> host cls
SyntaxError: invalid syntax
>>> str = 'Hello python!'
>>> n = len(str)
>>> print('문자열', str, '길이', n)
문자열 Hello python! 길이 13
>>> print('첫 문자', str[0], str[-n])
첫 문자 H H
>>> print('가운데 문자', str[n//2], str[-n//2])
가운데 문자 p p
>>> print('마지막 문자', str[n-1], str[-1])
마지막 문자 ! !
>>> 
====================================== RESTART: Shell ======================================
>>> str = 'Monty Python'
>>> len(str)
12
>>> str[0:5], str[6:], str[6:12]
('Monty', 'Python', 'Python')
>>> str[-12:-7], str[-6:], str[-6:0]
('Monty', 'Python', '')
>>> str[0:-6]
'Monty '
>>> 
====================================== RESTART: Shell ======================================
>>> str = '일요일 기러기'
>>> print(str[:3]. str[4:]) # 양수 이용
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(str[:3]. str[4:]) # 양수 이용
AttributeError: 'str' object has no attribute 'str'
>>> #양수이용
>>> print(str[:3]. str[4:]) #양수 이용
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(str[:3]. str[4:]) #양수 이용
AttributeError: 'str' object has no attribute 'str'
>>> print(str[:3], str[4:]) #양수 이용
일요일 기러기
>>> print(str[::-2]) #역순으로 한 문자씩 건너뛰기
기기일일
>>> /'
SyntaxError: invalid syntax
>>> print('// /' /" /a /b /n')
      
SyntaxError: EOL while scanning string literal
>>> 
====================================== RESTART: Shell ======================================
>>> value = input('실수(세 자리.두 자리로 345.78처럼)를 하나 입력하세요. >>')
실수(세 자리.두 자리로 345.78처럼)를 하나 입력하세요. >>345.78
>>> num = value.replace('.', '')
>>> sum = 0
>>> n = 0
>>> for (n = 0; n < 5; n++) {
	
SyntaxError: invalid syntax
>>> sum += int(num[0])
>>> sum += int(num[1])
>>> sum += int(num[2])
>>> sum += int(num[3])
>>> sum += int(num[4])
>>> print('입력값:', value)
입력값: 345.78
>>> print('모든 자릿수 합:', sum)
모든 자릿수 합: 27
>>> '->'join(num)
SyntaxError: invalid syntax
>>> '->'.join(num)
'3->4->5->7->8'
>>> 