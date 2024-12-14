DELIMITER
//
DROP PROCEDURE IF EXISTS add_to_cart //
CREATE PROCEDURE add_to_cart(
    IN p_user_id INT,
    IN p_product_id INT,
    IN p_quantity INT
)
BEGIN
    DECLARE v_cart_id INT;
    DECLARE v_cart_item_id INT;
    DECLARE v_product_price DECIMAL(25, 2);


    SELECT cart_id
    INTO v_cart_id
    FROM cart
    WHERE user_id = p_user_id;

    IF v_cart_id IS NULL THEN
        INSERT INTO cart(user_id, quantity, total)
        VALUES (p_user_id, p_quantity, 0);
        SET v_cart_id = LAST_INSERT_ID();
    END IF;

    SELECT cd.cart_detail_id, p.price
    INTO v_cart_item_id, v_product_price
    FROM cart_detail cd
             INNER JOIN product p ON cd.product_id = p.product_id
    WHERE cart_id = v_cart_id
      AND p.product_id = p_product_id;

    IF v_cart_item_id IS NULL THEN
        SELECT price
        INTO v_product_price
        FROM product
        WHERE product_id = p_product_id;

        INSERT INTO cart_detail(cart_id, product_id, quantity, price, total)
        VALUES (v_cart_id, p_product_id, p_quantity, v_product_price, v_product_price * p_quantity);
    ELSE
        IF p_quantity + (SELECT quantity FROM cart_detail WHERE cart_detail_id = v_cart_item_id) < 1 THEN
            DELETE FROM cart_detail WHERE cart_detail_id = v_cart_item_id;
        ELSE
            UPDATE cart_detail
            SET quantity = quantity + p_quantity,
                total    = v_product_price * (p_quantity + quantity),
                price    = v_product_price
            WHERE cart_detail_id = v_cart_item_id;
        END IF;
    END IF;

    UPDATE cart
    SET quantity = IFNULL(),
        total    = total + v_product_price * p_quantity
    WHERE cart_id = v_cart_id;
end
//
