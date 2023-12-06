Name:		texlive-hep-reference
Version:	67632
Release:	1
Summary:	Adjustments for publications in High Energy Physics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hep-reference
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-reference.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-reference.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hep-reference.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package makes some changes to the reference, citation and
footnote macros to improve the default behavior of LaTeX for
High Energy Physics publications.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hep-reference
%{_texmfdistdir}/tex/latex/hep-reference
%doc %{_texmfdistdir}/doc/latex/hep-reference

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
