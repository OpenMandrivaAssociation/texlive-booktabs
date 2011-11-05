# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/booktabs
# catalog-date 2009-09-24 15:05:48 +0200
# catalog-license gpl
# catalog-version 1.61803
Name:		texlive-booktabs
Version:	1.61803
Release:	1
Summary:	Publication quality tables in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/booktabs
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package enhances the quality of tables in LaTeX, providing
extra commands as well as behind-the-scenes optimisation.
Guidelines are given as to what constitutes a good table in
this context. From version 1.61, the package offers longtable
compatibility.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/booktabs/booktabs.sty
%doc %{_texmfdistdir}/doc/latex/booktabs/COPYING
%doc %{_texmfdistdir}/doc/latex/booktabs/README
%doc %{_texmfdistdir}/doc/latex/booktabs/booktabs.pdf
#- source
%doc %{_texmfdistdir}/source/latex/booktabs/booktabs.dtx
%doc %{_texmfdistdir}/source/latex/booktabs/booktabs.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
