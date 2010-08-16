%define name	nagios-check_x224
%define version	9734
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Nagios x224 plugin
Group:		Networking/Other
License:	BSD
URL:		http://exchange.nagios.org/directory/Plugins/Remote-Access/check_x224/details
Source0:	check_x224
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Checks that the most basic parts of a Remote Desktop connection succeeds.
The Remote Desktop protocol builds on a protocol called x224. This plugin
checks that the initial and most basic parts of a Remote Desktop connection -
the part which is specified by x224 - succeeds. I.e., it does a bit more than a
TCP connection test at port 3389. 

%prep

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_x224.cfg <<'EOF'
define command {
	command_name    check_x224
	command_line    %{_datadir}/nagios/plugins/check_x224 -H $HOSTADDRESS$
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_x224.cfg
%{_datadir}/nagios/plugins/check_x224

