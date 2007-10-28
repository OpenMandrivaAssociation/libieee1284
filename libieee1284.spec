%define major 3
%define libname %mklibname ieee1284_ %major
%define develname %mklibname ieee1284 -d
%define staticdevelname %mklibname ieee1284 -d -s

Summary:	libieee1284 is a cross-platform library for parallel port access
Name:		libieee1284
Version:	0.2.11
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
URL:		http://sourceforge.net/projects/libieee1284/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/libieee1284/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%py_requires -d

%description
libieee1284 is a cross-platform library for parallel port access

%package -n	%{libname}
Summary:        libieee1284 is a cross-platform library for parallel port access
Group:          System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
libieee1284 is a cross-platform library for parallel port access

%package -n	%{develname}
Summary:        libieee1284 is a cross-platform library for parallel port access
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

%prep

%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%post -p /sbin/ldconfig -n %{libname}

%postun -p /sbin/ldconfig -n %{libname}

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
%{_libdir}/python%{py_ver}/site-packages/*.so
%{_libdir}/python%{py_ver}/site-packages/*.la

%files -n %{staticdevelname}
%defattr(-,root,root)
%doc README
%{_libdir}/*.a
%{_libdir}/python%{py_ver}/site-packages/*.a
