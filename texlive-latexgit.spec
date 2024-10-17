Name:		texlive-latexgit
Version:	54811
Release:	2
Summary:	A LaTeX git wrapper
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latexgit
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexgit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexgit.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexgit.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides several macros to fetch git information
and typeset it. The macros defined by LaTeXgit can be helpful
to documentation authors and others to whom clear document
versioning is important.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/latexgit
%{_texmfdistdir}/tex/latex/latexgit
%doc %{_texmfdistdir}/doc/latex/latexgit

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
