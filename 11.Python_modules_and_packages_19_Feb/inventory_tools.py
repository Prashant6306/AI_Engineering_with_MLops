

WAREHOUSE = "Chennai Depot"

def check_stock(item):
    print(f"Stock for {item}: OK")

def run_audit():
    print("Running full audit...")
    check_stock("Laptops")
    check_stock("Monitors")

print("jai ganesh")
if __name__ == "__main__":
    run_audit()    # only runs directly
    print("jai ganesh1")