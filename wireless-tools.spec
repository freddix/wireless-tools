Summary:	Wireless ethernet configuration tools
Name:		wireless-tools
Version:	29
Release:	1
License:	GPL v2
Group:		Networking/Admin
Source0:	http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/wireless_tools.%{version}.tar.gz
# Source0-md5:	e06c222e186f7cc013fd272d023710cb
Patch0:		%{name}-optflags.patch
URL:		http://www.hpl.hp.com/personal/Jean_Tourrilhes/Linux/Tools.html
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the Wireless tools, used to manipulate the
Wireless Extensions. The Wireless Extension is an interface allowing
you to set Wireless LAN specific parameters and get the specific stats
for wireless networking equipment.

%package libs
Summary:	Wireless Extension library
Group:		Libraries

%description libs
Wireless Extension library.

%package devel
Summary:	Wireless Extension library (development files)
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Wireless Extension library (development files).

%prep
%setup -qn wireless_tools.%{version}
%patch0 -p1

%build
%{__make}				\
	CC="%{__cc}" OPT="%{rpmcflags}"	\
	KERNEL_SRC=%{_kernelsrcdir}	\
	OPTFLAGS="%{rpmcflags}"

%{__make} libiw.a			\
	CC="%{__cc}" OPT="%{rpmcflags}"	\
	KERNEL_SRC=%{_kernelsrcdir}	\
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_libdir},%{_includedir},%{_mandir}/man8}

%{__make} install install-dynamic			\
	INSTALL_DIR=$RPM_BUILD_ROOT%{_sbindir}		\
	INSTALL_INC=$RPM_BUILD_ROOT%{_includedir}	\
	INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir}		\
	INSTALL_MAN=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc READ* INSTA* PCM*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

