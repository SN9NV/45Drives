Name: gtools
Version: 2.0
Release: 10
Summary: Clustering cli tools
Source0: gtools-2.0.tar.gz
License: GPL
Group: Development/Tools 
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Beta release of gtools 2.0. Drive Map and Disk Pool tools

%prep
%setup -q

%build

%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/gtools/bin
install -m 0755 dmap $RPM_BUILD_ROOT/opt/gtools/bin/dmap
install -m 0755 loadtest $RPM_BUILD_ROOT/opt/gtools/bin/loadtest
install -m 0755 lsdev $RPM_BUILD_ROOT/opt/gtools/bin/lsdev
install -m 0755 lsmodel $RPM_BUILD_ROOT/opt/gtools/bin/lsmodel
install -m 0755 lstemp $RPM_BUILD_ROOT/opt/gtools/bin/lstemp
install -m 0755 lsvdev $RPM_BUILD_ROOT/opt/gtools/bin/lsvdev
install -m 0755 mapASR81605Z $RPM_BUILD_ROOT/opt/gtools/bin/mapASR81605Z
install -m 0755 maplsi $RPM_BUILD_ROOT/opt/gtools/bin/maplsi
install -m 0755 mapr750 $RPM_BUILD_ROOT/opt/gtools/bin/mapr750
install -m 0755 maprr3740 $RPM_BUILD_ROOT/opt/gtools/bin/maprr3740
install -m 0755 wipedev $RPM_BUILD_ROOT/opt/gtools/bin/wipedev
install -m 0755 zcreate $RPM_BUILD_ROOT/opt/gtools/bin/zcreate

install -m 0775 -d ${RPM_BUILD_ROOT}%{_bindir}
ln -sf /opt/gtools/bin/dmap ${RPM_BUILD_ROOT}%{_bindir}
ln -sf /opt/gtools/bin/loadtest ${RPM_BUILD_ROOT}%{_bindir}
ln -sf /opt/gtools/bin/lsdev ${RPM_BUILD_ROOT}%{_bindir}
#ln -sf /opt/gtools/bin/lsmodel ${RPM_BUILD_ROOT}%{_bindir}
#ln -sf /opt/gtools/bin/lstemp ${RPM_BUILD_ROOT}%{_bindir}
#ln -sf /opt/gtools/bin/lsvdev ${RPM_BUILD_ROOT}%{_bindir}
#ln -sf /opt/gtools/bin/mapASR81605Z ${RPM_BUILD_ROOT}%{_bindir}
#ln -sf /opt/gtools/bin/maplsi ${RPM_BUILD_ROOT}%{_bindir}
#ln -sf /opt/gtools/bin/mapr750 ${RPM_BUILD_ROOT}%{_bindir}
#ln -sf /opt/gtools/bin/maprr3740 ${RPM_BUILD_ROOT}%{_bindir}
ln -sf /opt/gtools/bin/wipedev ${RPM_BUILD_ROOT}%{_bindir}
ln -sf /opt/gtools/bin/zcreate ${RPM_BUILD_ROOT}%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo . .
echo "All done"

%files
/opt/gtools/bin/dmap
/opt/gtools/bin/loadtest
/opt/gtools/bin/lsdev
/opt/gtools/bin/lstemp
/opt/gtools/bin/lsmodel
/opt/gtools/bin/lsvdev
/opt/gtools/bin/mapASR81605Z
/opt/gtools/bin/maplsi
/opt/gtools/bin/mapr750
/opt/gtools/bin/maprr3740
/opt/gtools/bin/wipedev
/opt/gtools/bin/zcreate

%{_bindir}/dmap
%{_bindir}/loadtest
%{_bindir}/lsdev
#%{_bindir}/lstemp
#%{_bindir}/lsvdev
#%{_bindir}/mapASR81605Z
#%{_bindir}/maplsi
#%{_bindir}/mapr750
#%{_bindir}/maprr3740
%{_bindir}/wipedev
%{_bindir}/zcreate

%changelog
* Thu Dec 05 2016 BK
- Release 10 added check-root

* Thu Nov 23 2016 BK
- Release 9 Fixed mapping issue when switching machines

* Thu Nov 23 2016 BK
- Release 8 Re-added link lsdev to bin dir

* Tue Nov 22 2016 BK
- Release 7 Removed /usr/bin link for map* and ls* scripts
- Learned changelog of .spec needs to go in chron order

* Sun Nov 20 2016 BK
- Release 0 Initial Creation

* Sun Nov 20 2016 BK
- Release 1 Testing symlinks

* Sun Nov 20 2016 BK
- Release 2 Added symlinks

* Sun Nov 20 2016 BK
- Release 3 Permissions
 
* Sun Nov 20 2016 BK
- Release 4 Included loadtest and supporting scripts

* Sun Nov 20 2016 BK
- Release 5 Included added lstemp, lsvdev

* Sun Nov 20 2016 BK
- Release 6 Updates
