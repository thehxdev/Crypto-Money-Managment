
import os

os.system("title Money Management by Hx")

print("")
print("$$$ ONLY FOR CRYPTO MARKET $$$")
print("")
print("[+] Coded By Hossein (Hx) - @hxPyLover")
print("Version = 1.2.0")
print("")
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
Position_Size = (Risked_Capital /(Entry-Stop_Loss))
Margin = ((Position_Size * Entry)/Leverage)
Profit = (Position_Size * (Target-Entry))
Risk_Reward = (Profit/Risked_Capital)
roe = ((Profit/Margin)*100)

# Outputs
print("Risked Capital = "+str("%.1f" % Risked_Capital))
print("Position Size = "+str("%.3f" % Position_Size))
print("Margin = "+str("%.1f" % Margin))
print("Profit (At TP) = "+str("%.2f" % Profit))
print("R/R ratio = "+str("%.1f" % Risk_Reward))
print("Profit (% - With Leverage) = "+str("%.1f" % roe))

print("")

if Margin > Risked_Capital:
    print("Your Trade Is Valid.")

else:
    print("!!! You Cant Trade. Please Reduce Your Leverage !!!")


print("="*40)
print("")
Exit = input("Press Any Key To Exit...")
