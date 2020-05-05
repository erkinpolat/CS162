--The database will have a desks table, a stocks table, a summary table and an orders table

--Question 2
CREATE TABLE Desks(
	DeskId INTEGER PRIMARY KEY;
	Name TEXT;
);

CREATE TABLE Stocks(
	StockId INTEGER PRIMARY KEY;
	Name TEXT;
);

CREATE TABLE Orders(
	OrderId Integer PRIMARY KEY;
	OrderDate DATETIME;
	OrderedById INTEGER;
	OrderReceivedId INTEGER;
	Price INTEGER;
	Amount INTEGER;
	StockId INTEGER;
	FOREIGN KEY (OrderedById) REFERENCES Desks(DeskId);
	FOREIGN KEY (OrderReceivedId) REFERENCES Desks(DeskId);
	FOREIGN KEY (StockId) REFERENCES Stocks(StockId);
);

CREATE TABLE Summary(
	DeskId INTEGER;
	TotalOrdered INTEGER;
	TotalFilled INTEGER;
	TotalExchangeShare INTEGER;
	TotalExchangeDollar INTEGER;
	MinPrice INTEGER;
	MaxPrice INTEGER;
	SummaryDate DATETIME;
	FOREIGN KEY (DeskId) REFERENCES Desks(DeskId);
);

--Question 3
INSERT INTO Desks VALUES (1001, "First Desk");
INSERT INTO Desks VALUES (1002, "Second Desk");
INSERT INTO Desks VALUES (1003, "Third Desk");

INSERT INTO Stocks VALUES (2001, "First Stock");
INSERT INTO Stocks VALUES (2002, "Second Stock");
INSERT INTO Stocks VALUES (2003, "Third Stock");
INSERT INTO Stocks VALUES (2004, "Fourth Stock");

INSERT INTO Orders VALUES (3001, "2025-01-15", 1001, 1002, 10000, 100, 2001);
INSERT INTO Orders VALUES (3002, "2025-01-15", 1003, 1001, 15000, 80, 2002);
INSERT INTO Orders VALUES (3003, "2025-01-15", 1002, 1003, 16000, 120, 2002);
INSERT INTO Orders VALUES (3004, "2025-01-15", 1001, 1002, 6000, 120, 2003);
INSERT INTO Orders VALUES (3005, "2025-01-15", 1002, 1001, 14000, 90, 2001);
INSERT INTO Orders VALUES (3006, "2025-01-15", 1003, 1002, 13000, 100, 2003);

INSERT INTO Summary VALUES (1001, 220, 170, 390, 13000, 80, 120);
INSERT INTO Summary VALUES (1002, 210, 220, 430, -1000, 90, 120);
INSERT INTO Summary VALUES (1003, 220, 170, 390, -12000, 80, 120);

--Question 4
BEGIN TRANSACTION;
INSERT INTO Order VALUES (3007, "2025-01-15", 1003, 1001, 15000, 80, 2002);
UPDATE Summary s JOIN Orders o 
SET 
	s.TotalOrdered = s.TotalOrdered + o.Amount,
	s.TotalExchangeShare = s.TotalExchangeShare + o.Amount,
	s.TotalExchangeDollar = s.TotalExchangeDollar - o.Price
WHERE s.DeskId = o.OrderedById;
UPDATE Summary s JOIN Orders o 
SET 
	s.TotalFilled = s.TotalFilled + o.Amount,
	s.TotalExchangeShare = s.TotalExchangeShare + o.Amount,
	s.TotalExchangeDollar = s.TotalExchangeDollar + o.Price
WHERE s.DeskId = o.OrderReceivedId;
COMMIT TRANSACTION;

--Question 5
/* What we are doing here is a transaction with two parties involved where what disappears from one account needs
to appear in the other account. If the transaction were to get interrupted midway, we might make some stocks disappear
from one desk's account and then it doesn't appear in the receiver's account. We don't want this to happen.
*/


