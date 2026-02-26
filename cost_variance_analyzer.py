"""
============================================================
PROJECT 1: Cost Variance Analyzer
============================================================
Automates standard vs actual cost variance analysis for
manufacturing products — covers Material, Labor, and
Overhead variances with management reporting.

Covers:
  - Material Purchase Price Variance (PPV)
  - Material Usage Variance
  - Labor Rate Variance
  - Labor Efficiency Variance
  - Overhead Absorption Variance

Author : Himasree Medarametla | CMA (India) | Cost Accountant
Tools  : Python, Pandas, openpyxl
============================================================
"""

import pandas as pd

# ── SAMPLE DATA ─────────────────────────────────────────────────
# Generic electronics manufacturing product lines

products = [
    'Control Board Assembly',
    'Power Supply Unit',
    'Sensor Module',
    'Communication Interface',
    'Motor Drive Assembly'
]

data = {
    'Product': products,

    # --- MATERIAL ---
    'Std_Material_Cost': [1200, 850, 3400, 2100, 5600],
    'Act_Material_Cost': [1350, 820, 3650, 2300, 5400],
    'Std_Material_Qty':  [100,   80,  200,  150,  300],
    'Act_Material_Qty':  [108,   78,  215,  160,  290],
    'Std_Material_Price':[12.00, 10.63, 17.00, 14.00, 18.67],
    'Act_Material_Price':[12.50, 10.51, 16.98, 14.38, 18.62],

    # --- LABOR ---
    'Std_Labor_Cost':    [400,  300,  900,  600, 1500],
    'Act_Labor_Cost':    [420,  285,  950,  580, 1600],
    'Std_Labor_Hours':   [20,    15,   45,   30,   75],
    'Act_Labor_Hours':   [21,    14,   47,   29,   80],
    'Std_Labor_Rate':    [20.00, 20.00, 20.00, 20.00, 20.00],
    'Act_Labor_Rate':    [20.00, 20.36, 20.21, 20.00, 20.00],

    # --- OVERHEAD ---
    'Std_Overhead': [200, 150, 450, 300,  750],
    'Act_Overhead': [210, 145, 480, 310,  730],
}

df = pd.DataFrame(data)

# ── VARIANCE CALCULATIONS ────────────────────────────────────────

# Material Purchase Price Variance (PPV) = (Std Price - Act Price) x Act Qty
df['PPV'] = (df['Std_Material_Price'] - df['Act_Material_Price']) * df['Act_Material_Qty']

# Material Usage Variance = (Std Qty - Act Qty) x Std Price
df['Usage_Var'] = (df['Std_Material_Qty'] - df['Act_Material_Qty']) * df['Std_Material_Price']

# Labor Rate Variance = (Std Rate - Act Rate) x Act Hours
df['Labor_Rate_Var'] = (df['Std_Labor_Rate'] - df['Act_Labor_Rate']) * df['Act_Labor_Hours']

# Labor Efficiency Variance = (Std Hours - Act Hours) x Std Rate
df['Labor_Eff_Var'] = (df['Std_Labor_Hours'] - df['Act_Labor_Hours']) * df['Std_Labor_Rate']

# Overhead Variance
df['Overhead_Var'] = df['Std_Overhead'] - df['Act_Overhead']

# Total Variance & Summary
df['Total_Variance']  = df['PPV'] + df['Usage_Var'] + df['Labor_Rate_Var'] + df['Labor_Eff_Var'] + df['Overhead_Var']
df['Total_Std_Cost']  = df['Std_Material_Cost'] + df['Std_Labor_Cost'] + df['Std_Overhead']
df['Total_Act_Cost']  = df['Act_Material_Cost'] + df['Act_Labor_Cost'] + df['Act_Overhead']
df['Variance_%']      = ((df['Total_Act_Cost'] - df['Total_Std_Cost']) / df['Total_Std_Cost'] * 100).round(2)
df['Status']          = df['Total_Variance'].apply(lambda x: 'Favorable' if x >= 0 else 'Unfavorable')

# ── REPORT ──────────────────────────────────────────────────────

print("=" * 70)
print("       COST VARIANCE ANALYSIS REPORT — MONTHLY")
print("=" * 70)

report_cols = ['Product', 'Total_Std_Cost', 'Total_Act_Cost',
               'PPV', 'Usage_Var', 'Labor_Rate_Var',
               'Labor_Eff_Var', 'Overhead_Var', 'Total_Variance',
               'Variance_%', 'Status']

pd.set_option('display.float_format', '${:,.2f}'.format)
print(df[report_cols].to_string(index=False))

print("\n" + "=" * 70)
print("SUMMARY")
print(f"  Total Standard Cost : ${df['Total_Std_Cost'].sum():>12,.2f}")
print(f"  Total Actual Cost   : ${df['Total_Act_Cost'].sum():>12,.2f}")
total_var = df['Total_Variance'].sum()
status = 'FAVORABLE' if total_var >= 0 else 'UNFAVORABLE'
print(f"  Net Variance        : ${total_var:>12,.2f}  [{status}]")
print("=" * 70)

# Flag items needing management attention (variance > 2%)
print("\n⚠️  ITEMS REQUIRING MANAGEMENT ATTENTION (>2% variance):")
alerts = df[abs(df['Variance_%']) > 2][['Product', 'Variance_%', 'Status']]
if alerts.empty:
    print("  None — all products within 2% threshold.")
else:
    for _, row in alerts.iterrows():
        print(f"  - {row['Product']}: {row['Variance_%']}% [{row['Status']}]")

# ── EXPORT ───────────────────────────────────────────────────────
df[report_cols].to_excel('cost_variance_report.xlsx', index=False)
print("\n✅ Excel report saved: cost_variance_report.xlsx")
