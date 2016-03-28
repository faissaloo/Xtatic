Xtatic
===
Xtatic is a simple static site generator, just give it a directory and it will
crawl through all the subdirectories, looking for any .config files.
.config files look like this:  
```
template=./template.html
programName=Xtatic
description=<b>Xtatic</b> is a simple to use static site generator
```  
Note that everything is whitespace sensitive and the HTML to replace the name
with must all be on one line.  
An example html template would look like this:  
```
<h1>Program: headerText</h1>
<p/>
bodyText
```  
and would turn into:  
```
<h1>Program: Xtatic</h1>
<p/>
<b>Xtatic</b> is a simple to use static site generator
```  
The html document generated will have the same name and directory as the .config
file, just with .config replaced with .html.  

To use, just go to the top directory where your files are located and run xtatic.py.
