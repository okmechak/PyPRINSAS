PRINSAS version 2.21 1 Dec 2004
------------------------------------

Program PRINSAS (PRocessing and INterpretation of Small Angle Scattering data) takes raw SANS, SAXS, USANS and USAXS data, stores the data, and allows the user to further process and interpret the data. 
Although any small angle scattering data can be accepted, PRINSAS has been optimised for the processing and interpretation of SAS data for
rocks and other media with a wide distribution of scatterer sizes. 


Installation
------------

To install PRINSAS, run setup.exe. During installation, a number of error messages may arise. Just ignore these messages. In most cases the program will install regardless. Excel needs to be installed on the computer and the 'Solver' add-in loaded.

If it is to be installed on a PC with Windows 95, the file 'DCOM95' may need to be installed first. This file can be downloaded from the Microsoft site (www.microsoft.com): go to search.microsoft.com and search for 'DCOM95'. (Note: this may also apply to Windows 98 in which case DCOM98 may be required.)

Note that installation on Windows NT/2000/XP operating systems may require administrator access otherwise PRINSAS may not install correctly (for example, PRINSAS may not appear in the Windows 'Start' menu or it may not install at all).

Windows 2000 users may need to have Windows 2000 Service Pack 3. The program has been successfully installed on a PC with Windows 2000 (Service Pack 3) without administrator access by ignoring the error messages that arise during installation.

It is also recommend that macro virus protection in Excel is turned off whenver PRINSAS is run, otherwise a warning message will be displayed whenever some windows are opened in PRINSAS. To turn off macro virus protection, run Excel (before or after installing of PRINSAS), and go to 'Tools', 'Options' and display the 'General' tab then click 'Macro virus protection' off. (For Excel 2002 go to 'Tools', 'Options', 'Security' and click on 'Macro Security ...' and on the 'Security Level' tab select 'Low' ('Medium' may also be OK)), and on the 'Trusted Sources' tab, click to select the 'Trust access to Visual Basic Project' check box to turn it on.

Versions of Excel after Excel 97
--------------------------------
If the version of Excel is later than Excel 97 the Solver add-in will not work properly with PRINSAS. To solve this problem, the installed 'SOLVER.XLA' file must be removed, or renamed, and replaced with the 'SOLVER.XLA' that the setup program will install in the PRINSAS directory. (With Office XP, 'SOLVER.XLA' can usually be found in the C:\Program Files\Microsoft Office\Office10\Library\Solver\ directory.). For Excel 97 useres, 'SOLVER.XLA' can be deleted from the PRINSAS
directory.

Uninstalling
------------

To thoroughly uninstall PRINSAS, first run the program 'deregist.exe' found in the installation directory, then uninstall in the usual way (Control Panel, Add/Remove Programs and select PRINSAS). (Make sure derigist.exe closes first). Finally, delete the installation directory (typically C:\Program Files\PRINSAS 2.2), if still present.

System requirements
-------------------

A PC with a Microsoft Windows 95 or later and Microsoft Excel 97 or later. 
A Pentium 450 or faster is recommended. 
25MB initial hard disk space plus extra to allow the databases to grow.


Contact Information
-------------------
Dr Alan L Hinde
Geoscience Australia
GPO Box 378
Canberra City ACT 2601 Australia
email: Alan.Hinde@ga.gov.au

Geoscience Australia GEOCAT record number(GEOCAT): 40315

Copyright
---------
Copyright Commonwealth of Australia 2003. This work is copyright. Apart from any fair dealings for the purposes of study, research, criticism or review, as permitted under the Copyright Act, no part may be reproduced by any process without written permission. Copyright is the responsibility of the Chief Executive Officer, Geoscience Australia. Inquiries should be directed to the Chief Executive Officer, Geoscience Australia, GPO Box 378, Canberra City, ACT, 2601, Australia.


Disclaimer
----------
Geoscience Australia has tried to make the information in this product as accurate as possible. However, it does not guarantee that the information is totally accurate or complete. Therefore you should not rely solely on this information when making a commercial decision.


Version History
---------------

Version 1.0 21 August 2002
 
   Initial release

Version 2.0 16 October 2003

   Error treatment added: errors are input when importing data. Errors are
     (optionally) displayed on the plots. Propagated errors are calculated
     when desmearing and subtracting empty cell data for USANS. Errors are 
     transferred to the processed database but are ignored in any of the 
     data analysis routines.

   Version 2 will automatically update version 1 databases to version 2.

   AutoZoom improved.

   No longer asks if a worksheet can be deleted when exporting correlation
     plot to Excel.

   Improved Export to Excel for processed data: allows any selection of the 
     stored scattering curves to be exported along with any selection of 
     additional data associated with the curve (depth, vitrinite reflectance, 
     porosity, density and scattering length density only).
   
     The exported Excel workbook has a macro that allows I(Q) values to be
     interpolated at a specified Q value.

   Autozoom is invoked if the user releases the 'Mask excluded points' button.

   No restriction on the number of data points allowed for a dataset.

   When selecting a Porod Plot, the program automatically adds a composite
     fitted line.

   Menu's re-organised so that disabled menu items appear rather than not
     appearing at all.

   When editing SANS, USANS and processed data, the list may be spit into
     two segments. (Click and drag on the small black bar at the bottom left
     of the list window.)

   The program now checks whether Solver is installed in Excel before running
     routines that require Solver and during installation of PRINSAS.

   When fitting a histogram the program will now (optionally) automatically try 
     to fit the data.

   Accelerator keys added to some menu items. Also, if the shift key is held 
     while selecting another processed scattering curve, either with the mouse 
     or using the up-/down-arrow keys, any previous displayed curves are removed.

Version 2.0 18 November 2003
   
   Improvements were made to allow PRINSAS to work smoothly with Excel 2000 and
     later.

   SOLVER.XLA (Excel 97 version) now bundled with installation package to allow
     Excel 2000, and later, users to replace their existing SOLVER.XLA with
     one that works with PRINSAS.

   Bug in 'Export to EXCEL' for processed data fixed.  

Version 2.1 17 February 2004
   
   Lineary interpolation (on a log-log scale) now used to obtain better values of
     I(Q) in 'Ro vs I(Q)' and 'Depth vs I(Q)' routines.

   Improved histogram fit spreadsheet - user is now prompted to run the relevant 
      macros; error when setting minimum scale during 'SSA' macro fixed.

Version 2.2 10 May 2004
   
   The Excel file produced by 'Fit Histogram and SSA' (for processed data) now
      prompts the user to run the macros required to fit the data and display
      results. A plot of r^3 f(r) versus r is now produced when the 'SSA' macro 
      is run.

Version 2.21 1 Dec 2004
   Helpfile updated to include description of macros used in fitting a histogram
   and example of synthetic bimodal histogram data.

Version 2.22 28 Feb 2008
   Added Pressure and Temperature to data stored in the SASProc database for use in
   new macros in the SpecSurf_ file produced when fitting a histogram. The two new
   macros are:SLDPressureDependance and SLDPressureDependanceMA.