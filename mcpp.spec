%define major	0
%define libname	%mklibname %{name} %major
%define devname	%mklibname %{name} -d

Summary:	Alternative C/C++ preprocessor
Name:		mcpp
Version:	2.7.2
Release:	14
License:	BSD
Group:		Development/C++
Url:		http://mcpp.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# fedora patches
Patch0:		mcpp-manual.html.patch
# From http://www.zeroc.com/forums/patches/4445-patch-1-mcpp-2-7-2-a.html
Patch1:		patch.mcpp.2.7.2.txt
Patch2:		mcpp-automake-1.13.patch

%track
prog %{name} = {
	url = http://sourceforge.net/projects/mcpp/
	regex = %{name}-(__VER__)\.tar\.gz
	version = %{version}
}

%description
C/C++ preprocessor defines and expands macros and processes '#if',
'#include' and some other directives.

MCPP is an alternative C/C++ preprocessor with the highest conformance.
It supports multiple standards:	K&R, ISO C90, ISO C99, and ISO C++98.
MCPP is especially useful for debugging a source program which uses
complicated macros and also useful for checking portability of a source.

Though mcpp could be built as a replacement of GCC's resident
proprocessor or as a stand-alone program without using library build of
mcpp, this package installs only a program named 'mcpp' which links
shared library of mcpp and behaves independent from GCC.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package provides the libraries for mcpp.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%setup -q
%apply_patches

autoreconf -fi

%build
%configure2_5x \
	 --enable-mcpplib \
	--disable-static
%make 

%install
%makeinstall_std

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_defaultdocdir}/%{name}

%files -n %{libname}
%{_libdir}/libmcpp.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*

