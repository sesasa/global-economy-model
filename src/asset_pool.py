class AssetPool:
    def __init__(self, name, market_cap, currency='USD', sub_pools=None):
        self.name = name
        self.market_cap = market_cap
        self.currency = currency
        self.sub_pools = sub_pools or []  # List of child AssetPool objects
        self.flows = {}  # Dict of {target_pool_name: flow_volume}

    def add_sub_pool(self, sub_pool):
        self.sub_pools.append(sub_pool)

    def add_flow(self, target_name, volume):
        self.flows[target_name] = volume

    def total_market_cap(self):
        # Sum of self + sub-pools (recursive for hierarchy)
        return self.market_cap + sum(sp.total_market_cap() for sp in self.sub_pools)

    def __str__(self):
        return f"{self.name} ({self.currency}): ${self.total_market_cap():,.0f} - Flows: {self.flows}"

# Quick test (run this to see output)
if __name__ == "__main__":
    us_real_estate = AssetPool("US Real Estate", 70e12)
    asia_real_estate = AssetPool("Asia Real Estate", 150e12)
    real_estate = AssetPool("Real Estate", 0, sub_pools=[us_real_estate, asia_real_estate])
    
    real_estate.add_flow("Public Equity", 1e12)  # Example flow: $1T to equities
    
    print(real_estate)
    print(f"Total Real Estate Cap: ${real_estate.total_market_cap():,.0f}")