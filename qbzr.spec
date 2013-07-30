# spec originally for RHEL from: http://www.natemccallum.com/uploads/rpms/bzr/

Name:           qbzr
Version:        0.23.1
Release:        1
Summary:        Cross-platform GUI front end for Bazaar, based on Qt toolkit

Group:          Development/Other
License:        GPL
URL:            http://bazaar-vcs.org/QBzr
Source0:        https://launchpad.net/%{name}/0.22/%{version}/+download/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel bzr python-qt4
Requires:       python >= 2.6
Requires:       bzr >= 2.4
Requires:	python-qt4
Requires:	python-enchant
Requires:	python-pygments
Requires:	python-markupsafe

%description
QBzr is a collection of GUI plugins for Bazaar.  Among the included
plugins are:
    * qadd -- GUI for adding files or directories
    * qannotate -- GUI interface for file annotation
    * qbrowse -- Browse your branch a-la Trac Browse Source
    * qcat -- View the contents of a file as of a given revision
    * qcommit -- GUI interface to enter log message and
                 select changes to commit
    * qconfig -- Bazaar configuration
    * qdiff -- Side-by-side and unidiff view of changes.
    * qinfo -- information about branch
    * qinit -- Initialize new branch or shared repository
    * qlog -- Show log messages in GUI window.
    * qmerge -- Perform a three-way merge
    * qpull -- GUI interface for pull command
    * qpush -- GUI interface for push command
    * qrevert -- Revert changed files
    * qtag -- Edit tags 

%prep
%setup -q -n %{name}


%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --root %{buildroot} 
# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i $RPM_BUILD_ROOT/%py_puresitedir/bzrlib/plugins/qbzr/*.py


%clean


%files 
%defattr(-,root,root,-)
%dir %py_puresitedir/bzrlib/plugins/qbzr
%py_puresitedir/bzrlib/plugins/qbzr/*.py

%dir %py_puresitedir/bzrlib/plugins/qbzr/lib
%py_puresitedir/bzrlib/plugins/qbzr/lib/*.py

%dir %py_puresitedir/bzrlib/plugins/qbzr/lib/tests
%py_puresitedir/bzrlib/plugins/qbzr/lib/tests/*.py

%dir %py_puresitedir/bzrlib/plugins/qbzr/lib/extra
%py_puresitedir/bzrlib/plugins/qbzr/lib/extra/*.py

%dir %py_puresitedir/bzrlib/plugins/qbzr/lib/widgets
%py_puresitedir/bzrlib/plugins/qbzr/lib/widgets/*.py

%dir %py_puresitedir/bzrlib/plugins/qbzr/locale
%py_puresitedir/bzrlib/plugins/qbzr/locale/*

%py_puresitedir/bzrlib/plugins/qbzr/*.txt

%py_puresitedir/qbzr*.egg-info


%changelog
* Sat Sep 01 2012 Crispin Boylan <crisb@mandriva.org> 0.23.0-1
+ Revision: 816162
- New release

* Wed May 23 2012 Crispin Boylan <crisb@mandriva.org> 0.22.3-1
+ Revision: 800261
- New release

* Fri Apr 13 2012 Crispin Boylan <crisb@mandriva.org> 0.22.2-1
+ Revision: 790506
- New release

* Tue Feb 28 2012 Crispin Boylan <crisb@mandriva.org> 0.22.1-1
+ Revision: 781244
- New release

* Thu Feb 09 2012 Crispin Boylan <crisb@mandriva.org> 0.22.0-1
+ Revision: 772259
- New release

* Mon Feb 06 2012 Crispin Boylan <crisb@mandriva.org> 0.21.2-1
+ Revision: 771370
- New release

* Sun Aug 07 2011 Crispin Boylan <crisb@mandriva.org> 0.21.1-1
+ Revision: 693585
- New release

* Sun May 01 2011 Crispin Boylan <crisb@mandriva.org> 0.20.1-1
+ Revision: 661341
- New release

* Sat Feb 05 2011 Crispin Boylan <crisb@mandriva.org> 0.20.0-1
+ Revision: 636063
- New release

* Sat Nov 27 2010 Crispin Boylan <crisb@mandriva.org> 0.19.3-1mdv2011.0
+ Revision: 601760
- New release

* Tue Nov 02 2010 Crispin Boylan <crisb@mandriva.org> 0.19.2-2mdv2011.0
+ Revision: 591765
- Rebuild

* Sat Oct 02 2010 Crispin Boylan <crisb@mandriva.org> 0.19.2-1mdv2011.0
+ Revision: 582489
- New release

* Mon Sep 13 2010 Crispin Boylan <crisb@mandriva.org> 0.19.1-1mdv2011.0
+ Revision: 578083
- New release

* Sun Aug 08 2010 Crispin Boylan <crisb@mandriva.org> 0.19-2mdv2011.0
+ Revision: 567632
- Requires markupsafe

* Fri Aug 06 2010 Crispin Boylan <crisb@mandriva.org> 0.19-1mdv2011.0
+ Revision: 567028
- New release, requires bzr 2.1

* Thu Aug 05 2010 Crispin Boylan <crisb@mandriva.org> 0.18.7-1mdv2011.0
+ Revision: 566228
- New release

* Sun Jun 27 2010 Crispin Boylan <crisb@mandriva.org> 0.18.6-1mdv2011.0
+ Revision: 549205
- New release

* Mon Apr 05 2010 Crispin Boylan <crisb@mandriva.org> 0.18.5-1mdv2010.1
+ Revision: 531527
- New release

* Thu Mar 25 2010 Crispin Boylan <crisb@mandriva.org> 0.18.4-1mdv2010.1
+ Revision: 527364
- New release

* Fri Mar 05 2010 Crispin Boylan <crisb@mandriva.org> 0.18.3-1mdv2010.1
+ Revision: 514794
- New release

* Mon Feb 22 2010 Frederik Himpe <fhimpe@mandriva.org> 0.18.2-1mdv2010.1
+ Revision: 509690
- Update to new version 0.18.2

* Fri Feb 05 2010 Crispin Boylan <crisb@mandriva.org> 0.18.1-1mdv2010.1
+ Revision: 501122
- New release

* Fri Jan 22 2010 Crispin Boylan <crisb@mandriva.org> 0.18-1mdv2010.1
+ Revision: 494886
- New release

* Mon Nov 09 2009 Crispin Boylan <crisb@mandriva.org> 0.16-1mdv2010.1
+ Revision: 463835
- New release

* Sun Nov 08 2009 Crispin Boylan <crisb@mandriva.org> 0.15-1mdv2010.1
+ Revision: 462843
- New release

* Sat Oct 17 2009 Crispin Boylan <crisb@mandriva.org> 0.14.4-1mdv2010.0
+ Revision: 458000
- New release

* Fri Sep 18 2009 Crispin Boylan <crisb@mandriva.org> 0.14.2-1mdv2010.0
+ Revision: 444264
- New release

* Mon Sep 14 2009 Crispin Boylan <crisb@mandriva.org> 0.14.1-1mdv2010.0
+ Revision: 439697
- New release

* Sat Aug 22 2009 Crispin Boylan <crisb@mandriva.org> 0.14-1mdv2010.0
+ Revision: 419732
- New release

* Wed Aug 12 2009 Crispin Boylan <crisb@mandriva.org> 0.13.1-1mdv2010.0
+ Revision: 415323
- New release

* Mon Jul 13 2009 Crispin Boylan <crisb@mandriva.org> 0.12-1mdv2010.0
+ Revision: 395437
- New release

* Fri Jun 12 2009 Crispin Boylan <crisb@mandriva.org> 0.11-1mdv2010.0
+ Revision: 385383
- New release

* Tue Jun 02 2009 Crispin Boylan <crisb@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 382309
- New release

* Thu Apr 30 2009 Crispin Boylan <crisb@mandriva.org> 0.9.9-1mdv2010.0
+ Revision: 369184
- New release

* Sat Feb 14 2009 Crispin Boylan <crisb@mandriva.org> 0.9.8-1mdv2009.1
+ Revision: 340239
- New release

* Wed Feb 11 2009 Crispin Boylan <crisb@mandriva.org> 0.9.7-1mdv2009.1
+ Revision: 339607
- New release

* Sat Jan 10 2009 Crispin Boylan <crisb@mandriva.org> 0.9.6-1mdv2009.1
+ Revision: 328060
- Add bin
- Use proper file list
- New version

* Fri Dec 26 2008 Crispin Boylan <crisb@mandriva.org> 0.9.5-2mdv2009.1
+ Revision: 319455
- Rebuild for python2.6

* Fri Nov 07 2008 Crispin Boylan <crisb@mandriva.org> 0.9.5-1mdv2009.1
+ Revision: 300448
- Fix summary
- Initial mandriva package
- create qbzr

