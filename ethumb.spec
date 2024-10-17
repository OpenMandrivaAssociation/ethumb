#This package is OBSOLETE it has been merged into efl
%define major   1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	Enlightenment thumbnailing library
Name:		ethumb
Version:	1.7.8
Release:	1
License:	LGPLv3+
Group:		Graphical desktop/Enlightenment
Url:		https://www.enlightenment.org/
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
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

%package -n %{devname}
Summary:	Enlightenment thumbnailing library - devel files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
ethumb development headers and development libraries.

%prep
%setup -q

%build
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

%files -n %{devname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}*

