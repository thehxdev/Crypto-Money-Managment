import os

os.system("title Money Management by Hx")

print(" ")
print("$$$ ONLY FOR CRYPTO MARKET $$$")
print(" ")
print("[+] Coded By Hossein (Hx) - @hxPyLover")
print("Version = 1.0.0")
print(" ")
print("="*40)
Capital = input("Account Balance (Enter a round number): ")
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
Risked_Capital = "Risked Capital = "+str(int(Capital)*(Risk/100))
Position_Size = "Position Size = "+str(float(Capital*(Risk/100))/(Entry-Stop_Loss))
Margin = "Margin = "+str((((float(Capital*(Risk/100)))/(Entry-Stop_Loss))*Entry)/Leverage)
Profit = "Profit (At TP) = "+str((float(Capital*(Risk/100))/(Entry-Stop_Loss))*(Target-Entry))
Risk_Reward = "R/R ratio = "+str(((float(Capital*(Risk/100))/(Entry-Stop_Loss))*(Target-Entry))/(int(Capital)*(Risk/100)))

# Outputs
print(Risked_Capital)
print(Position_Size)
print(Margin)
print(Profit)
print(Risk_Reward)

print("="*40)
print("")
Exit = input("Exit?")