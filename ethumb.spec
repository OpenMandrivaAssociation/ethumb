#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/ethumb ethumb; \
#cd ethumb; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf ethumb-$PKG_VERSION.tar.xz ethumb/ --exclude .svn --exclude .*ignore

%define	svndate	20120103
%define	svnrev	66608

%define	major	1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname -d %{name}

Name:		ethumb
Version:	1.7.3
Release:	1
License:	LGPLv3+
Summary:	Enlightenment thumbnailing library
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	edje
BuildRequires:	evas
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(ecore-file)
BuildRequires:	pkgconfig(ecore-evas)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(edbus)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(lua)
# Can be added later:
#BuildRequires:	pkgconfig(epdf)

%description
New library to generate thumbnails.
There are still some important features to be implemented, like
client-server framework, edje thumbnails and a plugin API to integrate
it with emotion and like.

%package -n %{libname}
Summary:	Enlightenment thumbnailing library
Group:		System/Libraries

%description -n %{libname}
New library to generate thumbnails.

%package -n %{develname}
Summary:	Enlightenment thumbnailing library - devel files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
ethumb development headers and development libraries.

%prep
%setup -q

%build
#NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS README
%{_bindir}/ethumb
%{_bindir}/ethumbd
%{_bindir}/ethumbd_client
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ethumb
%{_libdir}/ethumb
%{_libexecdir}/ethumbd_slave

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}*



%changelog
* Thu Jun 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.1-1
+ Revision: 807363
- version update 1.0.1

* Tue Jan 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.1.1.66608-0.20120103.1
+ Revision: 759271
- added BR evas
- really evas module should be split out
- fixed BR
- new snapshot 0.1.1.66608
- merged UnityLinux spec
- disabled static build
- cleaned up spec

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 0.1.1.55225-1mdv2011.0
+ Revision: 622839
- new version 0.1.1.55225

* Tue Nov 16 2010 Funda Wang <fwang@mandriva.org> 0.1.1.54472-1mdv2011.0
+ Revision: 597993
- new version 0.1.1.54472

* Tue Nov 09 2010 Funda Wang <fwang@mandriva.org> 0.1-0.20101107.1mdv2011.0
+ Revision: 595175
- BR exif
- new snapshot

* Sun Jul 25 2010 Funda Wang <fwang@mandriva.org> 0.1-0.20100715.1mdv2011.0
+ Revision: 558269
- new snapshot

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 0.1-0.44424.1mdv2010.1
+ Revision: 478207
- New snapshot

* Sat Aug 08 2009 Funda Wang <fwang@mandriva.org> 0.1-0.41637.1mdv2010.0
+ Revision: 411620
- add BR for edje_cc
- import ethumb

