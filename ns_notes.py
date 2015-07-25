# 03HARDTHRESH, 03SCRUBBED, 15HARDTHRESH X GSREG, ANATICOR X YEO, ATOL

+ 4TT00116 remove from old
+ whole brain data is messed up
+ regenerate all zscores, and correlations due to strange subject memberships 
+ correlation matricies -- bottom rows are flipped 
+ generate new correlation martricies from nathans data


## THIS IS FOR THE 'HARD THREHOLD' ANALYSIS (reject > 1.5 mm FD at any point)
# 46: 15 HARDTHRESH
group1_strict = ['0023', '0024', '0025', '0028', '0030', '0031',
'0033', '0034', '0035', '0036', '0037', '0038', '0039',
'0040', '0041', '0042', '0043',
'060623_4TT00022', '060701_4TT00025', '060701_4TT00026',
'060712_4TT00031', '060712_4TT00032', '060719_4TT00035',
'060719_4TT00036', '060722_4TT00038', '060805_4TT00043',
'060805_4TT00044', '060809_4TT00046', '060819_4TT00055',
'060819_4TT00056', '060823_4TT00057', '060823_4TT00058',
'060902_4TT00063', '060902_4TT00064', '060906_4TT00065',
'060906_4TT00066', '060916_4TT00072', '060916_4TT00073',
'060919_4TT00074', '060919_4TT00075', '060920_4TT00076',
'061003_4TT00082', '061003_4TT00083', '061004_4TT00084',
'061004_4TT00085', '061014_4TT00091', '061017_4TT00092',
'061017_4TT00093', '061018_4TT00094', '061018_4TT00095',
'061028_4TT00102', '061028_4TT00103', '061107_4TT00109',
'061115_4TT00116']

# 62: 15 HARDTHRESH
group2_strict = ['0044', '0046', '0047', '0048', '0050', '0051',
'0052', '0055', '0058', '0061', '0062', '0065',
'0066', '0067', '0068', '0070', '0071', '0072',
'0073', '0074', '0075', '0077', '0078', '0079',
'0083', '0084',
'061107_4TT00108', '061115_4TT00117',
'061118_4TT00118', '061118_4TT00119', '061125_4TT00121',
'061129_4TT00122', '061129_4TT00123', '061206_4TT00129',
'061213_4TT00132', '061213_4TT00133', '061220_4TT00136',
'061220_4TT00137', '070103_4TT00140', '070103_4TT00141',
'070106_4TT00143', '070110_4TT00146', '070113_4TT00147',
'070113_4TT00148', '070117_4TT00151', '070117_4TT00152',
'070124_4TT00157', '070124_4TT00158', '070131_4TT00163',
'070203_4TT00165', '070207_4TT00169', '070214_4TT00174',
'070221_4TT00178', '070303_4TT00183', '070303_4TT00184',
'070307_4TT00187', '070317_4TT00194', '070317_4TT00195',
'070328_4TT00205', '070328_4TT00206', '070331_4TT00208']

# 54: 03HARDTHRESH, 03SCRUBBED
group1_fs03 = ['0023', '0024', '0025', '0028', '0030', '0031',
'0033', '0034', '0035', '0036', '0037', '0038', '0039',
'0040', '0041', '0042', '0043',
'060623_4TT00022', '060701_4TT00025', '060701_4TT00026',
'060712_4TT00031', '060712_4TT00032', '060719_4TT00035',
'060719_4TT00036', '060722_4TT00038', '060805_4TT00043',
'060805_4TT00044', '060809_4TT00046', '060819_4TT00055',
'060819_4TT00056', '060823_4TT00057', '060823_4TT00058',
'060902_4TT00063', '060902_4TT00064', '060906_4TT00065',
'060906_4TT00066', '060916_4TT00072', '060916_4TT00073',
'060919_4TT00074', '060919_4TT00075', '060920_4TT00076',
'061003_4TT00082', '061003_4TT00083', '061004_4TT00084',
'061004_4TT00085', '061014_4TT00091', '061017_4TT00092',
'061017_4TT00093', '061018_4TT00094', '061018_4TT00095',
'061028_4TT00102', '061028_4TT00103', '061107_4TT00109',
'061115_4TT00116']

# 34: 03HARDTHRESH, 03SCRUBBED
group2_fd03 = ['0044', '0047', '0048', '0050', '0051', '0052', '0062',
'0064', '0068', '0073', '0076', '0077', '0084',
'061118_4TT00118', '070307_4TT00187', '061129_4TT00123',
'070113_4TT00147', '070317_4TT00195', '070317_4TT00194',
'070103_4TT00141', '070131_4TT00163', '061107_4TT00108',
'061118_4TT00119', '061213_4TT00132', '070214_4TT00174',
'070124_4TT00158', '070303_4TT00183', '061129_4TT00122',
'061213_4TT00133', '061206_4TT00129', '070117_4TT00151',
'070328_4TT00205', '070207_4TT00169', '070124_4TT00157']



# ## THIS IS FOR HARD_THRESHOLD_ALT (SCRUB AT 1.5mm)
# # 54, no thresh
# group1_hardthresh_alt = ['0023', '0025', '0028', '0029', '0030', '0031',
# '0033', '0034', '0035', '0036', '0037', '0038',
# '0039', '0040', '0041', '0042', '0043',
# '060623_4TT00022', '060701_4TT00025', '060701_4TT00026',
# '060712_4TT00031', '060712_4TT00032', '060719_4TT00035',
# '060719_4TT00036', '060722_4TT00038', '060805_4TT00043',
# '060805_4TT00044', '060809_4TT00046', '060819_4TT00055',
# '060819_4TT00056', '060823_4TT00057', '060823_4TT00058',
# '060902_4TT00063', '060902_4TT00064', '060906_4TT00065',
# '060906_4TT00066', '060916_4TT00072', '060916_4TT00073',
# '060919_4TT00074', '060919_4TT00075', '060920_4TT00076',
# '061003_4TT00082', '061003_4TT00083', '061004_4TT00084',
# '061004_4TT00085', '061014_4TT00091', '061017_4TT00092',
# '061017_4TT00093', '061018_4TT00094', '061018_4TT00095',
# '061028_4TT00102', '061028_4TT00103', '061107_4TT00109',
# '061115_4TT00116']

# # 73, no thresh
# group2_hardthresh_alt = ['0044', '0046', '0047', '0048', '0050', '0051',
# '0052', '0054', '0055', '0058', '0060', '0061',
# '0062', '0064', '0065', '0066', '0067', '0068',
# '0070', '0071', '0072', '0073', '0074', '0075',
# '0076', '0077', '0078', '0079', '0081', '0082',
# '0083', '0084',
# '061107_4TT00108', '061115_4TT00117', '061118_4TT00118',
# '061118_4TT00119', '061125_4TT00121', '061129_4TT00122',
# '061129_4TT00123', '061206_4TT00129', '061213_4TT00132',
# '061213_4TT00133', '061220_4TT00136', '061220_4TT00137',
# '070103_4TT00140', '070103_4TT00141', '070106_4TT00142',
# '070106_4TT00143', '070110_4TT00145', '070110_4TT00146',
# '070113_4TT00147', '070113_4TT00148', '070117_4TT00151',
# '070117_4TT00152', '070124_4TT00157', '070124_4TT00158',
# '070131_4TT00163', '070131_4TT00164', '070203_4TT00165',
# '070207_4TT00169', '070214_4TT00174', '070221_4TT00177',
# '070221_4TT00178', '070303_4TT00183', '070303_4TT00184',
# '070307_4TT00186', '070307_4TT00187', '070314_4TT00193',
# '070317_4TT00194', '070317_4TT00195', '070328_4TT00205',
# '070328_4TT00206', '070331_4TT00208']

