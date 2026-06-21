"""
==============================================================
 FILE 1: Raw Data Generation (Dirty - Intentional Errors)
==============================================================
 Project  : Telecom Fraud Detection
 Region   : Nasr City, Cairo, Egypt (Vodafone Egypt - Regional)
 Customers: 5,000
 Period   : 3 Months (Jan 1, 2026 → Mar 31, 2026 | 89 days)
 Calls    : ~450,000  (avg 3 calls/customer/day)
 Fraud    : ~3% of customers (~150 fraud accounts)

 Raw data INTENTIONALLY contains:
   - Missing values (Nulls)
   - Duplicate records
   - Typos in categorical fields
   - Out-of-range values
   - Illogical timestamps
   - Malformed IDs
==============================================================
"""

import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# SETTINGS
# ─────────────────────────────────────────────
SEED            = 42
np.random.seed(SEED)
random.seed(SEED)

NUM_CUSTOMERS      = 5_000
START_DATE         = datetime(2026, 1, 1)
END_DATE           = datetime(2026, 3, 31)
NUM_DAYS           = (END_DATE - START_DATE).days + 1   # 89 days
AVG_CALLS_PER_DAY  = 3
FRAUD_RATE         = 0.03   # 3%  → ~150 fraud customers

OUTPUT_DIR = r"D:\Graduation\Dirty"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 62)
print("  GENERATING RAW (DIRTY) DATA — Nasr City | Jan-Mar 2026")
print("=" * 62)
print(f"  Customers : {NUM_CUSTOMERS:,}")
print(f"  Period    : {START_DATE.date()} → {END_DATE.date()} ({NUM_DAYS} days)")
print(f"  Avg Calls : {AVG_CALLS_PER_DAY} calls/customer/day")
print(f"  Fraud Rate: {FRAUD_RATE*100:.0f}%")
print("=" * 62)

# ─────────────────────────────────────────────
# Egyptian Arabic names — English transliteration
# ─────────────────────────────────────────────
first_names_male = [
    "Mohamed", "Ahmed", "Ali", "Omar", "Khaled", "Mostafa", "Youssef",
    "Ibrahim", "Hassan", "Hussein", "Tarek", "Walid", "Karim", "Rami",
    "Sami", "Nader", "Majed", "Bassam", "Amr", "Hossam", "Sherif",
    "Ayman", "Ashraf", "Wael", "Hany", "Tamer", "Essam", "Adel"
]
first_names_female = [
    "Fatima", "Nour", "Sara", "Mariam", "Dina", "Hana", "Rana",
    "Mona", "Heba", "Reem", "Noha", "Aya", "Yasmin", "Salma",
    "Doaa", "Amira", "Nada", "Rania", "Shimaa", "Eman", "Ghada"
]
middle_names = [
    "Mohamed", "Ahmed", "Ali", "Ibrahim", "Hassan", "Mahmoud",
    "Abdallah", "Abdel", "Omar", "Sayed", "Gamal", "Nabil",
    "Ramadan", "Farouk", "Salah", "Fathi", "Magdy", "Lotfy"
]
last_names = [
    "Mahmoud", "Abdullah", "Ibrahim", "Hassan", "Ali", "Ahmed",
    "El-Sayed", "Farouk", "Gamal", "El-Sharkawi", "El-Masry",
    "Zidan", "Salamah", "Mansour", "Rida", "Shahatah", "Badawi",
    "Abdel-Aziz", "Helmy", "Morsy", "Awad", "Qasim", "Nasser",
    "Hanafi", "El-Gazzar", "Ramadan", "Khalil", "El-Banna"
]

def random_full_name():
    gender = random.choice(["M", "F"])
    if gender == "M":
        fn = random.choice(first_names_male)
    else:
        fn = random.choice(first_names_female)
    mn = random.choice(middle_names)
    ln = random.choice(last_names)
    return f"{fn} {mn} {ln}"

# ─────────────────────────────────────────────
# Nasr City districts / zones
# ─────────────────────────────────────────────
districts = [
    "Nasr City - Zone 1",  "Nasr City - Zone 2",
    "Nasr City - Zone 3",  "Nasr City - Zone 7",
    "Nasr City - Zone 8",  "Nasr City - Zone 10",
    "Nasr City - El Zahraa","Nasr City - El Mirghany",
    "Nasr City - Mostafa El-Nahas", "Nasr City - Abbas El-Akkad"
]

subscription_plans = [
    "Prepaid Basic", "Prepaid Plus",
    "Postpaid 100",  "Postpaid 200", "Postpaid Business"
]

# ─────────────────────────────────────────────
# 1. CUSTOMERS TABLE  (customers_raw.csv)
# ─────────────────────────────────────────────
print("\n[1/4] Building customers table...")

customer_ids  = [f"VF-{str(i).zfill(6)}" for i in range(1, NUM_CUSTOMERS + 1)]
fraud_customers = set(random.sample(customer_ids, int(NUM_CUSTOMERS * FRAUD_RATE)))

customers_data = []
for cid in customer_ids:
    full_name    = random_full_name()
    age          = random.randint(18, 70)
    district     = random.choice(districts)
    plan         = random.choice(subscription_plans)
    reg_days_ago = random.randint(30, 1500)
    reg_date     = START_DATE - timedelta(days=reg_days_ago)
    credit_score = round(random.uniform(200, 900), 1)
    phone        = f"010{random.randint(10000000, 99999999)}"

    # ── DIRTY ERRORS ──────────────────────────────
    # Typos in plan (4%)
    if random.random() < 0.04:
        plan = random.choice(["prepaid basic", "POSTPAID 100",
                               "Postpaid100", "PostPaid 200", "postpaid business"])
    # Out-of-range age (2%)
    if random.random() < 0.02:
        age = random.choice([-1, 0, 150, 999])
    # Future registration date (1.5%)
    if random.random() < 0.015:
        reg_date = END_DATE + timedelta(days=random.randint(1, 200))
    # Missing district (3%)
    district_val = None if random.random() < 0.03 else district
    # Missing age (2.5%)
    age_val      = None if random.random() < 0.025 else age
    # Missing plan (2%)
    plan_val     = None if random.random() < 0.02 else plan
    # ──────────────────────────────────────────────

    customers_data.append({
        "customer_id"        : cid,
        "full_name"          : full_name,
        "phone_number"       : phone,
        "age"                : age_val,
        "district"           : district_val,
        "subscription_plan"  : plan_val,
        "registration_date"  : reg_date.strftime("%Y-%m-%d"),
        "is_fraud"           : 1 if cid in fraud_customers else 0,
        "credit_score"       : credit_score
    })

df_customers = pd.DataFrame(customers_data)

# Intentional duplicates: 1.5%
dup_idx      = df_customers.sample(frac=0.015, random_state=SEED).index
df_customers = pd.concat([df_customers, df_customers.loc[dup_idx]], ignore_index=True)

df_customers.to_csv(f"{OUTPUT_DIR}/01_customers_raw.csv", index=False)
print(f"   [OK] 01_customers_raw.csv  — {len(df_customers):,} records")


# ─────────────────────────────────────────────
# 2. CALLS TABLE  (calls_raw.csv)
# ─────────────────────────────────────────────
print("\n[2/4] Building calls table (~450,000 rows)...")

call_types       = ["Voice", "SMS", "Data", "International"]
call_types_dirty = call_types + ["voice", "VOICE", "Sms", "sms",
                                  "DATA", "Interntional", "INTERNATIONAL"]
dest_networks    = ["Vodafone", "Orange", "Etisalat", "WE"]

calls_data      = []
call_id_counter = 1

for cid in customer_ids:
    is_fraud = cid in fraud_customers

    for day_offset in range(NUM_DAYS):
        call_date  = START_DATE + timedelta(days=day_offset)
        base_calls = np.random.poisson(AVG_CALLS_PER_DAY)

        # Fraud customers spike in calls
        if is_fraud:
            if day_offset % 30 in [27, 28, 29] or random.random() < 0.12:
                base_calls = random.randint(15, 35)
            else:
                base_calls = np.random.poisson(5)

        for _ in range(base_calls):
            # Fraud → unusual hours (1 AM - 5 AM, 40% chance)
            if is_fraud and random.random() < 0.4:
                hour = random.randint(1, 5)
            else:
                hour = int(np.random.normal(14, 4))
                hour = max(6, min(23, hour))

            minute   = random.randint(0, 59)
            second   = random.randint(0, 59)
            call_dt  = call_date.replace(hour=hour, minute=minute, second=second)

            call_type = random.choice(call_types)

            # Duration
            if is_fraud:
                duration = random.choice([
                    random.randint(1, 5),
                    random.randint(300, 1800)
                ])
            else:
                duration = int(np.random.exponential(120))
                duration = max(5, min(3600, duration))

            dest_net = random.choice(dest_networks)

            # Cost (EGP)
            if call_type == "International":
                cost = round(duration / 60 * random.uniform(2.5, 5.0), 2)
            elif call_type == "Voice":
                cost = round(duration / 60 * random.uniform(0.15, 0.5), 2)
            elif call_type == "SMS":
                cost     = round(random.uniform(0.05, 0.15), 2)
                duration = 0
            else:  # Data
                cost     = round(random.uniform(0.1, 2.0), 2)
                duration = 0

            # ── DIRTY ERRORS ──────────────────────────────
            # Typos in call_type (4%)
            if random.random() < 0.04:
                call_type = random.choice(call_types_dirty)
            # Negative or extreme duration (1.5%)
            if random.random() < 0.015:
                duration = random.choice([-10, -1, 99999, 100000])
            # Negative cost (1%)
            if random.random() < 0.01:
                cost = round(random.uniform(-50, -0.1), 2)
            # Malformed customer_id: hyphen → underscore (0.8%)
            cid_val = cid
            if random.random() < 0.008:
                cid_val = cid.replace("VF-", "VF_")
            # Missing timestamp (1%)
            ts_val = (call_dt.strftime("%Y-%m-%d %H:%M:%S")
                      if random.random() > 0.01 else None)
            # ──────────────────────────────────────────────

            calls_data.append({
                "call_id"         : f"C{str(call_id_counter).zfill(7)}",
                "customer_id"     : cid_val,
                "timestamp"       : ts_val,
                "call_type"       : call_type,
                "duration_sec"    : duration,
                "destination_net" : dest_net,
                "cost_egp"        : cost,
                "is_fraud_call"   : 1 if is_fraud else 0
            })
            call_id_counter += 1

df_calls = pd.DataFrame(calls_data)

# Duplicates 0.5%
dup_calls = df_calls.sample(frac=0.005, random_state=SEED)
df_calls  = pd.concat([df_calls, dup_calls], ignore_index=True)
# Shuffle (unsorted)
df_calls  = df_calls.sample(frac=1, random_state=SEED).reset_index(drop=True)

df_calls.to_csv(f"{OUTPUT_DIR}/02_calls_raw.csv", index=False)
print(f"   [OK] 02_calls_raw.csv      — {len(df_calls):,} records")


# ─────────────────────────────────────────────
# 3. TRANSACTIONS TABLE  (transactions_raw.csv)
# ─────────────────────────────────────────────
print("\n[3/4] Building transactions table...")

tx_types       = ["Recharge", "Bill Payment", "Data Bundle",
                  "International Bundle", "Refund"]
tx_types_dirty = tx_types + ["recharge", "RECHARGE", "bill payment",
                               "refund ", " Refund", "Data bundle"]
channels       = ["App", "Kiosk", "Agent", "USSD", "Bank Transfer"]

transactions_data = []
tx_counter        = 1

for cid in customer_ids:
    is_fraud = cid in fraud_customers
    num_tx   = random.randint(20, 60) if is_fraud else random.randint(3, 20)

    for _ in range(num_tx):
        tx_date  = START_DATE + timedelta(days=random.randint(0, NUM_DAYS - 1))
        tx_type  = random.choice(tx_types)
        channel  = random.choice(channels)
        status   = random.choice(["Success","Success","Success","Failed","Pending"])

        if tx_type == "Recharge":
            amount = random.choice([10, 20, 30, 50, 100, 200])
        elif tx_type == "Bill Payment":
            amount = round(random.uniform(50, 500), 2)
        elif tx_type in ["Data Bundle", "International Bundle"]:
            amount = random.choice([15, 25, 35, 50, 75, 100])
        else:
            amount = round(random.uniform(5, 100), 2)

        # Fraud: unusually large top-ups
        if is_fraud and random.random() < 0.3:
            amount = random.choice([500, 1000, 2000, 5000])

        # ── DIRTY ERRORS ──────────────────────────────
        if random.random() < 0.04:
            tx_type = random.choice(tx_types_dirty)
        if random.random() < 0.015:
            amount = random.choice([-100, 0, 99999])
        channel_val = None if random.random() < 0.025 else channel
        # ──────────────────────────────────────────────

        transactions_data.append({
            "transaction_id"   : f"T{str(tx_counter).zfill(7)}",
            "customer_id"      : cid,
            "date"             : tx_date.strftime("%Y-%m-%d"),
            "transaction_type" : tx_type,
            "amount_egp"       : amount,
            "channel"          : channel_val,
            "status"           : status,
            "is_fraud"         : 1 if is_fraud else 0
        })
        tx_counter += 1

df_transactions = pd.DataFrame(transactions_data)

# Duplicates 1%
dup_tx         = df_transactions.sample(frac=0.01, random_state=SEED)
df_transactions = pd.concat([df_transactions, dup_tx], ignore_index=True)

df_transactions.to_csv(f"{OUTPUT_DIR}/03_transactions_raw.csv", index=False)
print(f"   [OK] 03_transactions_raw.csv — {len(df_transactions):,} records")


# ─────────────────────────────────────────────
# 4. COMPLAINTS TABLE  (complaints_raw.csv)
# ─────────────────────────────────────────────
print("\n[4/4] Building complaints table...")

complaint_types = [
    "Fraud Report",
    "Unknown Calls",
    "Unauthorized Balance Deduction",
    "Spam Messages",
    "Billing Issue",
    "Identity Theft",
    "Fake Collection Service"
]
resolutions     = ["Resolved", "Under Review", "Rejected",
                   "Transferred to Legal", None]
severity_clean  = ["Low", "Medium", "High", "Critical"]
severity_dirty  = severity_clean + ["low", "HIGH", "critical", "med", "MEDIUM"]

fraud_list        = list(fraud_customers)
complaints_data   = []
comp_counter      = 1

for _ in range(int(NUM_CUSTOMERS * 0.12)):   # 12% of customers have complaints
    reporter_id = (random.choice(customer_ids)
                   if random.random() < 0.6
                   else f"AGENT-{random.randint(1, 50):03d}")
    subject_id  = (random.choice(fraud_list)
                   if random.random() < 0.5
                   else random.choice(customer_ids))

    comp_date   = START_DATE + timedelta(days=random.randint(0, NUM_DAYS - 1))
    comp_type   = random.choice(complaint_types)
    resolution  = random.choice(resolutions)
    severity    = random.choice(severity_dirty)    # dirty: some typos

    days_res    = (random.randint(1, 30)
                   if resolution == "Resolved" else None)

    complaints_data.append({
        "complaint_id"   : f"CMP{str(comp_counter).zfill(5)}",
        "reporter_id"    : reporter_id,
        "subject_id"     : subject_id,
        "date"           : comp_date.strftime("%Y-%m-%d"),
        "complaint_type" : comp_type,
        "severity"       : severity,
        "resolution"     : resolution,
        "days_to_resolve": days_res
    })
    comp_counter += 1

df_complaints = pd.DataFrame(complaints_data)
df_complaints.to_csv(f"{OUTPUT_DIR}/04_complaints_raw.csv", index=False)
print(f"   [OK] 04_complaints_raw.csv  — {len(df_complaints):,} records")


# ─────────────────────────────────────────────
# SUMMARY
# ─────────────────────────────────────────────
print("\n" + "=" * 62)
print("  RAW DATA GENERATION COMPLETE")
print("=" * 62)
print(f"  Customers    : {len(df_customers):>10,}  (incl. {len(df_customers)-NUM_CUSTOMERS} duplicates)")
print(f"  Calls        : {len(df_calls):>10,}")
print(f"  Transactions : {len(df_transactions):>10,}")
print(f"  Complaints   : {len(df_complaints):>10,}")
print(f"  Fraud accts  : {len(fraud_customers):>10,}  ({FRAUD_RATE*100:.0f}% of customers)")
print(f"  Region       : Nasr City, Cairo, Egypt")
print(f"  Period       : {START_DATE.date()} → {END_DATE.date()}  ({NUM_DAYS} days)")
print(f"  Output dir   : {OUTPUT_DIR}")
print("=" * 62)
print("\n  [WARNING] Raw files contain intentional data quality issues:")
print("    - Null values (missing age, district, plan, channel, timestamp)")
print("    - Duplicate records")
print("    - Typos in categorical fields (call_type, plan, severity)")
print("    - Out-of-range values (age, duration, cost, amount)")
print("    - Future registration dates")
print("    - Malformed customer IDs (VF_ instead of VF-)")
print("\n  --> Run clean_data.py to produce clean versions.")
print("=" * 62)