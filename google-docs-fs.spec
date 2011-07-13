Summary:	A filesystem to access Google Docs using any computer
Name:		google-docs-fs
Version:	1.0
Release:	0.1.rc1%{?dist}.R

License:	GPLv2
Url:		http://code.google.com/p/google-docs-fs
Group:		System Environment/Base
Source0:	http://google-docs-fs.googlecode.com/files/%{name}-1.0rc1.tar.gz

BuildRequires:	fuse-devel
BuildRequires:	python-devel
Requires:	fuse-python
Requires:	python-gdata

BuildArch:	noarch


%description
This project aims to allow you to connect to Google Docs and treat it as a 
file system. Combine the portability of Google Docs with the flexibility and
power of using the office suite of your choice.

This will allow you to mount your Google Docs account as you would a normal
filesystem. You will then be able to use it as if it were a file system on
your hard disk, with all operations being transmitted seamlessly to Google
Docs.


%prep
%setup -q -n %{name}


%build


%install
python ./setup.py install \
    --prefix="%{_prefix}" \
    --root="%{buildroot}"

chmod 755 %{buildroot}%{python_sitelib}/googledocsfs/*.py*


%files
%defattr(-,root,root)
%doc README.txt LICENSE.txt
%{_bindir}/gmount*
%{_bindir}/gumount
%{python_sitelib}/google_docs_fs*.egg-info
%{python_sitelib}/googledocsfs/*.py*


%changelog
* Wed Jul 13 2011 Arkady L. Shane <ashejn@yandex-team.ru> 1.0-0.1.rc1
- initial version based on 1.0rc1
