import sqlite3

conn = sqlite3.connect('/Users/manishsingh/SEM4/downloads/sqlite-autoconf-3120100/team1DB.db')

print conn

print "Opened database successfully"


query_cust_pref_service = "select * from preference_services"
query_cust_pref_service = query_cust_pref_service  + "where customer_id = (select max(customer_id) from preference_services)"

cursor_cust_pref_service = conn.execute(query_cust_pref_service)

prepareString = ""

cust_pref_dict = { 'service_allergy': 0,'service_abortion': 0,'Service_Acupuncture': 0,'Service_BabyCare': 0,'Service_Cancer': 0,
'Service_Cardiac': 0,'Service_Chiropractic_Care': 0,'Service_Cosmetic_Surgery': 0,'Service_Dental': 0,
'Service_Diabetes': 0,'Service_EyeCare': 0,'Service_Habilitation': 0,'Service_Immunization': 0,
'Service_Infertility': 0,'Service_Mammogram': 0,'Service_MentalHealth': 0,'Service_Nursing': 0,
'Service_PostNatal': 0,'Service_PreNatal': 0,'Service_Referral': 0,'Service_Rehabilitation': 0,'Service_Surgery': 0,
'Service_Urgent_Care': 0,'Service_Weight_Loss': 0,'Service_X_Ray': 0}

# Pending : Check if you want to compare with NULL or Zero in the if condition
# start from 1 because 0th column is customer id 
for row in cursor_cust_pref_service:
	if row[1] != NULL
		prepareString += "service_allergy > 0 " 
		cust_pref_dict['service_allergy'] = row[1]

	if row[2] != NULL
		prepareString += "OR service_abortion > 0 "
		cust_pref_dict['service_abortion'] = row[2]

	if row[3] != NULL
		prepareString += "OR Service_Acupuncture > 0 "
		cust_pref_dict['Service_Acupuncture'] = row[3]

	if row[4] != NULL
		prepareString += "OR Service_BabyCare > 0 "
		cust_pref_dict['Service_BabyCare'] = row[4]

	if row[5] != NULL
		prepareString += "OR Service_Cancer > 0 "
		cust_pref_dict['Service_Cancer'] = row[5]

	if row[6] != NULL
		prepareString += "OR Service_Cardiac > 0 "
		cust_pref_dict['Service_Cardiac'] = row[6]

	if row[7] != NULL
		prepareString += "OR Service_Chiropractic_Care > 0 "
		cust_pref_dict['Service_Chiropractic_Care'] = row[7]

	if row[8] != NULL
		prepareString += "OR Service_Cosmetic_Surgery > 0 "
		cust_pref_dict['Service_Cosmetic_Surgery'] = row[8]

	if row[9] != NULL
		prepareString += "OR Service_Dental > 0 "
		cust_pref_dict['Service_Dental'] = row[9]

	if row[10] != NULL
		prepareString += "OR Service_Diabetes > 0 "
		cust_pref_dict['Service_Diabetes'] = row[10]

	if row[11] != NULL
		prepareString += "OR Service_EyeCare > 0 "
		cust_pref_dict['Service_EyeCare'] = row[11]

	if row[12] != NULL
		prepareString += "OR Service_Habilitation > 0 "
		cust_pref_dict['Service_Habilitation'] = row[12]

	if row[13] != NULL
		prepareString += "OR Service_Immunization > 0 "
		cust_pref_dict['Service_Immunization'] = row[13]

	if row[14] != NULL
		prepareString += "OR Service_Infertility > 0 "
		cust_pref_dict['Service_Infertility'] = row[14]

	if row[15] != NULL
		prepareString += "OR Service_Mammogram > 0 "
		cust_pref_dict['Service_Mammogram'] = row[15]

	if row[16] != NULL
		prepareString += "OR Service_MentalHealth > 0 "
		cust_pref_dict['Service_MentalHealth'] = row[16]

	if row[17] != NULL
		prepareString += "OR Service_Nursing > 0 "
		cust_pref_dict['Service_Nursing'] = row[17]

	if row[18] != NULL
		prepareString += "OR Service_PostNatal > 0 "
		cust_pref_dict['Service_PostNatal'] = row[18]

	if row[19] != NULL
		prepareString += "OR Service_PreNatal > 0 "
		cust_pref_dict['Service_PreNatal'] = row[19]

	if row[20] != NULL
		prepareString += "OR Service_Referral > 0 "
		cust_pref_dict['Service_Referral'] = row[20]
	
	if row[21] != NULL
		prepareString += "OR Service_Rehabilitation > 0 "
		cust_pref_dict['Service_Rehabilitation'] = row[21]

	if row[22] != NULL
		prepareString += "OR Service_Surgery > 0 "
		cust_pref_dict['Service_Surgery'] = row[22]

	if row[23] != NULL
		prepareString += "OR Service_Urgent_Care > 0 "
		cust_pref_dict['Service_Urgent_Care'] = row[23]

	if row[24] != NULL
		prepareString += "OR Service_Weight_Loss > 0 "
		cust_pref_dict['Service_Weight_Loss'] = row[24]

	if row[25] != NULL
		prepareString += "OR Service_X_Ray > 0 "
		cust_pref_dict['Service_X_Ray'] = row[25]


prepareString = "(" + prepareString + ")"


#  Get number_of_children, age, married status

query_personal = "SELECT age, married, number_of_children from personal_details"
query_personal += " WHERE customer_id = (SELECT max(customer_id) from personal_details"

cursor_personal = conn.execute(query_personal)

# Expecting one record only
for row in cursor_personal:
	cust_age = row[0]
	cust_marriage_status = row[1]
	cust_num_of_children = row[2]



 # Main query
query = "select pd.age, pd.married, pd.number_of_children,"
query = query + "hd.plan_id, hd.plan_marketing_name, hd.CHILD_ONLY_OFFERING, hd.ADULT_DENTAL, "
query = query + "hd.CHILD_DENTAL, hd.PREMIUM_CHILD, hd.PREM_ADULT_IND_AGE_21,"
query = query + "hd.PREM_ADULT_IND_AGE_27, hd.PREM_ADULT_IND_AGE_30, hd.PREM_ADULT_IND_AGE_40,"
query = query + "hd.PREM_ADULT_IND_AGE_50, hd.PREM_ADULT_IND_AGE_60, hd.PREM_COUPLE_21, "
query = query + "hd.PREM_COUPLE_30, hd.PREM_COUPLE_40, hd.PREM_COUPLE_50, hd.PREM_COUPLE_60, "
query = query + "hd.COUPLE1_CHILD_AGE_21, hd.COUPLE1_CHILD_AGE_30, hd.COUPLE1_CHILD_AGE_40, "
query = query + "hd.COUPLE1_CHILD_AGE_50, hd.COUPLE2_CHILDREN_AGE_21, hd.COUPLE2_CHILDREN_AGE_30, "
query = query + "hd.COUPLE2_CHILDREN_AGE_40, hd.COUPLE2_CHILDREN_AGE_50, hd.COUPLE3_OR_MORE_CHILDREN_AGE_21, "


query = query + "hd.COUPLE3_OR_MORE_CHILDREN_AGE_30, hd.COUPLE3_OR_MORE_CHILDREN_AGE_40, "
query = query + "hd.COUPLE3_OR_MORE_CHILDREN_AGE_50, hd.IND1_CHILD_AGE_21, hd.IND1_CHILD_AGE_30,"
query = query + "hd.IND1_CHILD_AGE_40, hd.IND1_CHILD_AGE_50, hd.IND2_CHILD_AGE_21, hd.IND2_CHILD_AGE_30, "
query = query + "hd.IND2_CHILD_AGE_40, hd.IND2_CHILD_AGE_50, hd.IND3_OR_MORE_CHILDREN_AGE_21, "
query = query + "hd.IND3_OR_MORE_CHILDREN_AGE_30, hd.IND3_OR_MORE_CHILDREN_AGE_40, "
query = query + "hd.IND3_OR_MORE_CHILDREN_AGE_50, hd.MED_DED_IND_STD, hd.MED_DED_FAM_STD,"


query = query + "hps.Service_Allergy, hps.Service_Abortion, hps.Service_Acupuncture, hps.Service_BabyCare, "
query = query + "hps.Service_Cancer, hps.Service_Cardiac, hps.Service_Chiropractic_Care, hps.Service_Cosmetic_Surgery ,"
query = query + "hps.Service_Dental , hps.Service_Diabetes, hps.Service_EyeCare, hps.Service_Habilitation, hps.Service_Immunization,"
query = query + "hps.Service_Infertility, hps.Service_Mammogram, hps.Service_MentalHealth, hps.Service_Nursing,"
query = query + "hps.Service_PostNatal, hps.Service_PreNatal, hps.Service_Referral, hps.Service_Rehabilitation , hps.Service_Surgery, "
query = query + "hps.Service_Urgent_Care , hps.Service_Weight_Loss, hps.Service_X_Ray"


query = query + "from hidata_new hd, personal_details pd, health_plan_services hps"
query = query + "where hd.state_code = pd.state_code"
query = query + "and hd.county_name = pd.county_name"
query = query + "and hd.plan_marketing_name = hps.planName"
# query = query + "and (hps.service_allergy = 1 OR hps.service_abortion = 1 OR ...) // generated dynamically"
query = query + prepareString
query = query + "and pd.state_code = v_state_code  //coming from frontend"
query = query + "and pd.county_name = v_county_name  // coming from frontend"
query = query + "and pd.customer_id =  ( select max(customer_id) from personal_details );"

cursor_main = conn.execute(query)

for row in cursor_main:
	v_age = row[0]
	v_married = row[1]
	v_number_of_children = row[2]
	v_plan_id = row[3]
	v_plan_marketing_name = row[4]
	v_child_only_offering = row[5]
	v_adult_dental = row[6]
	v_child_dental = row[7]
	v_premium_child = row[8]
	v_PREM_ADULT_IND_AGE_21 = row[9]
	v_PREM_ADULT_IND_AGE_27 = row[10]
	v_PREM_ADULT_IND_AGE_30 = row[11]
	v_PREM_ADULT_IND_AGE_40 = row[12]
	v_PREM_ADULT_IND_AGE_50 = row[13]
	v_PREM_ADULT_IND_AGE_60 = row[14]
	v_PREM_COUPLE_21 = row[15]
	v_PREM_COUPLE_30 = row[16]
	v_PREM_COUPLE_40 = row[17]
	v_PREM_COUPLE_50 = row[18]
	v_PREM_COUPLE_60 = row[19]
	v_COUPLE1_CHILD_AGE_21 = row[20]
	v_COUPLE1_CHILD_AGE_30 = row[21]
	v_COUPLE1_CHILD_AGE_40 = row[22]
	v_COUPLE1_CHILD_AGE_50 = row[23]
	v_COUPLE2_CHILDREN_AGE_21 = row[24]
	v_COUPLE2_CHILDREN_AGE_30 = row[25]
	v_COUPLE2_CHILDREN_AGE_40 = row[26]
	v_COUPLE2_CHILDREN_AGE_50 = row[27]
	v_COUPLE3_OR_MORE_CHILDREN_AGE_21 = row[28]


	v_COUPLE3_OR_MORE_CHILDREN_AGE_30 = row[29]
	v_COUPLE3_OR_MORE_CHILDREN_AGE_40 = row[30]
	v_COUPLE3_OR_MORE_CHILDREN_AGE_50 = row[31]
	v_IND1_CHILD_AGE_21 = row[32]
	v_IND1_CHILD_AGE_30 = row[33]
	v_IND1_CHILD_AGE_40 = row[34]
	v_IND1_CHILD_AGE_50 = row[35]

	v_IND2_CHILD_AGE_21 = row[36]
	v_IND2_CHILD_AGE_30 = row[37]
	v_IND2_CHILD_AGE_40 = row[38]
	v_IND2_CHILD_AGE_50 = row[39]

	v_IND3_OR_MORE_CHILDREN_AGE_21 = row[40]
	v_IND3_OR_MORE_CHILDREN_AGE_30 = row[41]
	v_IND3_OR_MORE_CHILDREN_AGE_40 = row[42]
	v_IND3_OR_MORE_CHILDREN_AGE_50 = row[43]
	v_MED_DED_IND_STD = row[44]
	v_MED_DED_FAM_STD = row[45]

	v_Service_Allergy=row[46]*0.02
	v_Service_Abortion=row[47]*0.02
	v_Service_Acupuncture=row[48]*0.02
	v_Service_BabyCare=row[49]*0.02
	v_Service_Cancer=row[50]*0.02
	v_Service_Cardiac=row[51]*0.02
	v_Service_Chiropractic_Care=row[52]*0.02
	v_Service_Cosmetic_Surgery=row[53]*0.02
	v_Service_Dental=row[54]*0.02
	v_Service_Diabetes=row[55]*0.02
	v_Service_EyeCare=row[56]*0.02
	v_Service_Habilitation=row[57]*0.02
	v_Service_Immunization=row[58]*0.02
	v_Service_Infertility=row[59]*0.02
	v_Service_Mammogram=row[60]*0.02
	v_Service_MentalHealth=row[61]*0.02
	v_Service_Nursing=row[62]*0.02
	v_Service_PostNatal=row[63]*0.02
	v_Service_PreNatal=row[64]*0.02
	v_Service_Referral=row[65]*0.02
	v_Service_Rehabilitation=row[66]*0.02
	v_Service_Surgery=row[67]*0.02
	v_Service_Urgent_Care=row[68]*0.02
	v_Service_Weight_Loss=row[69]*0.02
	v_Service_X_Ray=row[70]*0.02


	if cust_pref_dict['service_allergy'] > 0 :
		v_Service_Allergy *= cust_pref_dict['service_allergy'] 

	if cust_pref_dict['service_abortion'] > 0 :
		v_Service_Abortion *= cust_pref_dict['service_abortion'] 

	if cust_pref_dict['Service_Acupuncture'] > 0 :
		v_Service_Acupuncture *= cust_pref_dict['Service_Acupuncture'] 
	

	if cust_pref_dict['Service_BabyCare'] > 0 :
		v_Service_BabyCare *= cust_pref_dict['Service_BabyCare']


	if cust_pref_dict['Service_Cancer'] > 0 :
		v_Service_Cancer *= cust_pref_dict['Service_Cancer']

	if cust_pref_dict['Service_Cardiac'] > 0 :
		v_Service_Cardiac *= cust_pref_dict['Service_Cardiac'] 

	if cust_pref_dict['Service_Chiropractic_Care'] > 0 :
		v_Service_Chiropractic_Care *= cust_pref_dict['Service_Chiropractic_Care'] 

	if cust_pref_dict['Service_Cosmetic_Surgery'] > 0 :
		v_Service_Cosmetic_Surgery *= cust_pref_dict['Service_Cosmetic_Surgery']

	if cust_pref_dict['Service_Dental'] > 0 :
		v_Service_Dental *= cust_pref_dict['Service_Dental']

	if cust_pref_dict['Service_Diabetes'] > 0 :
		v_Service_Diabetes *= cust_pref_dict['Service_Diabetes'] 

	if cust_pref_dict['Service_EyeCare'] > 0 :
		v_Service_EyeCare *= cust_pref_dict['Service_EyeCare'] 

	if cust_pref_dict['Service_Habilitation'] > 0 :
		v_Service_Habilitation *= cust_pref_dict['Service_Habilitation'] 

	if cust_pref_dict['Service_Immunization'] > 0 :
		v_Service_Immunization *= cust_pref_dict['Service_Immunization'] 

	if cust_pref_dict['Service_Infertility'] > 0 :
		v_Service_Infertility *= cust_pref_dict['Service_Infertility'] 

	if cust_pref_dict['Service_Mammogram'] > 0 :
		v_Service_Mammogram *= cust_pref_dict['Service_Mammogram']

	if cust_pref_dict['Service_MentalHealth'] > 0 :
		v_Service_MentalHealth *= cust_pref_dict['Service_MentalHealth'] 

	if cust_pref_dict['Service_Nursing'] > 0 :
		v_Service_Nursing *= cust_pref_dict['Service_Nursing'] 

	if cust_pref_dict['Service_PostNatal'] > 0 :
		v_Service_PostNatal *= cust_pref_dict['Service_PostNatal'] 

	if cust_pref_dict['Service_PreNatal'] > 0 :
		v_Service_PreNatal *= cust_pref_dict['Service_PreNatal'] 

	if cust_pref_dict['Service_Referral'] > 0 :
		v_Service_Referral *= cust_pref_dict['Service_Referral'] 

	if cust_pref_dict['Service_Rehabilitation'] > 0 :
		v_Service_Rehabilitation *= cust_pref_dict['Service_Rehabilitation'] 

	if cust_pref_dict['Service_Surgery'] > 0 :
		v_Service_Surgery *= cust_pref_dict['Service_Surgery'] 

	if cust_pref_dict['Service_Urgent_Care'] > 0 :
		v_Service_Urgent_Care *= cust_pref_dict['Service_Urgent_Care'] 


	if cust_pref_dict['Service_Weight_Loss'] > 0 :
		v_Service_Weight_Loss *= cust_pref_dict['Service_Weight_Loss']

	if cust_pref_dict['Service_X_Ray'] > 0 :
		v_Service_X_Ray *= cust_pref_dict['Service_X_Ray'] 


    v_service_sum_derived = v_Service_Allergy + v_Service_Abortion+ v_Service_Acupuncture + 
                            v_Service_BabyCare + v_Service_Cancer + v_Service_Cardiac + v_Service_Chiropractic_Care
                            + v_Service_Cosmetic_Surgery + v_Service_Dental + v_Service_Diabetes + v_Service_EyeCare
                            + v_Service_Habilitation + v_Service_Immunization + v_Service_Infertility + 
                            v_Service_Mammogram + v_Service_MentalHealth + v_Service_Nursing + v_Service_PostNatal 
                            + v_Service_PreNatal + v_Service_Referral + v_Service_Rehabilitation + v_Service_Surgery +
                             v_Service_Urgent_Care + v_Service_Weight_Loss + v_Service_X_Ray


	# Pending things
	# Write if conditions 
	# Write insert query to load a custom table

	v_cust_premium = 0 
	
	if cust_marriage_status == 'N' and cust_num_of_children == 0 :
		if cust_age <= 21 :
			v_cust_premium = v_PREM_ADULT_IND_AGE_21

		if cust_age > 21 and cust_age <= 27 :
			v_cust_premium = v_PREM_ADULT_IND_AGE_27

		if cust_age > 27 and cust_age <= 30 :
			v_cust_premium = v_PREM_ADULT_IND_AGE_30

		if cust_age > 30 and cust_age <= 40 :
			v_cust_premium = v_PREM_ADULT_IND_AGE_40

		if cust_age > 40 and cust_age <= 50 :
			v_cust_premium = v_PREM_ADULT_IND_AGE_50
		
		if cust_age > 50 :
			v_cust_premium = v_PREM_ADULT_IND_AGE_60
		
	if cust_marriage_status == 'Y' and cust_num_of_children == 0 :
		if cust_age <= 21 :
			v_cust_premium = v_PREM_COUPLE_21

		if cust_age > 21 and cust_age <= 30 :
			v_cust_premium = v_PREM_COUPLE_30

		if cust_age > 30 and cust_age <= 40 :
			v_cust_premium = v_PREM_COUPLE_40 

		if cust_age > 40 and cust_age <= 50 :
			v_cust_premium = v_PREM_COUPLE_50 

		if cust_age > 50 : 
			v_cust_premium = v_PREM_COUPLE_60 
	

	if cust_marriage_status == 'Y' and cust_num_of_children == 1 :
		if cust_age <= 21 :
			v_cust_premium = v_COUPLE1_CHILD_AGE_21

		if cust_age > 21 and cust_age <= 30 :
			v_cust_premium = v_COUPLE1_CHILD_AGE_30

		if cust_age > 30 and cust_age <= 40 :
			v_cust_premium = v_COUPLE1_CHILD_AGE_40

		if cust_age > 40 :
			v_cust_premium = v_COUPLE1_CHILD_AGE_50 

		
	if cust_marriage_status == 'Y' and cust_num_of_children == 2 :
		if cust_age <= 21 :
			v_cust_premium = v_COUPLE2_CHILDREN_AGE_21

		if cust_age > 21 and cust_age <= 30 :
			v_cust_premium = v_COUPLE2_CHILDREN_AGE_30

		if cust_age > 30 and cust_age <= 40 :
			v_cust_premium = v_COUPLE2_CHILDREN_AGE_40

		if cust_age > 40 :
			v_cust_premium = v_COUPLE2_CHILDREN_AGE_50



	if cust_marriage_status == 'Y' and cust_num_of_children >= 3 :
		if cust_age <= 21 :
			v_cust_premium = v_COUPLE3_OR_MORE_CHILDREN_AGE_21

		if cust_age > 21 and cust_age <= 30 :
			v_cust_premium = v_COUPLE3_OR_MORE_CHILDREN_AGE_30

		if cust_age > 30 and cust_age <= 40 :
			v_cust_premium = v_COUPLE3_OR_MORE_CHILDREN_AGE_40

		if cust_age > 40 :
			v_cust_premium = v_COUPLE3_OR_MORE_CHILDREN_AGE_50


	if cust_marriage_status == 'N' and cust_num_of_children == 1 :
		if cust_age <= 21 :
			v_cust_premium = v_IND1_CHILD_AGE_21 

		if cust_age > 21 and cust_age <= 30 :
			v_cust_premium = v_IND1_CHILD_AGE_30

		if cust_age > 30 and cust_age <= 40 :
			v_cust_premium = v_IND1_CHILD_AGE_40

		if cust_age > 40 :
			v_cust_premium = v_IND1_CHILD_AGE_50


	if cust_marriage_status == 'N' and cust_num_of_children == 2 :
		if cust_age <= 21 :
			v_cust_premium = v_IND2_CHILD_AGE_21 

		if cust_age > 21 and cust_age <= 30 :
			v_cust_premium = v_IND2_CHILD_AGE_30

		if cust_age > 30 and cust_age <= 40 :
			v_cust_premium = v_IND2_CHILD_AGE_40

		if cust_age > 40 :
			v_cust_premium = v_IND2_CHILD_AGE_50


	if cust_marriage_status == 'N' and cust_num_of_children >= 3 :
		if cust_age <= 21 :
			v_cust_premium = v_IND3_OR_MORE_CHILDREN_AGE_21 

		if cust_age > 21 and cust_age <= 30 :
			v_cust_premium = v_IND3_OR_MORE_CHILDREN_AGE_30

		if cust_age > 30 and cust_age <= 40 :
			v_cust_premium = v_IND3_OR_MORE_CHILDREN_AGE_40

		if cust_age > 40 :
			v_cust_premium = v_IND3_OR_MORE_CHILDREN_AGE_50




print "Operation done successfully";

conn.close()

