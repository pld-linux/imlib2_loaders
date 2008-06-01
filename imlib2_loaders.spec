Summary:	Additional Loaders for Imlib2
Summary(pl.UTF-8):	Dodatkowe biblioteki wczytujące dla Imlib2
Name:		imlib2_loaders
Version:	1.4.1.000
Release:	1
License:	GPL v2+ (XCF loader), BSD-like (the rest)
Group:		Libraries
Source0:	http://download.enlightenment.org/snapshots/2008-01-25/%{name}-%{version}.tar.bz2
# Source0-md5:	4b04b6b11e0e7ae8494fdc554a880429
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.4
BuildRequires:	edb-devel >= 1.0.5
BuildRequires:	eet-devel >= 1.0.1
BuildRequires:	imlib2-devel >= 1.4.1.000
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	imlib2 >= 1.4.1.000
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
	--disable-static \
	--enable-edb \
	--enable-eet \
	--enable-xcf
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/imlib2/loaders/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README
%attr(755,root,root) %{_libdir}/imlib2/loaders/*.so
