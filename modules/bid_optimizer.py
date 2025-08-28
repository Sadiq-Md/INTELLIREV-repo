def suggest_bid_pricing(deal_size: str, region: str, industry: str) -> str:
    if region == "North America" and industry == "Banking":
        if deal_size.lower() == "large":
            return "Increase price by 5% (high margin segment)"
        else:
            return "Increase price by 2% (moderate margin)"
    elif region == "Europe":
        return "Maintain baseline pricing (competitive market)"
    elif industry == "Healthcare":
        return "Consider discounting by 3% to win bids"
    else:
        return "Stick to baseline pricing"
