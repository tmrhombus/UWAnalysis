TString columns = "EVENT:muon_pt_vec[0]:muon_pt_vec[1]:muon_eta:muNuRelPFIsoDB_A_vec[0]:muNuRelPFIsoDB_A_vec[1]:nrMu:nrMuLoose:nrEle";
TString columns = "EVENT:J1_pt:J1_eta:J1_CSVbtag:J2_pt:J2_eta:J2_CSVbtag:J3_pt:J3_eta:J3_CSVbtag";
TString columns = "EVENT:met_pt:met_phi:mt";
TString columns = "EVENT";

TString cuts = "";
TString cuts = "J2_pt<25."
TString cuts = "nrMuLoose>1 || nrEle>0"
TString cuts = "J3_pt>25 && J3_eta<2.4"

TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");

((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("C0_tt_mets_xyp.txt"); 

New_Tree->Scan(columns,cuts,"colsize=10")


TString cuts = "EVENT==41521178||EVENT==63254071||EVENT==63255300||EVENT==80374380||EVENT==80813409||EVENT==3198161||EVENT==3199742||EVENT==14724791||EVENT==24563282||EVENT==24565028||EVENT==24859406||EVENT==45726591||EVENT==45728588||EVENT==5091545||EVENT==73077908||EVENT==22132746||EVENT==22133688||EVENT==75771092||EVENT==75774107||EVENT==75774982||EVENT==75776981||EVENT==68490946||EVENT==65011123||EVENT==65011275||EVENT==65013670||EVENT==65022104||EVENT==65029744||EVENT==65029887||EVENT==65030129||EVENT==79331971||EVENT==88785947||EVENT==88786132||EVENT==88786715 27052224||EVENT==39787764||EVENT==57665257||EVENT==63257822||EVENT==80377142||EVENT==3197045||EVENT==4022494||EVENT==14715456||EVENT==45727082||EVENT==45733758||EVENT==5524207||EVENT==5524665||EVENT==6470591||EVENT==66899251||EVENT==66902586||EVENT==75770417||EVENT==76949400||EVENT==57931020||EVENT==70330402||EVENT==79325495||EVENT==88783739"

TString cuts = "EVENT==80365326||EVENT==80366795||EVENT==39787764||EVENT==57665257||EVENT==57676827||EVENT==80374101||EVENT==80374650||EVENT==80374889||EVENT==80376971||EVENT==80377142||EVENT==55344777||EVENT==55345026||EVENT==68490649||EVENT==52245065||EVENT==52246474||EVENT==52247237||EVENT==65021845||EVENT==65472216||EVENT==65031536||EVENT==65032098||EVENT==3196962||EVENT==3197155||EVENT==3199170||EVENT==3199316||EVENT==4022494||EVENT==14715456||EVENT==14719218||EVENT==24571506||EVENT==24860056||EVENT==24860133||EVENT==45727082||EVENT==45733758||EVENT==45733963||EVENT==57931020||EVENT==57934418||EVENT==70327976||EVENT==75784274||EVENT==75785603||EVENT==79335538||EVENT==88786430||EVENT==5521111||EVENT==5524665||EVENT==6474431||EVENT==73100821||EVENT==22130095||EVENT==22131361||EVENT==66899251||EVENT==75770417||EVENT==75777038||EVENT==76947283||EVENT==76949400"

# full selection different events
TString cuts = "EVENT==66899251||EVENT==3196962||EVENT==65011275||EVENT==5521111||EVENT==76947283"

TString cuts = "EVENT==1459415581||EVENT==1544476685||EVENT==1544918117||EVENT==117476215||EVENT==316876129||EVENT==317857209||EVENT==330478746||EVENT==330122556||EVENT==870494964||EVENT==869830633||EVENT==883045870||EVENT==883765627||EVENT==894908990||EVENT==912999435||EVENT==918010472||EVENT==928133536||EVENT==1133024300||EVENT==1150481484||EVENT==1178066995||EVENT==17134671||EVENT==76047019||EVENT==240432088||EVENT==294072903||EVENT==299633529||EVENT==667908316||EVENT==715111529||EVENT==737393364||EVENT==679763698||EVENT==697415475||EVENT==697591867||EVENT==746885145||EVENT==754027815||EVENT==788337880||EVENT==787651422||EVENT==957632739||EVENT==958059520||EVENT==163499994||EVENT==1464048296||EVENT==1504105739||EVENT==1511089127||EVENT==1517021045||EVENT==1516968971||EVENT==1516655727||EVENT==1531860623||EVENT==1534716800||EVENT==470348019||EVENT==727134142||EVENT==764285710||EVENT==18483377||EVENT==18932523||EVENT==18559460||EVENT==30672952||EVENT==84410792||EVENT==84724947||EVENT==87081283||EVENT==89472274||EVENT==88849865||EVENT==309967503||EVENT==310403855||EVENT==317797391||EVENT==317331475||EVENT==317410234||EVENT==348693373||EVENT==348920087||EVENT==368139312||EVENT==368212410||EVENT==384535942||EVENT==384195755||EVENT==44482422||EVENT==45525889||EVENT==45219557||EVENT==38026642||EVENT==54011628||EVENT==54231314||EVENT==57323730||EVENT==1270934396||EVENT==1270953297||EVENT==1271841378||EVENT==1271637525||EVENT==1282080079||EVENT==1453570047||EVENT==74048878||EVENT==789237982||EVENT==845170550||EVENT==845217507||EVENT==153083418||EVENT==201197705||EVENT==59854101||EVENT==66495100||EVENT==66785134||EVENT==66276963||EVENT==72468593||EVENT==75010659||EVENT==75635839||EVENT==178170134||EVENT==686085210||EVENT==686249196||EVENT==143046532||EVENT==143739388||EVENT==456876600||EVENT==177475787||EVENT==237697559||EVENT==237403208||EVENT==237703654||EVENT==1975948269||EVENT==1976726972||EVENT==1992153745||EVENT==2023516852||EVENT==2023792981||EVENT==2030304253||EVENT==2030229731||EVENT==2031355489||EVENT==2126672565||EVENT==2179887396||EVENT==56089148||EVENT==56079990||EVENT==55804155||EVENT==76932034||EVENT==40676311||EVENT==57296797||EVENT==72871186||EVENT==72064571||EVENT==74309968||EVENT==181616816||EVENT==258089235||EVENT==258898079"

TString cuts = "EVENT==1327388313||EVENT==1334042825||EVENT==1333768920||EVENT==1335837921||EVENT==1335200987||EVENT==1335992691||EVENT==1335798783||EVENT==1364531669||EVENT==1400265984||EVENT==1407423096||EVENT==563569764||EVENT==563558413||EVENT==221383128||EVENT==264031141||EVENT==264338377||EVENT==295989745||EVENT==296111345||EVENT==296803459||EVENT==441973525||EVENT==441476486||EVENT==486670642||EVENT==490658986||EVENT==489755643||EVENT==130130314||EVENT==155514310||EVENT==156255229||EVENT==447583916||EVENT==475482898||EVENT==475543982||EVENT==516156643||EVENT==526648052||EVENT==641884100||EVENT==641375895||EVENT==644291662||EVENT==944508721||EVENT==934853139||EVENT==992761661||EVENT==993231778||EVENT==993919413||EVENT==993587254||EVENT==993767039||EVENT==1152636225||EVENT==1152531777||EVENT==876845742||EVENT==104378875||EVENT==1078707297||EVENT==1079236699||EVENT==1078595300||EVENT==1078760760||EVENT==1078925322||EVENT==1079647801||EVENT==1115352116||EVENT==1159737857||EVENT==978792891||EVENT==977939074||EVENT==979003417||EVENT==992015791||EVENT==1036171322||EVENT==1054654412||EVENT==1054391163||EVENT==1072693726||EVENT==1073954822||EVENT==1084416092||EVENT==1116626261||EVENT==1186917777||EVENT==1185343536||EVENT==1185507209||EVENT==1208636684||EVENT==1225837306||EVENT==1245159950||EVENT==1246021966||EVENT==1245709140||EVENT==1245705097||EVENT==1245557123||EVENT==1273676461||EVENT==1289711592||EVENT==193317369||EVENT==194276996||EVENT==217550319||EVENT==856725871||EVENT==928211440||EVENT==966641919||EVENT==967067407||EVENT==1086654858||EVENT==1104501287||EVENT==1104859515||EVENT==1104093240||EVENT==338785958||EVENT==384897037||EVENT==445371814||EVENT==88735202||EVENT==89286620||EVENT==89970897||EVENT==89055164||EVENT==363884304||EVENT==187147579||EVENT==187050519||EVENT==185695966||EVENT==185958133||EVENT==274591371||EVENT==282803652||EVENT==283488470||EVENT==360971510||EVENT==361184297||EVENT==361471049||EVENT==710184645||EVENT==877578824||EVENT==1182984877||EVENT==1182971335||EVENT==158396297||EVENT==158577330||EVENT==206139237||EVENT==204460938||EVENT==94656066||EVENT==13878748||EVENT==89098893||EVENT==735686663||EVENT==751297675||EVENT==751504617||EVENT==786530067||EVENT==797424453||EVENT==833430436||EVENT==833496060||EVENT==833937412||EVENT==862426925||EVENT==911762048||EVENT==911499383||EVENT==924939851||EVENT==1016731638||EVENT==1041706522||EVENT==1082156667||EVENT==1081991192"