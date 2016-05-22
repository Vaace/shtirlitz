__author__ = ' not Timofey Khirianov'
# -*- coding: utf8 -*-
import argparse
import sys
from random import *


class Atbash:
	alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

	def __init__(self):
		lowercase_code = {self.alphabet[i]:self.alphabet[-i-1] for i in range(len(self.alphabet))}
		uppercase_code = {self.alphabet[i].upper():self.alphabet[-i-1].upper() for i in range(len(self.alphabet))}
		lowercase_decode = {self.alphabet[-i-1]:self.alphabet[i] for i in range(len(self.alphabet))}
		uppercase_decode = {self.alphabet[-i-1].upper():self.alphabet[i].upper() for i in range(len(self.alphabet))}
		self._encode = dict(lowercase_code)
		self._encode.update(uppercase_code)
		self._decode = dict(lowercase_decode)
		self._decode.update(uppercase_decode)
		

	def encode(self, line):
		if len(line) == 1:
			return self._encode[line] if line in self._encode else line
		else:
			return ''.join([self.encode(char) for char in line])

	def decode_it(self, line):
		if len(line) == 1:
			return self._decode[line] if line in self._decode else line
		else:
			return ''.join([self.decode_it(char) for char in line]) 
			

class Caesar:
    global alphabet
    alphabet = "ЯяЮюЭэЬьЫыЪъЩщШшЧчЦцХхФфУуТтСсРрПпОоНнМмЛлКкЙйИиЗзЖжЁёЕеДдГгВвБбАа"
    global key
    key = -32

    def __init__(self):
        self.alphabet = alphabet
        lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
        uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
        self._encode = dict(lowercase_code)
        self._encode.update(uppercase_code)
        self._decode = {}


    def encode(self, line):
        if len(line) == 1:
            return self._encode[line] if line in self._encode else line
        else:
            return ''.join([self.encode(char) for char in line])


    def decode(self, line):
        self.line = line
        translated = ''
        for symbol in self.line:
            if symbol in alphabet:
                num = alphabet.find(symbol)

                num = num +key
                if num >= len(alphabet):
                    num = num - len(alphabet)
                elif num < 0:
                    num = num + len(alphabet)
                translated = translated + alphabet[num]
        return translated



#--------------------------------
parser = argparse.ArgumentParser(
	description = 'Шифратор'
)
parser.add_argument(
	'-e',
	'--encode',
	action = 'store_true',
	help = 'Закодировать текст'
)
parser.add_argument(
	'-d',
	'--decode',
	action = 'store_true',
	help = 'Декодировать текст'
)
parser.add_argument(
	'filename',
	metavar = 'FILENAME',
	type = str,
	help = 'Имя входного файла'
)
parser.add_argument(
	'cipher',
	metavar = 'CIPHERTYPE',
	type = str,
	help = 'Тип шифра: напишите Atbash, если хотите использовать этот шифр, и Caesar, если хотите пользоваться шифром Цезаря'
)
#--------------------------------
args = parser.parse_args()
if not args.encode and not args.decode:
	print('Должен быть указан хотя бы один из параметров -e и -d', file = sys.stderr)
	sys.exit(-1)

input = open("input.txt",'r', encoding="utf8")
		
if 	args.cipher == 'Atbash':
	cipher = Atbash()
	if args.encode:
		encode_output = open('encoded_atbash.txt','w')
		print('---------------------------------------------------', file = encode_output)
		line = input.readline().rstrip()
		while line != '':
			print(cipher.encode(line), file = encode_output)
			line = input.readline().rstrip()
	if args.decode:
		decode_output = open('decoded_atbash.txt','w')
		print('---------------------------------------------------', file = decode_output)
		line = input.readline().rstrip()
		while line != '':
			print(cipher.decode_it(line), file = decode_output)
			line = input.readline().rstrip()
		
elif args.cipher == 'Caesar':
	cipher = Caesar()
	if args.encode:
		encode_output = open('encoded_caesar.txt','w')
		print('---------------------------------------------------', file = encode_output)
		line = input.readline().rstrip()
		while line != '':
			print(cipher.encode(line), file = encode_output)
			line = input.readline().rstrip()
		encode_output.close()
		print('Key is', key)
	if args.decode:
		caesar_output = open('caesar_decoded.txt', 'w')
		line = input.readline().rstrip()
		while line != '':
			print(cipher.decode(line), file = caesar_output)
			line = input.readline().rstrip()
		encode_output.close()
input.close()
output.close()