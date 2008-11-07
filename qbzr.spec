# spec originally for RHEL from: http://www.natemccallum.com/uploads/rpms/bzr/

Name:           qbzr
Version:        0.9.5
Release:        %mkrel 1
Summary:        QBzr is a cross-platform GUI front end for Bazaar, based on Qt toolkit.

Group:          Development/Other
License:        GPL
URL:            http://bazaar-vcs.org/QBzr
Source0:        https://launchpad.net/%{name}/stable/%{version}/+download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)

BuildArch:      noarch
BuildRequires:  python-devel bzr python-qt4
Requires:       python >= 2.4
Requires:       bzr >= 1.9
Requires:	python-qt4
Requires:	python-enchant
Requires:	python-pygments

%description
QBzr is a collection of GUI plugins for Bazaar.  Among the included
plugins are:
    * qadd -- GUI for adding files or directories
    * qannotate -- GUI interface for file annotation
    * qbrowse -- Browse your branch a-la Trac Browse Source
    * qcat -- View the contents of a file as of a given revision
    * qcommit -- GUI interface to enter log message and select changes to commit
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
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT --record=INSTALLED_FILES
# remove shebangs from all files as none should be executable scripts
sed -e '/^#!\//,1 d' -i $RPM_BUILD_ROOT/%py_puresitedir/bzrlib/plugins/qbzr/*.py


%clean
rm -rf $RPM_BUILD_ROOT


%files -f INSTALLED_FILES
%defattr(-,root,root,-)
