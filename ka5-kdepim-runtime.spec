%define		kdeappsver	21.04.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kdepim-runtime
Summary:	kdepim runtime
Name:		ka5-%{kaname}
Version:	21.04.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1ba511ae220cd8726abdfc48f9aeb7ee
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5NetworkAuth-devel
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Speech-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5XmlPatterns-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-notes-devel >= %{kdeappsver}
BuildRequires:	ka5-kalarmcal-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-kimap-devel >= %{kdeappsver}
BuildRequires:	ka5-kmailtransport-devel >= %{kdeappsver}
BuildRequires:	ka5-kmbox-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-libkgapi-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcalendarcore-devel >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcontacts-devel >= %{kframever}
BuildRequires:	kf5-kdav-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kholidays-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kitemmodels-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	libkolabxml-devel >= 1.1
BuildRequires:	libxslt-progs
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Runtime components for Akonadi KDE. This package contains Akonadi
agents written using KDE Development Platform libraries.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{ko,sr}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/akonadi_google_resource
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_ldap.so
%{_datadir}/knotifications5/akonadi_google_resource.notifyrc
%{_datadir}/kservices5/kcmldap.desktop
%attr(755,root,root) %{_bindir}/akonadi_akonotes_resource
%attr(755,root,root) %{_bindir}/akonadi_birthdays_resource
%attr(755,root,root) %{_bindir}/akonadi_contacts_resource
%attr(755,root,root) %{_bindir}/akonadi_davgroupware_resource
%attr(755,root,root) %{_bindir}/akonadi_ews_resource
%attr(755,root,root) %{_bindir}/akonadi_ewsmta_resource
%attr(755,root,root) %{_bindir}/akonadi_ical_resource
%attr(755,root,root) %{_bindir}/akonadi_icaldir_resource
%attr(755,root,root) %{_bindir}/akonadi_imap_resource
%attr(755,root,root) %{_bindir}/akonadi_kalarm_dir_resource
%attr(755,root,root) %{_bindir}/akonadi_kalarm_resource
%attr(755,root,root) %{_bindir}/akonadi_kolab_resource
%attr(755,root,root) %{_bindir}/akonadi_maildir_resource
%attr(755,root,root) %{_bindir}/akonadi_maildispatcher_agent
%attr(755,root,root) %{_bindir}/akonadi_mbox_resource
%attr(755,root,root) %{_bindir}/akonadi_migration_agent
%attr(755,root,root) %{_bindir}/akonadi_mixedmaildir_resource
%attr(755,root,root) %{_bindir}/akonadi_newmailnotifier_agent
%attr(755,root,root) %{_bindir}/akonadi_notes_resource
%attr(755,root,root) %{_bindir}/akonadi_openxchange_resource
%attr(755,root,root) %{_bindir}/akonadi_pop3_resource
%attr(755,root,root) %{_bindir}/akonadi_tomboynotes_resource
%attr(755,root,root) %{_bindir}/akonadi_vcard_resource
%attr(755,root,root) %{_bindir}/akonadi_vcarddir_resource
%attr(755,root,root) %{_bindir}/gidmigrator
%ghost %{_libdir}/libakonadi-filestore.so.5
%attr(755,root,root) %{_libdir}/libakonadi-filestore.so.5.*.*
%ghost %{_libdir}/libakonadi-singlefileresource.so.5
%attr(755,root,root) %{_libdir}/libakonadi-singlefileresource.so.5.*.*
%ghost %{_libdir}/libfolderarchivesettings.so.5
%attr(755,root,root) %{_libdir}/libfolderarchivesettings.so.5.*.*
%ghost %{_libdir}/libkmindexreader.so.5
%attr(755,root,root) %{_libdir}/libkmindexreader.so.5.*.*
%ghost %{_libdir}/libmaildir.so.5
%attr(755,root,root) %{_libdir}/libmaildir.so.5.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/akonadi.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/pop3.so
%dir %{_libdir}/qt5/plugins/akonadi/config
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/akonotesconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/birthdaysconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/contactsconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/icalconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/icaldirconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/kalarmconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/maildirconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/maildispatcherconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/mboxconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/mixedmaildirconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/newmailnotifierconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/notesconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/openxchangeconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/pop3config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/tomboynotesconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/vcardconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akonadi/config/vcarddirconfig.so
%{_datadir}/akonadi/accountwizard
%{_datadir}/akonadi/agents
%{_datadir}/akonadi/firstrun
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Maildir.Settings.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.MixedMaildir.Settings.xml
%{_iconsdir}/hicolor/128x128/apps/akonadi-ews.png
%{_iconsdir}/hicolor/128x128/apps/ox.png
%{_iconsdir}/hicolor/16x16/apps/akonadi-ews.png
%{_iconsdir}/hicolor/16x16/apps/ox.png
%{_iconsdir}/hicolor/22x22/apps/akonadi-ews.png
%{_iconsdir}/hicolor/24x24/apps/akonadi-ews.png
%{_iconsdir}/hicolor/32x32/apps/akonadi-ews.png
%{_iconsdir}/hicolor/32x32/apps/ox.png
%{_iconsdir}/hicolor/48x48/apps/akonadi-ews.png
%{_iconsdir}/hicolor/48x48/apps/ox.png
%{_iconsdir}/hicolor/64x64/apps/akonadi-ews.png
%{_iconsdir}/hicolor/64x64/apps/ox.png
%{_iconsdir}/hicolor/72x72/apps/akonadi-ews.png
%{_iconsdir}/hicolor/96x96/apps/akonadi-ews.png
%{_datadir}/knotifications5/akonadi_ews_resource.notifyrc
%{_datadir}/knotifications5/akonadi_maildispatcher_agent.notifyrc
%{_datadir}/knotifications5/akonadi_newmailnotifier_agent.notifyrc
%{_datadir}/knotifications5/akonadi_pop3_resource.notifyrc
%{_datadir}/kservices5/akonadi.protocol
%dir %{_datadir}/kservices5/akonadi
%dir %{_datadir}/kservices5/akonadi/davgroupware-providers
%{_datadir}/kservices5/akonadi/davgroupware-providers/citadel.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/davical.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/egroupware.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/nextcloud.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/opengroupware.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/owncloud-pre5.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/owncloud-pre9.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/owncloud.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/scalix.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/sogo.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/yahoo.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/zarafa.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/zimbra.desktop
%{_datadir}/kservices5/pop3.protocol
%{_datadir}/kservices5/pop3s.protocol
%{_datadir}/kservicetypes5/davgroupwareprovider.desktop
%{_datadir}/mime/packages/kdepim-mime.xml
%{_datadir}/qlogging-categories5/kdepim-runtime.categories
%{_datadir}/qlogging-categories5/kdepim-runtime.renamecategories
