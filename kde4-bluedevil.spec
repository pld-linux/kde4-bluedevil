
# TODO: needs cleaning BRs and Rs.

%define		qtver	4.6.3
%define		kde4ver	4.5.1
%define		orgname	bluedevil

Summary:	KDE Bluetooth framework
Summary(pl.UTF-8):	Podstawowe środowisko KDE Bluetooth
Name:		kde4-bluedevil
Version:	1.0
Release:	0.beta3.1
License:	GPL
Group:		X11/Applications
# get git: git clone git://gitorious.org/bluedevil/bluedevil.git
Source0:	%{orgname}-%{version}.tar.bz2
# Source0-md5:	e4fa4e634e60314f2529a43236b110ac
URL:		http://projects.ufocoders.com/projects/bluedevil
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdebase-workspace-devel >= %{kde4ver}
BuildRequires:	kde4-kdelibs-devel >= %{kde4ver}
BuildRequires:	libbluedevil-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	shared-desktop-ontologies-devel >= 0.2
BuildRequires:	soprano-devel >= 2.4.0.1
Requires:	obex-data-server
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

#%find_lang %{orgname} --all-name

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
%{_desktopdir}/kde4/*
%{_datadir}/dbus-1/services/org.kde.BlueDevil.Service.service
%{_libdir}/libbluedevilaction.so
%{_libdir}/kde4/*
