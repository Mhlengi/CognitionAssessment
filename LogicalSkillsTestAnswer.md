## Logical Skills Test : Answers
1. Answer C
2. Answer B 
3. Answer D
4. Answer C
5. Answer C
6. Answer B
7. Answer C
8. Answer C
9. Answer A
10. Answer E
11. Answer A
12. Answer E
13. Answer B
14. Answer B
15. Answer C
16. Answer B
17. Answer D
18. Answer A
19. Answer B
20. Answer B
21. Answer B
22. Answer D
23. Answer C
24. Answer C
25. Answer B
26. Answer D
27. Answer D
28. Answer 
Your tasks are:
- Draw the RDD design and include your data types for your fields
![DB_Schema_design](https://github.com/Mhlengi/CognitionAssessment/blob/master/Screenshot%202020-02-18%20at%2016.10.06.png)
- Write out the four statements that would allow you to generate the necessary report.
- Top 10 customers by purchase (cost) - BIG SPENDERS.
`SELECT Top 10 * 
FROM customers 
ORDER BY price DESC;`

- Top 10 customers by purchase (count) - QUANTITY OVER QUALITY.
`SELECT Top 10 * 
FROM customers 
ORDER BY unit DESC;`

- Top 3 Sales People by Nett Profit on Sales.
`SELECT Top 3 * customer_id
FROM sales
 ORDER BY nett_profit DESC;`

- Top 3 Sales People by Gross Sales value.
`SELECT Top 3 * customer_id
FROM sales
 ORDER BY gross_sales_value DESC;`
