#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kdepim-runtime
Summary:	kdepim runtime
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	006862b3cc554b8fd951888eeff9f1bf
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
BuildRequires:	cmake >= 3.20
BuildRequires:	cyrus-sasl-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-notes-devel >= %{kdeappsver}
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
BuildRequires:	libetebase-devel
BuildRequires:	libkolabxml-devel >= 1.1
BuildRequires:	libxslt-progs
BuildRequires:	ninja
BuildRequires:	qca-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Runtime components for Akonadi KDE. This package contains Akonadi
agents written using KDE Development Platform libraries.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


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
%{_datadir}/knotifications5/akonadi_google_resource.notifyrc
%attr(755,root,root) %{_bindir}/akonadi_akonotes_resource
%attr(755,root,root) %{_bindir}/akonadi_birthdays_resource
%attr(755,root,root) %{_bindir}/akonadi_contacts_resource
%attr(755,root,root) %{_bindir}/akonadi_davgroupware_resource
%attr(755,root,root) %{_bindir}/akonadi_etesync_resource
%attr(755,root,root) %{_bindir}/akonadi_ews_resource
%attr(755,root,root) %{_bindir}/akonadi_ewsmta_resource
%attr(755,root,root) %{_bindir}/akonadi_ical_resource
%attr(755,root,root) %{_bindir}/akonadi_icaldir_resource
%attr(755,root,root) %{_bindir}/akonadi_imap_resource
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
%{_datadir}/akonadi/accountwizard
%{_datadir}/akonadi/agents
%{_datadir}/akonadi/firstrun
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.Maildir.Settings.xml
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.MixedMaildir.Settings.xml
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_datadir}/knotifications5/akonadi_ews_resource.notifyrc
%{_datadir}/knotifications5/akonadi_maildispatcher_agent.notifyrc
%{_datadir}/knotifications5/akonadi_newmailnotifier_agent.notifyrc
%{_datadir}/knotifications5/akonadi_pop3_resource.notifyrc
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
%{_datadir}/mime/packages/kdepim-mime.xml
%{_datadir}/qlogging-categories5/kdepim-runtime.categories
%{_datadir}/qlogging-categories5/kdepim-runtime.renamecategories
%dir %{_libdir}/qt5/plugins/pim5/akonadi/config
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/akonotesconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/birthdaysconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/contactsconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/googleconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/icalconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/icaldirconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/maildirconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/maildispatcherconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/mboxconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/mixedmaildirconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/newmailnotifierconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/notesconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/openxchangeconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/pop3config.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/tomboynotesconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/vcardconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/akonadi/config/vcarddirconfig.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/kcms/kaddressbook/kcm_ldap.so
%attr(755,root,root) %{_libdir}/qt5/plugins/pim5/mailtransport/mailtransport_akonadiplugin.so
%{_desktopdir}/org.kde.akonadi_davgroupware_resource.desktop
%{_desktopdir}/org.kde.akonadi_google_resource.desktop
%{_desktopdir}/org.kde.akonadi_imap_resource.desktop
%{_desktopdir}/org.kde.akonadi_kolab_resource.desktop
%{_datadir}/kservices5/akonadi/davgroupware-providers/mailbox-org.desktop
%{_desktopdir}/org.kde.akonadi_contacts_resource.desktop
%{_desktopdir}/org.kde.akonadi_ews_resource.desktop
%{_desktopdir}/org.kde.akonadi_openxchange_resource.desktop
%{_desktopdir}/org.kde.akonadi_vcard_resource.desktop
%{_desktopdir}/org.kde.akonadi_vcarddir_resource.desktop
