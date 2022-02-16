import numpy as np
import pandas as pd



##################################parent class###########################################
class OptionPricing: 
    def __init__(self, r, k, S0, T, sigma) -> None:
        self.r = r          #risk-free interest rate
        self.k = k          #strike price 
        self.S0 = S0        #spot price
        self.T = T          #time-to-maturity
        self.sigma = sigma  #volatility

    def getPresentValueofOption(self):
        pass
##################################### Child class #############################################
class EuropeanOptionPricing(OptionPricing):
    def __init__(self, r, k, S0, T, sigma) -> None:
        super.__init__(r, k, S0, T, sigma)
    
    def getPresentValueofOption(self, N, option_type):
        S_t = S0 * np.exp((r - 0.5*sigma*sigma)*T + sigma*np.sqrt(T)*np.random.normal(size = N))
        if(option_type == "call" ):
            C_t = np.maximum(S_t - k)
            return np.mean(C_t)
        else:
            P_t = np.maximum(k - S_t, 0)
            return np.mean()

class AsianOptionPricing(OptionPricing):
    def __init__(self, r, k, S0, T, sigma) -> None:
        super.__init__(r, k, S0, T, sigma)
    
    def getPresentValueofOption(self, N, option_type):
        S_t = S0 * np.exp((r - 0.5*sigma*sigma)*T + sigma*np.sqrt(T)*np.random.normal(size = N))
        if(option_type == "call" ):
            C_t = np.maximum(S_t - k)
            return np.mean(C_t)
        else:
            P_t = np.maximum(k - S_t, 0)
            return np.mean()

if __name__ == '__main__':
    r = 0.08 ; k = 40 ;  S0 = 40 ; T=0.25 ; sigma = 0.3
    print("Hello Mohit!")
    Eu = EuropeanOptionPricing(r,k,S0,T, sigma)
    C0 = np.exp(-r*T) * Eu.getPresentValueofOption(1000, "call")
    print(f"Fair value of option price = {C0}")
