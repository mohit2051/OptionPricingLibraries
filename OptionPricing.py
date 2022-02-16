import numpy as np
import pandas as pd



##################################parent class###########################################
class OptionPricing: 
    def __init__(self, r, k, S0, T, sigma):
        self.r = r          #risk-free interest rate
        self.k = k          #strike price 
        self.S0 = S0        #spot price
        self.T = T          #time-to-maturity
        self.sigma = sigma  #volatility

    def getPresentValueofOption(self):
        pass
##################################### Child class #############################################
class EuropeanOptionPricing(OptionPricing):
    def __init__(self, r, k, S0, T, sigma):
        super().__init__(r, k, S0, T, sigma)
    
    
    def getPresentValueofOption(self, N, option_type):
        
        """
        This method returns the value of the European option at maturity

        """

        S_t = S0 * np.exp((r - 0.5*sigma*sigma)*T + sigma*np.sqrt(T)*np.random.normal(size = N))
        if(option_type == "call" ):
            C_t = np.maximum(S_t - k,0)
            return np.mean(C_t)
        else:
            P_t = np.maximum(k - S_t, 0)
            return np.mean(P_t)

class AsianOptionPricing(OptionPricing):
    def __init__(self, r, k, S0, T, sigma) -> None:
        super().__init__(r, k, S0, T, sigma)
    
    def getPresentValueofOption(self, I, M, option_type):

        """
        This method returns the value of the Asian option at maturity
        
        """

        dt = self.T/M
        values = sigma*np.sqrt(dt)*np.random.normal(size=(I,M)) + (r-sigma*sigma*0.5)*dt
        #print(values.shape)
        S_t = S0 * np.exp(np.cumsum(values, axis = 1))
        #S_t = S0 * np.exp((r - 0.5*sigma*sigma)*T + sigma*np.sqrt(T)*np.random.normal(size = N))
        if(option_type == "call" ):
            C_t = np.maximum(np.mean(S_t,axis=1) - k,0)
            return np.mean(C_t)
        else:
            P_t = np.maximum(k - np.mean(S_t,axis=1), 0)
            return np.mean(P_t)


if __name__ == '__main__':
    r = 0.08 ; k = 40 ;  S0 = 40 ; T=0.25 ; sigma = 0.3
    
    #European Option Prcing
    Eu = EuropeanOptionPricing(r,k,S0,T, sigma)
    C0 = np.exp(-r*T) * Eu.getPresentValueofOption(100000, "call")
    print(f"Fair value of European call option = {C0}")
    P0 = np.exp(-r*T) * Eu.getPresentValueofOption(100000, "put")
    print(f"Fair value of European put option = {P0}")

    #Asian Option Pricing
    As = AsianOptionPricing(r,k,S0,T, sigma)
    C0 = np.exp(-r*T) * As.getPresentValueofOption(100000, 200, "call")
    print(f"Fair value of Asian Call Option = {C0}")
    P0 = np.exp(-r*T) * As.getPresentValueofOption(100000, 200, "put")
    print(f"Fair value of Asian Put Option = {P0}")



