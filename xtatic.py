#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#####################################LICENCE####################################
#Copyright (c) 2016 Faissal Bensefia
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
################################################################################
import os
def replaceDict(string,di):
    for i in di:
        string=string.replace(i,di[i])
    return string

def createoutput(indict,fname):
    if "template" in indict:
        template=indict.pop("template").lstrip()
    else:
        print("Error: "+fname+" does not define a template")
        exit()
    with open(fname[:-6]+"html",'w') as file:
        file.write(replaceDict(open(template).read(),indict))
        print("Created "+fname[:-6]+"html")

def parseconfig(config):
    variables={}
    with open(config,'r') as file:
        for i in file:
            currentline=i.split("=",1)
            if len(currentline)>1:
                variables[currentline[0]]=currentline[1][:-1]
    createoutput(variables,config)

startingdir=os.path.abspath(".")
for i in os.walk("."):
    for ii in i[2]:
        if ii[-7:]==".config":
            print("Processing "+os.path.join(i[0],ii))
            os.chdir(i[0])
            parseconfig(ii)
