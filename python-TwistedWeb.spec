%define 	module	TwistedWeb

Summary:	Web library for Twisted
Summary(pl):	Biblioteka Web dla Twisted
Name:		python-%{module}
Version:	0.5.0
Release:	0.2
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Web/0.5/%{module}-%{version}.tar.bz2
# Source0-md5:	287b9402ca99d05e6d3be99413317633
URL:		http://twistedmatrix.com/projects/web/
BuildRequires:	python-devel >= 2.2
Requires:	python-Twisted >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted Web is a web application server written in pure Python, with 
APIs at multiple levels of abstraction to facilitate different kinds 
of web programming.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

install -d $RPM_BUILD_ROOT%{py_sitedir}
mv -f $RPM_BUILD_ROOT%{py_sitescriptdir}/* $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitedir}/twisted/web
