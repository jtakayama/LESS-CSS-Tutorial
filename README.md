LESS-CSS-Tutorial
=================

A repository for A13 (an ICS 691 course assignment).<br/>
This is an Eclipse IDE "static web content" project.<br/>

Disclaimers
-----------
All .html, .css, and .less code is based on 
http://www.hongkiat.com/blog/less-css-tutorial-design-slick-menu-nav-bar/.

To download lessc and the less javascript, see http://lesscss.org/.<br/>
To download prefix-free, see http://leaverou.github.com/prefixfree/.<br/>

This project is licensed under the 2-clause BSD license (see README.md).<br/>

Directory hierarchy
-------------------
/LESS-CSS-Tutorial<br/>
&nbsp;&nbsp;&nbsp;&nbsp;/WebContent<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/css<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/js<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/less<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/python<br/>

WebContent contains the .html pages. index.html is dependent on the .less
files, while index_css_version.html is dependent on the .css files generated
by less.

/css contains the .css generated from the .less scripts.
/js contains Javascript files for less and prefix-free.
/less contains .less scripts.
/python contains the lesscopy.py script. This invokes the lessc compiler
    on all .less scripts in /less and copies the .css output to the /css 
    directory using Linux/Unix system commands.

A Python interpreter is required to use the python script.
Lessc is required to recompile the .less files into .css files.
