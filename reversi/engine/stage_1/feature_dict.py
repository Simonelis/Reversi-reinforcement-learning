features_4d = [	[3, 10, 17, 24],		\
				[32, 41, 50, 59],		\
				[60, 53, 46, 39],	\
				[31, 22, 13, 4]	\
				]
	
features_5d = [	[4, 11, 18, 25, 32],		\
				[24, 33, 42, 51, 60],		\
				[59, 52, 45, 38, 31],	\
				[39, 30, 21, 12, 3]	\
					]
	
features_6d = [	[5, 12, 19, 26, 33, 40],		\
				[16, 25, 34, 43, 52, 61],		\
				[58, 51, 44, 37, 30, 23],	\
				[47, 38, 29, 20, 11, 2]	\
					]

features_7d = [	[8, 17, 26, 35, 44, 53, 62],		\
				[57, 50, 43, 36, 29, 22, 15],		\
				[55, 46, 37, 28, 19, 10, 1],	\
				[6, 13, 20, 27, 34, 41, 48]	\
					]

features_8d = [	[0, 9, 18, 27, 36, 45, 54, 63],		\
				[7, 14, 21, 28, 35, 42, 49, 56]	\
					]		
		
features_sc = [	[0, 9, 1, 8],     \
				[7, 14, 6, 15],     \
				[56, 49, 48, 57],     \
				[63, 54, 62, 55] \
				]				
				
features_c = [   [0, 9, 18, 8, 17, 16, 1, 10, 2], \
				[7, 14, 21, 6, 13, 5, 15, 22, 23],       \
				[56, 49, 42, 57, 50, 58, 48, 41, 40], 
				[63, 54, 45, 62, 53, 61, 55, 46, 47]
					]				
				
features_b1 =  [	[0, 8, 16, 24, 32, 40, 48, 56],		\
				[56, 57, 58, 59, 60, 61, 62, 63],\
				[63, 55, 47, 39, 31, 23, 15, 7],\
				[7, 6, 5, 4, 3, 2, 1, 0]	\
				]
				
features_b2 =  [	[1, 9, 17, 25, 33, 41, 49, 57],		\
				[48, 49, 50, 51, 52, 53, 54, 55],\
				[62, 54, 46, 38, 30, 22, 14, 6],\
				[15, 14, 13, 12, 11, 10, 9, 8]	\
				]				
				
features_b34 =  [	[2, 10, 18, 26, 34, 42, 50, 58],\
				[40, 41, 42, 43, 44, 45, 46, 47],\
				[61, 53, 45, 37, 29, 21, 13, 5],\
				[23, 22, 21, 20, 19, 18, 17, 16],
				[3, 11, 19, 27, 35, 43, 51, 59],
				[32, 33, 34, 35, 36, 37, 38, 39],
				[60, 52, 44, 36, 28, 20, 12, 4],
				[31, 30, 29, 28, 27, 26, 25, 24]\
				]	
				
features_group = [features_4d, features_5d, features_6d, features_7d,\
		features_8d, features_sc, features_c,  features_b1, features_b2, features_b34]
		
features_flat = features_4d + features_5d + features_6d + features_7d +\
				features_8d + features_sc + features_c + features_b1 + features_b2 +\
				features_b34
				
number_of_features = len(features_flat)

feature_indices = [ [] for i in range(64)]

def feature_index_function(i, feature):
	if i in feature:
		return 3 ** ( len(feature) - 1 - feature.index(i) )
	return []
	

for i in range(64):
	j = 0
	for feature in features_flat:
		to_append = feature_index_function(i, feature)
		if to_append != []:
			feature_indices[i].append([j,to_append])
		j += 1	
		
features_4d_dict = [[0 for i in range(10)] for j in range(3**len(features_4d[0]))]
features_5d_dict = [[0 for i in range(10)] for j in range(3**len(features_5d[0]))]
features_6d_dict = [[0 for i in range(10)] for j in range(3**len(features_6d[0]))]
features_7d_dict = [[0 for i in range(10)] for j in range(3**len(features_7d[0]))]
features_8d_dict = [[0 for i in range(10)] for j in range(3**len(features_8d[0]))]
features_sc_dict = [[0 for i in range(10)] for j in range(3**len(features_sc[0]))]
features_c_dict = [[0 for i in range(10)] for j in range(3**len(features_c[0]))]
features_b1_dict = [[0 for i in range(10)] for j in range(3**len(features_b1[0]))]
features_b2_dict = [[0 for i in range(10)] for j in range(3**len(features_b2[0]))]
features_b34_dict = [[0 for i in range(10)] for j in range(3**len(features_b34[0]))]

dicts_group = [features_4d_dict, features_5d_dict, features_6d_dict, \
				features_7d_dict, features_8d_dict,\
				features_sc_dict, features_c_dict, features_b1_dict,\
				features_b2_dict, features_b34_dict]

dicts_flat = []

for a_group, a_dict in zip(features_group, dicts_group):
	for feature in a_group:
		dicts_flat.append(a_dict)