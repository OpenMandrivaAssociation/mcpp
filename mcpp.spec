%define major		0
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d
%define staticdevelname	%mklibname %name -d -s

Name:		       	mcpp
Summary:    		Alternative C/C++ preprocessor
Version:    		2.7.2
Release:    		%mkrel 1
License:    		BSD
Group:      		Development/C++
Source:     		http://downloads.sourceforge.net/%name/%name-%version.tar.gz
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
%_libdir/*.so.*

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

%package -n		%staticdevelname
Summary:		Static development files for %name
Group:			Development/Other
Requires:		%develname = %version-%release
Provides:		%name-static-devel = %version-%release

%description -n		%staticdevelname
This package contains static development files for %name.

%files -n		%staticdevelname
%defattr(-,root,root)
%_libdir/*.a

#-------------------------------------------------------------------------
	
%prep
%setup -q

%build
%configure --enable-mcpplib
%make 

%install
rm -rf %buildroot
%makeinstall 

%clean
rm -rf %buildroot
