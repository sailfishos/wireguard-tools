Name:           wireguard-tools
Version:        1.0.20210914
Release:        1
URL:            https://www.wireguard.com/
Summary:        Fast, modern, secure VPN tunnel
License:        GPLv2
Source0:        %{name}-%{version}.tar.gz 

BuildRequires: make
BuildRequires: gcc

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

This package provides the wg binary for controlling WireGuard.

%package doc
Summary:    WireGuard tools documentation

%description doc
WireGuard tools documentation. Contains contrib examples and man pages.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%set_build_flags
## Start DNS Hatchet
pushd contrib/dns-hatchet
./apply.sh
popd
## End DNS Hatchet

%make_build RUNSTATEDIR=%{_rundir} -C src

%install
%make_install BINDIR=%{_bindir} MANDIR=%{_mandir} RUNSTATEDIR=%{_rundir} \
WITH_BASHCOMPLETION=yes WITH_WGQUICK=yes WITH_SYSTEMDUNITS=no -C src

%files
%doc README.md
%license COPYING
%{_bindir}/wg
%{_bindir}/wg-quick
%{_sysconfdir}/wireguard/
%{_datadir}/bash-completion/completions/wg
%{_datadir}/bash-completion/completions/wg-quick

%files doc
# Contrib files do not have proper permissions set
%defattr(0664, root, root, 0755)
%license COPYING
%doc contrib
%{_mandir}/man8/wg.8*
%{_mandir}/man8/wg-quick.8*
