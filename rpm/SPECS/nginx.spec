Name: nginx
Version: 1.9.12
Release: 1
Summary: nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server.

License: @@PACKAGE_LICENSE@@
URL: http://nginx.org
Packager: Jess Portnoy <jess@packman.io>


Source0: %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires: @@BUILD_REQUIRES@@
Requires: glibc, nss-softokn-freebl, openssl-libs, pcre, zlib

%description
nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server.

### dev package section
%package devel
Group: Development/Libraries
Summary: Development files for nginx
#Requires: @@DEV_PACKAGE_REQUIRES@@ 

%description devel
Headers and additional dev files needed for building and developing on top of nginx
### end dev package section

%prep
%setup -q

%build
%configure
#./configure --prefix=/usr
#./configure  --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info
make %{?_smp_mflags}
#inspect the Makefile and see if there is a test target, if so then:
#make test


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%_defaultdocdir/%{name} ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
# place license and README files in the right place.
mkdir -p ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}
if [ -r LICENSE ];then
	cp LICENSE ${RPM_BUILD_ROOT}%_defaultlicensedir/%{name}/
fi
for R in README*;do
        cp README* ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
done
for F in AUTHORS ChangeLog COPYING NEWS ;do
        if [ -r $F ];then
                cp $F ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
        fi
done




%clean
#rm -rf %{buildroot}

%pre

%post

%preun

%postun


%files
%defattr(-,root,root,-)

%doc
%_defaultlicensedir/%{name}
%doc %_defaultdocdir/%{name}/*

%files devel
%defattr(-,root,root)


%changelog

