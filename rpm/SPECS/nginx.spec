Name: nginx
Version: 1.9.12
Release: 1
Summary: nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server.

License: @@PACKAGE_LICENSE@@
URL: http://nginx.org
Packager: Jess Portnoy <jess@packman.io>


Source0: %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: pcre-devel zlib-devel 
Requires: nss-softokn-freebl, openssl-libs, pcre, zlib

%description
nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP/UDP proxy server.


%prep
%setup -q

%build
./configure --prefix=/usr/nginx
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

for F in AUTHORS ChangeLog COPYING NEWS INSTALL README*;do
        if [ -r $F ];then
                cp $F ${RPM_BUILD_ROOT}%_defaultdocdir/%{name}/
        fi
done


%clean
rm -rf %{buildroot}

%pre

%post

%preun

%postun


%files
%defattr(-,root,root,-)
%config(noreplace) /usr/nginx/conf/fastcgi.conf
%config(noreplace) /usr/nginx/conf/fastcgi.conf.default
%config(noreplace) /usr/nginx/conf/fastcgi_params
%config(noreplace) /usr/nginx/conf/fastcgi_params.default
%config(noreplace) /usr/nginx/conf/koi-utf
%config(noreplace) /usr/nginx/conf/koi-win
%config(noreplace) /usr/nginx/conf/mime.types
%config(noreplace) /usr/nginx/conf/mime.types.default
%config(noreplace) /usr/nginx/conf/nginx.conf
%config(noreplace) /usr/nginx/conf/nginx.conf.default
%config(noreplace) /usr/nginx/conf/scgi_params
%config(noreplace) /usr/nginx/conf/scgi_params.default
%config(noreplace) /usr/nginx/conf/uwsgi_params
%config(noreplace) /usr/nginx/conf/uwsgi_params.default
%config(noreplace) /usr/nginx/conf/win-utf
/usr/nginx/html/50x.html
/usr/nginx/html/index.html
/usr/nginx/sbin/nginx
%doc
%_defaultlicensedir/%{name}
%doc %_defaultdocdir/%{name}/*



%changelog

