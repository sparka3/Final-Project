# 590PR Final_Project

# Monte Carlo Simulation to optimize Over-The-Counter (OTC) financial market trading strategy: 

## Team Member(s): Shraddhaa Parkar,Priya Balgi,Shubham Rawlani


# Monte Carlo Simulation Scenario & Purpose:
Over-the-counter or off-exchange trading is done directly between two parties, without the supervision of an exchange. It is a decentralized market, without a central physical location, where market participants trade with one another through various communication modes such as the telephone, email, and proprietary electronic trading systems.
 A commodity market is a financial marketplace that trades in agricultural products such as wheat, coffee, cocoa, fruit and sugar. To procure the best commodity, Investment Bank/ Non-Banking Financial Services (IB/NBFC) collaborates with the suppliers (farmers/traders) from the remote location who may not be tech-savvy. Depending on the commodity prices in the market
Below given are the steps on how OTC trading takes place in the commodities market place.
  1.	Since IB/NBFC collaborate with suppliers, clients contact them for procuring commodities.
  2.	When the clients present a request to the IB/NBFC, the IB/NBFC post the request on the portal that sends a push message to all the       suppliers PAN India.
  3.	The suppliers contact the IB/NBFC and bid to sell their commodity.
Client < > IB/NBFC < > Suppliers
Example Given:
Client: ABC Traders, NBFC: Edelweiss, Suppliers: A, B, C, D
  1.	ABC Traders contact Edelweiss requesting for a procurement of 100 MT of Rice.
  2.	Edelweiss publishes the deal request 
  3.	Suppliers A, B, C, D contact Edelweiss to bid and seal the deal.
N suppliers contact Edelweiss and hence, it is very essential to prioritize every call and if not done, the following repercussion may take place:
  a.	Supplier relation disrupted
  b.	Loss of better deal
  c.	Client’s loss of trust


## Simulation's variables of uncertainty
The simulation variables of uncertainty are number of suppliers, average call time of supplier, time the supplier is willing to hold the call before hanging up, average response time from IB/NBFC and number of representatives required to reduce the average response time from IB/NBFC. Probability distributions that will be used are Normal and Triangular.

## Hypothesis or hypotheses before running the simulation:
The hypotheses before the running the simulation are:
1.	As the number of employees increase, there should be a decrease in wait time and response time.
2.	Number of suppliers decrease will cause response time to drop provided the number of employees from IB/NBFC are constant. 


## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)


## Instructions on how to use the program:

## All Sources Used:
https://www.investopedia.com/terms/o/over-the-countermarket.asp

https://creativemaths.net/blog/triangular-dist/

