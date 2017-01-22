Summary:	Additional Loaders for Imlib2
Summary(pl.UTF-8):	Dodatkowe biblioteki wczytujące dla Imlib2
Name:		imlib2_loaders
Version:	1.4.9
Release:	1
License:	GPL v2+ (XCF loader), BSD-like (the rest)
Group:		Libraries
Source0:	http://downloads.sourceforge.net/enlightenment/%{name}-%{version}.tar.bz2
# Source0-md5:	57c37318d5421b623c6c9d2680b98643
URL:		http://enlightenment.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	eet-devel >= 1.0.2
BuildRequires:	imlib2-devel >= 1.4.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	imlib2 >= 1.4.9
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-eet \
	--enable-xcf
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
%attr(755,root,root) %{_libdir}/imlib2/loaders/ani.so
%attr(755,root,root) %{_libdir}/imlib2/loaders/eet.so
%attr(755,root,root) %{_libdir}/imlib2/loaders/ico.so
%attr(755,root,root) %{_libdir}/imlib2/loaders/xcf.so
