from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
import pandas as pd
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server
import pickle
import numpy as np
model = pickle.load(open('loanreg45copy.pkl', 'rb'))
app = Flask(__name__)


def predict():
      funded_amnt = input("Enter the amount to be funded (1000 to 35000)",type=FLOAT)
      annual_inc = input("Applicant annual income(7500 to 1000000)", type=FLOAT)
      installment = input("Monthly Installment (30.44 to 1388.44)", type=FLOAT)
      dti = input("Debt-to-Income(0 to 34)", type=FLOAT)
      emp_length =input("Employment  Years(1 to 10)", type=FLOAT)
      open_acc = input("No.of open account(1 to 38)", type=NUMBER)
      total_acc = input("Total No.of accounts(3 to 68)", type=NUMBER)
      term_in_months = select('Terms in months', ['36', '60'])
      if (term_in_months == '36'):
            term_in_months = 6448

    
      else:
            term_in_months = 2088
      
      home_ownership = select('Select home ownership type', ['MORTGAGE','RENT','OWN','OTHER'])
      if (home_ownership == 'MORTGAGE'):
            home_ownership = 4422
        
      elif (home_ownership == 'RENT'):
            home_ownership = 3407
          
      elif (home_ownership == 'OWN'):
            home_ownership = 706

      else:
            home_ownership = 1
      loan_status = select('Select home ownership type', ['current','fully_paid','chargedoff','latethirtyonetoonetwenty','ingraceperiod','latesixteentothirty','Default'])
      if (loan_status == 'current'):
            loan_status = 7283
        
      elif (loan_status == 'fully_paid'):
            loan_status = 854
          
      elif (loan_status == 'chargedoff'):
            loan_status = 194

      elif (loan_status == 'latethirtyonetoonetwenty'):
            loan_status = 134
          
      elif (loan_status == 'ingraceperiod'):
            loan_status = 40

      elif (loan_status == 'latesixteentothirty'):
            loan_status = 16
      else:
            loan_status = 15
         
    
   
      purpose = select('Purpose for loan', ['debt_consolidation','credit_card','other','home_improvement','major_purchase','small_business','car','wedding','moving','medical','house','vacation','renewable_energy'])
      if (purpose == 'debt_consolidation'):
            purpose = 5131
        
      elif (purpose == 'credit_card'):
            purpose = 1961
    
      elif (purpose== 'other'):
            purpose = 383
          
      elif (purpose== 'home_improvement'):
            purpose = 438
             
      elif (purpose == 'major_purchase'):
            purpose = 159
          
      elif (purpose == 'small_business'):
            purpose = 132
          
      elif (purpose== 'car'):
            purpose = 75
    
      elif (purpose == 'wedding'):
            purpose = 52
    
      elif (purpose == 'moving'):
            purpose = 43
          
      elif (purpose == 'medical'):
            purpose = 60
          
          
      elif (purpose == 'house'):
            purpose = 50
          
               
      elif (purpose == 'vacation'):
            purpose = 41
    

      else:
            purpose = 11

      lst = ['funded_amnt','installment','emp_length','annual_inc','dti','open_acc','total_acc','TermInMonths','home_ownership','loan_status','purpose']
      tdf = pd.DataFrame({'funded_amnt':[funded_amnt],'installment':[installment],'emp_length':[emp_length],'annual_inc':[annual_inc],'dti':[dti],'open_acc':[open_acc],'total_acc':[total_acc],'term_in_months':[term_in_months],'home_ownership':[home_ownership],'loan_status':[loan_status],'purpose':[purpose]})
      prediction = model.predict(tdf)
      output = round(prediction[0], 2)

#if output < 25:
      #put_text("consult one of our consultant")
        
#elif output > 5:
 #     put_text("consult one of our consultant")

#else:
      put_text('Interest rate for the given criteria is :',output)

app.add_url_rule('/tool', 'webio_view', webio_view(predict),
             methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=float, default=8080)
    args = parser.parse_args()
    start_server(predict, port=args.port)
 
