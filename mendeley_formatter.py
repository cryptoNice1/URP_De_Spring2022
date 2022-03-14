# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:39:31 2022

@author: Melanie
"""
f = open("final_citations2.txt","w")

for line in open("special_citations.txt"):
    text = line.strip()
    
    #beginning text will be the citation label, allowing it to be found in the text itself
    label = text[:text.find(".")]
    if text[text.find(".")+3] != "." and text[0] == "K":
        authors = text[text.find(".")+2:text.find("(")-1].replace("&","",1).replace(".,",". and")
        year = text[text.find("(")+1:text.find(")")]
        
        text = text[text.find(")")+2:]
        title = text[:text.find(".")]
        
        
        for i,s in enumerate(text): 
            if s.isdigit(): break
        journal = text[text.find(".")+2:i-2]
        
        if text.find("(") == -1:
            volume = text[text.find(",")+2:text.rfind(",")]
            number = ""
        else:
            volume = text[text.find(",")+2:text.find("(")]
            number = text[text.find("(")+1:text.find(")")]
        pages = text[text.rfind(",")+2:-1]
    else:
        print(line)
        continue
    
    
    ordering = [("title",title),("author", authors),("journal",journal),("volume",volume),("number",number),("pages",pages),("year",year)]
    final = "@article{"+label+","+"\n"
    
    f.write("@article{"+label+",\n")
    for o in ordering:
        f.write(o[0]+"={"+o[1]+"},\n")
    f.write("}\n\n")
    
f.close()