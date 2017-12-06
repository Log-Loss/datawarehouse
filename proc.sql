#插入user表
INSERT INTO users (userId, profileName) SELECT DISTINCT userId, profileName FROM comments;
#插入products表
INSERT INTO products (productId) SELECT DISTINCT productId FROM comments;

#清空
DELETE FROM products;
DELETE FROM comments;
DELETE FROM users;