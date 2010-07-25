%define svnrel 20100715

%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary: Enlightenment thumbnailing library
Name: ethumb
Version: 0.1
Release: %mkrel -c %svnrel 1
License: LGPLv3+
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: evas-devel
BuildRequires: ecore-devel
BuildRequires: edje-devel edje
BuildRequires: e_dbus-devel
BuildRequires: emotion-devel

%description
New library to generate thumbnails.
There are still some important features to be implemented, like
client-server framework, edje thumbnails and a plugin API to integrate
it with emotion and like.

%package -n %libname
Summary: Enlightenment thumbnailing library
Group: System/Libraries

%description -n %libname
New library to generate thumbnails.

%package -n %develname
Summary: Enlightenment thumbnailing library - devel files
Group: System/Libraries
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %develname
ethumb development headers and development libraries.

%prep
%setup -q -n %name-%version

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

find %buildroot -name *.la | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/ethumb
%{_bindir}/ethumbd
%{_bindir}/ethumbd_client
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ethumb
%{_libdir}/ethumb
%{_libexecdir}/ethumbd_slave

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_includedir}/ethumb-0/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
