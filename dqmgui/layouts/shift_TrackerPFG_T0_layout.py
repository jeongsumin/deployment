def shiftTkPFGlayout(i, p, *rows): i["00 Shift/TrackerOfflinePromptFeedback/" + p] = DQMItem(layout=rows)

shiftTkPFGlayout(dqmitems, "01 - PixelPhase1 # of Cluster Trend",
   [{ 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_per_LumiBlock_PXBarrel",
      'description': "Mean cluster value per lumisection in barrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Phase1_MechanicalView/num_clusters_per_LumiBlock_PXForward",
      'description': "Mean cluster value per lumisection in endcap",
      'draw': { 'withref': "no" }}]
   )

shiftTkPFGlayout(dqmitems, "02 -SiStrip  # of Cluster Trend",
  [{ 'path': "SiStrip/MechanicalView/TIB/TotalNumberOfClusterProfile__TIB",
     'description': "Total # of Clusters in TIB with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TOB/TotalNumberOfClusterProfile__TOB",
     'description': "Total # of Clusters in TOB with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/TotalNumberOfClusterProfile__TID__MINUS",
     'description': "Total # of Clusters in TID -ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/TotalNumberOfClusterProfile__TID__PLUS",
     'description': "Total # of Clusters in TID +ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}],
  [{  'path':"SiStrip/MechanicalView/TEC/MINUS/TotalNumberOfClusterProfile__TEC__MINUS",
     'description': "Total # of Clusters in TEC -ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "},
   {  'path':"SiStrip/MechanicalView/TEC/PLUS/TotalNumberOfClusterProfile__TEC__PLUS",
     'description': "Total # of Clusters in TEC +ve side with event time in Seconds  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/SiStripOfflineDQMInstructions>SiStripOfflineDQMInstructions</a> "}])

shiftTkPFGlayout(dqmitems, "03 SiStrip OnTrackCluster",
  [{ 'path': "SiStrip/MechanicalView/TIB/Summary_ClusterStoNCorr_OnTrack__TIB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TIB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "no" }},
   { 'path': "SiStrip/MechanicalView/TOB/Summary_ClusterStoNCorr_OnTrack__TOB",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TOB  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "no" } }],
  [{ 'path': "SiStrip/MechanicalView/TID/MINUS/Summary_ClusterStoNCorr_OnTrack__TID__MINUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "no" }},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/Summary_ClusterStoNCorr_OnTrack__TID__PLUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TID +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "no" } }],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/Summary_ClusterStoNCorr_OnTrack__TEC__MINUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC -ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "no" }},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/Summary_ClusterStoNCorr_OnTrack__TEC__PLUS",
     'description': "Signal-to-Noise (corrected for the angle) for On-Track clusters in TEC +ve side - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineSiStrip>DQMShiftOfflineSiStrip</a> ", 'draw': { 'withref': "no" } }])

shiftTkPFGlayout(dqmitems, "04 - Cluster on track charge per Inner Ladders",
  [{ 'path': "PixelPhase1/Tracks/PXBarrel/chargeInner_PXLayer_1",
     'description': "corrected cluster charge (on track) in inner ladders in PXLayer 1",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Tracks/PXBarrel/chargeInner_PXLayer_2",
     'description': "corrected cluster charge (on track) in inner ladders in PXLayer 2",
     'draw': {'withref' : "no"}}],
  [{ 'path': "PixelPhase1/Tracks/PXBarrel/chargeInner_PXLayer_3",
     'description': "corrected cluster charge (on track) in inner ladders in PXLayer 3",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Tracks/PXBarrel/chargeInner_PXLayer_4",
     'description': "corrected cluster charge (on track) in inner ladders in PXLayer 4",
     'draw': {'withref' : "no"}}]
  )

shiftTkPFGlayout(dqmitems, "05 - Cluster on track charge per Outer Ladders",
  [{ 'path': "PixelPhase1/Tracks/PXBarrel/chargeOuter_PXLayer_1",
     'description': "corrected cluster charge (on track) in outer ladders in PXLayer 1",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Tracks/PXBarrel/chargeOuter_PXLayer_2",
     'description': "corrected cluster charge (on track) in outer ladders in PXLayer 2",
     'draw': {'withref' : "no"}}],
  [{ 'path': "PixelPhase1/Tracks/PXBarrel/chargeOuter_PXLayer_3",
     'description': "corrected cluster charge (on track) in outer ladders in PXLayer 3",
     'draw': {'withref' : "no"}},
   { 'path': "PixelPhase1/Tracks/PXBarrel/chargeOuter_PXLayer_4",
     'description': "corrected cluster charge (on track) in outer ladders in PXLayer 4",
     'draw': {'withref' : "no"}}]
  ) 

shiftTkPFGlayout(dqmitems, "06 - PixelPhase1 DeadROC Summary",
  [{ 'path': "PixelPhase1/deadRocTotal",
     'description': "Number of total dead ROCs summary",
     'draw': { 'withref': "no" }}]
  )

shiftTkPFGlayout(dqmitems, "07 - PixelPhase1 Cluster Position: Z vs Phi barrel summary",
	[{'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_1",
  	  'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_2",
      'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
    [{'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_3",
      'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXBarrel/clusterposition_zphi_PXLayer_4",
      'description': "Cluster position in global coordinates by Global Phi (y-axis) vs Global Z (x-axis) in layer 4 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
   )

shiftTkPFGlayout(dqmitems, "08 - PixelPhase1 Cluster Position: X vs Y endcap summary",
    [{'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+1",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+2",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_+3",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk +3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
    [{'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-1",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -1 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-2",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -2 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }},
     {'path': "PixelPhase1/Phase1_MechanicalView/PXForward/clusterposition_xy_PXDisk_-3",
      'description': "Cluster position in global coordinates by Global Y (y-axis) vs Global X (x-axis) in disk -3 of pixel endcap",
      'draw': { 'withref': "no", 'drawopts': "COLZ" }}],
	)

shiftTkPFGlayout(dqmitems, "09 - PixelPhase1 Residuals",
   [{ 'path': "PixelPhase1/Tracks/residual_x_PXBarrel",
      'description': "Track residuals x in PXBarrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/residual_x_PXForward",
      'description': "Track residuals x in PXForward",
      'draw': { 'withref': "no" }}],
   [{ 'path': "PixelPhase1/Tracks/residual_y_PXBarrel",
      'description': "Track residuals y in PXBarrel",
      'draw': { 'withref': "no" }},
    { 'path': "PixelPhase1/Tracks/residual_y_PXForward",
      'description': "Track residuals y in PXForward",
      'draw': { 'withref': "no" }}]
   )

shiftTkPFGlayout(dqmitems, "10a - TIB Residuals",
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_1/HitResiduals_TIB__Layer__1",
     'description': "Hit Residual in TIB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_2/HitResiduals_TIB__Layer__2",
     'description': "Hit Residual in TIB Layer #2"}],
  [{ 'path': "SiStrip/MechanicalView/TIB/layer_3/HitResiduals_TIB__Layer__3",
     'description': "Hit Residual in TIB Layer #3"},
   { 'path': "SiStrip/MechanicalView/TIB/layer_4/HitResiduals_TIB__Layer__4",
     'description': "Hit Residual in TIB Layer #4"}])
shiftTkPFGlayout(dqmitems, "10b - TOB Residuals",
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_1/HitResiduals_TOB__Layer__1",
     'description': "Hit Residual in TOB Layer #1"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_2/HitResiduals_TOB__Layer__2",
     'description': "Hit Residual in TOB Layer #2"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_3/HitResiduals_TOB__Layer__3",
     'description': "Hit Residual in TOB Layer #3"}],
  [{ 'path': "SiStrip/MechanicalView/TOB/layer_4/HitResiduals_TOB__Layer__4",
     'description': "Hit Residual in TOB Layer #4"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_5/HitResiduals_TOB__Layer__5",
     'description': "Hit Residual in TOB Layer #5"},
   { 'path': "SiStrip/MechanicalView/TOB/layer_6/HitResiduals_TOB__Layer__6",
     'description': "Hit Residual in TOB Layer #6"}])
shiftTkPFGlayout(dqmitems, "10c - TID+ Residuals",
  [{ 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_1/HitResiduals_TID__wheel__1",
     'description': "Hit Residuals in TID+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_2/HitResiduals_TID__wheel__2",
     'description': "Hit Residuals in TID+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/PLUS/wheel_3/HitResiduals_TID__wheel__3",
     'description': "Hit Residuals in TID+ Wheel #3 "}])
shiftTkPFGlayout(dqmitems, "10d - TID- Residuals",
 [{ 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_1/HitResiduals_TID__wheel__1",
     'description': "Hit Residuals in TID- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_2/HitResiduals_TID__wheel__2",
     'description': "Hit Residuals in TID- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TID/MINUS/wheel_3/HitResiduals_TID__wheel__3",
     'description': "Hit Residuals in TID- Wheel #3 "}])
shiftTkPFGlayout(dqmitems, "10e - TEC+ Residual",
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_1/HitResiduals_TEC__wheel__1",
     'description': "Hit Residual in TEC+ Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_2/HitResiduals_TEC__wheel__2",
     'description': "Hit Residual in TEC+ Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_3/HitResiduals_TEC__wheel__3",
     'description': "Hit Residual in TEC+ Wheel #3"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_4/HitResiduals_TEC__wheel__4",
     'description': "Hit Residual in TEC+ Wheel #4"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_5/HitResiduals_TEC__wheel__5",
  'description': "Hit Residual in TEC+ Wheel #5"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_6/HitResiduals_TEC__wheel__6",
     'description': "Hit Residual in TEC+ Wheel #6"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_7/HitResiduals_TEC__wheel__7",
     'description': "Hit Residual in TEC+ Wheel #7"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_8/HitResiduals_TEC__wheel__8",
     'description': "Hit Residual in TEC+ Wheel #8"},
   { 'path': "SiStrip/MechanicalView/TEC/PLUS/wheel_9/HitResiduals_TEC__wheel__9",
     'description': "Hit Residual in TEC+ Wheel #9"}])
shiftTkPFGlayout(dqmitems, "10f - TEC- Residual",
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_1/HitResiduals_TEC__wheel__1",
     'description': "Hit Residual in TEC- Wheel #1"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_2/HitResiduals_TEC__wheel__2",
     'description': "Hit Residual in TEC- Wheel #2"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_3/HitResiduals_TEC__wheel__3",
     'description': "Hit Residual in TEC- Wheel #3"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_4/HitResiduals_TEC__wheel__4",
   'description': "Hit Residual in TEC- Wheel #4"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_5/HitResiduals_TEC__wheel__5",
     'description': "Hit Residual in TEC- Wheel #5"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_6/HitResiduals_TEC__wheel__6",
     'description': "Hit Residual in TEC- Wheel #6"}],
  [{ 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_7/HitResiduals_TEC__wheel__7",
     'description': "Hit Residual in TEC- Wheel #7"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_8/HitResiduals_TEC__wheel__8",
     'description': "Hit Residual in TEC- Wheel #8"},
   { 'path': "SiStrip/MechanicalView/TEC/MINUS/wheel_9/HitResiduals_TEC__wheel__9",
     'description': "Hit Residual in TEC- Wheel #9"}])
shiftTkPFGlayout(dqmitems, "11a - Tracks (pp collisions)",
 [{ 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/NumberOfTracks_GenTk",
    'description': "Number of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/HitProperties/NumberOfRecHitsPerTrack_GenTk",
    'description': "Number of RecHits per Track - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPt_ImpactPoint_GenTk",
    'description': "Pt of Reconstructed Track - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }}],
 [{ 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/Chi2oNDF_GenTk",
    'description': "Chi Square per DoF -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackPhi_ImpactPoint_GenTk",
    'description': "Phi distribution of Reconstructed Tracks -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/TrackParameters/highPurityTracks/pt_1/GeneralProperties/TrackEta_ImpactPoint_GenTk",
    'description': " Eta distribution of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }}])
shiftTkPFGlayout(dqmitems, "11b - Tracks (Cosmic Tracking)",
 [{ 'path': "Tracking/TrackParameters/GeneralProperties/NumberOfTracks_CKFTk",
    'description': "Number of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/TrackParameters/HitProperties/NumberOfRecHitsPerTrack_CKFTk",
    'description': "Number of RecHits per Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackPt_CKFTk",
    'description': "Pt of Reconstructed Track  - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }}],
 [{ 'path': "Tracking/TrackParameters/GeneralProperties/Chi2oNDF_CKFTk",
    'description': "Chi Sqare per DoF  -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackPhi_CKFTk",
    'description': "Phi distribution of Reconstructed Tracks -  <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }},
  { 'path': "Tracking/TrackParameters/GeneralProperties/TrackEta_CKFTk",
    'description': " Eta distribution of Reconstructed Tracks - <a href=https://twiki.cern.ch/twiki/bin/view/CMS/DQMShiftOfflineTracking>DQMShiftOfflineTracking</a> ", 'draw': { 'withref': "no" }}])

