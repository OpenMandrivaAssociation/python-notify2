Summary:	Python interface to desktop notifications
Name:		python-notify2
Version:	0.3.1
Release:	3
License:	LGPLv2
Group:		Development/Python
Url:		https://pypi.org/project/notify2/
Source0:	https://files.pythonhosted.org/packages/aa/e8/d4b335aa739dc299a77766ecc5f1972d1de1993524aa94acef3219bba315/notify2-%{version}.tar.gz
BuildRequires:	python-setuptools

%description
Python interface to desktop notifications

%prep
%autosetup -p1 -n notify2-%{version}
%{__python} setup.py build

%install
%{__python} setup.py install --root=%{buildroot}

%files
%{python_sitelib}/notify2.py
%{python_sitelib}/*.egg-info
