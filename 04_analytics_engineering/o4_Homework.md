## Homework 4: Analytics Engineering for Data Engineering Zoomcamp 2026
---
###Q1: dbt run --select int_trips_unioned builds which models? (1 point
### Answer: int_trips_unioned only

---
###Q2: New value 6 appears in payment_type. What happens on dbt test?
### Answer: dbt fails the test with non-zero exit code

---
### Q3: Count of records in fct_monthly_zone_revenue? (1 point)
### Answer: 12,184

```sql
SELECT count(*) 
FROM `kestra-sandbox-485712.dbt_prod.fct_monthly_zone_revenue`;
```
---
### Q4: Zone with highest revenue for Green taxis in 2020? 
### Answer: East Harlem North

```sql
SELECT pickup_zone, SUM(revenue_monthly_total_amount) AS total_revenue
FROM `kestra-sandbox-485712.dbt_prod.fct_monthly_zone_revenue`
WHERE EXTRACT(YEAR FROM revenue_month) = 2020 AND service_type = 'Green'
GROUP BY pickup_zone
ORDER BY total_revenue DESC
LIMIT 1;
```
---
### Q5: Total trips for Green taxis in October 2019?
### Answer: 384,624

```sql
SELECT SUM(total_monthly_trips)
FROM `kestra-sandbox-485712.dbt_prod.fct_monthly_zone_revenue`
WHERE revenue_month = '2019-10-01' AND service_type = 'Green';
```
---
### Q6: Count of records in stg_fhv_tripdata (filter dispatching_base_num IS NULL)?
### Answer: 43,244,693

```sql
SELECT COUNT(*)
FROM kestra-sandbox-485712.zoomcamp.fhv_tripdata
WHERE dispatching_base_num IS NOT NULL;
```
