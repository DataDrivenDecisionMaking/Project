import sqlite3

conn = sqlite3.connect('/Users/manishsingh/SEM4/downloads/sqlite-autoconf-3120100/team1DB.db')
cursor_insert = conn.cursor()

print conn
print "Opened database successfully"


#GET THE CUSTOMER PREFERRED WEIGHTS FOR PREMIUM AND DEDUCTIBLE
query_cust_pref_cost = "SELECT premium_weight, deductible_weight FROM preferences_cost"
cursor_cust_pref_cost = conn.execute(query_cust_pref_cost)

for row in cursor_cust_pref_cost:
	v_pref_premium_weight = row[0]
	v_pref_deductible_weight = row[1]

query_cust_pref_service = "select service_allergy,service_abortion,Service_Acupuncture,Service_BabyCare,Service_Cancer"
query_cust_pref_service +=",Service_Cardiac,Service_Chiropractic_Care,Service_Cosmetic_Surgery,Service_Dental,"
query_cust_pref_service +="Service_Diabetes,Service_EyeCare,Service_Habilitation,Service_Immunization,Service_Infertility,"
query_cust_pref_service +="Service_Mammogram,Service_MentalHealth,Service_Nursing,Service_PostNatal,Service_PreNatal,"
query_cust_pref_service +="Service_Referral,Service_Rehabilitation,Service_Surgery,Service_Urgent_Care,Service_Weight_Loss,Service_X_Ray from preferences_services"
query_cust_pref_service += " where customer_id = (select max(customer_id) from preferences_services)"
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
	if row[0]: 
		prepareString += "service_allergy > 0 " 
		cust_pref_dict['service_allergy'] = row[0]

	if row[1]:
		prepareString += "OR service_abortion > 0 "
		cust_pref_dict['service_abortion'] = row[1]

	if row[2]:
		prepareString += "OR Service_Acupuncture > 0 "
		cust_pref_dict['Service_Acupuncture'] = row[2]

	if row[3]:
		prepareString += "OR Service_BabyCare > 0 "
		cust_pref_dict['Service_BabyCare'] = row[3]

	if row[4]:
		prepareString += "OR Service_Cancer > 0 "
		cust_pref_dict['Service_Cancer'] = row[4]

	if row[5]:
		prepareString += "OR Service_Cardiac > 0 "
		cust_pref_dict['Service_Cardiac'] = row[5]

	if row[6]:
		prepareString += "OR Service_Chiropractic_Care > 0 "
		cust_pref_dict['Service_Chiropractic_Care'] = row[6]

	if row[7]:
		prepareString += "OR Service_Cosmetic_Surgery > 0 "
		cust_pref_dict['Service_Cosmetic_Surgery'] = row[7]

	if row[8]:
		prepareString += "OR Service_Dental > 0 "
		cust_pref_dict['Service_Dental'] = row[8]

	if row[9]:
		prepareString += "OR Service_Diabetes > 0 "
		cust_pref_dict['Service_Diabetes'] = row[9]

	if row[10]:
		prepareString += "OR Service_EyeCare > 0 "
		cust_pref_dict['Service_EyeCare'] = row[10]

	if row[11]:
		prepareString += "OR Service_Habilitation > 0 "
		cust_pref_dict['Service_Habilitation'] = row[11]

	if row[12]:
		prepareString += "OR Service_Immunization > 0 "
		cust_pref_dict['Service_Immunization'] = row[12]

	if row[13]:
		prepareString += "OR Service_Infertility > 0 "
		cust_pref_dict['Service_Infertility'] = row[13]

	if row[14]:
		prepareString += "OR Service_Mammogram > 0 "
		cust_pref_dict['Service_Mammogram'] = row[14]

	if row[15]:
		prepareString += "OR Service_MentalHealth > 0 "
		cust_pref_dict['Service_MentalHealth'] = row[15]

	if row[16]:
		prepareString += "OR Service_Nursing > 0 "
		cust_pref_dict['Service_Nursing'] = row[16]

	if row[17]:
		prepareString += "OR Service_PostNatal > 0 "
		cust_pref_dict['Service_PostNatal'] = row[17]

	if row[18]:
		prepareString += "OR Service_PreNatal > 0 "
		cust_pref_dict['Service_PreNatal'] = row[18]

	if row[19]:
		prepareString += "OR Service_Referral > 0 "
		cust_pref_dict['Service_Referral'] = row[19]
	
	if row[20]:
		prepareString += "OR Service_Rehabilitation > 0 "
		cust_pref_dict['Service_Rehabilitation'] = row[20]

	if row[21]:
		prepareString += "OR Service_Surgery > 0 "
		cust_pref_dict['Service_Surgery'] = row[21]

	if row[22]:
		prepareString += "OR Service_Urgent_Care > 0 "
		cust_pref_dict['Service_Urgent_Care'] = row[22]

	if row[23]:
		prepareString += "OR Service_Weight_Loss > 0 "
		cust_pref_dict['Service_Weight_Loss'] = row[23]

	if row[24]:
		prepareString += "OR Service_X_Ray > 0 "
		cust_pref_dict['Service_X_Ray'] = row[24]


prepareString = "(" + prepareString + ")"


#  Get number_of_children, age, married status

query_personal = "SELECT customer_id, age, married, number_of_children from personal_details"
query_personal += " WHERE customer_id = (SELECT max(customer_id) from personal_details)"
cursor_personal = conn.execute(query_personal)

# Expecting one record only
for row in cursor_personal:
	cust_id = row[0]
	cust_age = row[1]
	cust_marriage_status = row[2]
	cust_num_of_children = row[3]

#To be populated / fetched from frontend

v_state_code='IN'
v_county_name='Scott'


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
query = query + " from hidata_new hd, personal_details pd, health_plan_services hps"
query = query + " where hd.state_code = pd.state_code"
query = query + " and hd.county_name = pd.county_name"
query = query + " and hd.plan_marketing_name = hps.planName and "
query = query + prepareString
query = query + " and pd.state_code = '"+v_state_code+"'"
query = query + " and pd.county_name = '"+v_county_name+"'"
query = query + " and pd.customer_id =  ( select max(customer_id) from personal_details )"

cursor_main = conn.execute(query)


# START OF THE MAIN CURSOR
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

	if cust_marriage_status = 'Y' or cust_num_of_children > 0 :
		v_cust_deductible = v_MED_DED_FAM_STD
	else
		v_cust_deductible = v_MED_DED_IND_STD 
	
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


    # Insert into weight_table now
    insert_query = "INSERT INTO weight_table values("+cust_id+","+v_plan_id+","+v_plan_marketing_name+","+v_cust_premium
    insert_query += ","+ v_cust_deductible + ",0,"+v_service_sum_derived

    cursor_insert.execute(insert_query)
    conn.commit()



#NOTE : BELOW CODE WORKS OUTSIDE THE MAIN CURSOR

# Get the max and min values of premium and deductible for normalization
query_weight_table_max = "SELECT max(v_premium), max(v_deductible) from weight_table"
cursor_weight_table_max = conn.execute(query_weight_table_max)

for row in cursor_weight_table_max:
	max_premium = row[0]
	max_deductible = row[1]

# Normalize premium and deductible in weight table
query_weight_table_normalize = "UPDATE weight_table set v_premium = v_premium/"+max_premium
query_weight_table_normalize += ", v_deductible = v_deductible/"+max_deductible+" where v_customer_id = "+cust_id

cursor_update_normalize = conn.cursor()
cursor_update_normalize.execute(query_weight_table_normalize)
conn.commit()


# Update premium and deductible in weight table
query_wt_tbl_prem_ded_upd = "UPDATE weight_table set v_premium = v_premium*"+v_pref_premium_weight
query_wt_tbl_prem_ded_upd += ", v_deductible = v_deductible*"+v_pref_deductible_weight+" where v_customer_id = "+cust_id

cursor_prem_ded_upd = conn.cursor()
cursor_prem_ded_upd.execute(query_wt_tbl_prem_ded_upd)
conn.commit()

#Update Final Score in weight table

query_wt_final_score_upd = "Update weight_table set v_final_score = v_service_score/(v_deductible + v_premium)"
query_wt_final_score_upd += " where v_customer_id ="+ cust_id;

cursor_final_score_upd = conn.cursor()
cursor_final_score_upd.execute(query_wt_final_score_upd)
conn.commit()


print "Operation done successfully";

conn.close()

