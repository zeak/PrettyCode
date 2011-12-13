#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       pretty-code.py
#       
#       Copyright 2011 akshay <akshay@akshay-laptop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       

import requests
import argparse

def prettyPrint(sCode):
	try:
		prettyData = requests.post('http://prettyprinter.de/module.php?name=PrettyPrinter',
			data={'source':sCode, 'addnewlines':'on','skiphtml':'on'}).content.replace(u'&lt;','<').replace(u'&gt',u'>')
	except Exception:
		print "Error Reacing the Pretty Server"
		return ''
	code = prettyData
	return code

def main():
	parser = argparse.ArgumentParser(description='Pretty Print C++ Code',\
		epilog = 'Small Hackish script by akshay(akshay.is.gr8@gmail.com)')
	
	parser.add_argument('File',help='Specify a file to prettify')
	
	parser.add_argument('-o',dest='outfile', help='Send Pretty Code to Specified File', \
			nargs='?',default = None )
	args = parser.parse_args()
	try:
		code = open(args.File,'r').read()
	except Exception:
		print args.File
		print "An Error Occured While Reading The Specified File"
		return 0
	
	pCode = prettyPrint(code)
	if args.outfile is not None:
		try:
			oFile = open(args.outfile,'w')
		except Exception:
			print "A Error Occured While Writing the File"
			return 0 
		oFile.write(pCode)
	else:
		print pCode
	return 1


if __name__ == '__main__':
	main()

