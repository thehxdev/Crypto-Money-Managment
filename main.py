print("\n$$$ ONLY FOR CRYPTO MARKET $$$\n")
print("[+] Coded By Hossein (Hx) - @thehxdev")
print("Version = 2.0.0\n")
print("="*40)

Capital = float(input("Account Balance: "))
Entry = float(input("Entry Price: "))
Stop_Loss = float(input("StopLoss: "))
Target = float(input("Target: "))
Risk = float(input("Risk (0.1 - 100): "))
Leverage = int(input("Leverage: "))
print("="*40)

# Formulas
Risked_Capital = (Capital * (Risk / 100))
Position_Size = (Risked_Capital / (Entry - Stop_Loss))
Margin = ((Position_Size * Entry) / Leverage)
Profit = (Position_Size * (Target - Entry))
Risk_Reward = (Profit / Risked_Capital)
#Roe = ((Profit / Margin) * 100)

print("{0}\n{1}\n{2}\n{3}\n{4}\n".format(
              f"Risked Capital = {round(Risked_Capital , 1)}",
              f"Position Size = {round(Position_Size , 3)}",
              f"Margin = {round(Margin , 1)}",
              f"Profit = {round(Profit , 2)}",
              f"R/R ratio = {round(Risk_Reward , 1)}",
              ))


if Margin > Risked_Capital:
    print("Your Trade Is Valid.")
else:
    print("!!! You Can't Trade. Please Reduce Your Leverage !!!")


print("="*40)
Exit = input("\nPress Any Key To Exit...")
