Summary:	GNU OCR
Summary(pl):	Program GNU do OCR
Name:		gocr
Version:	0.3.4
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	http://prdownloads.sourceforge.net/jocr/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-paths.patch
URL:		http://jocr.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	netpbm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xprefix	/usr/X11R6
%define		_xbindir	%{_xprefix}/bin

%description
GOCR is an optical character recognition program, released under the
GNU General Public License. It reads images in many formats (pnm, pbm,
pgm, ppm, some pcx and tga image files (or PNM from stdin); if
pnm-tools installed and running linux-like system you can also use
pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp and others) and outputs
a text file.

%description -l pl
GOCR jest programem do rozpoznawania pisma wypuszczonym na licencji
GNU GPL. Czyta obrazki w formatach pnm, pbm, pgm, ppm, niektóre pcx
i tga; je¿eli s± zainstalowane narzêdzia do PNM, mo¿e te¿ czytaæ
pnm.gz, pnm.bz2, png,jpg, tiff, gif, bmp i inne. Wynikiem jest plik
tekstowy.

%package gtk
Summary:	Gtk+ frontend for gocr
Summary(pl):	Frontend Gtk+ do gocr
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Requires:	%{name} = %{version}

%description gtk
Gtk+-based frontend for gocr.

%description gtk -l pl
Frontend do gocr oparty o Gtk+.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
%configure
%{__make}

(cd frontend/gnome
autoconf
(cd src ; autoconf)
%configure --prefix=%{_xprefix} --bindir=%{_xbindir}
%{__make})

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ln -sf gnome/mkinstalldirs frontend/mkinstalldirs
%{__make} -C frontend/gnome install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS CREDITS HISTORY README REMARK.txt REVIEW TODO \
	doc/{examples.txt,ocr.ps,unicode.txt} \
	frontend/gnome/{AUTHORS,README,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files gtk
%defattr(644,root,root,755)
%doc frontend/gnome/*.gz
%attr(755,root,root) %{_xbindir}/*
