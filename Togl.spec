Summary:	Togl - Tk OpenGL Widget
Summary(pl):	Togl - Biblioteka widgetów dla Tk
Name:		Togl
Version:	1.7
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/togl/%{name}-%{version}.tar.gz
# Source0-md5:	0e7da2559513b064dbb0934dc128b46d
URL:		http://togl.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	tcl >= 8.3
BuildRequires:	tk >= 8.3
BuildRequires:	xorg-lib-libXmu-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Togl is a Tk widget for OpenGL rendering.

%description -l pl
Togl jest widgetem Tk do renderowania OpenGL.

%package devel
Summary:	Togl devel
Summary(pl):	Togl - czê¶æ dla programistów
Group:		Development/Libraries

%description devel
Header files and examples for Togl.

%description devel -l pl
Pliki nag³ówkowe i przyk³ady do Togl.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

for f in double gears index overlay texture ; do
	install ${f}.c ${f}.tcl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
done

# for texture
install ben.rgb tree2.rgba $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.stubs TODO Togl.html
%dir %{_libdir}/Togl%{version}
%attr(755,root,root) %{_libdir}/Togl%{version}/libTogl%{version}.so
%{_libdir}/Togl%{version}/pkgIndex.tcl

%files devel
%defattr(644,root,root,755)
%{_includedir}/togl*.h
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.c
%{_examplesdir}/%{name}-%{version}/*.tcl
%{_examplesdir}/%{name}-%{version}/*.rgb*
