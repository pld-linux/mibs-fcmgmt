Summary:	MIBs for Fibre Channel Management
Name:		mibs-fcmgmt
Version:	20010115
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.icir.org/fenner/mibs/extracted/FIBRE-CHANNEL-MGMT-MIB-ipfc-06.txt
# Source0-md5:	c82341f30138c8b6b9cc3970d644600b
Requires:	mibs-dirs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mibdir	%{_datadir}/mibs

%description
MIBs for Fibre Channel Management.

%prep
%setup -qcT
cp -a %{SOURCE0} FIBRE-CHANNEL-MGMT-MIB

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mibdir}
cp -a *-MIB $RPM_BUILD_ROOT%{mibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{mibdir}/*
