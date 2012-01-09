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
Version:	0.1.1.%{svnrev}
Release:	0.%{svndate}.1
License:	LGPLv3+
Summary:	Enlightenment thumbnailing library
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	%{name}-%{version}.tar.xz
 
BuildRequires:	edje
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(edbus)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libexif)

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
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la | xargs rm

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

