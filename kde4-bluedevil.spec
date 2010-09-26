
%define		kde4ver	4.4.5
%define		orgname	bluedevil

Summary:	KDE Bluetooth framework
Summary(pl.UTF-8):	Podstawowe środowisko KDE Bluetooth
Name:		kde4-bluedevil
Version:	1.0
Release:	0.rc4.1
License:	GPL
Group:		X11/Applications
# get git: git clone git://gitorious.org/bluedevil/bluedevil.git
Source0:	http://www.afiestas.org/files/%{orgname}-v%{version}rc4-1.tgz
# Source0-md5:	c967bce0edd20c2937db5071c7b735df
URL:		http://www.afiestas.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kde4ver}
BuildRequires:	libbluedevil-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	shared-mime-info
Requires:	bluez
Requires:	obex-data-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BlueDevil is a set of components, which integrates bluetooth within
the KDE SC, for example adding a system preference module (KCM), or
allowing to browse the files in a cell phone from you favorite file
browser.

%prep
%setup -q -n %{orgname}-rc4-1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bluedevil-*
%dir %{_datadir}/apps/bluedevil
%{_datadir}/apps/bluedevil/*
%{_datadir}/mime/packages/bluedevil-mime.xml
%{_datadir}/kde4/servicetypes/actionplugin.desktop
%{_datadir}/kde4/services/bluedevil-input.desktop
%{_datadir}/kde4/services/bluedevil-audio.desktop
%{_datadir}/kde4/services/sendfile.desktop
%{_datadir}/kde4/services/bluedevildevices.desktop
%{_datadir}/kde4/services/bluedeviladapters.desktop
%{_datadir}/kde4/services/bluedeviltransfer.desktop
%{_datadir}/kde4/services/bluetooth.protocol
%{_datadir}/kde4/services/obexftp.protocol
%{_datadir}/kde4/services/kded/bluedevil.desktop
%{_datadir}/kde4/services/kded/obexftpdaemon.desktop
%{_desktopdir}/kde4/*
%{_datadir}/dbus-1/services/org.kde.BlueDevil.Service.service
%{_libdir}/libbluedevilaction.so
%{_libdir}/kde4/*
