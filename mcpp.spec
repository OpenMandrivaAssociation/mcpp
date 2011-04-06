%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Name:		       	mcpp
Summary:    		Alternative C/C++ preprocessor
Version:    		2.7.2
Release:    		%mkrel 3
License:    		BSD
Group:      		Development/C++
Source:     		http://downloads.sourceforge.net/%name/%name-%version.tar.gz
# fedora patches
Patch0:     		mcpp-manual.html.patch
# From http://www.zeroc.com/forums/patches/4445-patch-1-mcpp-2-7-2-a.html
Patch1:     		patch.mcpp.2.7.2.txt
URL:        		http://mcpp.sourceforge.net/
Requires:		%libname = %version-%release
BuildRoot:  		%_tmppath/%name-%version-%release-buildroot

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
%defattr(-,root,root,-)
%_bindir/*
%_mandir/man1/*
%_defaultdocdir/%name

#-------------------------------------------------------------------------

%package -n		%libname
Summary:		Libraries for %name
Group:			System/Libraries

%description -n		%libname
This package provides the libraries for mcpp.

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %libname
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %libname
%endif

%files -n		%libname
%defattr(-,root,root)
%_libdir/*.so.%{major}.*

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
%_libdir/*.la
%_libdir/*.so
%_includedir/*

#-------------------------------------------------------------------------
	
%prep
%setup -q
%patch0 -p0 -b -z.euc-jp
%patch1 -p1

%build
%configure --enable-mcpplib --disable-static
%make 

%install
rm -rf %buildroot
%makeinstall 

%clean
rm -rf %buildroot

