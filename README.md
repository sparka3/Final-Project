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
For the optimization of OTC financial trading strategy, the following assumptions have been made:
1. Number of Employees : 1/2/3/4
2. The suppliers call duration has been assumed to be for a minimum of one minute and a maximum of 12 minutes.
3. The supplier wait time has been assumed to be for a maximum of 20 minutes.
4. The suppliers will be attended to on a first come first serve basis.
5. In case of any technical errors,i.e. if the supplier hold time is a negative integer,  the supplier call will be dropped.

## Instructions on how to use the program:
For the program, 2000 simulations have been considered. These simulations will be handled by 4 employees starting from finding calculation with what happens if there is only 1 employee to if there are 4 employees

The output has been presented in a tabluar format that displays the calculation of drop out percentage and average response time.
                  Dropout Percent  Avg Response Time
No. of Employees                                    
1                       90.913399            35.0035
2                       45.454545             5.0000
3                       45.454545             3.0000
4                       36.363636             2.0000

## All Sources Used:
https://www.investopedia.com/terms/o/over-the-countermarket.asp

https://creativemaths.net/blog/triangular-dist/

