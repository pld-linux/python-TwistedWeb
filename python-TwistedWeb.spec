%define 	module	TwistedWeb
%define		major	0.6
%define		minor	0

Summary:	Web library for Twisted
Summary(pl):	Biblioteka Web dla Twisted
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Web/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	a681931d2eb747ca871ef71d8d1f5ff1
URL:		http://twistedmatrix.com/projects/web/
BuildRequires:	python-devel >= 2.2
BuildRequires:	ZopeInterface
BuildRequires:	python-TwistedCore >= 2.4.0
Requires:	python-TwistedCore >= 2.4.0
Obsoletes:	python-Twisted-web
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted Web is a web application server written in pure Python, with
APIs at multiple levels of abstraction to facilitate different kinds
of web programming.

%description -l pl
Twisted Web to serwer aplikacji WWW napisany w czystym Pythonie z API
o wielu poziomach abstrakcji, maj±cych u³atwiæ ró¿ne rodzaje
programowania WWW.

%package doc
Summary:	Documentation for TwistedWeb
Summary(pl):	Dokumentacja do TwistedWeb
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for TwistedWeb.

%description doc -l pl
Dokumentacja offline do TwistedWeb.

%package examples
Summary:	Example programs for TwistedWeb
Summary(pl):	Programy przyk³adowe do TwistedWeb
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for TwistedWeb.

%description examples -l pl
Ten pakiet zawiera przyk³adowe programy dla TwistedWeb.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

install doc/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -ar doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/twisted/web
%{py_sitedir}/twisted/plugins/*
%{_mandir}/man1/*

%files doc
%defattr(644,root,root,755)
%doc doc/howto doc/img

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
