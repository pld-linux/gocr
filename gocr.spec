Summary:	GNU OCR
Summary(pl.UTF-8):	Program GNU do OCR
Name:		gocr
Version:	0.45
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/jocr/%{name}-%{version}.tar.gz
# Source0-md5:	134d459f64656b201ca66eebafa108f0
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-link.patch
Patch1:		%{name}-lib64.patch
URL:		http://jocr.sourceforge.net/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
BuildRequires:	netpbm-devel
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
Requires:	netpbm-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GOCR is an optical character recognition program, released under the
GNU General Public License. It reads images in many formats (pnm, pbm,
pgm, ppm, some pcx and tga image files (or PNM from stdin); if
pnm-tools installed and running linux-like system you can also use
pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp and others) and outputs a
text file.

%description -l pl.UTF-8
GOCR jest programem do rozpoznawania pisma wypuszczonym na licencji
GNU GPL. Czyta obrazki w formatach pnm, pbm, pgm, ppm, niektóre pcx i
tga; jeżeli są zainstalowane narzędzia do PNM, może też czytać pnm.gz,
pnm.bz2, png,jpg, tiff, gif, bmp i inne. Wynikiem jest plik tekstowy.

%package tcl
Summary:	Tcl/Tk frontend for gocr
Summary(pl.UTF-8):	Frontend Tcl/Tk do gocr
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	tk
# dropped, GTK+ 1.x code which nobody cared to update
Obsoletes:	gocr-gtk

%description tcl
Tcl/Tk frontend for gocr.

%description tcl -l pl.UTF-8
Frontend Tcl/Tk do gocr.

%prep
%setup -q
%patch0 -p1
%if "%{_lib}" != "lib"
%patch1 -p1
%endif

%build
cp -f /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	--with-netpbm=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# nothing useful yet
rm $RPM_BUILD_ROOT%{_libdir}/libPgm2asc.a
rm $RPM_BUILD_ROOT%{_includedir}/gocr.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CREDITS HISTORY README REMARK.txt REVIEW TODO
%doc doc/{examples.txt,gocr.html,unicode.txt}
%attr(755,root,root) %{_bindir}/gocr
%{_mandir}/man1/gocr.1*

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gocr.tcl
%{_desktopdir}/gocr.desktop
%{_pixmapsdir}/gocr.png
