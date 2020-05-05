--Question 2
BEGIN TRANSACTION;
UPDATE Inventory SET Quantity = Quantity + 99 WHERE WarehouseID=4001 AND ProductID=3001;
INSERT INTO SupplierOrders VALUES (6003, 5001, 3001, 4001, 99, "DELIVERED", "2025-01-15", "2025-01-21");
COMMIT;

--Question 3
BEGIN TRANSACTION;
INSERT INTO Orders VALUES (1001, 2001, "2025-01-01 10:00:00", 202501);
INSERT INTO OrderItems VALUES (1001, 3002, 500);
COMMIT;

--Question 4
--We need to get the customer's adress where the customer id matches the id of the customer we want to update.
--This doesn't aaffect the rest of the tables or the rest of the information in the customers table

--Question 5
--We also would need to delete any references to that product in the other tables where it is referenced.
--Howeverl I think it is also important to first delete the references of the product before deleting the actual product table entry.
DELETE FROM SupplierOrders WHERE ProductID=3003;
DELETE FROM SupplierProduct WHERE ProductID=3003;
DELETE FROM Inventory WHERE ProductID=3003;
DELETE FROM OrderItems WHERE ProductID=3003;
DELETE FROM Products WHERE ProductID=3003;

--Question 6
/*Since the orders of the customers and the orders of the suppliers are in different tables we cannot
really get a table that summarizes the cost and revenue accummulated from each order.
Having a general orders table would help us have this easier. However, this is still a possible query where 
supplier orders, customer orders, suppliers and potentially warehouses are joined.
