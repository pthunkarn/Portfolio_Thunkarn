SELECT *
FROM customers
JOIN invoice
ON customer.id = invoice.id
