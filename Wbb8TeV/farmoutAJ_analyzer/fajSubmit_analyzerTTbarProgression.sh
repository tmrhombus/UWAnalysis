#voms-proxy-init --voms cms --valid 100:00

START=$(date +%s);
echo "Started at `date`"

mkdir -p ${uwa}/Wbb8TeV/SampleInfo/${version}/Lists
mkdir -p ./Submit_${version}

lumi_mu="19780" # Interlochen
lumi_ele="19671" # Interlochen

shifts[0]="noshift"

## choose sample
for samplename in \
 "WJets" \
 "W1Jet" \
 "W2Jet" \
 "W3Jet" \
 "Drell" \
 "DrellLM" \
 "T_s" \
 "T_t" \
 "T_tW" \
 "Tbar_s" \
 "Tbar_t" \
 "Tbar_tW" \
 "W4Jet" \
 "Wbb4F" \
 "TTbar_full" \
 "TTbar_semi" \
 "WW" \
 "WZ" \
 "ZZ" 

do
 echo "${samplename}"
 # count the total number of events, put in a file if it's not there
 initevents="${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/initialEvents.txt"
 touch ${initevents} 
 if ! grep -F "${samplename}" ${initevents} 
 then 
  echo "Need to count events.. making list"
  # make a list of all the sample filenames
  find ${hdfs}/${version}/roots/ntuple/${version}_${samplename}*PATMC*/*root > \
   ${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/list_${samplename}.txt #
  
  cp "${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/list_${samplename}.txt" \
     "${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/xrd_list_${samplename}.txt" #
  # format as xrootd
  mylist="${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/xrd_list_${samplename}.txt"
  sed -i 's@/hdfs/@root://cmsxrootd.hep.wisc.edu//@g' $mylist #

  echo "                    .. counting events"
  python ./eventCounter.py ${samplename} \
     ${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/list_${samplename}.txt \
     ${initevents}
  echo "                    .. counted events"
 else
  mylist="${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/xrd_list_${samplename}.txt"
 fi
 # or just set it by hand(:
 #mylist="${uwa}/Wbb8TeV/SampleInfo/${version}/xrd_list_${samplename}.txt" 

 # set up sample specific stuff from initialEvents.txt
 nrE="$(grep -P ${samplename} ${initevents} | sed -n -e "s@${samplename} Events: @@p")"
 xc="$(grep -P  ${samplename} ${initevents} | sed -n -e "s@${samplename} XC: @@p")"
 isMC="kTRUE"
 ## or put it in by hand
 #nrE="1234567" 
 #xc="12.34"
 if [[ ${samplename} == W*Jet* ]]
  then isW="kTRUE"
  else isW="kFALSE"
 fi

 echo $nrE
 echo $xc

 # for shift in list above
 for theshift in "${shifts[@]}"
 do
  treename="muEleEventTree/eventTree"
  if [[ ${theshift} == SFs ]]     ; then treename="muEleEventTree/eventTree"             ; fi
  if [[ ${theshift} == JESUp ]]   ; then treename="muEleEventTreeJetUp/eventTree"        ; fi
  if [[ ${theshift} == JESDown ]] ; then treename="muEleEventTreeJetDown/eventTree"      ; fi
  if [[ ${theshift} == MESUp ]]   ; then treename="muEleEventTreeMuonUp/eventTree"       ; fi
  if [[ ${theshift} == MESDown ]] ; then treename="muEleEventTreeMuonDown/eventTree"     ; fi
  if [[ ${theshift} == EESUp ]]   ; then treename="muEleEventTreeElectronUp/eventTree"   ; fi
  if [[ ${theshift} == EESDown ]] ; then treename="muEleEventTreeElectronDown/eventTree" ; fi

  # make correct executable xx_callHistoFillerTTbarProgression()
  cp template_callHistoFillerTTbarProgression.cc    "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@PSANDSHIFT@${samplename}_${theshift}@g" "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@PSNAME@${samplename}@g"                 "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@LUMIMU@${lumi_mu}@g"                    "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@LUMIELE@${lumi_ele}@g"                  "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@NREVENTS@${nrE}@g"                      "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@CROSSSEC@${xc}@g"                       "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@ISMC@${isMC}@g"                         "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@ISW@${isW}@g"                           "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@SHIFT@${theshift}@g"                    "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"
  sed -i "s@TREENAME@${treename}@g"                 "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"

  farmoutAnalysisJobs \
   --infer-cmssw-path \
   --fwklite \
   --input-file-list=${mylist} \
   --input-files-per-job=30 \
   --use-hdfs \
   --extra-inputs=${uwa}/Wbb8TeV/farmoutAJ_analyzer/histoFillerTTbarProgression.C,${uwa}/Wbb8TeV/farmoutAJ_analyzer/histoFillerTTbarProgression.h \
   ${version}_${runname} \
   "./Submit_${version}/${samplename}_${theshift}_callHistoFillerTTbarProgression.cc"

 done # theshift in shifts[@]
done # samplename in mc_samples


for samplename in \
 "DataA_8TeVMu" \
 "DataA_8TeVEle" \
 "DataB_8TeVMu" \
 "DataC_8TeVMu" \
 "DataD_8TeVMu" \
 "DataB_8TeVEle" \
 "DataC_8TeVEle" \
 "DataD_8TeVEle" 

do
 echo "${samplename}"
 # make a list of all the sample filenames

 find ${hdfs}/${version}/roots/ntuple/${version}_${samplename}-*PATData/*root > \
  ${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/list_${samplename}.txt #

 cp "${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/list_${samplename}.txt" \
    "${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/xrd_list_${samplename}.txt" #
 # format as xrootd
 mylist="${uwa}/Wbb8TeV/SampleInfo/${version}/Lists/xrd_list_${samplename}.txt"
 sed -i 's@/hdfs/@root://cmsxrootd.hep.wisc.edu//@g' $mylist #

 # we shouldn't scale data..
 nrE="100"
 xc="-1"
 isMC="kFALSE"
 isW="kFALSE"
 theshift=""

 if [[ ${samplename} == *Mu ]];  then treename="muonEventTree/eventTree"     ; fi
 if [[ ${samplename} == *Ele ]]; then treename="electronEventTree/eventTree" ; fi

 # make correct executable xx_callHistoFillerTTbarProgression()
 cp template_callHistoFillerTTbarProgression.cc   "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@PSANDSHIFT@${samplename}${theshift}@g" "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@PSNAME@${samplename}@g"                "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@LUMIMU@${lumi_mu}@g"                   "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@LUMIELE@${lumi_ele}@g"                 "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@NREVENTS@${nrE}@g"                     "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@CROSSSEC@${xc}@g"                      "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@ISMC@${isMC}@g"                        "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@ISW@${isW}@g"                          "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@SHIFT@${theshift}@g"                   "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"
 sed -i "s@TREENAME@${treename}@g"                "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"

 farmoutAnalysisJobs \
  --infer-cmssw-path \
  --fwklite \
  --use-hdfs \
  --input-file-list=${mylist} \
  --input-files-per-job=100 \
  --extra-inputs=${uwa}/Wbb8TeV/farmoutAJ_analyzer/histoFillerTTbarProgression.C,${uwa}/Wbb8TeV/farmoutAJ_analyzer/histoFillerTTbarProgression.h \
  ${version}_${runname} \
  "./Submit_${version}/${samplename}${theshift}_callHistoFillerTTbarProgression.cc"

done # samplename in data_samples

END=$(date +%s);
echo "Finished at `date`"
echo $((END-START)) | awk '{print int($1/60)":"int($1%60)}'
