Summary:	GNU OCR
Summary(pl):	Program GNU do OCR
Name:		gocr
Version:	0.37
Release:	3
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/jocr/%{name}-%{version}.tar.gz
# Source0-md5:	824984b5d5c44b6e3c2a1a1d5fb6d48e
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://jocr.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	netpbm-devel
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOCR is an optical character recognition program, released under the
GNU General Public License. It reads images in many formats (pnm, pbm,
pgm, ppm, some pcx and tga image files (or PNM from stdin); if
pnm-tools installed and running linux-like system you can also use
pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp and others) and outputs a
text file.

%description -l pl
GOCR jest programem do rozpoznawania pisma wypuszczonym na licencji
GNU GPL. Czyta obrazki w formatach pnm, pbm, pgm, ppm, niekt�re pcx i
tga; je�eli s� zainstalowane narz�dzia do PNM, mo�e te� czyta� pnm.gz,
pnm.bz2, png,jpg, tiff, gif, bmp i inne. Wynikiem jest plik tekstowy.

%package gtk
Summary:	Gtk+ frontend for gocr
Summary(pl):	Frontend Gtk+ do gocr
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}

%description gtk
Gtk+-based frontend for gocr.

%description gtk -l pl
Frontend do gocr oparty o Gtk+.

%prep
%setup -q

%build
%{__aclocal}
cp -f /usr/share/automake/config.* .
%{__autoconf}
%configure
%{__make}

# ok its ugly..but works
cd frontend/gnome
rm -f Makefile configure src/missing
%{__aclocal}
%{__automake}
%{__autoconf}
cd src
%{__aclocal}
%{__automake}
%{__autoconf}
cd ..
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Graphics,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} -C frontend/gnome install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS HISTORY README REMARK.txt REVIEW TODO
%doc doc/{examples.txt,gocr.html,unicode.txt}
%attr(755,root,root) %{_bindir}/gocr
%{_mandir}/man1/gocr.1*

%files gtk
%defattr(644,root,root,755)
%doc frontend/gnome/{AUTHORS,README,TODO}
%attr(755,root,root) %{_bindir}/gtk-ocr
%{_applnkdir}/Graphics/*
%{_pixmapsdir}/*