SET FOREIGN_KEY_CHECKS = 0;
SET GROUP_CONCAT_MAX_LEN=32768;
SET @tables = NULL;
SELECT GROUP_CONCAT('`', table_name, '`') INTO @tables
  FROM information_schema.tables
  WHERE table_schema = (SELECT DATABASE());
SELECT IFNULL(@tables,'dummy') INTO @tables;

SET @tables = CONCAT('DROP TABLE IF EXISTS ', @tables);
PREPARE stmt FROM @tables;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
SET FOREIGN_KEY_CHECKS = 1;

--
-- Table structure for table users
--
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users
  (
     id          INT NOT NULL auto_increment,
     name        VARCHAR(50) NOT NULL,
     mobile      VARCHAR(15) NULL,
     email       VARCHAR(64) NOT NULL,
     password    VARCHAR(32) NOT NULL,
     profile     VARCHAR(255),
     last_login  DATETIME DEFAULT NULL,
     is_verified TINYINT(1) DEFAULT '0',
     verified_at DATETIME NULL,
     created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id),
     UNIQUE KEY uq_mobile (mobile),
     UNIQUE KEY uq_email (email)
  )
engine=innodb
DEFAULT charset=utf8;
--
-- Table structure for table roles
--
DROP TABLE IF EXISTS roles;

CREATE TABLE IF NOT EXISTS roles
  (
     id         INT NOT NULL auto_increment,
     name       VARCHAR(50) NOT NULL,
     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id),
     KEY roles_name (name)
  )
engine=innodb
DEFAULT charset=utf8;
--
-- Table structure for table user_role
--

DROP TABLE IF EXISTS user_role;

CREATE TABLE IF NOT EXISTS user_role
  (
     id         INT NOT NULL auto_increment,
     users_id   INT NOT NULL,
     roles_id   INT NOT NULL,
     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id),
     UNIQUE KEY users_id (users_id),
     KEY users_roles_role_id (roles_id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE user_role
  ADD CONSTRAINT users_roles_roles_id_fkey FOREIGN KEY (roles_id) REFERENCES
  roles (id) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT users_roles_users_id_fkey FOREIGN KEY (users_id) REFERENCES
  users (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table users_address
--

DROP TABLE IF EXISTS users_address;

CREATE TABLE IF NOT EXISTS users_address
  (
     id           INT NOT NULL auto_increment,
     users_id     INT NOT NULL,
     state        VARCHAR(255) NOT NULL,
     city         VARCHAR(255) NOT NULL,
     country      VARCHAR(100) NOT NULL,
     zip_code     VARCHAR(50) NOT NULL,
     address_1    TEXT NOT NULL,
     address_2    TEXT,
     landmark     TEXT,
     is_default   TINYINT(1) NOT NULL DEFAULT '0',
     address_type ENUM('Home', 'Office', 'Other') DEFAULT NULL,
     is_deleted   TINYINT(1) NOT NULL DEFAULT '0',
     created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id),
     KEY user_address_ibfk_1 (users_id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE users_address
  ADD CONSTRAINT user_address_users_id_fkey FOREIGN KEY (users_id) REFERENCES
  users (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table categories
--
DROP TABLE IF EXISTS category;

CREATE TABLE IF NOT EXISTS category
  (
     id          INT NOT NULL auto_increment,
     parent_id   INT NOT NULL,
     name        VARCHAR(255) NOT NULL,
     description TEXT NOT NULL,
     image       VARCHAR(255) NOT NULL,
     sort_order  INT NOT NULL,
     status      TINYINT(1) NOT NULL DEFAULT '1',
     created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id),
     KEY category_parent_id (parent_id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE category
  ADD CONSTRAINT category_parent_id_fkey FOREIGN KEY (parent_id) REFERENCES
  category (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table category_tag
--
DROP TABLE IF EXISTS category_tag;

CREATE TABLE category_tag
  (
     id           INT NOT NULL auto_increment,
     category_id  INT NOT NULL,
     seo_title    VARCHAR(255) DEFAULT NULL,
     seo_desc     TEXT NOT NULL,
     seo_keywords VARCHAR(255) DEFAULT NULL,
     h1_tag       VARCHAR(255) DEFAULT NULL,
     h2_tag       VARCHAR(255) DEFAULT NULL,
     h3_tag       VARCHAR(255) DEFAULT NULL,
     alt_img_tag  VARCHAR(255) NOT NULL,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE category_tag
  ADD CONSTRAINT category_tag_category_id_fkey FOREIGN KEY (category_id)
  REFERENCES category (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table attribute
--

DROP TABLE IF EXISTS attribute;
CREATE TABLE IF NOT EXISTS attribute
  (
     id         INT NOT NULL auto_increment,
     name       VARCHAR(255) NOT NULL,
     sort_order INT NOT NULL,
     created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;
--
-- Table structure for table coupon
--
DROP TABLE IF EXISTS coupon;
CREATE TABLE IF NOT EXISTS coupon
  (
     id           INT NOT NULL auto_increment,
     code         VARCHAR(255) NOT NULL,
     description  TEXT,
     active       BOOLEAN DEFAULT true,
     coupon_type  ENUM('Amount', 'Percentage') NOT NULL,
     coupon_value NUMERIC,
     sort_order   INT NOT NULL,
     start_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     end_at       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     created_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

--
-- Table structure for table product
--

DROP TABLE IF EXISTS product;
CREATE TABLE product
  (
     id          INT NOT NULL auto_increment,
     category_id INT NOT NULL,
     name        VARCHAR(255) NOT NULL,
     sku         VARCHAR(10) NOT NULL,
     description TEXT,
     status      TINYINT(1) NOT NULL DEFAULT '1',
     created_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE product
  ADD CONSTRAINT product_category_id_fkey FOREIGN KEY (category_id) REFERENCES
  category (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table product_meta
--

DROP TABLE IF EXISTS product_meta;
CREATE TABLE product_meta
  (
     id             INT NOT NULL auto_increment,
     product_id     INT NOT NULL,
     quantity       INT NOT NULL,
     original_price DECIMAL(6, 2) NOT NULL,
     discount_price DECIMAL(6, 2) NULL,
     tax_percentage DECIMAL(2, 2) NULL,
     created_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     updated_at     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE product_meta
  ADD CONSTRAINT product_meta_product_id_fkey FOREIGN KEY (product_id)
  REFERENCES product (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table product_meta
--
DROP TABLE IF EXISTS product_img;

CREATE TABLE product_img
  (
     id          INT NOT NULL auto_increment,
     product_id  INT NOT NULL,
     img         VARCHAR(255) NOT NULL,
     thumb_img   VARCHAR(255) NOT NULL,
     file_type   ENUM('Image', 'Video') NOT NULL DEFAULT 'Image',
     alt_img_tag VARCHAR(255) NOT NULL,
     sort_order  INT NOT NULL,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE product_img
  ADD CONSTRAINT product_img_product_id_fkey FOREIGN KEY (product_id) REFERENCES
  product (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table product_attribute
--
DROP TABLE IF EXISTS product_attribute;

CREATE TABLE product_attribute
  (
     id           INT NOT NULL auto_increment,
     product_id   INT NOT NULL,
     attribute_id INT NOT NULL,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE product_attribute
  ADD CONSTRAINT product_attribute_product_id_fkey FOREIGN KEY (product_id)
  REFERENCES product (id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE product_attribute
  ADD CONSTRAINT product_attribute_attribute_id_fkey FOREIGN KEY (attribute_id)
  REFERENCES attribute (id) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Table structure for table product_tag
--

DROP TABLE IF EXISTS product_tag;

CREATE TABLE product_tag
  (
     id           INT NOT NULL auto_increment,
     product_id   INT NOT NULL,
     seo_title    VARCHAR(255) DEFAULT NULL,
     seo_desc     TEXT NOT NULL,
     seo_keywords VARCHAR(255) DEFAULT NULL,
     h1_tag       VARCHAR(255) DEFAULT NULL,
     h2_tag       VARCHAR(255) DEFAULT NULL,
     h3_tag       VARCHAR(255) DEFAULT NULL,
     alt_img_tag  VARCHAR(255) NOT NULL,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE product_tag
  ADD CONSTRAINT product_tag_product_id_fkey FOREIGN KEY (product_id) REFERENCES
  product (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table product_cart
--
DROP TABLE IF EXISTS product_cart;

CREATE TABLE product_cart
  (
     id         INT NOT NULL auto_increment,
     product_id INT NOT NULL,
     users_id   INT NOT NULL,
     coupon_id  INT NOT NULL,
     quantity   INT NOT NULL,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE product_cart
  ADD CONSTRAINT product_cart_product_id_fkey FOREIGN KEY (product_id)
  REFERENCES product (id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE product_cart
  ADD CONSTRAINT product_cart_users_id_fkey FOREIGN KEY (users_id) REFERENCES
  users (id) ON DELETE CASCADE ON UPDATE CASCADE;
--
-- Table structure for table product_attribute
--
DROP TABLE IF EXISTS order_status;
CREATE TABLE order_status
  (
     id   INT NOT NULL auto_increment,
     name INT NOT NULL,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

--
-- Table structure for table user_order
--
DROP TABLE IF EXISTS user_order;
CREATE TABLE user_order
  (
     id               INT NOT NULL auto_increment,
     users_id         INT NOT NULL,
     users_address_id INT NOT NULL,
     coupon_id        INT NOT NULL,
     order_status_id  INT NOT NULL,
     delivery_charge  DECIMAL(6, 2) NOT NULL,
     payment_mode     VARCHAR(50) NULL,
     transaction_id   VARCHAR(50) NULL,
     delivery_at      DATETIME NULL,
     order_at         DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE user_order
  ADD CONSTRAINT user_order_users_address_id_fkey FOREIGN KEY (users_address_id)
  REFERENCES users_address (id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE user_order
  ADD CONSTRAINT user_order_users_id_fkey FOREIGN KEY (users_id) REFERENCES
  users (id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE user_order
  ADD CONSTRAINT user_order_coupon_id_fkey FOREIGN KEY (coupon_id) REFERENCES
  coupon (id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE user_order
  ADD CONSTRAINT user_order_order_status_id_fkey FOREIGN KEY (order_status_id)
  REFERENCES order_status (id) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Table structure for table order_product
--
DROP TABLE IF EXISTS order_product;

CREATE TABLE order_product
  (
     id             INT NOT NULL auto_increment,
     user_order_id  INT NOT NULL,
     product_id     INT NOT NULL,
     product_name   VARCHAR(255) NOT NULL,
     quantity       INT NOT NULL,
     product_price  DECIMAL(6, 2) NOT NULL,
     discount_price DECIMAL(6, 2) NOT NULL,
     tax_percentage DECIMAL(6, 2) NOT NULL,
     total_amount   DECIMAL(6, 2) NOT NULL,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;

ALTER TABLE order_product
  ADD CONSTRAINT order_product_user_order_id_fkey FOREIGN KEY (user_order_id)
  REFERENCES user_order (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE order_product
  ADD CONSTRAINT order_product_product_id_fkey FOREIGN KEY (product_id)
  REFERENCES product (id) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Table structure for table banner
--
DROP TABLE IF EXISTS banner;
CREATE TABLE banner
  (
     id            INT NOT NULL AUTO_INCREMENT,
     image         VARCHAR(255) NOT NULL,
     sort_order    INT NOT NULL,
     title         VARCHAR(255) NOT NULL,
     sub_title     VARCHAR(255) NOT NULL,
     has_rout_link BOOLEAN NOT NULL DEFAULT false,
     rout_link     VARCHAR(255) NOT NULL,
     PRIMARY KEY (id)
  )
engine=innodb
DEFAULT charset=utf8;
