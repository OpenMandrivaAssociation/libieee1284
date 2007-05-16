%define libname %mklibname ieee1284_ 3

Summary:	libieee1284 is a cross-platform library for parallel port access
Name:		libieee1284
Version:	0.2.10
Release:	%mkrel 3
Source0:	http://cyberelk.net/tim/data/libieee1284/stable/%{name}-%{version}.tar.bz2
License:	LGPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://sourceforge.net/projects/libieee1284/
%py_requires -d

%description
libieee1284 is a cross-platform library for parallel port access

%package -n	%{libname}
Summary:        libieee1284 is a cross-platform library for parallel port access
Group:          System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
libieee1284 is a cross-platform library for parallel port access

%package -n	%{libname}-devel
Summary:        libieee1284 is a cross-platform library for parallel port access
Group:          Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}0-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{libname}-devel
The %{name}-devel package includes the header files and .so libraries
necessary for developing programs which will access parallel port devices 
using the %{name} library.

If you are going to develop programs which will access parallel port
devices, you should install %{name}-devel.  You'll also need to have
the %{name} package installed.

%package -n	%{libname}-static-devel
Summary:        Static library for libieee1284
Group:          Development/C
Provides:	%{name}-static-devel = %{version}-%{release}
Requires:	%{libname}-devel = %{version}-%{release}

%description -n	%{libname}-static-devel
The %{name}-devel package includes the static libraries
necessary for developing programs which will access parallel port devices 
using the %{name} library.

If you are going to develop programs which will access parallel port
devices, you should install %{name}-devel.  You'll also need to have
the %{name} package installed.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%post -p /sbin/ldconfig -n %{libname}
%postun -p /sbin/ldconfig -n %{libname}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc README AUTHORS ChangeLog INSTALL NEWS TODO
%{_bindir}/libieee1284_test
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man3/*
%{_libdir}/python%{py_ver}/site-packages/*.so
%{_libdir}/python%{py_ver}/site-packages/*.la

%files -n %{libname}-static-devel
%defattr(-,root,root)
%doc README
%{_libdir}/*.a
%{_libdir}/python%{py_ver}/site-packages/*.a
