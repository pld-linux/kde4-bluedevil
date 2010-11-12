
%define		kde4ver	4.5
%define		orgname	bluedevil

Summary:	KDE Bluetooth framework
Summary(pl.UTF-8):	Podstawowe środowisko KDE Bluetooth
Name:		kde4-bluedevil
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://media.ereslibre.es/2010/11/bluedevil-v%{version}.tar.bz2
# Source0-md5:	b20d9c234adfe3c498f5577a88cd2f03
URL:		http://www.afiestas.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kde4ver}
BuildRequires:	libbluedevil-devel >= 1.8
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
%setup -q -n %{orgname}-v%{version}

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
%attr(755,root,root) %{_bindir}/bluedevil-audio
%attr(755,root,root) %{_bindir}/bluedevil-authorize
%attr(755,root,root) %{_bindir}/bluedevil-confirmmodechange
%attr(755,root,root) %{_bindir}/bluedevil-helper
%attr(755,root,root) %{_bindir}/bluedevil-input
%attr(755,root,root) %{_bindir}/bluedevil-monolithic
%attr(755,root,root) %{_bindir}/bluedevil-requestconfirmation
%attr(755,root,root) %{_bindir}/bluedevil-requestpin
%attr(755,root,root) %{_bindir}/bluedevil-sendfile
%attr(755,root,root) %{_bindir}/bluedevil-wizard
%{_datadir}/apps/bluedevil
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
%{_desktopdir}/kde4/bluedevil-audio.desktop
%{_desktopdir}/kde4/bluedevil-input.desktop
%{_desktopdir}/kde4/bluedevil-monolithic.desktop
%{_desktopdir}/kde4/bluedevil-sendfile.desktop
%{_desktopdir}/kde4/bluedevil-wizard.desktop
%{_datadir}/dbus-1/services/org.kde.BlueDevil.Service.service
%attr(755,root,root) %{_libdir}/libbluedevilaction.so
%attr(755,root,root) %{_libdir}/kde4/bluedevilaudioactionplugin.so
%attr(755,root,root) %{_libdir}/kde4/bluedevilinputactionplugin.so
%attr(755,root,root) %{_libdir}/kde4/bluedevilsendfileactionplugin.so
%attr(755,root,root) %{_libdir}/kde4/kcm_bluedeviladapters.so
%attr(755,root,root) %{_libdir}/kde4/kcm_bluedevildevices.so
%attr(755,root,root) %{_libdir}/kde4/kcm_bluedeviltransfer.so
%attr(755,root,root) %{_libdir}/kde4/kded_bluedevil.so
%attr(755,root,root) %{_libdir}/kde4/kded_obexftpdaemon.so
%attr(755,root,root) %{_libdir}/kde4/kio_bluetooth.so
%attr(755,root,root) %{_libdir}/kde4/kio_obexftp.so
