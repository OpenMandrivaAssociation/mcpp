%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Alternative C/C++ preprocessor
Name:		mcpp
Version:	2.7.2
Release:	23
License:	BSD
Group:		Development/C++
Url:		http://mcpp.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

# (tpg) patches from Debian
Patch1:		01-zeroc-fixes.patch
Patch2:		02-gniibe-fixes.patch
Patch3:		03-gniibe-fix-11.patch
Patch4:		04-gniibe-fix-12.patch
Patch5:		05-gniibe-fix-13.patch
Patch6:		06-gniibe-fix-autotools.patch

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
Requires:	%{name} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%autosetup -p1

sed -i 's/-lmcpp/libmcpp.la/' src/Makefile.am

autoreconf -fi

%build
%configure \
	--enable-mcpplib \
	--disable-static

%make_build

%install
%make_install

%files
%{_bindir}/*
%doc %{_mandir}/man1/*
%doc %{_docdir}/%{name}

%files -n %{libname}
%{_libdir}/libmcpp.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/*
