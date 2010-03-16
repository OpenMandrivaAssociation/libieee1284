%define major 3
%define libname %mklibname ieee1284_ %major
%define develname %mklibname ieee1284 -d
%define staticdevelname %mklibname ieee1284 -d -s

Summary:	Cross-platform library for parallel port access
Name:		libieee1284
Version:	0.2.11
Release:	%mkrel 7
License:	LGPLv2+
Group:		System/Libraries
URL:		http://sourceforge.net/projects/libieee1284/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/libieee1284/%{name}-%{version}.tar.bz2
Patch0:		libieee1284-0.2.11-linkage.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel

%description
libieee1284 is a cross-platform library for parallel port access

%package -n	%{libname}
Summary:        Cross-platform library for parallel port access
Group:          System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
libieee1284 is a cross-platform library for parallel port access

%package -n	%{develname}
Summary:        Development files for libieee1284
Group:          Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:       ieee1284-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}0-devel = %{version}-%{release}
Obsoletes:	%{mklibname ieee1284_ 3 -d}

%description -n	%{develname}
The %{name}-devel package includes the header files and .so libraries
necessary for developing programs which will access parallel port devices 
using the %{name} library.

If you are going to develop programs which will access parallel port
devices, you should install %{name}-devel.  You'll also need to have
the %{name} package installed.

%package -n	%{staticdevelname}
Summary:        Static library for libieee1284
Group:          Development/C
Requires:	%{develname} = %{version}-%{release}
Provides:       ieee1284-static-devel
Provides:       %{name}-static-devel = %{version}-%{release}
Obsoletes:      %{mklibname ieee1284_ 3 -d -s}

%description -n	%{staticdevelname}
The %{staticdevelname} package includes the static libraries
necessary for developing programs which will access parallel port devices 
using the %{name} library.

If you are going to develop programs which will access parallel port
devices, you should install %{name}-devel.  You'll also need to have
the %{name} package installed.

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
%configure2_5x --with-python
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{py_platsitedir}/*.{a,la}

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README AUTHORS ChangeLog INSTALL NEWS TODO
%{_bindir}/libieee1284_test
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man3/*

%files -n %{staticdevelname}
%defattr(-,root,root)
%doc README
%{_libdir}/*.a

%files -n python-%{name}
%defattr(-,root,root)
%{py_platsitedir}/*.so
