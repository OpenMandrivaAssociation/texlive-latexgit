%global tl_name latexgit
%global tl_revision 54811

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A LaTeX git wrapper
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latexgit
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexgit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexgit.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexgit.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides several macros to fetch git information and
typeset it. The macros defined by LaTeXgit can be helpful to
documentation authors and others to whom clear document versioning is
important.

