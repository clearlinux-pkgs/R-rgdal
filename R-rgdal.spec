#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-rgdal
Version  : 1.6.6
Release  : 46
URL      : https://cran.r-project.org/src/contrib/rgdal_1.6-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rgdal_1.6-6.tar.gz
Summary  : Bindings for the 'Geospatial' Data Abstraction Library
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0+ MIT
Requires: R-rgdal-lib = %{version}-%{release}
Requires: R-rgdal-license = %{version}-%{release}
Requires: R-sp
BuildRequires : R-sp
BuildRequires : buildreq-R
BuildRequires : gdal-dev
BuildRequires : proj-dev
BuildRequires : sqlite-autoconf-dev

%description
Summary of rgdal installation and drivers
The CRAN rgdal source package will work with the installed GDAL,
with all its drivers, where the availability of drivers is the user's
responsibility. This applies where the user installs
GDAL from source. If the user on Windows, OSX or Linux installs a GDAL
binary, she will get the drivers in that binary (and its dependencies),
for example KyngChaos GDAL frameworks for OSX.

%package lib
Summary: lib components for the R-rgdal package.
Group: Libraries
Requires: R-rgdal-license = %{version}-%{release}

%description lib
lib components for the R-rgdal package.


%package license
Summary: license components for the R-rgdal package.
Group: Default

%description license
license components for the R-rgdal package.


%prep
%setup -q -n rgdal

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681922765

%install
export SOURCE_DATE_EPOCH=1681922765
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-rgdal
cp %{_builddir}/rgdal/LICENSE.note %{buildroot}/usr/share/package-licenses/R-rgdal/f74e642de545485c0383e3fa333530a67c891f8f || :
cp %{_builddir}/rgdal/inst/LICENSE.TXT %{buildroot}/usr/share/package-licenses/R-rgdal/1a1ee79fb4ea4003f473c60e0b596fcbbb49b4d7 || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rgdal/ChangeLog
/usr/lib64/R/library/rgdal/DESCRIPTION
/usr/lib64/R/library/rgdal/INDEX
/usr/lib64/R/library/rgdal/LICENSE.TXT
/usr/lib64/R/library/rgdal/Meta/Rd.rds
/usr/lib64/R/library/rgdal/Meta/data.rds
/usr/lib64/R/library/rgdal/Meta/features.rds
/usr/lib64/R/library/rgdal/Meta/hsearch.rds
/usr/lib64/R/library/rgdal/Meta/links.rds
/usr/lib64/R/library/rgdal/Meta/nsInfo.rds
/usr/lib64/R/library/rgdal/Meta/package.rds
/usr/lib64/R/library/rgdal/Meta/vignette.rds
/usr/lib64/R/library/rgdal/NAMESPACE
/usr/lib64/R/library/rgdal/NEWS.md
/usr/lib64/R/library/rgdal/OSGeo4W_test
/usr/lib64/R/library/rgdal/R/rgdal
/usr/lib64/R/library/rgdal/R/rgdal.rdb
/usr/lib64/R/library/rgdal/R/rgdal.rdx
/usr/lib64/R/library/rgdal/README
/usr/lib64/R/library/rgdal/README.windows
/usr/lib64/R/library/rgdal/SVN_VERSION
/usr/lib64/R/library/rgdal/data/GridsDatums.rda
/usr/lib64/R/library/rgdal/data/nor2k.rda
/usr/lib64/R/library/rgdal/doc/CRS_projections_transformations.R
/usr/lib64/R/library/rgdal/doc/CRS_projections_transformations.Rmd
/usr/lib64/R/library/rgdal/doc/CRS_projections_transformations.html
/usr/lib64/R/library/rgdal/doc/OGR_shape_encoding.R
/usr/lib64/R/library/rgdal/doc/OGR_shape_encoding.Rnw
/usr/lib64/R/library/rgdal/doc/OGR_shape_encoding.pdf
/usr/lib64/R/library/rgdal/doc/PROJ6_GDAL3.R
/usr/lib64/R/library/rgdal/doc/PROJ6_GDAL3.Rmd
/usr/lib64/R/library/rgdal/doc/PROJ6_GDAL3.html
/usr/lib64/R/library/rgdal/doc/index.html
/usr/lib64/R/library/rgdal/etc/obj_with_comments.RData
/usr/lib64/R/library/rgdal/etc/obj_without_comments.RData
/usr/lib64/R/library/rgdal/etc/point.cpg
/usr/lib64/R/library/rgdal/etc/point.dbf
/usr/lib64/R/library/rgdal/etc/point.prj
/usr/lib64/R/library/rgdal/etc/point.shp
/usr/lib64/R/library/rgdal/etc/point.shx
/usr/lib64/R/library/rgdal/etc/point_LinuxGDAL.RData
/usr/lib64/R/library/rgdal/etc/point_WinCRAN.RData
/usr/lib64/R/library/rgdal/etc/test_dfs.RData
/usr/lib64/R/library/rgdal/help/AnIndex
/usr/lib64/R/library/rgdal/help/aliases.rds
/usr/lib64/R/library/rgdal/help/paths.rds
/usr/lib64/R/library/rgdal/help/rgdal.rdb
/usr/lib64/R/library/rgdal/help/rgdal.rdx
/usr/lib64/R/library/rgdal/html/00Index.html
/usr/lib64/R/library/rgdal/html/R.css
/usr/lib64/R/library/rgdal/include/projects.h
/usr/lib64/R/library/rgdal/m4/ax_cxx_compile_stdcxx.m4
/usr/lib64/R/library/rgdal/misc/GGHB.IG_CRS.rda
/usr/lib64/R/library/rgdal/misc/meuse.png
/usr/lib64/R/library/rgdal/misc/snow.png
/usr/lib64/R/library/rgdal/pictures/MR5905167_372.nc
/usr/lib64/R/library/rgdal/pictures/Rlogo.jpg
/usr/lib64/R/library/rgdal/pictures/SOURCES
/usr/lib64/R/library/rgdal/pictures/SP27GTIF.TIF
/usr/lib64/R/library/rgdal/pictures/big_int_arc_file.asc
/usr/lib64/R/library/rgdal/pictures/cea.tif
/usr/lib64/R/library/rgdal/pictures/erdas_spnad83.tif
/usr/lib64/R/library/rgdal/pictures/logo.jpg
/usr/lib64/R/library/rgdal/pictures/scaleoffset.dat
/usr/lib64/R/library/rgdal/pictures/scaleoffset.vrt
/usr/lib64/R/library/rgdal/pictures/test_envi_class.envi
/usr/lib64/R/library/rgdal/pictures/test_envi_class.hdr
/usr/lib64/R/library/rgdal/tests/test_enforce_xy.R
/usr/lib64/R/library/rgdal/tests/test_enforce_xy.Rout.save
/usr/lib64/R/library/rgdal/tests/test_proj.R
/usr/lib64/R/library/rgdal/tests/test_proj.Rout.save
/usr/lib64/R/library/rgdal/tests/tests.R
/usr/lib64/R/library/rgdal/tests/tests.Rout.save
/usr/lib64/R/library/rgdal/tests/tripup.R
/usr/lib64/R/library/rgdal/tests/tripup.Rout.save
/usr/lib64/R/library/rgdal/vectors/PacoursIKA2.DAT
/usr/lib64/R/library/rgdal/vectors/PacoursIKA2.ID
/usr/lib64/R/library/rgdal/vectors/PacoursIKA2.MAP
/usr/lib64/R/library/rgdal/vectors/PacoursIKA2.TAB
/usr/lib64/R/library/rgdal/vectors/SOURCES
/usr/lib64/R/library/rgdal/vectors/Up.dat
/usr/lib64/R/library/rgdal/vectors/Up.id
/usr/lib64/R/library/rgdal/vectors/Up.ind
/usr/lib64/R/library/rgdal/vectors/Up.map
/usr/lib64/R/library/rgdal/vectors/Up.tab
/usr/lib64/R/library/rgdal/vectors/airports.gml
/usr/lib64/R/library/rgdal/vectors/b_pump.gpkg
/usr/lib64/R/library/rgdal/vectors/cities.dbf
/usr/lib64/R/library/rgdal/vectors/cities.htm
/usr/lib64/R/library/rgdal/vectors/cities.prj
/usr/lib64/R/library/rgdal/vectors/cities.sbn
/usr/lib64/R/library/rgdal/vectors/cities.sbx
/usr/lib64/R/library/rgdal/vectors/cities.shp
/usr/lib64/R/library/rgdal/vectors/cities.shx
/usr/lib64/R/library/rgdal/vectors/kiritimati_primary_roads.dbf
/usr/lib64/R/library/rgdal/vectors/kiritimati_primary_roads.prj
/usr/lib64/R/library/rgdal/vectors/kiritimati_primary_roads.sbn
/usr/lib64/R/library/rgdal/vectors/kiritimati_primary_roads.sbx
/usr/lib64/R/library/rgdal/vectors/kiritimati_primary_roads.shp
/usr/lib64/R/library/rgdal/vectors/kiritimati_primary_roads.shx
/usr/lib64/R/library/rgdal/vectors/ps_cant_31.MID
/usr/lib64/R/library/rgdal/vectors/ps_cant_31.MIF
/usr/lib64/R/library/rgdal/vectors/scot_BNG.dbf
/usr/lib64/R/library/rgdal/vectors/scot_BNG.prj
/usr/lib64/R/library/rgdal/vectors/scot_BNG.shp
/usr/lib64/R/library/rgdal/vectors/scot_BNG.shx
/usr/lib64/R/library/rgdal/vectors/test64.csv
/usr/lib64/R/library/rgdal/vectors/test64.csvt
/usr/lib64/R/library/rgdal/vectors/test64.vrt
/usr/lib64/R/library/rgdal/vectors/test_trk2.gpx
/usr/lib64/R/library/rgdal/vectors/trin_inca_pl03.dbf
/usr/lib64/R/library/rgdal/vectors/trin_inca_pl03.shp
/usr/lib64/R/library/rgdal/vectors/trin_inca_pl03.shx

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rgdal/libs/rgdal.so
/usr/lib64/R/library/rgdal/libs/rgdal.so.avx2
/usr/lib64/R/library/rgdal/libs/rgdal.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-rgdal/1a1ee79fb4ea4003f473c60e0b596fcbbb49b4d7
/usr/share/package-licenses/R-rgdal/f74e642de545485c0383e3fa333530a67c891f8f
