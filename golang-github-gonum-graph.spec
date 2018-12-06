# http://github.com/gonum/graph

%global goipath         github.com/gonum/graph
%global commit          bde6d0fbd9dec5a997e906611fe0364001364c41


%gometa -i

Name:           %{goname}
Version:        0.9
Release:        12%{?dist}
Summary:        Graph packages for the Go language
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

Patch0:         add-license.patch
Patch1:         Fix-formatting-errors.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/gonum/floats)
BuildRequires: golang(github.com/gonum/matrix/mat64)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%patch0 -p1
%patch1 -p1

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d path

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.9-11.gitbde6d0f
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0.9-10
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5
- https://fedoraproject.org/wiki/Changes/golang1.7

* Thu Jul 14 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.9-4
- Fix Exclusive arches for golang/openblas

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitbde6d0f
- First package for Fedora
  resolves: #1269935
