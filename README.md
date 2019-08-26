# PyPRINSAS

Computer program for the processing and interpretation of small-angle scattering data tailored to the analysis of sedimentary rocks


It is replica of Windows program PRINSAS that takes as input raw (post-reduction) small-
angle neutron and small-angle X-ray scattering (SANS and SAXS) data
obtained from various worldwide facilities, displays the raw curves in interactive
log–log plots, and allows processing of the raw curves. Separate raw SANS and
ultra-small-angle neutron scattering (USANS) curves can be combined into
complete scattering curves for an individual sample. The combined curves can
be interpreted and information inferred about sample structure, using built-in
functions. These have been tailored for geological samples and other porous
media, and include the ability to obtain an arbitrary distribution of scatterer
sizes, the corresponding specific surface area of scatterers, and porosity (when
the scatterers are pores), assuming spherical scatterers. A fractal model may also
be assumed and the fractal dimension obtained. A utility for calculating
scattering length density from the component oxides is included in the program.

Source:  
Journal of Applied Crystallography  
ISSN 0021-8898  
PRINSAS – a Windows-based computer program for the processing and interpretation of small-angle scattering data tailored to the analysis of sedimentary rocks   
Alan L.Hinde   


## Download Prebuild Packages
  TODO(add dowload links to patches)

## System setup and Dependencies
  At first install [Anaconda](https://www.anaconda.com/)(Python3 version only)
  
  After that install next packages:
 - [PyQtGraph](http://www.pyqtgraph.org/) - GUI
 - [SciPy](https://www.scipy.org/) - Fitting and Analysis tool
 - [PyOpenGL](http://pyopengl.sourceforge.net/) - Dependencie of PyQtGraph
 - [Kivy](https://kivy.org/#home) - GUI. pip install kivy
 - [MySQL](https://www.tutorialspoint.com/python/python_database_access) - pip install mysqlclient
 
 
Dependecies for PyInstaller(if You would like to build executables):
 - PyGTK
 - PyQt5
 
There easiest way to install above tools is using __pip__ tool from command prompt(it comes with Anaconda package).
>Note: if command pompt says that __pip__ command isn't recognized(even Anaconda is installed) then you have to modify Path Environmental Variable, with appending location to pip tool(which is placed in folder Scripts of Anaconda installation root folder)

pip install PyOpenGL PyOpenGL_accelerate pyqtgraph


## Making of Stand Alone app from Python project

Run

> pyinstaller main.py

If You encountered error "recursive call depth exceeded", then run next command:

> pyinstaller main.py

it will create main.spec file and add next lines to its beginning:

>import sys  
>sys.setrecursionlimit(5000)#or bigger number

and finally run:

> pyinstaller main.spec

#### UPD:
I decided to use the most basic GUI library - Tinker and pyinstaller doesn't has support to it.