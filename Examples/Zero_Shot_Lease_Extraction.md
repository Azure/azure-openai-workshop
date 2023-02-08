# Overview  
-using zero shot, pass in natural language instruction, sample lease, and visualize output  
-using model text-davinci-003[^reference]  
-prompt image  
# What is zero shot learning?  
-Ask chatgpt!  
`What is zero shot learning and why is it powerful?`
```
Zero shot learning is a type of machine learning algorithm that allows a model to make predictions on data it has never seen before.  
This is significant because it allows the model to make predictions on data it has never seen before, which can be useful in a  
variety of applications, such as natural language processing, computer vision, and robotics. It also allows the model to generalize  
better, as it can make predictions on data it has never seen before. This is powerful because it allows the model to make  
predictions on data it has never seen before, which can be useful in a variety of applications.  
```  

# Prompt  
### Natural Language Instruction Task + prompt  
```
Using the lease below, return a json object containing:  
  
Lessor, Lessee, Property Address, Property Description, Net Size of Property, Net Size of Property Units, Gross Size of Property,  
Gross Size of Propery Units, Contract Start Date, Lease Start Date, Lease End Date, Lease Term (include the units),  
Monthly Lease Amount (include currency), Payment Frequency, Payment Address.  

Format dates as YYYY-MM-DD. 

Lease:  
```  
```LEASE AGREEMENT
Between
BOB MARSHALL
and
THE UNITED STATES OF AMERICA
ARTICLE ONE: PARTIES
I
This lease is entered into this 23th day of May, 1997, by Bob Marshall, 9 Parma Avenue, Ft.
Overview Heights, St. James, Barbados, hereinafter referred to as "the LANDLORD", and the
United States of America, acting by Frank P. Lesco, Administrative Officer of the Embassy of the
United States of America at Becktowntown, Barbados, hereinafter referred to as "the TENANT".  

ARTICLE TWO: DESCRIPTION OF PREMlSES
The LANDLORD hereby leases to the TENANT the following described Premises, together
with their appurtenances. This property comprises 3 bedrooms, 2 bathrooms, living-dining
room, family room, and kitchen, of approximately 1,725 net square feet located at #205 Lifton
Avenue, Ft. Overview Heights, St. James, Barbados, The property will be used as a diplomatic
residence in Barbados. An inventory of any mechanical and electrical equipment on the
premises, as well as condition reports of the premises, equipment, and furniture and furni shings
provided by the LANDLORD, as they now exist, signed by both parties, is attached to and made
part of this lease.  

ARTICLE THREE: LEASE TERM
The tenn of this lease shall be for six (6) years beginning June 28, 1997 and ending June 27, 2003.  

ARTICLE FOUR: LEASE RENEWAL
The lease is renewable by the TENANT under these same tenns and conditions for a further
period of 3 years, or until June 27, 2006, provided that written notice is given to the
LANDLORD at least 90 days prior to the date this Lease or any extension of it would othenvise
expIre.
In the event the TENANT exercises its right to renew, the renewal rate shall be fair market
rental, to be determined by the parties hereto. Within 90 days prior to the tennination date of the
present rental period, the LANDLORD shall give notice to the TENANT in writing of the
proposed rental amount of the renewal period. Unless the TENANT objects to the proposed rent
within twenty-one days of the receipt of such notice, the rental charge will take effect in the next
rental term.  

ARTICLE FIVE: PAYMENT
The TENANT shall pay the LANDLORD for the premises rented and for other services provided
at the following rate and terms: BDS$5,300 per month for the initial three years and BDS$5,950
for the remaining three years.
All financial obligations of the TENANT resulting from this Lease are subject to the availability
of funds appropriated annually by the Congress of the United States of America. Payments are
to be made quarterly in advance, except that the initial payment shall be for six months for the
period of June 28 through December 27, 1997 (BDS$36,200) to the LANDLORD at 11 Parma Avenue, Ft. Overview Heights, St. James, Barbados.
```  
### Output  
```json
{
  "Lessor": "Bob Marshall",
  "Lessee": "The United States of America",
  "Property Address": "#205 Lifton Avenue, Ft. Overview Heights, St. James, Barbados",
  "Property Description": "3 bedrooms, 2 bathrooms, living-dining room, family room, and kitchen",
  "Net Size of Property": 1725,
  "Net Size of Property Units": "square feet",
  "Gross Size of Property": null,
  "Gross Size of Propery Units": null,
  "Contract Start Date": "1997-05-23",
  "Lease Start Date": "1997-06-28",
  "Lease End Date": "2003-06-27",
  "Lease Term": "6 years",
  "Monthly Lease Amount": "BDS$5,300",
  "Payment Frequency": "quarterly in advance",
  "Payment Address": "11 Parma Avenue, Ft. Overview Heights, St. James, Barbados"
}
```

# References
azure documentation  
azure openai  

# Credit:  
* Kevin Tupper <kevin.tupper@microsoft.com>
* Brandon Cowen <brandoncowen@microsoft.com>
