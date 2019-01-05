#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 14:34:38 2018

@author: yiyunwu
"""
from tkinter import *


def ReadFiles(file_name):
    file1=open(file_name,"r")
    text=[]
    #temp_text=file1.readlines()
    #temp_text=temp_text.split()
    for line in file1:
        lines=[]
        temp_line=line.lower().split()
        for word in temp_line:
            temp_word=word.strip('()-+,.;:*\!""''^%#`~?/<>{}[]|')
            if '-' in temp_word:
                temp_word=temp_word.replace('-',' ')
                temp_word2=temp_word.split()
                for i in range(len(temp_word2)):
                    lines.append(temp_word2[i])
            else:
                lines.append(temp_word)
        text.append(lines)
    file1.close()
    return text

def DataBase(filename):
    file2=open(filename,"r")
    sum_files=[]
    for name in file2:
        #print(name)
        temp_name=name.strip('\n')
        temp_text=ReadFiles(temp_name)
        sum_files.append(temp_text)
    file2.close()
    return sum_files

def InvertedIndex(database):
    dictionary={}
    file_num=len(database)
    for i in range(0,file_num):
        for j in range(len(database[i])):
            for word in database[i][j]:
                doc=[0 for i in range(file_num)]
                if word!="" and (word in dictionary):
                    num=dictionary[word][i]
                    dictionary[word][i]=num+1
                elif word!="":
                    dictionary[word]=doc
                    dictionary[word][i]=1
    return dictionary
             
def Search(word_location,dictionary):
    #lbl = Label(window, text="Hello") 
    #lbl.grid(column=0, row=0) 
    #btn = button(window, text="Click Me") 
    #btn.grid(column=1, row=0) 
    #window.mainloop()
    
    signal=1
    while(signal==1):
        print('\n1.search a word\n2.seach adjacent words\n3.search not adjacent words\n4.search a partial term\n5.highlight terms\n6. quit')
        choice=input('\nPlease enter your choice:')
        if choice=='1':
            filename=[i for i in range(1,len(word_location)+1)]
            term=input('\nPlease enter the term you want to choose:')
            term=term.lower()
            if term in dictionary:
                length=len(dictionary[term])
                freq=dictionary[term]
                for i in range(0,length):
                    for j in range(i+1,length):
                        if freq[i]<freq[j]:
                            temp=freq[i]
                            freq[i]=freq[j]
                            freq[j]=temp
                            temp2=filename[i]
                            filename[i]=filename[j]
                            filename[j]=temp2
                print('\nThe result is:')
                print('\n',filename)
                print('\n',freq)
            else:
                print('\nCannot find the term you search.')
        elif choice=='2':
            signal2=0
            adj_freq=[0 for i in range(0,len(word_location))]
            filename=[i for i in range(1,len(word_location)+1)]
            term=input('\nPlease enter the term you want to choose:')
            term=term.lower()
            search_words=term.split()
            for i in range(0,len(word_location)):
                for j in range(len(word_location[i])):
                    for k in range(len(word_location[i][j])):
                        if word_location[i][j][k]==search_words[0] and word_location[i][j][k+1]==search_words[1]:
                            adj_freq[i]=adj_freq[i]+1
                            signal2=1
            for i in range(0,len(word_location)):
                for j in range(i+1,len(word_location)):
                    if adj_freq[i]<adj_freq[j]:
                        temp=adj_freq[i]
                        adj_freq[i]=adj_freq[j]
                        adj_freq[j]=temp
                        temp2=filename[i]
                        filename[i]=filename[j]
                        filename[j]=temp2
            if signal2==1:
                print('\nThe result is:')
                print('\n',filename)
                print('\n',adj_freq)
            else:
                print('\nCannot find the terms you search.')
        elif choice=='3':
            term=input('\nPlease enter the term you want to choose:')
            term=term.lower()
            search_words=term.split()
            signal3=0
            signal4=0
            filename1=[i for i in range(1,len(word_location)+1)]
            filename2=[i for i in range(1,len(word_location)+1)]
            for i in range(0,len(word_location)):
                for j in range(len(word_location[i])):
                    for k in range(len(word_location[i][j])):
                        if word_location[i][j][k]==search_words[0]:
                            signal3=1
                        if word_location[i][j][k]==search_words[2]:
                            signal4=1
            if signal3==1 and signal4==1:
                freq1=dictionary[search_words[0]]
                freq2=dictionary[search_words[2]]
            for i in range(0,len(word_location)):
                for j in range(i+1,len(word_location)):
                    if freq1[i]<freq1[j]:
                        temp=freq1[i]
                        freq1[i]=freq1[j]
                        freq1[j]=temp
                        temp2=filename1[i]
                        filename1[i]=filename1[j]
                        filename1[j]=temp2
            for i in range(0,len(word_location)):
                for j in range(i+1,len(word_location)):
                    if freq2[i]<freq2[j]:
                        temp=freq2[i]
                        freq2[i]=freq2[j]
                        freq2[j]=temp
                        temp2=filename2[i]
                        filename2[i]=filename2[j]
                        filename2[j]=temp2
            if signal3==1 and signal4==1:
                print('\nThe result is:\n')
                print('\n',filename1)
                print('\n',freq1)
                print('\n',filename2)
                print('\n',freq2)
            else:
                print("\nCannot find!")
        elif choice=='4':
            signal5=0
            term=input('\nPlease enter the term you want to choose:')
            term=term.lower()
            filename=[i for i in range(1,len(word_location)+1)]
            for key in dictionary:
                temp_str=key[0:len(term)]
                if temp_str==term:
                    freq=dictionary[key]
                    signal5=1
            for i in range(0,len(word_location)):
                for j in range(i+1,len(word_location)):
                    if freq[i]<freq[j]:
                        temp=freq[i]
                        freq[i]=freq[j]
                        freq[j]=temp
                        temp2=filename[i]
                        filename[i]=filename[j]
                        filename[j]=temp2
            if signal5==1:
                print('\nThe result is:\n')
                print('\n',filename)
                print('\n',freq)
            else:
                print("\nCannot find!")
            
        #elif choice==5:
            
        else:
            signal=0

            
       
text=DataBase("file-name.txt")
dic=InvertedIndex(text)
Search(text,dic)