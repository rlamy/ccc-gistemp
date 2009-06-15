#!/bin/sh
#
# Driver script for CCC reimplementation of GISTEMP in Python.  One
# day soon this file will become Python.
#
# Nick Barnes, Ravenbrook Limited, 2008-09-13.
#
# First draft: steps 0, 1, 3 are in Python; steps 2, 4, 5 still in
# FORTRAN.  Very rough cut.

fortran_compile=$FC
if [ "$FC" = "" ]
then echo "set an environment variable FC to the FORTRAN 90 compiler"
     echo "command, e.g. FC=gfortran42"
     exit
fi

# Compile all the FORTRAN
mkdir -p bin
${fortran_compile} code/STEP2/text_to_binary.f -o bin/text_to_binary.exe
${fortran_compile} code/STEP2/split_binary.f -o bin/split_binary.exe
${fortran_compile} code/STEP2/trim_binary.f -o bin/trim_binary.exe
${fortran_compile} code/STEP2/invnt.f -o bin/invnt.exe
${fortran_compile} code/STEP2/toANNanom.f -o bin/toANNanom.exe
${fortran_compile} code/STEP2/PApars.f code/STEP2/tr2.f code/STEP2/t2fit.f -o bin/PApars.exe
${fortran_compile} code/STEP2/flags.f -o  bin/flags.exe
${fortran_compile} code/STEP2/padjust.f -o bin/padjust.exe
${fortran_compile} code/STEP4_5/trimSBBX.f -o bin/trimSBBX.exe
${fortran_compile} code/STEP4_5/SBBXotoBX.f -o bin/SBBXotoBX.exe
${fortran_compile} code/STEP4_5/zonav.f -o bin/zonav.exe
${fortran_compile} code/STEP4_5/annzon.f -o bin/annzon.exe

# Go.
mkdir -p work log result
echo "====> STEP 0 ===="
python code/step0.py
sort < work/v2.mean_comb.unsorted > work/v2.mean_comb

echo "====> STEP 1 ===="
python code/step1.py

echo "====> STEP 2 ===="
echo "converting text to binary file"
bin/text_to_binary.exe `cat work/GHCN.last_year`

echo "breaking up Ts.bin into 6 zonal files"
bin/split_binary.exe

echo "trimming Ts.bin1-6"
bin/trim_binary.exe

for i in 1 2 3 4 5 6
  do  mv work/Ts.bin$i.trim work/Ts.GHCN.CL.$i
done

echo "preparations for urban adjustment"
bin/invnt.exe work/Ts.GHCN.CL > work/Ts.GHCN.CL.station.list

echo "Creating annual anomalies"
for n in 1 2 3 4 5 6
do ln work/Ts.GHCN.CL.$n work/fort.2
   if bin/toANNanom.exe
   then mv work/fort.3 work/ANN.dTs.GHCN.CL.$n
   else rm work/fort.[23] ; echo "no luck with Ts.GHCN.CL.$n" ; exit ; fi
   rm work/fort.2
done

for n in 1 2 3 4 5 6
do
   cp work/ANN.dTs.GHCN.CL.$n  work/fort.3$n
done

bin/PApars.exe 1000 20 > log/PApars.GHCN.CL.1000.20.log
bin/flags.exe >> log/PApars.GHCN.CL.1000.20.log
rm -f work/fort.78

echo 'CCdStationID  slope-l  slope-r knee    Yknee    slope     Ymid      RMS     RMSl 3-rur+urb ext.range flag' > work/PApars.list
cat work/fort.2 >> work/PApars.list
rm work/fort.2

mv work/fort.66   log/PApars.statn.log.GHCN.CL.1000.20
mv work/fort.77   log/PApars.statn.use.GHCN.CL.1000.20
mv work/fort.79   log/PApars.noadj.stations.list

ln work/PApars.list work/fort.1
for n in 1 2 3 4 5 6
do
   unit=`expr 11 + $n`
   ln work/Ts.GHCN.CL.$n work/fort.$unit
done
bin/padjust.exe > log/padjust.log
rm work/fort.1[2-7] work/fort.1

for n in 1 2 3 4 5 6
do
   unit=`expr 21 + $n`
   mv  work/fort.$unit work/Ts.GHCN.CL.PA.$n
done

bin/invnt.exe work/Ts.GHCN.CL.PA > work/Ts.GHCN.CL.PA.station.list

echo "====> STEP 3 ===="
python code/step3.py
mv work/SBBX1880.Ts.GHCN.CL.PA.1200 work/fort.10
GFORTRAN_CONVERT_UNIT="big_endian:10" bin/trimSBBX.exe
mv work/fort.11 work/SBBX1880.Ts.GHCN.CL.PA.1200

echo "====> skipping STEP 4; see code/STEP4_5/do_comb_step4.sh ===="

echo "====> STEP 5 ===="
# At least for now, our SBBX.HadR2 file is generated on a GISS AIX
# machine, so has big-endian binary data.  So we use
# GFORTRAN_CONVERT_UNIT to tell that to Fortran.

GFORTRAN_CONVERT_UNIT="big_endian:11" bin/SBBXotoBX.exe 100 0 > log/SBBXotoBX.log
bin/zonav.exe > log/zonav.Ts.ho2.GHCN.CL.PA.log
bin/annzon.exe  > log/annzon.Ts.ho2.GHCN.CL.PA.log

python code/step5res.py result/GLB.Ts.ho2.GHCN.CL.PA.txt > result/google-chart.url
echo "See result/google-chart.url"
