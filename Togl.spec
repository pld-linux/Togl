Summary:	Togl - Tk OpenGL Widget
Summary(pl):	Togl - Biblioteka widgetów dla Tk
Name:		Togl
Version:	1.6
Release:	3
License:	Open Source (see LICENSE file for details)
Group:		Libraries
Source0:	http://dl.sourceforge.net/togl/%{name}-%{version}.tar.gz
# Source0-md5:	1019f483ee1564c98310ff3ca9a75463
URL:		http://togl.sf.net/
BuildRequires:	OpenGL-devel
BuildRequires:	tk >= 8.3
BuildRequires:	tcl >= 8.3
Requires:	OpenGL
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__make} \
	CC="%{__cc}" \
	COPTS="-c %{rpmcflags} -fPIC -DPC_LINUX %{?debug:-DDEBUG} -DUSE_TCL_STUBS -DUSE_TK_STUBS -DUSE_LOCAL_TK_H" \
	SHLINK="%{__cc} -shared" \
	LIBDIRS="\$(TCL_LIB) -L/usr/X11R6/lib" \
	TCL_VER="8.3"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir}/Togl-%{version},%{_includedir},%{_examplesdir}/%{name}-%{version}}

install togl.so pkgIndex.tcl $RPM_BUILD_ROOT%{_libdir}/Togl-%{version}

for f in double gears index overlay texture ; do
	install ${f}.c ${f}.so ${f}.tcl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
done
# for texture
install ben.rgb tree2.rgba $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install togl.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE Togl.html
%dir %{_libdir}/Togl-%{version}
%attr(755,root,root) %{_libdir}/Togl-%{version}/togl.so
%{_libdir}/Togl-%{version}/*.tcl

%files devel
%defattr(644,root,root,755)
%attr(644,root,root) %{_includedir}/togl.h
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.so
%{_examplesdir}/%{name}-%{version}/*.c
%{_examplesdir}/%{name}-%{version}/*.tcl
%{_examplesdir}/%{name}-%{version}/*.rgb*
