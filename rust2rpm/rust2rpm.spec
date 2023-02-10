%bcond_without check

%global commit 3443c98887f019eab11903f1fc76f086cbf0814c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rust2rpm
Version:        24~pre.0.git.%{shortcommit}
Release:        1%{?dist}
Summary:        Generate RPM spec files for Rust crates
License:        MIT

URL:            https://pagure.io/fedora-rust/rust2rpm
Source:         %{url}/archive/%{commit}/rust2rpm-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with check}
BuildRequires:  cargo
%endif

Requires:       cargo
Requires:       cargo2rpm
Requires:       cargo-rpm-macros

# obsolete old Provides
Obsoletes:      rust2rpm < 24
Obsoletes:      cargo-inspector < 24

# obsolete + provide removed Python subpackages
Provides:       python3-rust2rpm = %{version}-%{release}
Obsoletes:      python3-rust2rpm < 24
Provides:       python3-rust2rpm-core = %{version}-%{release}
Obsoletes:      python3-rust2rpm-core < 24

%description
rust2rpm is a tool that automates the generation of RPM spec files for
Rust crates.

%prep
%autosetup -n rust2rpm-%{shortcommit} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

# cargo-inspector is no longer needed
rm %{buildroot}/%{_bindir}/cargo-inspector

%check
%if %{with check}
%tox
%endif

%files
%license LICENSE
%doc README.md
%doc NEWS
%{_bindir}/rust2rpm
%{python3_sitelib}/rust2rpm-*.dist-info/
%{python3_sitelib}/rust2rpm/

%changelog
* Fri Feb 10 2023 Fabio Valentini <decathorpe@gmail.com> - 24~pre.0.git.3443c98-1
- Initial packaging.

