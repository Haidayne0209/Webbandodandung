DELIMITER //

DROP TRIGGER IF EXISTS `update_order_item` //
CREATE TRIGGER `update_order_item`
AFTER INSERT ON `order`
FOR EACH ROW
BEGIN
    DECLARE v_cart_id INT;

    -- Get the cart ID for the user
    SELECT cart_id INTO v_cart_id
    FROM cart
    WHERE user_id = NEW.user_id
    LIMIT 1;

    -- Insert order details from cart details
    INSERT INTO order_detail (order_id, product_id, quantity, price, total)
    SELECT NEW.order_id, product_id, quantity, price, total
    FROM cart_detail
    WHERE cart_id = v_cart_id;

    -- Delete cart details and the cart
    DELETE FROM cart_detail WHERE cart_id = v_cart_id;
    DELETE FROM cart WHERE cart_id = v_cart_id;

END //

DELIMITER ;
