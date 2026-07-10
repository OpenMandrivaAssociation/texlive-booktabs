%global tl_name booktabs
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.61803398
Release:	%{tl_revision}.1
Summary:	Publication quality tables in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/booktabs
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/booktabs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enhances the quality of tables in LaTeX, providing extra
commands as well as behind-the-scenes optimisation. Guidelines are given
as to what constitutes a good table in this context. From version 1.61,
the package offers longtable compatibility.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/booktabs
%dir %{_datadir}/texmf-dist/source/latex/booktabs
%dir %{_datadir}/texmf-dist/tex/latex/booktabs
%doc %{_datadir}/texmf-dist/doc/latex/booktabs/README
%doc %{_datadir}/texmf-dist/doc/latex/booktabs/booktabs.pdf
%doc %{_datadir}/texmf-dist/source/latex/booktabs/booktabs.dtx
%doc %{_datadir}/texmf-dist/source/latex/booktabs/booktabs.ins
%{_datadir}/texmf-dist/tex/latex/booktabs/booktabs.sty
