Name: myapp
Version: 1.0
Release: 1%{?dist}
Summary: My awesome app
License: GPL
Group: Applications/System
URL: https://example.com/myapp
Source0: myapp.tar.gz

BuildRequires: python3-devel, tkinter

%description
My awesome app is an amazing tool that you will love.

%prep
%setup -q -n myapp

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%{python3_sitelib}/myapp/
/usr/bin/myapp

%changelog
* Mon Feb 20 2023 My Name <myname@example.com> - 1.0-1
- Initial build.
