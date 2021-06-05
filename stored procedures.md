~~~
CREATE VIEW table_view AS
SELECT * FROM data_users.users;
~~~

~~~
DELIMITER$$
CREATE PROCEDURE create_table()
BEGIN
    CREATE TABLE IF NOT EXISTS users(
  	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	address VARCHAR(50) NOT NULL,
	password VARCHAR(128) NOT NULL,
	comments VARCHAR(100));
END;$$
DELIMITER;
~~~

~~~
DELIMITER$$
CREATE PROCEDURE adding_user(id_user INT, name_user VARCHAR(50), last_name_user VARCHAR(30), address_user VARCHAR(50), pass_user VARCHAR(128), comments_user VARCHAR(100))
BEGIN
    INSERT INTO data_users.table_view VALUES(id_user, name_user, last_name_user, address_user, SHA2(pass_user, 0), comments_user);
END;$$
DELIMITER;
~~~

~~~
DELIMITER$$
CREATE PROCEDURE delete_user(id_user INT)
BEGIN
    DELETE FROM data_users.table_view WHERE id= id_user;
END;$$
DELIMITER;
~~~

~~~
DELIMITER$$
CREATE PROCEDURE read_user(id_user int)
BEGIN
    SELECT * FROM data_users.table_view where id= id_user;
END;$$
DELIMITER;
~~~

~~~
DELIMITER$$
CREATE PROCEDURE update_user(id_user INT, name_user VARCHAR(50), last_name_user VARCHAR(30), address_user VARCHAR(50), pass_user VARCHAR(128), comments_user VARCHAR(100))
BEGIN
    UPDATE data_users.table_view set
	name=name_user,
	last_name=last_name_user,
	address=address_user,
	password=pass_user,
	comments= comments_user
	where id= id_user;
END;$$
DELIMITER;
~~~
