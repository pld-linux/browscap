Summary:	PHP browscap file
Name:		browscap
Version:	5009
Release:	1
License:	Freeware
Group:		Applications/Text
URL:		http://browscap.org/
Source0:	php_%{name}.ini
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The browscap.ini file contains information about each known browser.

It is a standard text file that lists features a browser supports and
maps browser capabilities to the HTTP User Agent header.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/php_browscap.ini
