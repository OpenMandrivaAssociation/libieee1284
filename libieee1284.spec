%define major 3
%define libname %mklibname ieee1284_ %{major}
%define develname %mklibname ieee1284 -d

Summary:	Cross-platform library for parallel port access
Name:		libieee1284
Version:	0.2.11
Release:	10
License:	LGPLv2+
Group:		System/Libraries
URL:		http://sourceforge.net/projects/libieee1284/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/libieee1284/%{name}-%{version}.tar.bz2
Patch0:		libieee1284-0.2.11-linkage.patch
BuildRequires:	python-devel

%description
libieee1284 is a cross-platform library for parallel port access

%package -n	%{libname}
Summary:	Cross-platform library for parallel port access
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
libieee1284 is a cross-platform library for parallel port access

%package -n	%{develname}
Summary:	Development files for libieee1284
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	ieee1284-devel
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname ieee1284_ 3 -d}

%description -n	%{develname}
The %{name}-devel package includes the header files and .so libraries
necessary for developing programs which will access parallel port devices 
using the %{name} library.

%package -n	python-%{name}
Group:		Development/Python
Summary:	Python bindings for libieee2384
Conflicts:	%{name}-devel < %{version}-%{release}
%py_requires -d

%description -n python-%{name}
This package contains python bindings for libieee2384.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x \
	--with-python
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

#rm -f %{buildroot}%{py_platsitedir}/*.a

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README AUTHORS ChangeLog INSTALL NEWS TODO
%{_bindir}/libieee1284_test
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

%files -n python-%{name}
%{py_platsitedir}/*.so
