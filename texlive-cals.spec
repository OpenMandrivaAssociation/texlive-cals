%global tl_name cals
%global tl_revision 43003

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4.2
Release:	%{tl_revision}.1
Summary:	Multipage tables with wide range of features
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cals
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cals.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cals.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cals.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a set of macros to typeset multipage tables with
repeatable headers and footers, with cells spanned over rows and
columns. Decorations are supported: padding, background color, width of
separation rules. The code is compatible with multicol and bidi.

