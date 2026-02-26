# 🔍 Cost Variance Analyzer

**Manufacturing cost variance analysis tool — automates PPV, Usage, Labor Rate, Labor Efficiency, and Overhead variance calculations.**

## What This Solves
In manufacturing companies like Foxconn, cost accountants must manually compare standard costs vs actual costs every month across dozens of products. This tool automates that entire workflow.

## Variances Calculated
| Variance Type | Formula |
|---|---|
| Purchase Price Variance (PPV) | (Std Price − Act Price) × Act Qty |
| Material Usage Variance | (Std Qty − Act Qty) × Std Price |
| Labor Rate Variance | (Std Rate − Act Rate) × Act Hours |
| Labor Efficiency Variance | (Std Hours − Act Hours) × Std Rate |
| Overhead Variance | Std Overhead − Act Overhead |

## Output
- ✅ Full variance report with Favorable/Unfavorable flags
- ✅ Management alert for products exceeding 2% threshold
- ✅ Interactive HTML dashboard (4 charts)
- ✅ Excel export for audit trail

## How to Run
```bash
pip install pandas plotly openpyxl
python cost_variance_analyzer.py
```

## Skills Demonstrated
`Standard Costing` `Variance Analysis` `Manufacturing Finance` `Python` `Pandas` `Plotly` `Excel Automation`
