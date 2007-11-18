#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc
#
%include	/usr/lib/rpm/macros.java
%define		_snap	20070504-1631
Summary:	WebScarab - a Web Application Review tool for Java
Name:		webscarab
Version:	0.1
Release:	0.3
License:	GPL v2
Group:		Development/Languages/Java
URL:		http://www.owasp.org/index.php/OWASP_WebScarab_Project
Source0:	http://dl.sourceforge.net/owasp/%{name}-src-%{_snap}.zip
# Source0-md5:	b3ba39de51f3715aab4a7d75b7c8a4d5
BuildRequires:	ant
BuildRequires:	beanshell >= 2.0-0.b1
BuildRequires:	bsf >= 2.3.0
BuildRequires:	chardet
BuildRequires:	concurrent
BuildRequires:	htmlparser
BuildRequires:	jakarta-commons-logging >= 1.0.4
BuildRequires:	javahelp >= 2.0.02
BuildRequires:	jcommon >= 0.8.7
BuildRequires:	jfreechart >= 0.9.12
BuildRequires:	jpackage-utils
BuildRequires:	openamf
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	tagsoup >= 1.0rc2
BuildRequires:	wsdl4j
Requires:	jpackage-utils
Requires:	jre > 1.4
%if %(locale -a | grep -q '^en_US$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildArch:	noarch
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664} noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
WebScarab is a Web Application Review tool. It sprang from the designs
of the people inhabiting the WebAppSec list run from SourceForge, for
a powerful, free, open tool for reviewing web applications for
security vulnerabilities. Not much of the original design has actually
been implemented as envisioned. WebScarab started as a spider that
could download all the pages on a site. It stayed that way for almost
a year, before I decided to take lessons learned during the
development of Exodus and implement them as part of WebScarab.

%prep
%setup -q -n %{name}-%{_snap}
cp ../webscarab-current/server.p12 .

%build
required_jars="
bsf
concurrent
htmlparser
bsf
beanshell
jfreechart
jcommon
jhelp
chardet
tagsoup
wsdl
openamf
commons-logging
"
export CLASSPATH=$(build-classpath $required_jars)

export LC_ALL=en_US # source code not US-ASCII
%ant compile %{?with_javadoc:javadoc} proguard izpack

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_bindir}}
cp -a . $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
#%attr(755,root,root) %{_bindir}/%{name}
%{_appdir}
