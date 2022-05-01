import os

os.system("title Money Management by Hx")

print(" ")
print("$$$ ONLY FOR CRYPTO MARKET $$$")
print(" ")
print("[+] Coded By Hossein (Hx) - @hxPyLover")
print("Version = 1.1.0")
print(" ")
print("="*40)
Capital = input("Account Balance (None Decimals): ")
Entry = input("Entry Price: ")
Stop_Loss = input("StopLoss: ")
Target = input("Target: ")
Risk = input("Risk (0.1 - 100): ")
Leverage = input("Leverage: ")
print("="*40)

Capital = int(Capital)
Entry = float(Entry)
Stop_Loss = float(Stop_Loss)
Target = float(Target)
Risk = float(Risk)
Leverage = int(Leverage)

# Formulas
Risked_Capital = (Capital*(Risk/100))
Position_Size = (Capital*(Risk/100)/(Entry-Stop_Loss))
Margin = ((((Capital*(Risk/100))/(Entry-Stop_Loss))*Entry)/Leverage)
Profit = ((Capital*(Risk/100)/(Entry-Stop_Loss))*(Target-Entry))
Risk_Reward = (((Capital*(Risk/100)/(Entry-Stop_Loss))*(Target-Entry))/(int(Capital)*(Risk/100)))
roe = ((Profit/Margin)*100)

# Outputs
print("Risked Capital = "+str(Risked_Capital))
print("Position Size = "+str(Position_Size))
print("Margin = "+str(Margin))
print("Profit (At TP) = "+str(Profit))
print("R/R ratio = "+str(Risk_Reward))
print("Profit (% - With Leverage) = "+str(roe))

print("="*40)
print("")
Exit = input("Press Any Key To Exit...")
