%define 	module	TwistedWeb
%define		major	8.0
%define		minor	0

Summary:	Web library for Twisted
Summary(pl.UTF-8):	Biblioteka Web dla Twisted
Name:		python-%{module}
Version:	%{major}.%{minor}
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Web/%{major}/%{module}-%{version}.tar.bz2
# Source0-md5:	f13d39085503ac5cb7edc2c4a0012d52
URL:		http://twistedmatrix.com/projects/web/
BuildRequires:	ZopeInterface
BuildRequires:	python-TwistedCore >= 2.4.0
BuildRequires:	python-devel >= 2.2
Requires:	python-TwistedCore >= 2.4.0
Obsoletes:	python-Twisted-web
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted Web is a web application server written in pure Python, with
APIs at multiple levels of abstraction to facilitate different kinds
of web programming.

%description -l pl.UTF-8
Twisted Web to serwer aplikacji WWW napisany w czystym Pythonie z API
o wielu poziomach abstrakcji, mających ułatwić różne rodzaje
programowania WWW.

%package doc
Summary:	Documentation for TwistedWeb
Summary(pl.UTF-8):	Dokumentacja do TwistedWeb
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for TwistedWeb.

%description doc -l pl.UTF-8
Dokumentacja offline do TwistedWeb.

%package examples
Summary:	Example programs for TwistedWeb
Summary(pl.UTF-8):	Programy przykładowe do TwistedWeb
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for TwistedWeb.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla TwistedWeb.

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

cp -a doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitedir}/*.egg-info
%{py_sitedir}/twisted/web
%{py_sitedir}/twisted/plugins/*

%files doc
%defattr(644,root,root,755)
%doc doc/howto doc/img

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
