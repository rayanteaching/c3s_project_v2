# ERA5 Monthly QC Report

## Scope
- Dataset family: ERA5 monthly Northern Hemisphere collection
- Period: 2000-01 to 2025-12
- Datasets: tp, t2m, ws10m, z500, t850, z950

## Structural QC
- Structural QC reference: `runs/2026-04-17_era5_monthly_qc_full/structure_qc_summary.csv`
- Structural QC status: passed
- Files per dataset: 312 GRIB + 312 request JSON + 312 SHA256

## Scientific sanity QC pass criteria
- Full monthly coverage from 2000-01 through 2025-12
- Finite domain mean, domain minimum, and domain maximum for every monthly field
- Positive seasonal-cycle amplitude in the domain-mean monthly climatology
- Nonnegative domain-mean values for tp, ws10m, z500, and z950
- Domain-mean plausible range check for t2m and t850: 180 K to 330 K

## Dataset summary

| Dataset | Units | Count | Start | End | Mean(domain mean) | Min(domain mean) | Max(domain mean) | Min(domain min) | Max(domain max) | Climatology amplitude | Passed |
|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| tp | m | 312 | 2000-01 | 2025-12 | 0.003045 | 0.002126 | 0.003858 | 0.000000 | 0.100140 | 0.001483 | True |
| t2m | K | 312 | 2000-01 | 2025-12 | 288.723984 | 281.529423 | 295.481751 | 222.291061 | 316.150146 | 12.631135 | True |
| ws10m | m s**-1 | 312 | 2000-01 | 2025-12 | 5.324684 | 4.669780 | 6.150278 | 0.441642 | 17.522024 | 1.088977 | True |
| z500 | m**2 s**-2 | 312 | 2000-01 | 2025-12 | 55942.692303 | 54941.475290 | 57084.915746 | 47370.312500 | 58604.972656 | 1841.394609 | True |
| t850 | K | 312 | 2000-01 | 2025-12 | 282.860214 | 276.708244 | 289.482875 | 238.093063 | 308.485596 | 11.327118 | True |
| z950 | m**2 s**-2 | 312 | 2000-01 | 2025-12 | 5373.445341 | 5274.677740 | 5461.156339 | 2271.658447 | 7248.177734 | 69.884742 | True |

## Generated plots

### tp
- Time series: `runs/2026-04-17_era5_monthly_qc_full/plots/tp_domain_mean_timeseries.png`
- Monthly climatology: `runs/2026-04-17_era5_monthly_qc_full/plots/tp_monthly_climatology.png`

### t2m
- Time series: `runs/2026-04-17_era5_monthly_qc_full/plots/t2m_domain_mean_timeseries.png`
- Monthly climatology: `runs/2026-04-17_era5_monthly_qc_full/plots/t2m_monthly_climatology.png`

### ws10m
- Time series: `runs/2026-04-17_era5_monthly_qc_full/plots/ws10m_domain_mean_timeseries.png`
- Monthly climatology: `runs/2026-04-17_era5_monthly_qc_full/plots/ws10m_monthly_climatology.png`

### z500
- Time series: `runs/2026-04-17_era5_monthly_qc_full/plots/z500_domain_mean_timeseries.png`
- Monthly climatology: `runs/2026-04-17_era5_monthly_qc_full/plots/z500_monthly_climatology.png`

### t850
- Time series: `runs/2026-04-17_era5_monthly_qc_full/plots/t850_domain_mean_timeseries.png`
- Monthly climatology: `runs/2026-04-17_era5_monthly_qc_full/plots/t850_monthly_climatology.png`

### z950
- Time series: `runs/2026-04-17_era5_monthly_qc_full/plots/z950_domain_mean_timeseries.png`
- Monthly climatology: `runs/2026-04-17_era5_monthly_qc_full/plots/z950_monthly_climatology.png`

## Conclusion
- Scientific sanity QC passed for all six ERA5 monthly datasets.
- The tracked ERA5 monthly collection is structurally complete and scientifically plausible for workflow continuation.
