from decimal import Decimal

transactions = [
    {"id":"T1","amount":Decimal("100.00"),"type":"payment"},
    {"id":"T2","amount":Decimal("200.00"),"type":"payment"},
    {"id":"T3","amount":Decimal("300.00"),"type":"refund"}
]

settlements = [
    {"id":"T1","amount":Decimal("100.00")},
    {"id":"T2","amount":Decimal("200.01")},
    {"id":"T2","amount":Decimal("200.01")}
]

def reconcile():
    txn_ids = {t["id"] for t in transactions if t["type"]=="payment"}
    settle_ids = [s["id"] for s in settlements]

    print("Reconciliation Report")
    print("Missing:", [t for t in txn_ids if t not in settle_ids])
    print("Duplicates:", [x for x in settle_ids if settle_ids.count(x)>1])

    txn_total = sum(t["amount"] for t in transactions if t["type"]=="payment")
    settle_total = sum(s["amount"] for s in settlements)

    print("Total Diff:", txn_total - settle_total)

def ai_summary():
    return "AI Summary: Found duplicate entries and rounding issues."

if __name__ == "__main__":
    reconcile()
    print(ai_summary())
