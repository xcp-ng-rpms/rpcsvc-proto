%global package_speccommit ee22c9c1825f3d34328aac5586028307a25e990c
%global usver 1.4
%global xsver 2
%global xsrel %{xsver}%{?xscount}%{?xshash}
#
# spec file for package rpcsvc-proto
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           rpcsvc-proto
Version:        1.4
Release: %{?xsrel}%{?dist}
Summary:        RPC protocol definitions
License:        BSD and LGPLv2+
Url:            https://github.com/thkukuk/rpcsvc-proto
Source0: rpcsvc-proto-1.4.tar.xz

Conflicts: glibc-headers < 2.26.9000-36
Conflicts: glibc-common < 2.26.9000-36

BuildRequires: make
BuildRequires:  gcc
BuildRequires: automake, autoconf

%description
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package devel
Summary:        RPC protocol definitions

%description devel
The rpcsvc-proto package includes several rpcsvc header files
and RPC protocol definitions from SunRPC sources (as shipped with
glibc).

%package -n rpcgen
Summary:        RPC protocol compiler
Provides:       rpcgen

%description -n rpcgen
rpcgen is a tool that generates C code to implement an RPC protocol.
The input to rpcgen is a language similar to C known as RPC Language
(Remote Procedure Call Language).

%prep
%autosetup -p 1

%build
%configure
%make_build

%install
%make_install

# rquota.x and rquota.h are provided by quota
rm -f $RPM_BUILD_ROOT%{_prefix}/include/rpcsvc/rquota.[hx]

%files devel
%license COPYING
%{_includedir}/rpcsvc/

%files -n rpcgen
%{_bindir}/rpcgen
%{_mandir}/man1/rpcgen.1*

%changelog
* Tue Jan 21 2025 XenServer Rebuild <rebuild@xenserver.com> - 1.4-2
- CP-53310: XenServer 9 rebuild

* Wed Jul 05 2023 Lin Liu <lin.liu@citrix.com> - 1.4-1
- First imported release

