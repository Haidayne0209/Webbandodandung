DELIMITER
//
DROP TRIGGER IF EXISTS `update_total_cart` //
create trigger `update_total_cart`
    after insert
    on `cart_detail`
    for each row
begin
    declare v_total decimal(25, 2);
    select sum(IFNULL(total, 0)) into v_total from cart_detail where cart_id = new.cart_id;
    update cart set total = v_total where cart_id = new.cart_id;
end //
