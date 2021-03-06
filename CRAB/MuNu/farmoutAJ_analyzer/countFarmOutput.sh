echo
echo "${version} ${runname}"

shifts[0]="SFs"
shifts[1]="JESUp"
shifts[2]="JESDown"
shifts[3]="LESUp"
shifts[4]="LESDown"

tabs 15

hmcf=0
nmcf=0
hmcm=0
nmcm=0
hdf=0
ndf=0
hdm=0
ndm=0

for sample in \
 "WJets_p1" \
 "WJets_p2" \
 "W1Jet_p1" \
 "W1Jet_p2" \
 "W2Jet_p1" \
 "W2Jet_p2" \
 "W3Jet_p1" \
 "W3Jet_p2" \
 "W4Jet" \
 "Wbb4F" \
 "TTbar_full" \
 "TTbar_semi" \
 "Drell" \
 "T_s" \
 "T_t" \
 "T_tW" \
 "Tbar_s" \
 "Tbar_t" \
 "Tbar_tW" \
 "WW" \
 "WZ" \
 "ZZ"

do
 
 nf=$(ls -d /nfs_scratch/tperry/${version}_${sample}-MuEle-PATMC_V*/*/ | wc -l)
 n5=$((((${nf}+49)/50)))
 nm=$(ls -d /nfs_scratch/tperry/${version}_${sample}-mergeFilesJob/*/ | wc -l)

 hf=$(ls -1 /hdfs/store/user/tperry/${version}_${sample}-MuEle-PATMC_V*/*.root | wc -l)
 h5=$((((${hf}+49)/50)))
 hm=$(ls -1 /hdfs/store/user/tperry/${version}_${sample}-mergeFilesJob/*.root | wc -l)

 hmcf=$(($hmcf+$hf)) 
 nmcf=$(($nmcf+$nf)) 
 hmcm=$(($hmcm+$hm)) 
 nmcm=$(($nmcm+$nm)) 
 
 df=$((${nf}-${hf}))
 pf=`echo "${hf} ${nf}" | awk '{printf "%.5f \n", 100*$1/$2}'`

 echo -e "${sample}\t /nfs\t /hdfs"
 echo -e "  full\t ${nf}\t ${hf}\t  ${pf}% Complete"
 echo -e "  full/50\t ${n5}\t ${h5}\t ${df} failed jobs"
 echo -e "  merged\t ${nm}\t ${hm}"

 if [[ $sample == *"_p"* ]]
 then
  sample=${sample%_p1}
  sample=${sample%_p2}
 fi
 for myshift in "${shifts[@]}" 
  do
  na=$(ls -d /nfs_scratch/tperry/${version}_${runname}-${sample}_${myshift}_callHistoFiller/*/ | wc -l)
  ha=$(ls -1 /hdfs/store/user/tperry/${version}_${runname}-${sample}_${myshift}_callHistoFiller/*.root | wc -l) 
  echo -e "  ${myshift}\t ${na}\t ${ha} "
 done
 echo
done

pmcf=`echo "${hmcf} ${nmcf}" | awk '{printf "%.5f \n", 100*$1/$2}'`
echo
echo "Total MC"
echo "/nfs ${nmcf}   /hdfs ${hmcf}  ${pmcf}% Completed"
echo
echo


for sample in \
 "DataA_8TeVMu" \
 "DataB_8TeVMu" \
 "DataC_8TeVMu" \
 "DataD_8TeVMu" \
 "DataA_8TeVEle" \
 "DataB_8TeVEle" \
 "DataC_8TeVEle" \
 "DataD_8TeVEle" 

do
 
 # 
 nf=$(ls -d /nfs_scratch/tperry/${version}_${sample}-*-PATData/*/ | wc -l)
 n5=$((((${nf}+49)/50)))
 nm=$(ls -d /nfs_scratch/tperry/${version}_${sample}-mergeFilesJob/*/ | wc -l)

 hf=$(ls -1 /hdfs/store/user/tperry/${version}_${sample}-*-PATData/*.root | wc -l)
 h5=$((((${hf}+49)/50)))
 hm=$(ls -1 /hdfs/store/user/tperry/${version}_${sample}-mergeFilesJob/*.root | wc -l)

 hdf=$(($hdf+$hf)) 
 ndf=$(($ndf+$nf)) 
 hdm=$(($hdm+$hm)) 
 ndm=$(($ndm+$nm)) 

 df=$((${nf}-${hf}))
 pf=`echo "${hf} ${nf}" | awk '{printf "%.5f \n", 100*$1/$2}'`

 echo -e "${sample}\t /nfs\t /hdfs"
 echo -e "  full\t ${nf}\t ${hf}\t  ${pf}% Complete"
 echo -e "  full/50\t ${n5}\t ${h5}\t ${df} failed jobs"
 echo -e "  merged\t ${nm}\t ${hm}"

  na=$(ls -d /nfs_scratch/tperry/${version}_${runname}-${sample}_callHistoFiller/*/ | wc -l)
  ha=$(ls -1 /hdfs/store/user/tperry/${version}_${runname}-${sample}_callHistoFiller/*.root | wc -l) 
  echo -e "  \t ${na}\t ${ha} "
 echo
done

pdf=`echo "${hdf} ${ndf}" | awk '{printf "%.5f \n", 100*$1/$2}'`
echo
echo "Total Data"
echo "/nfs ${ndf}   /hdfs ${hdf}  ${pdf}% Completed"
echo
echo

