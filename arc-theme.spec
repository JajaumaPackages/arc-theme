Name:           arc-theme
Version:        20160923
Release:        1%{?dist}
Summary:        A flat theme with transparent elements

License:        GPLv3
URL:            https://github.com/horst3180/arc-theme
Source0:        https://github.com/horst3180/arc-theme/archive/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel
Requires:       gtk2
Requires:       gtk3
Requires:       gnome-themes-standard
Requires:       gtk-murrine-engine

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell
which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity,
Budgie, Pantheon, XFCE, Mate, etc.


%prep
%setup -q
./autogen.sh


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%files
%doc AUTHORS HACKING.md README.md
%license COPYING
%{_datadir}/themes/Arc
%{_datadir}/themes/Arc-Dark
%{_datadir}/themes/Arc-Darker


%changelog
* Tue Sep 27 2016 Jajauma's Packages <jajauma@yandex.ru> - 20160923-1
- Public release
