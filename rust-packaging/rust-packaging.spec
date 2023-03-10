%global commit c4872324021c70dc2d4c01f50b4938528cebd0ec
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rust-packaging
Version:        24~pre.6.git.%{shortcommit}
Release:        1%{?dist}
Summary:        RPM macros and generators for building Rust packages
License:        MIT

URL:            https://pagure.io/fedora-rust/rust-packaging
Source:         %{url}/archive/%{commit}/rust-packaging-%{shortcommit}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n rust-rpm-macros
Summary:        RPM macros for building Rust projects
Obsoletes:      rust-packaging < 24

%description -n rust-rpm-macros 
RPM macros for building Rust projects.

%package -n rust-srpm-macros
Summary:        RPM macros for building source packages for Rust projects

%description -n rust-srpm-macros
RPM macros for building source packages for Rust projects.

%package -n cargo-rpm-macros
Summary:        RPM macros for building projects with cargo

Obsoletes:      rust-packaging < 24
Provides:       rust-packaging = %{version}-%{release}

Requires:       cargo
Requires:       cargo2rpm
Requires:       gawk
Requires:       rust-rpm-macros
Requires:       rust-srpm-macros

%description -n cargo-rpm-macros
RPM macros for building projects with cargo.

%prep
%autosetup -n rust-packaging-%{shortcommit} -p1

%build

%install
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.cargo
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust
install -D -p -m 0644 -t %{buildroot}/%{_rpmmacrodir} macros.d/macros.rust-srpm
install -D -p -m 0644 -t %{buildroot}/%{_fileattrsdir} fileattrs/cargo.attr

%files -n rust-rpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.rust

%files -n rust-srpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.rust-srpm

%files -n cargo-rpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.cargo
%{_fileattrsdir}/cargo.attr

%changelog
* Fri Feb 10 2023 Fabio Valentini <decathorpe@gmail.com> - 24~pre.6.git.c487232-1
- Bump to commit c487232.

