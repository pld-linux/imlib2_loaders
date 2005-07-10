Summary:	Additional Loaders for Imlib2
Name:		imlib2_loaders
Version:	1.2.1.001
%define	_snap	20050704
Release:	0.%{_snap}.0.1
License:	Mixed (BSD and GPL)
Group:		Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/libs/%{name}-%{_snap}.tar.gz
# Source0-md5:	ff63cea4860ae7c085895ab452cac179
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edb-devel
BuildRequires:	eet-devel
BuildRequires:	imlib2-devel
BuildRequires:	libtool
Requires:	imlib2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains additional image loaders for Imlib2 which for
some reason (such as license issues) are not distributed with Imlib2
directly.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--enable-edb \
	--enable-eet \
	--enable-xcf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/imlib2/loaders/*.so
