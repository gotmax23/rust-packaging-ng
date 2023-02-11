%bcond_without check

%global commit 5808e2d96a120af2c4f29ad9573c620a64301d19
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           cargo2rpm
Version:        0.1.0~pre.1.git.%{shortcommit}
Release:        1%{?dist}
Summary:        Translation layer between cargo and RPM
License:        MIT

URL:            https://pagure.io/fedora-rust/cargo2rpm
Source:         %{url}/archive/%{commit}/cargo2rpm-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

Requires:       cargo

%description
Low-level translation layer between cargo and RPM.

%prep
%autosetup -n cargo2rpm-%{shortcommit} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%if %{with check}
%tox
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/cargo2rpm
%{python3_sitelib}/cargo2rpm-*.dist-info/
%{python3_sitelib}/cargo2rpm/

%changelog
* Sat Feb 11 2023 Fabio Valentini <decathorpe@gmail.com> - 0.1.0~pre.1.git.5808e2d-1
- Bump to commit 5808e2d.

* Fri Feb 10 2023 Fabio Valentini <decathorpe@gmail.com> - 0.1.0~pre.0.git.adf2cb9-1
- Initial packaging.

