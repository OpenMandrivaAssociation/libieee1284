%define major 3
%define libname %mklibname ieee1284_ %{major}
%define develname %mklibname ieee1284 -d

Summary:	Cross-platform library for parallel port access
Name:		libieee1284
Version:	0.2.11
Release:	12
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
Obsoletes:	%{mklibname ieee1284_ 3 -d} < 0.2.11-12

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
	--with-python \
	--disable-static

%make

%install
%makeinstall_std

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


%changelog
* Sun Nov 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.2.11-10
+ Revision: 733966
- fix configure line
- rebuild
- clean up spec
- disable static build & pkg
- removed .la files
- removed old ldconfig scriptlets
- removed mkrel & BuildRoot
- shortened devel description

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.11-9
+ Revision: 660262
- mass rebuild

* Wed Mar 31 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.2.11-8mdv2011.0
+ Revision: 530452
- rebuild because i586 and x86_64 repos are not in sync

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.11-7mdv2010.1
+ Revision: 520870
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.2.11-6mdv2010.0
+ Revision: 425568
- rebuild

* Mon Jan 26 2009 Funda Wang <fwang@mandriva.org> 0.2.11-5mdv2009.1
+ Revision: 333715
- split out python binding

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.2.11-4mdv2009.1
+ Revision: 319537
- rebuild with python 2.6

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.2.11-3mdv2009.0
+ Revision: 222888
- rebuild
- fix summary-not-capitalized
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Nov 14 2007 Funda Wang <fwang@mandriva.org> 0.2.11-2mdv2008.1
+ Revision: 108822
- rebuild

* Sun Oct 28 2007 Funda Wang <fwang@mandriva.org> 0.2.11-1mdv2008.1
+ Revision: 102730
- New version 0.2.11

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.10-5mdv2008.0
+ Revision: 76974
- cleanup borked deps

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.2.10-4mdv2008.0
+ Revision: 76861
- new devel naming

* Wed May 16 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.2.10-3mdv2008.0
+ Revision: 27294
- Specfile cleanup, forcing a package rebuild.


* Mon Jan 15 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.2.10-2mdv2007.0
+ Revision: 109310
- Rebuild against python 2.5
- Use py_requires macro instead of manual hacks.
- Import libieee1284

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.2.10-2mdk
- Rebuild

* Tue Jun 14 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.2.10-1mdk
- 0.2.10
- %%mkrel

* Thu Feb 17 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.2.9-1mdk
- 0.2.9

* Fri Jan 07 2005 Till Kamppeter <till@mandrakesoft.com> 0.2.8-2mdk
- Rebuild

