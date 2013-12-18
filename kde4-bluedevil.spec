%define		kdever	4.7.2
%define		qtver	4.7.4
%define		orgname	bluedevil
%define		state	stable

# git archive --format=tar --remote=git://anongit.kde.org/bluedevil bluez5  \
# --prefix=bluedevil-%{version}/ | bzip2 >libbluedevil-%{version}-%{snap}.tar.bz2
%define		snap	20131218

Summary:	KDE Bluetooth framework
Summary(pl.UTF-8):	Podstawowe środowisko KDE Bluetooth
Name:		kde4-bluedevil
Version:	2.0.0
Release:	0.%{snap}.1
Epoch:		1
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{state}/bluedevil/%{version}/src/%{orgname}-%{version}.tar.xz
Source0:	%{orgname}-%{version}-%{snap}.tar.bz2
# Source0-md5:	5030d655be2b1d0b4ec5d083b6881c67
URL:		http://www.afiestas.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	libbluedevil-devel >= 2.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
Requires:	bluez >= 5.0
Obsoletes:	kde4-kdebluetooth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BlueDevil is a set of components, which integrates bluetooth within
the KDE SC, for example adding a system preference module (KCM), or
allowing to browse the files in a cell phone from you favorite file
browser.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#%find_lang %{orgname}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

#%files -f %{orgname}.lang
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bluedevil-audio
%attr(755,root,root) %{_bindir}/bluedevil-input
%attr(755,root,root) %{_bindir}/bluedevil-monolithic
%attr(755,root,root) %{_bindir}/bluedevil-network-dun
%attr(755,root,root) %{_bindir}/bluedevil-network-panu
%attr(755,root,root) %{_bindir}/bluedevil-sendfile
%attr(755,root,root) %{_bindir}/bluedevil-wizard
%attr(755,root,root) %{_libdir}/kde4/libexec/bluedevil-requestconfirmation
%attr(755,root,root) %{_libdir}/kde4/libexec/bluedevil-requestpin
%attr(755,root,root) %{_libdir}/kde4/libexec/bluedevil-authorize
%attr(755,root,root) %{_libdir}/kde4/libexec/bluedevil-confirmmodechange
%{_datadir}/apps/bluedevil
%{_datadir}/apps/bluedevilwizard
%{_datadir}/mime/packages/bluedevil-mime.xml
%{_datadir}/kde4/servicetypes/actionplugin.desktop
%{_datadir}/kde4/services/bluedevil-audio.desktop
%{_datadir}/kde4/services/bluedevil-input.desktop
%{_datadir}/kde4/services/bluedevil-network-dun.desktop
%{_datadir}/kde4/services/bluedevil-network-panu.desktop
%{_datadir}/kde4/services/bluedeviladapters.desktop
%{_datadir}/kde4/services/bluedevildevices.desktop
%{_datadir}/kde4/services/bluedevilsendfile.desktop
%{_datadir}/kde4/services/bluedeviltransfer.desktop
%{_datadir}/kde4/services/bluetooth.protocol
%{_datadir}/kde4/services/obexftp.protocol
%{_datadir}/kde4/services/sendfile.desktop
%{_datadir}/kde4/services/kded/bluedevil.desktop
%{_datadir}/kde4/services/kded/obexftpdaemon.desktop
%{_desktopdir}/kde4/bluedevil-audio.desktop
%{_desktopdir}/kde4/bluedevil-input.desktop
%{_desktopdir}/kde4/bluedevil-monolithic.desktop
%{_desktopdir}/kde4/bluedevil-network-dun.desktop
%{_desktopdir}/kde4/bluedevil-network-panu.desktop
%{_desktopdir}/kde4/bluedevil-sendfile.desktop
%{_desktopdir}/kde4/bluedevil-wizard.desktop
%attr(755,root,root) %{_libdir}/libbluedevilaction.so
%attr(755,root,root) %{_libdir}/kde4/bluedevilaudioactionplugin.so
%attr(755,root,root) %{_libdir}/kde4/bluedevilinputactionplugin.so
%attr(755,root,root) %{_libdir}/kde4/bluedevilnetworkdunactionplugin.so
%attr(755,root,root) %{_libdir}/kde4/bluedevilnetworkpanuactionplugin.so
%attr(755,root,root) %{_libdir}/kde4/bluedevilsendfileactionplugin.so
%attr(755,root,root) %{_libdir}/kde4/bluetoothfiletiemaction.so
%attr(755,root,root) %{_libdir}/kde4/kcm_bluedeviladapters.so
%attr(755,root,root) %{_libdir}/kde4/kcm_bluedevildevices.so
%attr(755,root,root) %{_libdir}/kde4/kcm_bluedeviltransfer.so
%attr(755,root,root) %{_libdir}/kde4/kded_bluedevil.so
%attr(755,root,root) %{_libdir}/kde4/kded_obexftpdaemon.so
%attr(755,root,root) %{_libdir}/kde4/kio_bluetooth.so
%attr(755,root,root) %{_libdir}/kde4/kio_obexftp.so
