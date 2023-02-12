-- Creating a trigger that decreases number of remaining items
-- after an order is placed
CREATE TRIGGER upd_items BEFORE UPDATE ON items
FOR EACH ROW SET @remain = @remain - NEW.item
