# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)
# code starts here






# code ends here


# --------------
# code starts here


#code ends here

banks = bank.drop(columns="Loan_ID")
null = banks.isnull().sum()
print(null)
print('-----------------------')
bank_mode = banks.mode()
print(bank_mode)
values = {'Gender':'Male', 
'Married':'Yes',
 'Dependents':0, 
 'Education':"Graduate", 
 'Self_Employed':'No',  
 'ApplicantIncome':2500,
 'CoapplicantIncome':0.0,
 'LoanAmount':120.0,
 'Loan_Amount_Term':360.0,
 'Credit_History':1.0,'Property_Area':'Semiurban', 'Loan_Status':'Y'}

print(bank_mode)
print('-----------------------')
banks = banks.fillna(value=values)
print(banks.isnull().sum())


# --------------
# Code starts here
import numpy as np
avg_loan_amount = banks.pivot_table(index=['Gender','Married','Self_Employed'], values='LoanAmount',aggfunc=np.mean)


print(avg_loan_amount)



# --------------
# code starts here
import numpy as np
loan_approved_se = banks[(banks['Self_Employed']=="Yes") & (banks['Loan_Status']=='Y')]['Gender']



loan_approved_nse = banks[(banks['Self_Employed']=="No") & (banks['Loan_Status']=='Y')]['Gender']

print(loan_approved_se.size)


percentage_se = ((loan_approved_se.size)*100/614)
percentage_nse = ((loan_approved_nse.size)*100/614)
print(percentage_nse)
# code ends here


# --------------
# code starts here

#loan_term = banks['Loan_Amount_Term'].apply(lambda x : x / 12)
loan_term = banks.Loan_Amount_Term.apply(lambda x : x / 12)
big_loan_term = len(loan_term[loan_term >= 25])




# code ends here


# --------------
# code ends here

loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()




# code ends here


