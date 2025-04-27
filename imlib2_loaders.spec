#
# Conditional build:
%bcond_with	eet	# eet images support

Summary:	Additional Loaders for Imlib2
Summary(pl.UTF-8):	Dodatkowe biblioteki wczytujące dla Imlib2
Name:		imlib2_loaders
Version:	1.12.5
Release:	1
License:	GPL v2+ (XCF loader), BSD-like (the rest)
Group:		Libraries
Source0:	https://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.xz
# Source0-md5:	7e0c6acb75ba739c7d777f2d1677532f
URL:		https://www.enlightenment.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
%{?with_eet:BuildRequires:	eet-devel >= 1.0.2}
BuildRequires:	imlib2-devel >= 1.10.0
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	imlib2 >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains additional image loaders for Imlib2 which for
some reason (such as license issues) are not distributed with Imlib2
directly.

%description -l pl.UTF-8
Ten pakiet zawiera dodatkowe biblioteki wczytujące obrazy dla Imlib2,
które z jakiegoś powodu (jak na przykład problemy licencyjne) nie są
rozprowadzane bezpośrednio z biblioteką Imlib2.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-eet%{!?with_eet:=no}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/imlib2/loaders/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README
%if %{with eet}
%attr(755,root,root) %{_libdir}/imlib2/loaders/eet.so
%endif
%attr(755,root,root) %{_libdir}/imlib2/loaders/xcf.so
