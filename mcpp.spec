%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Name:		       	mcpp
Summary:    		Alternative C/C++ preprocessor
Version:    		2.7.2
Release:    		6
License:    		BSD
Group:      		Development/C++
Source:     		http://downloads.sourceforge.net/%name/%name-%version.tar.gz
# fedora patches
Patch0:     		mcpp-manual.html.patch
# From http://www.zeroc.com/forums/patches/4445-patch-1-mcpp-2-7-2-a.html
Patch1:     		patch.mcpp.2.7.2.txt
URL:        		http://mcpp.sourceforge.net/
Requires:		%libname = %version-%release

%description
C/C++ preprocessor defines and expands macros and processes '#if',
'#include' and some other directives.

MCPP is an alternative C/C++ preprocessor with the highest conformance.
It supports multiple standards: K&R, ISO C90, ISO C99, and ISO C++98.
MCPP is especially useful for debugging a source program which uses
complicated macros and also useful for checking portability of a source.

Though mcpp could be built as a replacement of GCC's resident
proprocessor or as a stand-alone program without using library build of
mcpp, this package installs only a program named 'mcpp' which links
shared library of mcpp and behaves independent from GCC.

%files
%_bindir/*
%_mandir/man1/*
%_defaultdocdir/%name

#-------------------------------------------------------------------------

%package -n		%libname
Summary:		Libraries for %name
Group:			System/Libraries

%description -n		%libname
This package provides the libraries for mcpp.

%files -n		%libname
%defattr(-,root,root)
%_libdir/*.so.%{major}*

#-------------------------------------------------------------------------

%package -n		%develname
Summary:		Development files for %name
Group:			Development/Other
Requires:		%name = %version-%release
Provides:		%name-devel = %version-%release

%description -n 	%develname
This package contains development files for %name.

%files -n		%develname
%defattr(-,root,root)
%_libdir/*.so
%_includedir/*

#-------------------------------------------------------------------------
	
%prep
%setup -q
%patch0 -p0 -b -z.euc-jp
%patch1 -p1

autoreconf -fi

%build
%configure --enable-mcpplib --disable-static
%make 

%install
%makeinstall 


%changelog
* Wed Apr 06 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.7.2-3mdv2011.0
+ Revision: 651329
- fixed file list
- added autoreconf to fix libtool error
- fixed malformed patch
- rebuild
- added fedora patches
- disabled static build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 2.7.2-1mdv2009.1
+ Revision: 324860
- update to new version 2.7.2

* Fri Nov 07 2008 Michael Scherer <misc@mandriva.org> 2.7.1-1mdv2009.1
+ Revision: 300738
- import mcpp


* Wed Oct 22 2008 incubusss <mdv@incubusss.net> 2.7.1-1mdv2009.0
- initial package
