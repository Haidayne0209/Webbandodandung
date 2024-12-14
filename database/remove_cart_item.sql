DELIMITER
//
DROP PROCEDURE IF EXISTS remove_cart_item //
CREATE PROCEDURE remove_cart_item(IN pCartItemId INT)
BEGIN
    DECLARE v_cart_id INT;
    DECLARE vSumQuantity INT DEFAULT 0;
    DECLARE vSumTotal DECIMAL(25, 7) DEFAULT 0;

    SELECT cart_id INTO v_cart_id FROM cart_detail where cart_detail_id = pCartItemId;

    SELECT IFNULL(SUM(quantity), 0), IFNULL(SUM(total), 0)
    INTO vSumQuantity, vSumTotal
    FROM cart_detail
    WHERE cart_id = v_cart_id;

    delete from cart_detail where cart_detail_id = pCartItemId;

    UPDATE cart
    SET quantity = vSumQuantity,
        total    = vSumTotal
    WHERE cart_id = v_cart_id;
end
//
