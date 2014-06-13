# revision 30784
# category Package
# catalog-ctan /macros/latex/contrib/cals
# catalog-date 2011-12-30 16:30:48 +0100
# catalog-license lppl1.3
# catalog-version 2.0.1
Name:		texlive-cals
Version:	2.0.1
Release:	8
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
%{_texmfdistdir}/tex/latex/cals/cals.sty
%doc %{_texmfdistdir}/doc/latex/cals/README
%doc %{_texmfdistdir}/doc/latex/cals/cals.pdf
%doc %{_texmfdistdir}/doc/latex/cals/examples/demo.pdf
%doc %{_texmfdistdir}/doc/latex/cals/examples/demo.tex
%doc %{_texmfdistdir}/doc/latex/cals/examples/table1.tex
%doc %{_texmfdistdir}/doc/latex/cals/examples/table2.tex
%doc %{_texmfdistdir}/doc/latex/cals/examples/table3.tex
%doc %{_texmfdistdir}/doc/latex/cals/examples/table4.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/README
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_10_create.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_10_create.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_20_colwidth.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_20_colwidth.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_30_decor.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_30_decor.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_40_width.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_40_width.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_50_hooks.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/cell/test_50_hooks.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/colsep/test_10_outone.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/colsep/test_10_outone.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/colsep/test_20_row.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/colsep/test_20_row.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_10_withwidth2.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_10_withwidth2.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_20_withcolor2.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_20_withcolor2.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_30_halfwidth.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_30_halfwidth.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_50_maxwidth.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_50_maxwidth.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_60_row.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_60_row.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_70_align.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/decoration/test_70_align.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/llt/test_10_cons_rot.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/llt/test_10_cons_rot.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/llt/test_20_snoc_decons.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/llt/test_20_snoc_decons.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/llt/test_30_all.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/llt/test_30_all.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_010_wrongbreak.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_010_wrongbreak.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_020_wrongnobreak.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_020_wrongnobreak.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_030_spanbreak.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_030_spanbreak.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_040_rowheight.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_040_rowheight.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_050_leftskip_rowspan.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_050_leftskip_rowspan.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_060_alignment.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_060_alignment.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_065_alignment.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/regression/test_065_alignment.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_10_waitrule.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_10_waitrule.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_15_waitover.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_15_waitover.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_20_pack.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_20_pack.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_30_jointwo.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_30_jointwo.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_35_joinone.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_35_joinone.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_40_construct.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/rowsep/test_40_construct.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_10_queue.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_10_queue.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_20_decor.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_20_decor.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_30_iftlrb.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_30_iftlrb.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_40_lr_queue.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_40_lr_queue.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_50_dimen.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_50_dimen.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_60_content.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_60_content.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_70_intercept.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_70_intercept.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_80_marker.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/span/test_80_marker.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/support/LatexTest.py
%doc %{_texmfdistdir}/doc/latex/cals/test/support/run_tests.py
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_10_ifbreak.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_10_ifbreak.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_20_dispatch.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_20_dispatch.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_30_issue_rowsep.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_30_issue_rowsep.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_40_issuerow.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_40_issuerow.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_50_row.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_50_row.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_60_whitespace.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_60_whitespace.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_70_lrskip.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/table/test_70_lrskip.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/template.txt
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_10_simple_2x2_with_parbreak.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_10_simple_2x2_with_parbreak.png
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_10_simple_2x2_with_parbreak.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_20_thead_tfoot.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_20_thead_tfoot.png
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_20_thead_tfoot.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_30_tbreak.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_30_tbreak.png
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_30_tbreak.tex
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_40_span.chk
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_40_span.png
%doc %{_texmfdistdir}/doc/latex/cals/test/visual_tables/test_40_span.tex
#- source
%doc %{_texmfdistdir}/source/latex/cals/cals.dtx
%doc %{_texmfdistdir}/source/latex/cals/cals.ins
%doc %{_texmfdistdir}/source/latex/cals/cell.dtx
%doc %{_texmfdistdir}/source/latex/cals/colsep.dtx
%doc %{_texmfdistdir}/source/latex/cals/decor.dtx
%doc %{_texmfdistdir}/source/latex/cals/lltokens.dtx
%doc %{_texmfdistdir}/source/latex/cals/rowsep.dtx
%doc %{_texmfdistdir}/source/latex/cals/span.dtx
%doc %{_texmfdistdir}/source/latex/cals/table.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
