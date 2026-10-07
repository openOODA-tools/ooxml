Name:           ooxml
Version:        0.1.0
Release:        1%{?dist}
Summary:        Streaming XML parser with XPath evaluation and JSON Lines stream conversion.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooxml
Source0:        ooxml-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooxml is a sovereign, capability-bounded XML INSPECTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooxml
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooxml-uninstall

%files
/usr/bin/ooxml
/usr/bin/ooxml-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
