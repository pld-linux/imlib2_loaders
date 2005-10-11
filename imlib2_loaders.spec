Summary:	Additional Loaders for Imlib2
Summary(pl):	Dodatkowe biblioteki wczytuj±ce dla Imlib2
Name:		imlib2_loaders
Version:	1.2.1.010
Release:	1
License:	Mixed (BSD and GPL)
Group:		Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	d70d26cd1b1dc7a84dff0e75c234e529
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edb-devel >= 1.0.5
BuildRequires:	eet-devel
BuildRequires:	imlib2-devel >= 1.2.1
BuildRequires:	libtool
Requires:	imlib2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains additional image loaders for Imlib2 which for
some reason (such as license issues) are not distributed with Imlib2
directly.

%description -l pl
Ten pakiet zawiera dodatkowe biblioteki wczytuj±ce obrazy dla Imlib2,
które z jakiego¶ powodu (jak na przyk³ad problemy licencyjne) nie s±
rozprowadzane bezpo¶rednio z bibliotek± Imlib2.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/imlib2/loaders/*.so
