Name:		vgabios
Version:	0.6b
Release:	3.4%{?dist}
Summary:	LGPL implementation of a vga video bios

Group:		Applications/Emulators		
License:	LGPLv2
URL:		http://www.nongnu.org/vgabios/
Source0:	http://savannah.gnu.org/download/%{name}/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch: x86_64 noarch

Provides: vgabios-qxl

BuildRequires:	dev86
BuildArch: noarch
Patch1:		%{name}-provide-high-res.patch
# For bz#569473 - spice: Need vgabios for qxl device
Patch2: vgabios-use-VBE-LFB-address-from-PCI-base-address-if-present.patch
# For bz#569473 - spice: Need vgabios for qxl device
Patch3: vgabios-qxl-vgabios.patch

%description
vgabios is an LPGL implementation of a bios for a video card.
It is tied to plex86/bochs, althoug it will likely work on other
emulators. It is not intended for use in real cards.


%prep 
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build 
make clean
make biossums %{?_smp_mflags}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vgabios
install -m 0644 VGABIOS-lgpl-*.bin $RPM_BUILD_ROOT%{_datadir}/vgabios 


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/vgabios/
%doc README COPYING
%{_datadir}/vgabios/VGABIOS-lgpl-latest.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.cirrus.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.cirrus.debug.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.qxl.bin
%{_datadir}/vgabios/VGABIOS-lgpl-latest.qxl.debug.bin


%changelog
* Thu Mar 18 2010 Eduardo Habkost <ehabkost@redhat.com> - vgabios-0.6b-3.4.el6
- Add VGABIOS-lgpl-latest.qxl.bin to file list
- Add Provides: vgabios-qxl to allow other packages to require vgabios.qxl
- Related: bz#569473
  (spice: Need vgabios for qxl device)

* Thu Mar 18 2010 Eduardo Habkost <ehabkost@redhat.com> - vgabios-0.6b-3.3.el6
- vgabios-use-VBE-LFB-address-from-PCI-base-address-if-present.patch [bz#569473]
- vgabios-qxl-vgabios.patch [bz#569473]
- Resolves: bz#569473
  (spice: Need vgabios for qxl device)

* Wed Jan 13 2010 Eduardo Habkost <ehabkost@redhat.com> - vgabios-0.6b-3.2.el6
- Build only on x86_64
- Resolves: bz#554862
  (vgabios should not be shipped on i686/ppc64/s390x, only on x86_64)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.6b-3.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Glauber Costa <glommer@redhat.com> - 0.6b-2
- properly add the patch

* Fri Jun 19 2009 Glauber Costa <glommer@redhat.com> - 0.6b-1
- applied vgabios-provide-high-res.patch, that should fix #499060
- Changed versioning naming, since the "b" in 0.6b does not stand for beta.

* Mon Mar 02 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.5.b
- fixed naming to comply with guidelines.

* Tue Feb 17 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.4beta
- removed leftovers and fixed rpmlint errors.

* Mon Feb 16 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.3beta
- using dev86 to build directly on all arches, made package noarch.
  No more binaries \o/

* Fri Feb 13 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.2beta
- Addressing BZ 485418: added doc section, clean build root before
  we proceed, own vgabios directory
* Fri Feb 13 2009 Glauber Costa <glommer@redhat.com> - 0.6-0.1beta
- Created initial package
