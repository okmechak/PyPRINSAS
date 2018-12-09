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

## System setup and Dependencies
  At first install [Anaconda](https://www.anaconda.com/)(Python3 version only)
  
  After that install next packages:
 - [PyQtGraph](http://www.pyqtgraph.org/) - GUI
 - [SciPy](https://www.scipy.org/) - Fitting and Analysis tool
 - [PyOpenGL](http://pyopengl.sourceforge.net/) - Dependencie of PyQtGraph

There easiest way to install above tools is using __pip__ tool from command prompt(it will installed with Anaconda package).
>Note: if command pompt says that __pip__ command isn't recognized(even Anaconda is installed) then you have to modify Path Environmental Variable, with appending location to pip tool(which is placed in folder Scripts of Anaconda installation root folder)

pip install PyOpenGL PyOpenGL_accelerate pyqtgraph
