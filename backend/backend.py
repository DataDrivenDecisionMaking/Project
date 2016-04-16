import sqlite3

conn = sqlite3.connect('/Users/manishsingh/SEM4/downloads/sqlite-autoconf-3120100/team1DB.db')

print conn

print "Opened database successfully"



query_cust_pref_service = "select * from preference_services"
query_cust_pref_service = query_cust_pref_service  + "where customer_id = (select max(customer_id) from preference_services)"

cursor_cust_pref_service = conn.execute(query_cust_pref_service)

prepareString = ""

// Pending : Check if you want to compare with NULL or Zero in the if condition

for row in cursor_cust_pref_service:
	if row[1] != NULL
		prepareString += "service_allergy > 0 " 
	if row[2] != NULL
		prepareString += "OR service_abortion > 0 "
	if row[3] != NULL
		prepareString += "OR Service_Acupuncture > 0 "
	if row[4] != NULL
		prepareString += "OR Service_BabyCare > 0 "
	if row[5] != NULL
		prepareString += "OR Service_Cancer > 0 "
	if row[6] != NULL
		prepareString += "OR Service_Cardiac > 0 "
	if row[7] != NULL
		prepareString += "OR Service_Chiropractic_Care > 0 "
	if row[8] != NULL
		prepareString += "OR Service_Cosmetic_Surgery > 0 "
	if row[9] != NULL
		prepareString += "OR Service_Dental > 0 "
	if row[10] != NULL
		prepareString += "OR Service_Diabetes > 0 "
	if row[11] != NULL
		prepareString += "OR Service_EyeCare > 0 "
	if row[12] != NULL
		prepareString += "OR Service_Habilitation > 0 "
	if row[13] != NULL
		prepareString += "OR Service_Immunization > 0 "
	if row[14] != NULL
		prepareString += "OR Service_Infertility > 0 "
	if row[15] != NULL
		prepareString += "OR Service_Mammogram > 0 "
	if row[16] != NULL
		prepareString += "OR Service_MentalHealth > 0 "
	if row[17] != NULL
		prepareString += "OR Service_Nursing > 0 "
	if row[18] != NULL
		prepareString += "OR Service_PostNatal > 0 "
	if row[19] != NULL
		prepareString += "OR Service_PreNatal > 0 "
	if row[20] != NULL
		prepareString += "OR Service_Rehabilitation > 0 "
	if row[21] != NULL
		prepareString += "OR Service_Surgery > 0 "
	if row[22] != NULL
		prepareString += "OR Service_Urgent_Care > 0 "
	if row[23] != NULL
		prepareString += "OR Service_Weight_Loss > 0 "
	if row[24] != NULL
		prepareString += "OR Service_X_Ray > 0 "


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

cursor = conn.execute(query)

for row in cursor:
	print "Name:=", row[0]

print "Operation done successfully";

conn.close()

