def economic_risk(data):
    risk = 0
    if data.inflation == "rising":
        risk += 2
    if data.market_volatility == "high":
        risk += 2
    if data.price_cycle == "high":
        risk += 1
    return risk
