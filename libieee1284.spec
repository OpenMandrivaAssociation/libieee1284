%define _disable_ld_no_undefined 1

# libieee1284 is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define major	3
%define libname %mklibname ieee1284_ %{major}
%define devname %mklibname ieee1284 -d
%define lib32name %mklib32name ieee1284_ %{major}
%define dev32name %mklib32name ieee1284 -d

%define git 20250127

#define _disable_lto 1
Summary:	Cross-platform library for parallel port access
Name:		libieee1284
Version:	0.2.11
Release:	%{git}.33
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/twaugh/libieee1284
Source0:	http://ovh.dl.sourceforge.net/sourceforge/libieee1284/%{name}-%{version}.tar.bz2
# git taken from https://github.com/twaugh/libieee1284

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	xmlto
BuildRequires:	pkgconfig(python3) python

%description
libieee1284 is a cross-platform library for parallel port access.

%package -n	%{libname}
Summary:	Cross-platform library for parallel port access
Group:		System/Libraries

%description -n	%{libname}
libieee1284 is a cross-platform library for parallel port access

%package -n	%{devname}
Summary:	Development files for libieee1284
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	ieee1284-devel = %{EVRD}

%description -n	%{devname}
The %{name}-devel package includes the header files and .so libraries
necessary for developing programs which will access parallel port devices 
using the %{name} library.

%package -n	python-%{name}
Summary:	Python bindings for libieee2384
Group:		Development/Python
Requires:	pkgconfig(python)

%description -n python-%{name}
This package contains python bindings for libieee2384.

%if %{with compat32}
%package -n	%{lib32name}
Summary:	Cross-platform library for parallel port access (32-bit)
Group:		System/Libraries

%description -n	%{lib32name}
libieee1284 is a cross-platform library for parallel port access

%package -n	%{dev32name}
Summary:	Development files for libieee1284 (32-bit)
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n	%{dev32name}
The %{name}-devel package includes the header files and .so libraries
necessary for developing programs which will access parallel port devices 
using the %{name} library.
%endif

%prep
%autosetup -p1

export CONFIGURE_TOP="$(pwd)"
./bootstrap
%if %{with compat32}
mkdir build32
cd build32
%configure32 --without-python
cd ..
%endif

mkdir build
cd build
%configure \
	--with-python \
	--disable-static

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libieee1284.so.%{major}*

%files -n %{devname}
%doc README AUTHORS ChangeLog INSTALL NEWS TODO
%{_bindir}/libieee1284_test
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libieee1284.pc
%{_mandir}/man3/*

%files -n python-%{name}
%{python_sitearch}/ieee1284module.so

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libieee1284.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/libieee1284.pc
%endif
