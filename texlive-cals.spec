Name:		texlive-cals
Version:	2.4.2
Release:	3
Summary:	Multipage tables with wide range of features
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cals
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cals.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cals.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cals.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to typeset multipage tables with
repeatable headers and footers, and with cells spanned over
rows and columns. Decorations are supported: padding,
background color, width of separation rules. The package is
compatible with multicol and pdfsync.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cals
%doc %{_texmfdistdir}/doc/latex/cals
#- source
%doc %{_texmfdistdir}/source/latex/cals

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
